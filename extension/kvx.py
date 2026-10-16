"""Ripple-aware repair of stale KV caches after document edits (GPU study).

Question: after a length-preserving edit, does recomputing the cache from the edit to the end of the last
dependent sentence ("path window", GraphPath), with the dependent sentences found by an index built AT EDIT TIME,
beat the published repair policies at equal or lower cost, especially where Mao et al.'s CarrierWindow is weak,
and does it hold for more hops and more dependents?  Baseline paper: Mao, Mackey, Lin, "Contiguity, Not
Importance: Budgeted Repair of Stale KV Caches After Document Edits", arXiv:2609.17983 (derived alias->lookup
benchmark, EditLocal, CarrierWindow, margin recovery).  Erratum arms follow Li, arXiv:2606.17107.

Subcommands
  build    make the test items (model-independent text; every edit checked length-preserving in all 3 tokenizers;
           optional LLM dependency graphs if OPENAI_API_KEY is set)
  run      one model: integrity checks, then every arm on every item, appended to results_<model>.jsonl
  analyze  tables with bootstrap intervals -> results.md / results.json
  selftest CPU-only check of item building, index graph and analysis with a stub tokenizer (no torch needed)

Every number in the write-up must come from results_<model>.jsonl via `analyze`.
"""
import argparse, bisect, collections, hashlib, json, math, os, random, re, statistics, sys, time, traceback

MODELS = {
    "qwen3": ["Qwen/Qwen3-8B"],
    "llama": ["meta-llama/Llama-3.1-8B-Instruct", "unsloth/Llama-3.1-8B-Instruct"],
    "mistral": ["mistralai/Mistral-7B-Instruct-v0.3", "unsloth/mistral-7b-instruct-v0.3"],
}
ENTITIES = ["Varnex", "Tolbrook", "Quillon", "Marandi", "Oskeli", "Pemberra", "Halvost", "Drennick", "Calvaro", "Sevrin",
            "Ombrel", "Kastrup", "Nerevan", "Feldrin", "Torvanna"]
ALIASES = ["Alpha", "Beta", "Gamma", "Delta", "Sigma", "Omega", "Kappa", "Theta", "Lambda", "Zeta", "Iota", "Tau"]
GROUPS = ["Kestrel", "Falcon", "Heron", "Osprey", "Plover", "Curlew", "Merlin", "Harrier", "Egret", "Lapwing"]
ATTRS = ["code", "tag", "room"]
LETTERS = "BCDFGHJKLMNPQRSTVWXZ"
NOISE = ["Company {e} opened a new office in Beirut.", "Company {e} employs about 340 people.",
         "Company {e} was founded in 1987.", "Company {e} sponsors a local football club."]
VOCAB = set(w.lower() for w in ENTITIES + ALIASES + GROUPS + ["alias", "aliases"])
CELLS = ["direct", "derived_d0", "derived_d250", "derived_d1500", "hop3", "fanout3", "noisy_d250"]
# indirect cells (from the teammate's second proof of concept): the edit names a plan by its ordinal ("the sixth plan")
# and the rows name it by its number ("Plan six"), so no word is shared between the edit and the dependent rows
CELLS_INDIRECT = ["indirect_d250", "indirect_d1500"]
ALL_CELLS = CELLS + CELLS_INDIRECT
ORDS = ["second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
NUMS = ["two", "three", "four", "five", "six", "seven", "eight", "nine"]
PRICES = {"gpt-4o-mini": (0.15, 0.60), "gpt-4.1": (2.0, 8.0), "gpt-4.1-mini": (0.40, 1.60), "gpt-4o": (2.5, 10.0)}
PREFIX_TOK, TAIL_TOK = 600, 600
STOP = set("the a an of to in on at for and or but is are was were be been by with from as that this it its which who "
           "his her their they he she we you i not no has have had do does did will would can could than then there "
           "into over after before about also such these those other more most some any all each".split())
INSTR = "Read the document, then answer the question."


# ------------------------------------------------------------------------------------------- filler text

def clean_wikitext(line):
    s = line.strip()
    for a, b in ((" @-@ ", "-"), (" @,@ ", ","), (" @.@ ", "."), (" ,", ","), (" .", "."), (" ;", ";"), (" :", ":"),
                 ("( ", "("), (" )", ")"), (" 's", "'s"), (" n't", "n't"), (' " ', ' "')):
        s = s.replace(a, b)
    return s


def load_filler(log):
    paras = []
    try:
        from datasets import load_dataset
        ds = load_dataset("Salesforce/wikitext", "wikitext-103-raw-v1", split="validation")
        for row in ds:
            s = clean_wikitext(row["text"])
            if not s or s.startswith("=") or len(s.split()) < 60: continue
            if set(re.findall(r"[a-z]+", s.lower())) & VOCAB: continue
            if re.search(r"\b[A-Z]\d\b", s): continue  # no code-like tokens
            paras.append(s)
        log(f"filler: {len(paras)} wikitext-103 validation paragraphs")
    except Exception as e:
        log(f"filler: wikitext download failed ({e!r}); using synthetic filler")
    if len(paras) < 200:
        rng = random.Random(0)
        depts = ["facilities", "logistics", "security", "finance", "research", "support", "training", "network"]
        objs = ["visitor logs", "supply orders", "equipment lists", "maintenance tickets", "budget notes", "shift rosters"]
        for i in range(3000):
            paras.append(" ".join(f"The {rng.choice(depts)} team {rng.choice(['reviews', 'archives', 'updates', 'audits'])} "
                                  f"the {rng.choice(objs)} {rng.choice(['every Monday', 'each quarter', 'before noon'])}."
                                  for _ in range(6)))
    return paras


def split_sentences(p):
    return [s for s in re.split(r"(?<=[.!?])\s+", p) if s]


# ------------------------------------------------------------------------------------------- items

class Doc:
    """Paragraphs of sentences with character spans; roles mark the edit and dependent sentences."""
    def __init__(self):
        self.paras = []  # list of list of (text, role)

    def add_para(self, sents):
        self.paras.append(list(sents))

    def render(self, edit_new=None):
        text, sents, para_ends = "", [], []
        for pi, para in enumerate(self.paras):
            if pi: text += "\n\n"
            for si, (s, role) in enumerate(para):
                if si: text += " "
                if role == "edit" and edit_new is not None: s = edit_new
                a = len(text); text += s
                sents.append({"start": a, "end": len(text), "role": role, "para": pi, "text": s})
            para_ends.append(len(text))
        return text, sents, para_ends


def ntok(tok, text):
    return len(tok(text, add_special_tokens=False)["input_ids"])


def take(pool, rng, target, tok):
    out, n = [], 0
    while n < target:
        p = pool[rng.randrange(len(pool))]
        out.append(p); n += ntok(tok, p) + 2
    return out


def make_item(cell, seed, pool, tok):
    """Model-independent item. tok = reference tokenizer for distances (exact token spans are per model, at run)."""
    rng = random.Random(f"{cell}-{seed}")
    e = rng.choice(ENTITIES)
    a_old, a_new = rng.sample(ALIASES, 2)
    code = lambda: f"{rng.choice(LETTERS)}{rng.randint(1, 9)}"
    d = Doc()
    for p in take(pool, rng, PREFIX_TOK, tok): d.add_para([(s, "fill") for s in split_sentences(p)])
    host = split_sentences(pool[rng.randrange(len(pool))])[:2]
    attr = "code"; queried = []
    if cell == "direct":
        c_old, c_new = code(), code()
        while c_new == c_old: c_new = code()
        edit_old = f"The current record states that Company {e}'s code is {c_old}."
        edit_new = f"The current record states that Company {e}'s code is {c_new}."
        d.add_para([(edit_old, "edit")] + [(s, "fill") for s in host])
        rule = ""; ans_old, ans_new = c_old, c_new
        erratum = f"[STATE UPDATE] Company {e}: code -> {c_new} (was {c_old}). This overrides any earlier value and conclusion."
        dep_groups = []
    else:
        edit_old, edit_new = f"Company {e} uses alias {a_old}.", f"Company {e} uses alias {a_new}."
        erratum = f"[STATE UPDATE] Company {e}: alias -> {a_new} (was {a_old}). This overrides any earlier value and conclusion."
        dist = {"derived_d0": 0, "derived_d250": 250, "derived_d1500": 1500, "noisy_d250": 250,
                "indirect_d250": 250, "indirect_d1500": 1500}.get(cell, 250)
        new_key, old_key = a_new, a_old

        def rows(lines):  # two lines, random order (row order matters for graphs built before the edit)
            rng.shuffle(lines); return lines

        if cell == "hop3":
            g_old, g_new = rng.sample(GROUPS, 2)
            c_old, c_new = code(), code()
            while c_new == c_old: c_new = code()
            stages = [rows([(f"Alias {a_old} belongs to group {g_old}.", "dep0"), (f"Alias {a_new} belongs to group {g_new}.", "dep0")]),
                      rows([(f"Group {g_old} has code {c_old}.", "dep1"), (f"Group {g_new} has code {c_new}.", "dep1")])]
            rule = f"Company {e}'s code is the code of the group that its alias belongs to. "
            queried = ["dep1"]
        elif cell == "fanout3":
            vals = {}
            stages = []
            for k, at in enumerate(ATTRS):
                vo, vn = code(), code()
                while vn == vo: vn = code()
                vals[at] = (vo, vn)
                stages.append(rows([(f"Alias {a_old} has {at} {vo}.", f"dep{k}"), (f"Alias {a_new} has {at} {vn}.", f"dep{k}")]))
            qk = rng.randrange(3); attr = ATTRS[qk]; c_old, c_new = vals[attr]
            rule = f"Company {e}'s {attr} is the {attr} of the alias it uses. "
            queried = [f"dep{qk}"]
        elif cell.startswith("indirect"):
            o_old, o_new = rng.sample(range(len(ORDS)), 2)
            edit_old, edit_new = f"Company {e} uses the {ORDS[o_old]} plan.", f"Company {e} uses the {ORDS[o_new]} plan."
            erratum = f"[STATE UPDATE] Company {e}: plan -> {ORDS[o_new]} (was {ORDS[o_old]}). This overrides any earlier value and conclusion."
            c_old, c_new = code(), code()
            while c_new == c_old: c_new = code()
            stages = [rows([(f"Plan {NUMS[o_old]} maps to code {c_old}.", "dep0"), (f"Plan {NUMS[o_new]} maps to code {c_new}.", "dep0")])]
            rule = f"Company {e}'s code is the code of the plan it uses. "
            queried = ["dep0"]
            new_key, old_key = f"Plan {NUMS[o_new]}", f"Plan {NUMS[o_old]}"
        else:
            c_old, c_new = code(), code()
            while c_new == c_old: c_new = code()
            stages = [rows([(f"Alias {a_old} maps to code {c_old}.", "dep0"), (f"Alias {a_new} maps to code {c_new}.", "dep0")])]
            rule = f"Company {e}'s code is the code of the alias it uses. "
            queried = ["dep0"]
        ans_old, ans_new = c_old, c_new
        noise = [n.format(e=e) for n in NOISE] if cell == "noisy_d250" else []
        if dist == 0:
            d.add_para([(edit_old, "edit")] + stages[0] + [(s, "fill") for s in host])
            stages = stages[1:]
        else:
            d.add_para([(edit_old, "edit")] + [(s, "fill") for s in host])
        for st in stages:
            gap = take(pool, rng, max(0, dist - ntok(tok, " ".join(host))) if st is stages[0] and dist else 250, tok)
            for gi, p in enumerate(gap):
                sents = [(s, "fill") for s in split_sentences(p)]
                if noise and gi == 0: sents.insert(1, (noise.pop(), "noise"))
                d.add_para(sents)
            hp = split_sentences(pool[rng.randrange(len(pool))])
            d.add_para(st + [(s, "fill") for s in hp])
        dep_groups = sorted({r for para in d.paras for _, r in para if r.startswith("dep")})
    tail = take(pool, rng, TAIL_TOK, tok)
    for ti, p in enumerate(tail):
        sents = [(s, "fill") for s in split_sentences(p)]
        if cell == "noisy_d250" and ti < 2: sents.insert(1, (NOISE[ti].format(e=e), "noise"))
        d.add_para(sents)
    text_old, sents_old, para_ends = d.render()
    text_new, sents_new, _ = d.render(edit_new=edit_new)
    question = f"{rule}What {attr} applies to Company {e}?" if cell != "direct" else f"What is the code of Company {e}?"
    deps = [x for x in sents_new if x["role"].startswith("dep")]
    new_first = None
    if cell != "direct" and deps:  # does the row the edit makes relevant come before the row it made irrelevant?
        new_first = (new_key + " ") in (deps[0]["text"] + " ")
    return {"id": f"{cell}-{seed}", "cell": cell, "seed": seed, "entity": e, "alias_old": a_old if cell != "direct" else None,
            "alias_new": a_new if cell != "direct" else None, "text_old": text_old, "text_new": text_new,
            "sentences": sents_new, "para_ends": para_ends, "edit_old": edit_old, "edit_new": edit_new,
            "question": question, "attr": attr, "ans_old": ans_old, "ans_new": ans_new, "erratum": erratum,
            "dep_roles": dep_groups, "queried_roles": queried or dep_groups, "new_first": new_first}


def token_view(item, tok):
    """Per-tokenizer token ids and spans. None if the edit is not length-preserving and contiguous in the edit sentence."""
    eo = tok(item["text_old"], return_offsets_mapping=True, add_special_tokens=False)
    en = tok(item["text_new"], return_offsets_mapping=True, add_special_tokens=False)
    io, inew = eo["input_ids"], en["input_ids"]
    if len(io) != len(inew): return None
    changed = [i for i, (x, y) in enumerate(zip(io, inew)) if x != y]
    if not changed or changed[-1] - changed[0] + 1 != len(changed): return None
    offs = en["offset_mapping"]
    starts = [o[0] for o in offs]; ends = [o[1] for o in offs]

    def span(a, b):
        i, j = bisect.bisect_right(ends, a), bisect.bisect_left(starts, b)
        return (i, j) if j > i else None

    sent_spans = [span(s["start"], s["end"]) for s in item["sentences"]]
    if any(x is None for x in sent_spans): return None
    edit_i = next(i for i, s in enumerate(item["sentences"]) if s["role"] == "edit")
    es = sent_spans[edit_i]
    if changed[0] < es[0] or changed[-1] >= es[1]: return None
    para_end_tok = [bisect.bisect_left(starts, pe) for pe in item["para_ends"]]
    ao, an = tok(item["ans_old"], add_special_tokens=False)["input_ids"], tok(item["ans_new"], add_special_tokens=False)["input_ids"]
    if len(ao) != len(an): return None
    return {"ids_old": io, "ids_new": inew, "changed": changed, "sent_spans": sent_spans, "edit_i": edit_i,
            "para_end_tok": para_end_tok, "ans_old_ids": ao, "ans_new_ids": an}


# ------------------------------------------------------------------------------------------- edit-time word index

WORD = re.compile(r"[A-Za-z][A-Za-z0-9']*|\d+[A-Za-z]*")


def index_graph(item, max_hops=3, rare_df=3):
    """Deployable dependency finder built at edit time, no model and no oracle.
    Seeds = words that differ between the old and new edited sentence. A later sentence is reached if it contains a
    seed; its rare words (in at most `rare_df` sentences, not stopwords) become seeds for the next hop."""
    sents = item["sentences"]
    # seeds: words the edit changed; later hops: names and codes (capitalised or containing a digit) that are rare
    words = [set(w.lower() for w in WORD.findall(s["text"])) for s in sents]
    names = [set(w.lower() for w in WORD.findall(s["text"]) if w[0].isupper() or any(c.isdigit() for c in w)) for s in sents]
    df = collections.Counter(w for ws in words for w in ws)
    old = set(w.lower() for w in WORD.findall(item["edit_old"])); new = set(w.lower() for w in WORD.findall(item["edit_new"]))
    seeds = (old ^ new) - STOP
    edit_i = next(i for i, s in enumerate(sents) if s["role"] == "edit")
    reached, frontier = set(), seeds
    for _ in range(max_hops):
        if not frontier: break
        hit = {i for i in range(edit_i + 1, len(sents)) if i not in reached and words[i] & frontier}
        if not hit: break
        reached |= hit
        frontier = {w for i in hit for w in names[i] if df[w] <= rare_df and w not in STOP} - seeds
        seeds |= frontier
    return sorted(reached)


# ------------------------------------------------------------------------------------------- LLM graph (optional)

DEPENDENCE_RULE = ("Sentence j depends on an earlier sentence i if a reader needs sentence i to use or interpret sentence j, "
                   "or if changing a name, alias, code, or value in sentence i could change what sentence j means or what a "
                   "reader concludes from it. Sharing only a general topic is not dependence.")


def llm_graph(item, client, model="gpt-4o-mini"):
    """Built once from the ORIGINAL document (before any edit), as a storage-time system would."""
    texts = [s["text"] for s in item["sentences"]]
    ei = next(i for i, s in enumerate(item["sentences"]) if s["role"] == "edit")
    texts[ei] = item["edit_old"]
    prompt = ("Document, one sentence per line:\n" + "\n".join(f"{i}: {t}" for i, t in enumerate(texts)) + f"\n\n{DEPENDENCE_RULE}\n"
              'List every dependency as a pair [i, j] with i < j (sentence j depends on sentence i). Return only JSON {"edges": [[i, j], ...]}.')
    for attempt in range(5):
        try:
            r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}], temperature=0,
                                               response_format={"type": "json_object"}, seed=42)
            raw = r.choices[0].message.content
            pairs = json.loads(raw).get("edges", [])
            found = []

            def collect(x):
                if isinstance(x, (list, tuple)):
                    if len(x) == 2 and all(isinstance(n, (int, float)) for n in x): found.append(x)
                    else:
                        for y in x: collect(y)
            collect(pairs)
            edges = sorted({tuple(sorted((int(a), int(b)))) for a, b in found if 0 <= int(a) < len(texts) and 0 <= int(b) < len(texts) and a != b})
            later = collections.defaultdict(list)
            for a, b in edges: later[a].append(b)
            seen, stack = set(), [ei]
            while stack:
                for j in later.get(stack.pop(), []):
                    if j > ei and j not in seen: seen.add(j); stack.append(j)
            return {"reached": sorted(seen), "n_edges": len(edges), "usage": [r.usage.prompt_tokens, r.usage.completion_tokens]}
        except Exception as e:
            time.sleep(3 * 2 ** attempt)
    return None


def llm_edit(item, client, model="gpt-4o-mini"):
    """Asked AT EDIT TIME: which later sentences depend on the edited sentence, given its old and new text."""
    texts = [s["text"] for s in item["sentences"]]
    ei = next(i for i, s in enumerate(item["sentences"]) if s["role"] == "edit")
    prompt = ("Document, one sentence per line:\n" + "\n".join(f"{i}: {t}" for i, t in enumerate(texts)) +
              f"\n\nSentence {ei} has just been edited. It used to read: \"{item['edit_old']}\" It now reads: \"{item['edit_new']}\"\n"
              f"{DEPENDENCE_RULE}\nWhich later sentences (number greater than {ei}) depend on sentence {ei} after this edit, directly "
              'or through other sentences? Return only JSON {"sentences": [j, ...]}.')
    for attempt in range(5):
        try:
            r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}], temperature=0,
                                               response_format={"type": "json_object"}, seed=42)
            got = json.loads(r.choices[0].message.content).get("sentences", [])
            flat = []

            def collect(x):
                if isinstance(x, (list, tuple)):
                    for y in x: collect(y)
                elif isinstance(x, (int, float)): flat.append(int(x))
            collect(got)
            return {"reached": sorted({j for j in flat if ei < j < len(texts)}), "usage": [r.usage.prompt_tokens, r.usage.completion_tokens]}
        except Exception:
            time.sleep(3 * 2 ** attempt)
    return None


def short(m):
    return m.replace("gpt-", "").replace("-", "").replace(".", "")


# ------------------------------------------------------------------------------------------- build

def load_tokenizer(key, log):
    from transformers import AutoTokenizer
    for repo in MODELS[key]:
        try:
            t = AutoTokenizer.from_pretrained(repo)
            log(f"tokenizer {key}: {repo}")
            return t, repo
        except Exception as e:
            log(f"tokenizer {key}: {repo} not accessible ({type(e).__name__}); trying next")
    raise RuntimeError(f"no accessible repo for {key}")


def cmd_build(args):
    log = make_log(args.out_dir)
    toks = {k: load_tokenizer(k, log)[0] for k in MODELS}
    ref = toks["qwen3"]
    pool = load_filler(log)
    client = None
    cells = CELLS_INDIRECT if args.cells == "indirect" else CELLS
    llm_models = [m for m in os.environ.get("LLM_MODELS", "gpt-4o-mini,gpt-4.1").split(",") if m] if args.cells == "indirect" else ["gpt-4o-mini"]
    if os.environ.get("OPENAI_API_KEY") and not args.no_llm:
        from openai import OpenAI
        client = OpenAI(); log(f"LLM graphs: {llm_models}" + (" (before the edit, and asked at edit time)" if args.cells == "indirect" else ""))
    else:
        log("LLM graphs: off (no OPENAI_API_KEY)")
    items, rejected, usage = [], collections.Counter(), [0, 0]
    for cell in cells:
        n, seed = 0, 0
        while n < args.n and seed < args.n * 4:
            it = make_item(cell, seed, pool, ref); seed += 1
            if any(token_view(it, t) is None for t in toks.values()):
                rejected[cell] += 1; continue
            it["index_reached"] = index_graph(it)
            items.append(it); n += 1
        log(f"  {cell}: {n} items ({rejected[cell]} rejected as not length-preserving in some tokenizer)")
    cost = 0.0
    if client:  # LLM graphs, 8 calls at a time
        import concurrent.futures as cf
        jobs = [("pre", m) for m in llm_models] + ([("edit", m) for m in llm_models] if args.cells == "indirect" else [])
        for kind, m in jobs:
            fn = (lambda x, m=m: llm_graph(x, client, m)) if kind == "pre" else (lambda x, m=m: llm_edit(x, client, m))
            u = [0, 0]
            with cf.ThreadPoolExecutor(8) as ex:
                for it, g in zip(items, ex.map(fn, items)):
                    it.setdefault(f"llm_{kind}", {})[m] = g["reached"] if g else None
                    if g: u = [u[0] + g["usage"][0], u[1] + g["usage"][1]]
            pr = PRICES.get(m, (2.5, 10.0)); c = u[0] / 1e6 * pr[0] + u[1] / 1e6 * pr[1]; cost += c
            log(f"  LLM {kind}-edit graphs with {m}: done, ${c:.2f}")
        for it in items:  # the main run's gp_llm / gp_hybrid arms use gpt-4o-mini's graph built before the edit
            it["llm_reached"] = it.get("llm_pre", {}).get("gpt-4o-mini")
    path = os.path.join(args.out_dir, "items.jsonl" if args.cells != "indirect" else "items_indirect.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for it in items: f.write(json.dumps(it) + "\n")
    log(f"built {len(items)} items -> {path}; LLM graph cost ${cost:.2f}")
    # graph quality against the construction's ground truth (model-independent)
    for cell in cells:
        sub = [it for it in items if it["cell"] == cell and it["dep_roles"]]
        if not sub: continue
        q = [graph_quality(it, it["index_reached"]) for it in sub]
        line = f"  {cell}: index recall {statistics.mean(x[0] for x in q):.2f} (extra {statistics.mean(x[1] for x in q):.1f})"
        for kind in ("pre", "edit"):
            for m in llm_models:
                qs = [graph_quality(it, it[f"llm_{kind}"][m]) for it in sub if it.get(f"llm_{kind}", {}).get(m) is not None]
                if qs: line += f"; {kind}-edit {m} recall {statistics.mean(x[0] for x in qs):.2f} (extra {statistics.mean(x[1] for x in qs):.1f})"
        log(line)


def graph_quality(it, reached):
    truth = {i for i, s in enumerate(it["sentences"]) if s["role"].startswith("dep")}
    got = set(reached or [])
    return (len(truth & got) / len(truth) if truth else 1.0, len(got - truth))


# ------------------------------------------------------------------------------------------- model runtime (GPU)

class Runner:
    """Own forward pass over a preallocated KV cache, so arbitrary position sets can be recomputed in place.
    Works for Llama-, Mistral- and Qwen3-style decoders (Qwen3 adds per-head q_norm/k_norm)."""
    def __init__(self, model):
        import torch
        self.torch = torch
        self.model = model; self.m = model.model; cfg = model.config
        self.L = len(self.m.layers)
        self.nh, self.nkv = cfg.num_attention_heads, cfg.num_key_value_heads
        self.hd = getattr(cfg, "head_dim", None) or cfg.hidden_size // cfg.num_attention_heads
        self.groups = self.nh // self.nkv
        att = self.m.layers[0].self_attn
        self.scale = getattr(att, "scaling", self.hd ** -0.5)
        self.qk_norm = hasattr(att, "q_norm")
        self.dev = next(model.parameters()).device; self.dtype = next(model.parameters()).dtype
        sw = getattr(cfg, "sliding_window", None)
        self.sliding = sw if (sw and getattr(cfg, "use_sliding_window", True)) else None

    def new_cache(self, cap):
        t = self.torch
        return ([t.zeros(1, self.nkv, cap, self.hd, device=self.dev, dtype=self.dtype) for _ in range(self.L)],
                [t.zeros(1, self.nkv, cap, self.hd, device=self.dev, dtype=self.dtype) for _ in range(self.L)])

    def clone(self, cache, upto=None):
        K, V = cache
        return ([k.clone() for k in K], [v.clone() for v in V])

    @staticmethod
    def _cat(a, b):
        import torch
        return torch.cat((a, b), dim=-1)

    def run(self, cache, ids, positions, want_logits=False, track_span=None, track_layers=None, chunk=512):
        """Recompute `positions` (sorted list of ints) with token `ids` (list) into `cache` IN PLACE.
        Each position attends to every cached key at or before it. Returns logits of the given positions (float32)
        if want_logits; if track_span=(a, b), also returns per-query attention mass on keys a..b-1."""
        t = self.torch
        F = t.nn.functional
        pos = t.tensor(positions, device=self.dev, dtype=t.long)
        S = len(positions); kv_len = int(positions[-1]) + 1
        x = t.tensor([ids], device=self.dev, dtype=t.long)
        h = self.m.embed_tokens(x)
        cos, sin = self.m.rotary_emb(h, pos[None])
        cos, sin = cos[:, None], sin[:, None]
        keypos = t.arange(kv_len, device=self.dev)
        K, V = cache
        mass = t.zeros(S, device=self.dev, dtype=t.float32) if track_span else None
        nl = 0
        for li, layer in enumerate(self.m.layers):
            att = layer.self_attn
            xn = layer.input_layernorm(h)
            q = att.q_proj(xn).view(1, S, self.nh, self.hd)
            k = att.k_proj(xn).view(1, S, self.nkv, self.hd)
            v = att.v_proj(xn).view(1, S, self.nkv, self.hd)
            if self.qk_norm:
                q = att.q_norm(q); k = att.k_norm(k)
            q, k, v = q.transpose(1, 2), k.transpose(1, 2), v.transpose(1, 2)
            q = q * cos + self._cat(-q[..., self.hd // 2:], q[..., : self.hd // 2]) * sin
            k = k * cos + self._cat(-k[..., self.hd // 2:], k[..., : self.hd // 2]) * sin
            K[li][:, :, pos] = k; V[li][:, :, pos] = v
            Kf = K[li][:, :, :kv_len].repeat_interleave(self.groups, dim=1)
            Vf = V[li][:, :, :kv_len].repeat_interleave(self.groups, dim=1)
            outs = []
            for c0 in range(0, S, chunk):
                qc = q[:, :, c0:c0 + chunk]
                mask = (keypos[None, :] <= pos[c0:c0 + chunk, None])[None, None]
                outs.append(F.scaled_dot_product_attention(qc, Kf, Vf, attn_mask=mask, scale=self.scale))
                if track_span and (track_layers is None or li in track_layers):
                    sc = (qc.float() @ Kf.float().transpose(-1, -2)) * self.scale
                    sc = sc.masked_fill(~mask, float("-inf")).softmax(-1)
                    mass[c0:c0 + chunk] += sc[..., track_span[0]:track_span[1]].sum(-1).mean(1)[0]
                    nl += 1 if c0 == 0 else 0
            o = t.cat(outs, dim=2).transpose(1, 2).reshape(1, S, -1)
            h = h + att.o_proj(o)
            h = h + layer.mlp(layer.post_attention_layernorm(h))
        res = []
        if want_logits:
            res.append(self.model.lm_head(self.m.norm(h))[0].float())
        if track_span:
            res.append(mass / max(1, nl))
        return res


def cmd_run(args):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    log = make_log(args.out_dir, f"log_{args.model}.txt")
    torch.manual_seed(0)
    tok, repo = load_tokenizer(args.model, log)
    try:
        model = AutoModelForCausalLM.from_pretrained(repo, dtype=torch.bfloat16, device_map="cuda", attn_implementation="sdpa")
    except TypeError:
        model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map="cuda", attn_implementation="sdpa")
    model.eval()
    R = Runner(model)
    log(f"== run {args.model} ({repo}) on {torch.cuda.get_device_name(0)}: layers {R.L}, heads {R.nh}/{R.nkv}, head_dim {R.hd}, "
        f"qk_norm {R.qk_norm}, sliding {R.sliding}")
    prefix_ids, suffix_tpl = chat_parts(tok, args.model)
    items = [json.loads(l) for l in open(args.items, encoding="utf-8")]
    items.sort(key=lambda it: (it["seed"], ALL_CELLS.index(it["cell"])))  # interleave cells so partial results cover all
    if args.limit:
        per = collections.Counter(); keep = []
        for it in items:
            if per[it["cell"]] < args.limit: keep.append(it); per[it["cell"]] += 1
        items = keep
    tag = {"followup": "_followup", "indirect": "_indirect"}.get(args.arms, "") + ("_smoke" if args.limit else "")
    out_path = os.path.join(args.out_dir, f"results_{args.model}{tag}.jsonl")
    done = set()
    if os.path.exists(out_path):
        done = {json.loads(l)["id"] for l in open(out_path, encoding="utf-8")}
    with torch.no_grad():
        integrity(R, tok, model, prefix_ids, items[0], log)
        fout = open(out_path, "a", encoding="utf-8")
        t0 = time.time()
        for n, it in enumerate(items):
            if it["id"] in done: continue
            try:
                rec = evaluate(R, tok, prefix_ids, suffix_tpl, it, args)
            except Exception as e:
                rec = {"id": it["id"], "cell": it["cell"], "error": repr(e)[:400]}
                log(f"  {it['id']}: ERROR {traceback.format_exc()[-600:]}")
            fout.write(json.dumps(rec) + "\n"); fout.flush()
            if (n + 1) % 10 == 0 or n == len(items) - 1:
                log(f"  {args.model}: {n + 1}/{len(items)} items, {time.time() - t0:.0f}s")
        fout.close()
    log(f"== {args.model} done -> {out_path}")


def chat_parts(tok, key):
    """Token ids before the document, and a function giving the ids after it (question + chat closing)."""
    marker_d, marker_q = "<<<DOC>>>", "<<<Q>>>"
    content = f"{INSTR}\n\nDocument:\n{marker_d}\n\nQuestion: {marker_q}"
    kw = {"enable_thinking": False} if key == "qwen3" else {}
    rendered = tok.apply_chat_template([{"role": "user", "content": content}], tokenize=False, add_generation_prompt=True, **kw)
    pre, rest = rendered.split(marker_d)
    mid, post = rest.split(marker_q)
    prefix_ids = tok(pre, add_special_tokens=False)["input_ids"]

    def suffix(question, attr, erratum=None):
        q = f"{mid}{question}\nAnswer with the {attr} only.{post}"
        return tok(q, add_special_tokens=False)["input_ids"]
    return prefix_ids, suffix


def integrity(R, tok, model, prefix_ids, item, log):
    """(1) our forward matches the library forward; (2) recomputing every position of the stale cache with the edited
    text reproduces a fresh prefill of the edited text."""
    import torch
    v = token_view(item, tok)
    ids = prefix_ids + v["ids_new"][:400]
    cache = R.new_cache(len(ids) + 8)
    ours = R.run(cache, ids, list(range(len(ids))), want_logits=True)[0][-1]
    ref = model(input_ids=torch.tensor([ids], device=R.dev)).logits[0, -1].float()
    rel = ((ours - ref).abs().max() / ref.abs().max()).item()
    top_ours, top_ref = set(ours.topk(5).indices.tolist()), set(ref.topk(5).indices.tolist())
    log(f"integrity 1: max relative logit difference {rel:.4f}; top-5 overlap {len(top_ours & top_ref)}/5; argmax equal {ours.argmax().item() == ref.argmax().item()}")
    if rel > 0.05 or ours.argmax().item() != ref.argmax().item():
        raise RuntimeError("our forward pass does not match the library's; stopping")
    P = len(prefix_ids); T = P + len(v["ids_new"])
    stale = R.new_cache(T + 8); R.run(stale, prefix_ids + v["ids_old"], list(range(T)))
    fresh = R.new_cache(T + 8); R.run(fresh, prefix_ids + v["ids_new"], list(range(T)))
    rep = R.clone(stale); R.run(rep, prefix_ids + v["ids_new"], list(range(T)))
    err = max((a[:, :, :T].float() - b[:, :, :T].float()).abs().max().item() for a, b in zip(rep[0], fresh[0]))
    scale = max(b[:, :, :T].float().abs().max().item() for b in fresh[0])
    log(f"integrity 2: full recompute vs fresh prefill, max key difference {err:.4f} (key scale {scale:.1f})")
    if err > 0.02 * scale:
        raise RuntimeError("recomputing every position does not reproduce a fresh prefill; stopping")
    del stale, fresh, rep
    torch.cuda.empty_cache()


def evaluate(R, tok, prefix_ids, suffix_fn, it, args):
    import torch
    v = token_view(it, tok)
    P = len(prefix_ids); n_doc = len(v["ids_new"]); T = P + n_doc
    old_ids, new_ids = prefix_ids + v["ids_old"], prefix_ids + v["ids_new"]
    suffix = suffix_fn(it["question"], it["attr"])
    err_ids = tok("\n\n" + it["erratum"], add_special_tokens=False)["input_ids"]
    cap = T + len(err_ids) + len(suffix) + 24
    ch = [c + P for c in v["changed"]]; edit_start, edit_end = ch[0], ch[-1] + 1
    sp = [(a + P, b + P) for a, b in v["sent_spans"]]
    roles = [s["role"] for s in it["sentences"]]
    dep = [i for i, r in enumerate(roles) if r.startswith("dep")]
    qdep = [i for i, r in enumerate(roles) if r in it["queried_roles"]]
    edit_para = it["sentences"][v["edit_i"]]["para"]
    para_end = v["para_end_tok"][edit_para] + P

    # stale prefill, with attention mass from every position to the edited sentence (for the attention arm)
    es = sp[v["edit_i"]]
    stale = R.new_cache(cap)
    mass = R.run(stale, old_ids, list(range(T)), track_span=es, track_layers=set(range(0, R.L, 4)))[0]
    oracle = R.new_cache(cap); R.run(oracle, new_ids, list(range(T)))

    def score(cache, extra_ids=None):
        """Margin (new - old answer, length-averaged log-prob, teacher forced) and greedy answer text."""
        c = R.clone(cache); start = T
        if extra_ids:
            R.run(c, extra_ids, list(range(T, T + len(extra_ids)))); start = T + len(extra_ids)
        lg = R.run(c, suffix, list(range(start, start + len(suffix))), want_logits=True)[0]
        s_end = start + len(suffix)
        out = {}
        for name, ans in (("new", v["ans_new_ids"]), ("old", v["ans_old_ids"])):
            lp = torch.log_softmax(lg[-1], -1)[ans[0]].item()
            if len(ans) > 1:
                l2 = R.run(c, ans[:-1], list(range(s_end, s_end + len(ans) - 1)), want_logits=True)[0]
                lp += sum(torch.log_softmax(l2[j], -1)[ans[j + 1]].item() for j in range(len(ans) - 1))
            out[name] = lp / len(ans)
        gen, nxt, p = [], int(lg[-1].argmax().item()), s_end
        for _ in range(8):
            if nxt == tok.eos_token_id or tok.decode([nxt]).strip() == "" and gen: break
            gen.append(nxt)
            nxt = int(R.run(c, [nxt], [p], want_logits=True)[0][-1].argmax().item()); p += 1
        text = tok.decode(gen, skip_special_tokens=True)
        del c
        return out["new"] - out["old"], text

    def has(text, code):
        return re.search(rf"(?<![A-Za-z0-9]){re.escape(code)}(?![0-9])", text) is not None

    m_stale, g_stale = score(stale)
    m_or, g_or = score(oracle)
    gap = m_or - m_stale
    rec = {"id": it["id"], "cell": it["cell"], "new_first": it.get("new_first"), "n_doc": n_doc, "gap": gap, "m_stale": m_stale, "m_oracle": m_or,
           "gen_stale": g_stale, "gen_oracle": g_or,
           "dist_tokens": (sp[dep[0]][0] - edit_end) if dep else 0}
    kept = gap >= 1.0 and m_or > 0 and has(g_or, it["ans_new"]) and not has(g_or, it["ans_old"]) and not has(g_stale, it["ans_new"])
    rec["kept"] = kept
    rec["reject"] = None if kept else ("gap" if gap < 1.0 or m_or <= 0 else "oracle_answer" if not (has(g_or, it["ans_new"]) and not has(g_or, it["ans_old"])) else "stale_answer")
    if not kept:
        return rec

    def upto(i):
        return sp[i][1]
    last_dep = max((upto(i) for i in dep), default=edit_end)
    idx = it.get("index_reached") or []
    llm = it.get("llm_reached")
    arms = {"none": [], "edit_only": ch}
    for k in (32, 64, 128, 256, 512, 1024):
        arms[f"el{k}"] = ch + list(range(edit_end, min(T, edit_end + k)))
    arms["boundary"] = ch + list(range(edit_end, max(edit_end, para_end)))
    if dep:
        a0 = sp[qdep[0]][0]
        arms["carrier32"] = ch + list(range(a0, min(T, a0 + 32)))
        arms["carrier_rows"] = sorted(set(ch) | {p for i in dep for p in range(*sp[i])})
        arms["gp_oracle"] = ch + list(range(edit_end, last_dep))
    arms["gp_index"] = ch + list(range(edit_end, max((upto(i) for i in idx), default=edit_end)))
    if llm is not None:
        arms["gp_llm"] = ch + list(range(edit_end, max((upto(i) for i in llm), default=edit_end)))
        arms["gp_hybrid"] = ch + list(range(edit_end, max((upto(i) for i in set(llm) | set(idx)), default=edit_end)))
    kb = max(32, len(arms["gp_index"]) - len(ch))
    down = mass[edit_end:].float()
    top = (down.topk(min(kb, len(down))).indices + edit_end).tolist()
    arms["attn_topk"] = sorted(set(ch) | set(top))
    blocks = down[: (len(down) // 32) * 32].view(-1, 32).sum(-1)
    nb = max(1, kb // 32)
    arms["attn_blocks"] = sorted(set(ch) | {edit_end + 32 * b + j for b in blocks.topk(min(nb, len(blocks))).indices.tolist() for j in range(32)})
    arms["suffix"] = list(range(edit_start, T))
    arms["full"] = list(range(T))
    if getattr(args, "arms", "main") in ("followup", "indirect"):
        # Controls for the matched-budget result. Reference arms first (must reproduce the main run exactly).
        ref = {k: arms[k] for k in ("none", "edit_only", "el32", "carrier_rows", "gp_index", "attn_topk", "full") if k in arms}
        rng = random.Random(f"followup-{it['id']}")
        pop = list(range(edit_end, T))
        f = dict(ref)
        if dep:  # the gap from the edit up to the first dependent sentence, without the dependent sentences
            f["stopshort"] = ch + list(range(edit_end, sp[min(dep)][0]))
        # same budget as the path window, positions chosen at random (tokens, and 32-token blocks)
        f["random_matched"] = sorted(set(ch) | set(rng.sample(pop, min(kb, len(pop)))))
        nblk = len(pop) // 32
        f["random_blocks"] = sorted(set(ch) | {edit_end + 32 * b + j for b in rng.sample(range(nblk), min(nb, nblk)) for j in range(32)})
        # attention without the graph's budget: fixed budgets, and attention deciding where to stop
        for k in (32, 128, 512):
            f[f"attn_k{k}"] = sorted(set(ch) | set((down.topk(min(k, len(down))).indices + edit_end).tolist()))
        for k in (128, 512):
            nbk = max(1, k // 32)
            f[f"attn_blocks_k{k}"] = sorted(set(ch) | {edit_end + 32 * b + j for b in blocks.topk(min(nbk, len(blocks))).indices.tolist() for j in range(32)})
        mx = float(down.max())
        for tau in (0.25, 0.10):
            far = (down >= tau * mx).nonzero().flatten()
            last = edit_end + int(far.max()) + 1 if len(far) else edit_end
            f[f"attn_stop{int(tau * 100)}"] = ch + list(range(edit_end, last))
        if args.arms == "followup":
            arms = f
        else:  # indirect: every main arm, the key controls, and every LLM dependency finder (with and without the index)
            for k in ("stopshort", "random_matched", "attn_k128", "attn_k512"):
                if k in f: arms[k] = f[k]
            path = lambda reached: ch + list(range(edit_end, max((upto(i) for i in reached), default=edit_end)))
            for kind, tagk in (("llm_pre", "pre"), ("llm_edit", "edit")):
                for m, reached in (it.get(kind) or {}).items():
                    if reached is None: continue
                    arms[f"gp_{tagk}_{short(m)}"] = path(reached)
                    arms[f"gp_{tagk}hyb_{short(m)}"] = path(set(reached) | set(idx))
    res = {}
    for name, pos in arms.items():
        pos = sorted(set(pos))
        c = R.clone(stale)
        torch.cuda.synchronize(); t1 = time.perf_counter()
        if pos: R.run(c, [new_ids[p] for p in pos], pos)
        torch.cuda.synchronize(); ms = (time.perf_counter() - t1) * 1000
        m, g = score(c)
        res[name] = {"mr": (m - m_stale) / gap, "acc": float(has(g, it["ans_new"]) and not has(g, it["ans_old"])),
                     "old": float(has(g, it["ans_old"])), "tokens": len(pos), "ms": ms, "gen": g}
        del c
    # erratum arms: append the correction after the document (Li 2606.17107); the in-place cache is stale or partly fixed
    for name, base in () if getattr(args, "arms", "main") == "followup" else (("erratum_bare", []), ("erratum_field", ch), ("erratum_el32", arms["el32"])):
        c = R.clone(stale)
        if base: R.run(c, [new_ids[p] for p in sorted(set(base))], sorted(set(base)))
        m, g = score(c, extra_ids=err_ids)
        res[name] = {"mr": (m - m_stale) / gap, "acc": float(has(g, it["ans_new"]) and not has(g, it["ans_old"])),
                     "old": float(has(g, it["ans_old"])), "tokens": len(set(base)) + len(err_ids), "ms": None, "gen": g}
        del c
    rec["arms"] = res
    rec["graph"] = {"index_recall_extra": graph_quality(it, idx), "llm_recall_extra": graph_quality(it, llm) if llm is not None else None}
    del stale, oracle
    torch.cuda.empty_cache()
    return rec


# ------------------------------------------------------------------------------------------- analysis

def boot_mean(xs, n=2000, seed=1):
    xs = [x for x in xs if x is not None and not (isinstance(x, float) and math.isnan(x))]
    if not xs: return (float("nan"),) * 3
    rng = random.Random(seed)
    bs = sorted(sum(rng.choice(xs) for _ in xs) / len(xs) for _ in range(n))
    return sum(xs) / len(xs), bs[int(0.025 * n)], bs[int(0.975 * n) - 1]


def paired(a, b, n=2000):
    d = [x - y for x, y in zip(a, b)]
    return boot_mean(d, n)


ARM_ORDER = ["none", "edit_only", "el32", "el64", "el128", "el256", "el512", "el1024", "boundary", "carrier32", "carrier_rows",
             "attn_topk", "attn_blocks", "erratum_bare", "erratum_field", "erratum_el32", "gp_index", "gp_llm", "gp_hybrid",
             "gp_oracle", "suffix", "full", "stopshort", "random_matched", "random_blocks", "attn_k32", "attn_k128", "attn_k512",
             "attn_blocks_k128", "attn_blocks_k512", "attn_stop25", "attn_stop10"]


def cmd_analyze(args):
    out = {"models": {}}
    md = ["# KV repair results", ""]
    for mk in MODELS:
        path = os.path.join(args.out_dir, f"results_{mk}{args.tag}.jsonl")
        if not os.path.exists(path): continue
        recs = [json.loads(l) for l in open(path, encoding="utf-8")]
        errs = [r for r in recs if "error" in r]
        kept = [r for r in recs if r.get("kept")]
        md += [f"## {mk}", "", f"{len(recs)} items, {len(kept)} kept, {len(errs)} errors; rejected: "
               + json.dumps(collections.Counter(r.get("reject") for r in recs if not r.get("kept") and "error" not in r)), ""]
        out["models"][mk] = {}
        for cell in ALL_CELLS:
            rs = [r for r in kept if r["cell"] == cell]
            if not rs: continue
            present = sorted({a for r in rs for a in r["arms"]})
            arm_list = [a for a in ARM_ORDER if a in present] + [a for a in present if a not in ARM_ORDER]
            md += [f"### {mk} / {cell} (n={len(rs)}, median distance {statistics.median(r['dist_tokens'] for r in rs):.0f} tokens, "
                   f"median doc {statistics.median(r['n_doc'] for r in rs):.0f} tokens)", "",
                   "| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |", "|---|---|---|---|---|---|---|"]
            cell_out = {}
            for arm in arm_list:
                vals = [r["arms"][arm] for r in rs if arm in r["arms"]]
                if not vals: continue
                m, lo, hi = boot_mean([x["mr"] for x in vals])
                acc = 100 * statistics.mean(x["acc"] for x in vals); old = 100 * statistics.mean(x["old"] for x in vals)
                tk = statistics.mean(x["tokens"] for x in vals)
                ms = [x["ms"] for x in vals if x["ms"] is not None]
                cell_out[arm] = {"mr": m, "ci": [lo, hi], "median": statistics.median(x["mr"] for x in vals), "acc": acc, "tokens": tk}
                md.append(f"| {arm} | {m:.2f} [{lo:.2f}, {hi:.2f}] | {cell_out[arm]['median']:.2f} | {acc:.0f} | {old:.0f} | {tk:.0f} | "
                          f"{(statistics.mean(ms) if ms else float('nan')):.0f} |")
            md.append("")
            for a, b in (("gp_index", "random_matched"), ("gp_index", "random_blocks"), ("gp_index", "stopshort"), ("gp_index", "attn_stop25"),
                         ("gp_index", "attn_k512"), ("gp_index", "el32"), ("gp_index", "carrier32"), ("gp_index", "erratum_field"), ("gp_index", "attn_blocks"),
                         ("gp_oracle", "gp_index"), ("gp_hybrid", "gp_index"),
                         ("gp_edithyb_4omini", "gp_index"), ("gp_edithyb_41", "gp_index"), ("gp_edithyb_41", "gp_prehyb_41"),
                         ("gp_oracle", "gp_edithyb_41"), ("gp_oracle", "gp_edithyb_4omini")):
                both = [r for r in rs if a in r["arms"] and b in r["arms"]]
                if not both: continue
                d, lo, hi = paired([r["arms"][a]["mr"] for r in both], [r["arms"][b]["mr"] for r in both])
                da, alo, ahi = paired([r["arms"][a]["acc"] for r in both], [r["arms"][b]["acc"] for r in both])
                md.append(f"- {a} minus {b}: MR {d:+.2f} [{lo:+.2f}, {hi:+.2f}]; accuracy {100 * da:+.0f} [{100 * alo:+.0f}, {100 * ahi:+.0f}] points (n={len(both)})")
            # cost frontier: EditLocal sweep vs path window at its mean cost
            el = sorted((cell_out[a]["tokens"], cell_out[a]["mr"]) for a in cell_out if re.fullmatch(r"el\d+", a))
            if "gp_index" in cell_out and len(el) > 1:
                tg = cell_out["gp_index"]["tokens"]
                below = [p for p in el if p[0] <= tg]; above = [p for p in el if p[0] >= tg]
                if below and above:
                    (t0, m0), (t1, m1) = below[-1], above[0]
                    interp = m0 if t1 == t0 else m0 + (m1 - m0) * (math.log(tg) - math.log(t0)) / (math.log(t1) - math.log(t0))
                    md.append(f"- EditLocal at the path window's mean cost ({tg:.0f} tokens, log-interpolated): MR {interp:.2f} vs gp_index {cell_out['gp_index']['mr']:.2f}")
            if cell in CELLS_INDIRECT:  # does the result depend on which row comes first?
                for nf in (True, False):
                    sub = [r for r in rs if r.get("new_first") is nf]
                    if not sub: continue
                    parts = [f"{a} {statistics.mean(r['arms'][a]['mr'] for r in sub if a in r['arms']):.2f}"
                             for a in arm_list if a.startswith("gp_") and all(a in r["arms"] for r in sub)]
                    md.append(f"- rows {'new first' if nf else 'old first'} (n={len(sub)}): " + "; ".join(parts))
            gq = [r["graph"]["index_recall_extra"] for r in rs]
            md += [f"- index graph: dependent recall {statistics.mean(g[0] for g in gq):.2f}, extra sentences {statistics.mean(g[1] for g in gq):.1f}", ""]
            out["models"][mk][cell] = cell_out
    with open(os.path.join(args.out_dir, f"results{args.tag}.md"), "w", encoding="utf-8") as f: f.write("\n".join(md) + "\n")
    with open(os.path.join(args.out_dir, f"results{args.tag}.json"), "w", encoding="utf-8") as f: json.dump(out, f, indent=1)
    print("\n".join(md))


# ------------------------------------------------------------------------------------------- selftest (CPU, no torch)

class StubTok:
    """Whitespace-and-punctuation tokenizer with offsets, enough to test building, spans and the index graph."""
    def __call__(self, text, return_offsets_mapping=False, add_special_tokens=False):
        toks = [(m.start(), m.end()) for m in re.finditer(r"\w+|[^\w\s]", text)]
        ids = [int(hashlib.md5(text[a:b].encode()).hexdigest()[:6], 16) for a, b in toks]
        d = {"input_ids": ids}
        if return_offsets_mapping: d["offset_mapping"] = toks
        return d


def cmd_selftest(args):
    log = make_log(args.out_dir)
    tok = StubTok(); pool = load_filler(lambda m: log(m)) if args.wikitext else load_filler_synth()
    for cell in ALL_CELLS:
        ok, recall, extra, dist = 0, [], [], []
        for seed in range(20):
            it = make_item(cell, seed, pool, tok)
            v = token_view(it, tok)
            if v is None: continue
            ok += 1
            r, x = graph_quality(it, index_graph(it)); recall.append(r); extra.append(x)
            dep = [i for i, s in enumerate(it["sentences"]) if s["role"].startswith("dep")]
            if dep: dist.append(v["sent_spans"][dep[0]][0] - (v["changed"][-1] + 1))
            assert it["text_old"].count(it["edit_old"]) == 1 and it["text_new"].count(it["edit_new"]) == 1
            if cell == "direct": assert it["ans_new"] not in it["text_old"]
        log(f"selftest {cell}: {ok}/20 valid; index recall {statistics.mean(recall) if recall else float('nan'):.2f}; "
            f"extra {statistics.mean(extra) if extra else float('nan'):.1f}; distance to first dependent (stub tokens) "
            f"{statistics.median(dist) if dist else 0:.0f}")
    it = make_item("hop3", 1, pool, tok)
    log("example hop3 dependents: " + " | ".join(s["text"] for s in it["sentences"] if s["role"].startswith("dep")))
    log("example hop3 index reached: " + " | ".join(it["sentences"][i]["text"] for i in index_graph(it)))


def load_filler_synth():
    rng = random.Random(0)
    words = "river valley station market harbour council railway museum garden bridge tower village festival".split()
    return [" ".join(f"The {rng.choice(words)} near the {rng.choice(words)} was rebuilt in {rng.randint(1800, 1990)}." for _ in range(7))
            for _ in range(500)]


def make_log(out_dir, name="log.txt"):
    os.makedirs(out_dir, exist_ok=True)
    f = open(os.path.join(out_dir, name), "a", encoding="utf-8")

    def log(msg):
        print(msg, flush=True); f.write(msg + "\n"); f.flush()
    return log


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("--out-dir", default="out"); b.add_argument("--n", type=int, default=50); b.add_argument("--no-llm", action="store_true")
    b.add_argument("--cells", default="main", choices=["main", "indirect"])
    r = sub.add_parser("run"); r.add_argument("--model", required=True, choices=list(MODELS)); r.add_argument("--items", default="out/items.jsonl")
    r.add_argument("--out-dir", default="out"); r.add_argument("--limit", type=int, default=0)
    r.add_argument("--arms", default="main", choices=["main", "followup", "indirect"])
    a = sub.add_parser("analyze"); a.add_argument("--out-dir", default="out"); a.add_argument("--tag", default="")
    s = sub.add_parser("selftest"); s.add_argument("--out-dir", default="out_selftest"); s.add_argument("--wikitext", action="store_true")
    args = ap.parse_args()
    {"build": cmd_build, "run": cmd_run, "analyze": cmd_analyze, "selftest": cmd_selftest}[args.cmd](args)


if __name__ == "__main__":
    main()

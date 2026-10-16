"""LaTeX tables and figure coordinates for the KV paper, generated from the run artefacts (no hand-copied numbers)."""
import json, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "..", "results")  # repo layout: results/main, results/followup, results/indirect
MAIN = json.load(open(os.path.join(RES, "main", "results.json"), encoding="utf-8"))["models"]
FU = json.load(open(os.path.join(RES, "followup", "results_followup.json"), encoding="utf-8"))["models"]
MODELS = [("qwen3", "Qwen3-8B"), ("llama", "Llama-3.1-8B"), ("mistral", "Mistral-7B")]
CELLS = [("derived_d0", r"derived, $d{=}0$"), ("derived_d250", r"derived, $d{=}250$"), ("derived_d1500", r"derived, $d{=}1500$"),
         ("hop3", "3 hops"), ("fanout3", "fan-out 3"), ("noisy_d250", r"noisy, $d{=}250$")]
BS = "\\"
os.makedirs(os.path.join(HERE, "tables"), exist_ok=True)


def get(m, c, arm):
    for src in (MAIN, FU):
        v = src.get(m, {}).get(c, {}).get(arm)
        if v is not None: return v
    return None


def write(name, rows):
    with open(os.path.join(HERE, "tables", name), "w", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")


def num(x, d=2):
    s = f"{x:.{d}f}"
    if s.startswith("-0.00") or s == "-0.0": s = s[1:]
    return s.replace("-", "$-$")


# Table: MR for every model x cell x key arm
ARMS = ["el32", "carrier32", "carrier_rows", "erratum_field", "gp_llm", "random_matched", "stopshort", "attn_k128", "attn_k512", "gp_index"]
for metric, fname, d in (("mr", "t_mr.tex", 2), ("acc", "t_acc.tex", 0)):
    rows = []
    for mi, (m, mname) in enumerate(MODELS):
        for ci, (c, cname) in enumerate(CELLS):
            n = None
            cells = []
            for a in ARMS:
                v = get(m, c, a)
                if v is None: cells.append("--"); continue
                x = v[metric]
                s = num(x, d)
                if a == "gp_index": s = BS + "textbf{" + s + "}"
                cells.append(s)
            lead = (BS + "multirow{6}{*}{" + mname + "}") if ci == 0 else ""
            rows.append(f"{lead} & {cname} & " + " & ".join(cells) + " " + BS + BS)
        if mi < len(MODELS) - 1: rows.append(BS + "midrule")
    write(fname, rows)

# Table: cost (tokens recomputed), mean over the three models, and EditLocal at the path window's cost
rows = []
for c, cname in CELLS:
    tk = lambda a: statistics.mean(get(m, c, a)["tokens"] for m, _ in MODELS)
    rows.append(f"{cname} & {tk('gp_index'):.0f} & {tk('suffix'):.0f} & {tk('full'):.0f} & {100 * tk('gp_index') / tk('full'):.0f}\\% " + BS + BS)
write("t_cost.tex", rows)

# Figure: EditLocal budget sweep vs path window and attention@512, mean over models
fig = {}
for c in ("derived_d250", "derived_d1500", "hop3"):
    pts = []
    for k in (32, 64, 128, 256, 512, 1024):
        a = f"el{k}"
        pts.append((statistics.mean(get(m, c, a)["tokens"] for m, _ in MODELS), statistics.mean(get(m, c, a)["mr"] for m, _ in MODELS)))
    gp = (statistics.mean(get(m, c, "gp_index")["tokens"] for m, _ in MODELS), statistics.mean(get(m, c, "gp_index")["mr"] for m, _ in MODELS))
    at = (statistics.mean(get(m, c, "attn_k512")["tokens"] for m, _ in MODELS), statistics.mean(get(m, c, "attn_k512")["mr"] for m, _ in MODELS))
    fig[c] = {"el": " ".join(f"({x:.0f},{y:.3f})" for x, y in pts), "gp": f"({gp[0]:.0f},{gp[1]:.3f})", "attn": f"({at[0]:.0f},{at[1]:.3f})"}
json.dump(fig, open(os.path.join(HERE, "tables", "fig.json"), "w"), indent=1)

# Numbers quoted in the text
facts = {}
for m, _ in MODELS:
    recs = [json.loads(l) for l in open(os.path.join(RES, "main", f"results_{m}.jsonl"), encoding="utf-8")]
    kept = [r for r in recs if r.get("kept")]
    facts[m] = {"kept": len(kept), "n": len(recs),
                "dist": {c: statistics.median(r["dist_tokens"] for r in kept if r["cell"] == c) for c, _ in CELLS},
                "doc": {c: statistics.median(r["n_doc"] for r in kept if r["cell"] == c) for c, _ in CELLS},
                "direct": {a: get(m, "direct", a)["mr"] for a in ("edit_only", "gp_index", "el32")},
                "erratum_acc": {c: get(m, c, "erratum_field")["acc"] for c, _ in CELLS},
                "el_at_cost": None}
json.dump(facts, open(os.path.join(HERE, "tables", "facts.json"), "w"), indent=1)
print(json.dumps(fig, indent=1)); print(json.dumps(facts, indent=1))
print(open(os.path.join(HERE, "tables", "t_cost.tex")).read())


# ---------------------------------------------------------------- indirect run (paraphrased dependencies)
import random as _r
IND = os.path.join(RES, "indirect")
ICELLS = [("indirect_d250", r"$d{=}250$"), ("indirect_d1500", r"$d{=}1500$")]


def _boot(x, n=2000):
    g = _r.Random(1); b = sorted(sum(g.choice(x) for _ in x) / len(x) for _ in range(n))
    return sum(x) / len(x), b[int(0.025 * n)], b[int(0.975 * n) - 1]


def _union(r, names):  # windows all start at the edit, so the union of two path windows is the longer one
    return max((r["arms"][a] for a in names if a in r["arms"]), key=lambda x: x["tokens"])


IARMS = [("index", ["gp_index"]), ("pre4omini", ["gp_pre_4omini"]), ("pre41", ["gp_pre_41"]), ("edit41", ["gp_edit_41"]),
         ("both41", ["gp_pre_41", "gp_edit_41"]), ("attn512", ["attn_k512"]), ("oracle", ["gp_oracle"])]
rows, ifacts, order = [], {}, {"new": {k: [] for k, _ in IARMS}, "old": {k: [] for k, _ in IARMS}}
for mi, (m, mname) in enumerate(MODELS):
    recs = [json.loads(l) for l in open(os.path.join(IND, f"results_{m}_indirect.jsonl"), encoding="utf-8")]
    kept = [r for r in recs if r.get("kept")]
    ifacts[m] = {"kept": len(kept), "n": len(recs)}
    for ci, (c, cname) in enumerate(ICELLS):
        sub = [r for r in kept if r["cell"] == c]
        cells = []
        for key, names in IARMS:
            v = [_union(r, names)["mr"] for r in sub]
            mean, lo, hi = _boot(v)
            s = num(mean)
            if key == "both41": s = BS + "textbf{" + s + "}"
            cells.append(s)
            for r in sub: order["new" if r["new_first"] else "old"][key].append(_union(r, names)["mr"])
        acc = 100 * statistics.mean(_union(r, ["gp_pre_41", "gp_edit_41"])["acc"] for r in sub)
        lead = (BS + "multirow{2}{*}{" + mname + "}") if ci == 0 else ""
        rows.append(f"{lead} & {cname} & {len(sub)} & " + " & ".join(cells) + f" & {acc:.0f} " + BS + BS)
    if mi < len(MODELS) - 1: rows.append(BS + "midrule")
write("t_indirect.tex", rows)
rows = []
for key, label in (("pre41", "gpt-4.1, before the edit"), ("edit41", "gpt-4.1, at edit time"), ("both41", "gpt-4.1, both"), ("oracle", "oracle")):
    rows.append(f"{label} & {num(statistics.mean(order['new'][key]))} & {num(statistics.mean(order['old'][key]))} " + BS + BS)
write("t_order.tex", rows)
ifacts["order_n"] = {k: len(v["oracle"]) for k, v in order.items()}
json.dump(ifacts, open(os.path.join(HERE, "tables", "facts_indirect.json"), "w"), indent=1)
print(open(os.path.join(HERE, "tables", "t_indirect.tex")).read()); print(open(os.path.join(HERE, "tables", "t_order.tex")).read()); print(ifacts)

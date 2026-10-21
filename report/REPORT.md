# How Far Does an Edit Reach? Extending "Contiguity, Not Importance" to derived and paraphrased facts

**Team:** Nour Shreif · Hadi Ghazi ([@hadigghazi](https://github.com/hadigghazi)) · Karin Zoabi
**Topic:** grounding and memory (KV-cache reuse after document edits).
**Baseline paper:** Mingyang Mao, Wyatt Mackey, Xiaomin Lin. *Contiguity, Not Importance: Budgeted Repair of Stale KV
Caches After Document Edits.* arXiv:2609.17983, 2026.

The paper (7 pages, IEEE format) is [`paper.pdf`](paper.pdf). `paper/` holds the LaTeX source of an earlier draft (the final
version was edited in Overleaf); its tables
are generated from `../results/` by `paper/make_tables.py`. This report follows the course template and
summarises it.

## Abstract

When a cached document is edited, the cached states of text that depends on the edit go stale. The baseline
repairs them by recomputing a fixed window after the edit, which fails when the answer is a derived fact far
from the edit. The window from the edit to the dependent text is left untested. We test it on Qwen3-8B,
Llama-3.1-8B and Mistral-7B, over 450 items per model and 40 policies, with the stopping point found by a word
index built at edit time:
- for explicit links, it repairs every cell (margin recovery 0.99 to 1.00, 95 to 100% correct answers) at 18
  to 50% of the cost of a re-read, where fixed windows, carrier windows, appended errata and small-LLM graphs
  each fail somewhere;
- for paraphrased links, the index fails, and gpt-4.1 graphs built before and at edit time recover 0.84 to 0.98.

The controls show that repair must reach the dependent text, including the text the edit made irrelevant.

## 1. The baseline paper

### 1.1 Problem

A serving system keeps a document's KV cache to avoid re-reading it. After an in-place edit, every state
computed after the edited text is stale, and re-reading the whole document costs a full prefill. The question
is which positions to recompute within a budget.

### 1.2 Solution

The paper compares training-free repair policies at a matched budget K of recomputed positions. Each
recomputed position attends to the cache, a mix of refreshed and stale states.

- **EditLocal** recomputes the edit plus the next K tokens.
- **CarrierWindow** is an oracle diagnostic: K tokens placed at the text that carries the answer.
- **Importance-based selectors** (attention, deviation, structure) are also compared.

The metric is **margin recovery** (MR): the new-minus-old answer margin, normalised so that the stale cache
scores 0 and a full re-read scores 1.

### 1.3 Results

A contiguous EditLocal window beats importance-based selection (hence the title). On a **derived** benchmark,
where an edited alias selects between two unchanged lookup rows d tokens later, EditLocal@32 recovers 0.01 to
0.09 at d = 250 and 0.01 to 0.02 at d = 1500. CarrierWindow recovers about 0.90 on Qwen but 0.43 on Llama. The
paper names a window from the edit to the dependent text as the next step and does not test it. It releases no
code.

## 2. Our extension

### 2.1 Motivation

Any fixed budget, whether EditLocal or CarrierWindow, can't adapt to how far an edit reaches, and that reach
differs per document. The path window was untested. The appended erratum of Li (arXiv:2606.17107) had not been
tested on derived facts at a distance. Our team's two proofs of concept, by Nour Shreif on Qwen2.5-3B, showed
the path window working on synthetic documents and raised the question of how to find where to stop.

### 2.2 Method

- **Path window:** recompute contiguously from the edit to the end of the furthest dependent sentence, then stop.
- **Edit-time word index** (`index_graph()`): starts from the words that differ between the old and new edited
  sentence and follows rare names and codes for up to three hops. It needs no model.
- **LLM finders** (`llm_graph()`, `llm_edit()`): a dependency graph built from the original document before the
  edit, and a query at edit time given the old and new sentence. Each uses gpt-4o-mini and gpt-4.1.
- **Benchmark** (`make_item()`): 9 cells × 50 items on real WikiText-103 text:
  - direct;
  - derived at d = 0, 250 and 1,500;
  - 3 hops;
  - fan-out 3;
  - noisy;
  - indirect at d = 250 and 1,500.

  Every edit is length-preserving in all three tokenizers, and the row order is random.
- **Validity checks:** the full re-read must improve the margin by at least one nat per token and generate the
  new code, and the stale cache must not.
- **Policies (40):**
  - floors and ceilings;
  - an EditLocal sweep (32 to 1,024 tokens); a paragraph boundary;
  - CarrierWindow; rows only;
  - path windows with oracle, index, LLM or hybrid stopping;
  - erratum variants;
  - attention-picked positions and blocks (matched or fixed budgets, two stopping rules);
  - random positions and blocks at a matched budget; StopShort.

### 2.3 Implementation notes

Everything is in `extension/kvx.py`, with subcommands `build`, `run`, `analyze` and `selftest`.
- Repair uses our own forward pass over a preallocated cache, generalised from the team's proof-of-concept
  operator to Qwen3 (q_norm/k_norm), Llama and Mistral.
- It's checked against the library before every run: logits within 0.8%, the same top-5 tokens, and an exact
  match for a full recompute.
- Models run in bfloat16, one L40S per model, on RunPod. The run guides are `extension/RUN-*.md`.
- The data is `data/items*.jsonl`. The results are in `results/`.

## 3. Results

### 3.1 Reproduction of the baseline

| d = 250 | Mao et al. | Ours |
|---|---|---|
| EditLocal@32, Qwen3 / Llama / Mistral | 0.01 / 0.09 / 0.01 | 0.01 / 0.04 / 0.02 |
| CarrierWindow, Qwen3 / Llama | 0.90 / 0.43 | 0.92 / 0.30 (Mistral 0.62) |

The pattern reproduces. Our cohort differs in its background text, row order, edit position and validity
checks (see `baseline/README.md`).

### 3.2 Extension versus baseline

Margin recovery on the explicit-link cells, over 3 models:

| Policy | Result |
|---|---|
| **Path window, edit-time index** | **0.99 to 1.00 in all 18 cells; 95 to 100% correct** |
| EditLocal@32, d ≥ 250 | at most 0.06 |
| Fixed window at the path window's mean cost | 0.44 to 0.81 |
| CarrierWindow | Qwen 0.92 to 0.95; Llama 0.30 to 0.46; Mistral 0.56 to 0.69; ≈0 at 3 hops |
| Erratum + edited field | 68 to 100% correct on Llama; 11 to 54% on Qwen and Mistral |
| gpt-4o-mini graph before the edit | 0.09 to 0.53 |
| Random positions at the same budget | at most 0.36 |
| StopShort (gap without the rows) | at most 0.05 |
| Attention-picked, fixed 512 tokens | 0.98 to 1.00 |

The path window costs 29 to 65% of recomputing to the end, and 18 to 50% of a full re-read at a distance.

Paraphrased links ("the sixth plan" vs "Plan six"), margin recovery:

| Way of finding the dependents | Result |
|---|---|
| Oracle | 0.98 to 1.02 |
| Word index | 0.11 to 0.42 |
| gpt-4o-mini | ≈0 to 0.31 |
| gpt-4.1, before the edit | 0.73 to 0.94 |
| gpt-4.1, at edit time | 0.38 to 0.77 |
| **gpt-4.1, both** | **0.84 to 0.98** |
| Attention@512 | 0.98 to 1.03 |

Pooled by row order, the edit-time query scores 0.21 when the new row comes first and 1.01 when the old row
comes first; combining both graphs gives 0.86 and 1.01.

### 3.3 Honest assessment

**Worked:** the path window, whenever it knows where to stop. The edit-time index finds that point for
explicit links at almost no cost.

**Didn't:**
- the index on paraphrased links;
- small LLM graphs;
- every fixed budget;
- the erratum outside Llama.

**Not an advantage of ours:** attention-picked positions also repair at a fixed 512 tokens, more cheaply at long
range. That's consistent with PatchKV's stored-attention blocks, and it fails at Mao's 32-token budget. They
need attention statistics and a budget that isn't known in advance.

**New insight:** a complete dependency set includes the text the edit made irrelevant, whose stale states
still assert the old answer.

**Built-in advantage:** the index's perfect precision on explicit cells is partly built in, because the filler
was filtered for the benchmark's names.

## 4. Related work

| Work | What it does | How we differ |
|---|---|---|
| **PatchKV** (Yang et al., arXiv:2609.26219) | edit-local window plus distant blocks chosen by stored attention | our attention result is consistent with it; we add derived and paraphrased facts and a model-free stopping rule |
| **Li** (arXiv:2606.17107) | appended erratum, tested on gated policy facts on one model | we test it on derived facts at a distance on three models |
| **Cai and Cai** (arXiv:2607.23693) | when appended corrections beat edits in sparse event caches | |
| **CacheBlend** (Yao et al., EuroSys 2025) | selective recompute when joining cached chunks | a different kind of staleness |
| **RippleEdits** (Cohen et al.) and **MQuAKE** (Zhong et al.) | ripple effects of edits in model weights | our cells play the same role for a cached document |

We found no published test of the edit-to-dependent path window, of the erratum on derived facts at a distance,
or of 3-hop, fan-out or paraphrased links in KV repair (novelty check of 14 October 2026).

## 5. Limitations and what full validation would require

- Dependencies are inserted template sentences in real background text. There are no real documents or real
  edits, and edits are single and length-preserving.
- Few paraphrased items were kept on Llama and Mistral (25 and 32 of 100).
- Documents reach at most about 3,550 tokens, and models are 7 to 8B.
- The cost of obtaining attention statistics isn't counted.
- The LLM graphs ran once at temperature 0.
- An edit-time LLM call takes seconds, against about 50 ms for the path repair and 200 to 225 ms for a full
  re-read, so it's practical only as a background step or a fallback.

Full validation would need real documents with real edits (including insertions and deletions), longer
contexts, larger models and more rewording types.

## References

1. M. Mao, W. Mackey, X. Lin. Contiguity, Not Importance: Budgeted Repair of Stale KV Caches After Document Edits. arXiv:2609.17983, 2026.
2. B. Li. Models Take Notes at Prefill: KV Cache Can Be Editable and Composable. arXiv:2606.17107, 2026.
3. G. Yang, R. Guo, S. He, S. Chen, Y. Hu, K. Li. PatchKV: Efficient KV Cache Recovery for Dynamically Edited LLM Contexts. arXiv:2609.26219, 2026.
4. Z. Cai, Z. Cai. Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV. arXiv:2607.23693, 2026.
5. J. Yao et al. CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion. EuroSys 2025, arXiv:2405.16444.
6. R. Cohen, E. Biran, O. Yoran, A. Globerson, M. Geva. Evaluating the Ripple Effects of Knowledge Editing in Language Models. TACL 12, 2024.
7. Z. Zhong, Z. Wu, C. D. Manning, C. Potts, D. Chen. MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions. EMNLP 2023.
8. Qwen Team. Qwen3 Technical Report. arXiv:2505.09388, 2025. A. Dubey et al. The Llama 3 Herd of Models. arXiv:2407.21783, 2024. A. Q. Jiang et al. Mistral 7B. arXiv:2310.06825, 2023.
9. S. Merity, C. Xiong, J. Bradbury, R. Socher. Pointer Sentinel Mixture Models. ICLR 2017 (WikiText-103).

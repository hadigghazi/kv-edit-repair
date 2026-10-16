# Baseline: Mao et al., "Contiguity, Not Importance" (arXiv:2609.17983)

**Paper:** Mingyang Mao, Wyatt Mackey and Xiaomin Lin, *Contiguity, Not Importance: Budgeted Repair of Stale KV
Caches After Document Edits*, arXiv:2609.17983, September 2026.

**What it does.** A document's KV cache goes stale after an edit. Instead of re-reading the whole document, a
repair policy recomputes a budget of K positions in place.

The paper:
- defines **margin recovery** (MR): 0 means no better than the stale cache, 1 means as good as a full re-read;
- compares training-free policies at a matched budget;
- finds that a **contiguous window right after the edit (EditLocal)** beats importance-based selection;
- shows that EditLocal fails on a **derived** fact: an edited alias selects between two unchanged lookup rows
  placed 250 or 1,500 tokens later;
- tests an oracle **CarrierWindow**, a window placed at those rows;
- names the window from the edit to the dependent text as the natural next step and **leaves it untested**.

## How we reproduce it (option 2 of the template: reimplemented)

The paper releases no code, so we reimplemented the parts we need. The work is in one script,
`extension/kvx.py`, so the baseline and the extension run on exactly the same runtime and items. The baseline
pieces are:

| Paper component | Where in `extension/kvx.py` |
|---|---|
| In-place repair of a set of positions, each attending to every cached key at or before it | `Runner.run`, generalised from our team's proof-of-concept operator to Qwen3 (q_norm/k_norm), Llama and Mistral |
| Margin recovery | `evaluate()`: margin = length-averaged log p(new) − log p(old), teacher-forced; MR = (m − m_stale) / (m_full − m_stale) |
| Derived benchmark (alias → two lookup rows at distance d ∈ {0, 250, 1500}) | `make_item()`, cells `derived_d0`, `derived_d250`, `derived_d1500` |
| EditLocal (K tokens after the edit) | arms `el32` … `el1024` |
| CarrierWindow (32 tokens at the carrier rows, oracle) | arm `carrier32` |

Before every run, `integrity()` checks our forward pass against the library: last-token logits differ by at
most 0.8% with identical top-5 tokens, and recomputing every position reproduces a fresh prefill exactly.

## Reproduced numbers against the paper's

The models are the same three families as the paper: Qwen3-8B, Llama-3.1-8B-Instruct (ungated mirror) and
Mistral-7B-Instruct-v0.3. Margin recovery at d = 250:

| Policy | Mao et al. | This reproduction |
|---|---|---|
| EditLocal@32, Qwen3 / Llama / Mistral | 0.01 / 0.09 / 0.01 | 0.01 / 0.04 / 0.02 |
| EditLocal@32 at d = 1500 | 0.01 to 0.02 | −0.02 / 0.02 / −0.01 |
| CarrierWindow, Qwen3 / Llama | 0.90 / 0.43 | 0.92 / 0.30 (Mistral 0.62) |

The paper's figures are as reported in arXiv:2609.17983; ours come from `results/main/results.json`. The
pattern reproduces: EditLocal fails at a distance on every model, and CarrierWindow works on Qwen but not on
Llama. Our cohort differs in ways that can move the absolute numbers:
- the background is real WikiText-103 text, not the paper's;
- the row order is random;
- the edit sits mid-document;
- every item must pass generation-based validity checks.

**Command:** this is the `main` run in `extension/RUN-main.md`. On 3× L40S GPUs it takes about 35 minutes for
all three models in parallel.

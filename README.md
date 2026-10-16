# How far does an edit reach? Repairing derived facts in stale KV caches

Team project for **Data Science for Conversational AI** (Lebanese University). Topic: **grounding and memory**.
The repo was created from the course template `ahmabboud/dsca-team-template`.

**Team:** Nour Shreif · Hadi Ghazi ([@hadigghazi](https://github.com/hadigghazi)) · Karin Zoabi

**Baseline paper:** M. Mao, W. Mackey and X. Lin, *Contiguity, Not Importance: Budgeted Repair of Stale KV
Caches After Document Edits*, arXiv:2609.17983, 2026.

## In one paragraph

When a cached document is edited, the cached states of any text that *depends* on the edit go stale. Mao et
al. show that the standard repair, recomputing a fixed window after the edit, fails when the answer is a
derived fact far from the edit. They name the fix, a window from the edit to the end of the dependent text, as
untested. We test it on Qwen3-8B, Llama-3.1-8B and Mistral-7B, with 450 items per model and 40 repair policies,
and find where to stop with a word index built at edit time:
- for explicit links, it repairs every cell (margin recovery 0.99 to 1.00, 95 to 100% correct answers) at 18
  to 50% of the cost of a re-read;
- for paraphrased links ("the sixth plan" vs "Plan six"), the word index fails, and gpt-4.1 dependency graphs
  built before and at edit time recover 0.84 to 0.98.

The controls show that repair needs to *reach* the dependent text, not just to spend enough budget. They also
show that the dependency set must include the text the edit made irrelevant.

## Where things are

| Folder | Contents |
|---|---|
| [`baseline/`](baseline/README.md) | Mao et al.'s method, reimplemented (no code was released), with our reproduced numbers next to theirs |
| [`extension/`](extension/README.md) | `kvx.py`, the whole study in one script (benchmark builder, repair runtime with integrity checks, 40 policies, analysis), plus the run guides |
| [`results/`](results/README.md) | Every result of the three GPU runs (main, follow-up controls, paraphrased links): tables and per-item records |
| [`data/`](data/README.md) | The exact benchmark items we ran (generated; background text from WikiText-103) |
| [`report/`](report/REPORT.md) | The report (`REPORT.md`), the 6-page IEEE paper draft (`paper.pdf`) and its LaTeX source, whose tables are generated from `results/` |
| `slides/` | The defense deck (to come) |
| `tests/` | The template's smoke test, plus CPU tests of the benchmark builder and the word index |

## Quick start

```
pip install -r requirements.txt          # pytest, python-dotenv
pytest                                    # CPU only: structure, builder, spans, word index
python extension/kvx.py selftest          # the same checks, verbose
```

The GPU runs (3× L40S, about two and a half hours of pod time over three runs) are described in
`extension/RUN-*.md`. The whole study cost
about US$7.60 of GPU time and US$1.73 of API calls.

## Credit

The path-window idea, the first two proofs of concept, the swapped-row test and the indirect ("paraphrased")
documents are Nour Shreif's. The GPU study generalises her repair operator to three model families.

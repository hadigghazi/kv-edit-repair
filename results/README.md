# Results

Outputs of the three GPU runs, copied unchanged from the pods. Each subfolder has the `analyze` tables
(`results*.md` and `.json`, with bootstrap intervals) and one per-item record per model (`results_<model>*.jsonl`).

| Folder | Run | Items | Policies |
|---|---|---|---|
| `main/` | 7 explicit-dependency cells (with the per-model run logs) | 350 per model | 22 (EditLocal sweep, CarrierWindow, rows, path windows, erratum, attention at matched budget, suffix, full) |
| `followup/` | the same items | 350 per model | the controls: StopShort, random positions and blocks, attention at fixed budgets and two stopping rules, plus 7 reference arms that reproduced the main run exactly |
| `indirect/` | 2 paraphrased-link cells | 100 per model | the main set plus LLM graphs (gpt-4o-mini and gpt-4.1, before the edit and at edit time) and their hybrids |

Each per-item record has:
- `kept` and `reject`: the validity checks;
- `gap`, `m_stale` and `m_oracle`: the margins;
- `gen_stale` and `gen_oracle`: the generated answers;
- `dist_tokens` and `n_doc`;
- `arms`, giving for each policy its MR, accuracy, old-answer flag, tokens recomputed, repair time in ms and the
  generated answer.

To regenerate the tables, run `python extension/kvx.py analyze --out-dir results/main`, or the same with
`--out-dir results/followup --tag _followup` or `--out-dir results/indirect --tag _indirect`. The
paper's LaTeX tables are produced from these files by `report/paper/make_tables.py`.

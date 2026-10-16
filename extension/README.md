# Extension: edit-time path windows, and what repair has to reach

## What we changed or added relative to the baseline

1. **The path window** that Mao et al. name but don't test. It recomputes contiguously from the edit to the
   end of the furthest dependent sentence, then stops.
2. **A model-free way to find where to stop.** A word index built at edit time
   (`index_graph()` in `kvx.py`):
   - it starts from the words that differ between the old and new edited sentence;
   - it follows rare names and codes for up to three hops.
3. **LLM dependency finders for paraphrased links:**
   - a graph built from the original document before the edit (`llm_graph()`);
   - a query at edit time, given the old and new sentence (`llm_edit()`);
   - each with gpt-4o-mini and gpt-4.1, and in combination.
4. **A larger benchmark** (`make_item()`), with nine cells of 50 items:
   - direct;
   - derived at distance 0, 250 and 1,500;
   - 3 hops;
   - fan-out 3;
   - noisy (distracting mentions of the same company);
   - **indirect** at distance 250 and 1,500 ("the sixth plan" vs "Plan six", from our second proof of concept).
5. **Competing policies and controls:**
   - Li's appended erratum (arXiv:2606.17107);
   - attention-picked positions and blocks, at matched and fixed budgets, plus two stopping rules;
   - random positions at a matched budget;
   - StopShort (the gap without the dependent rows);
   - rows only;
   - recompute to the end;
   - full re-read.

In all, there are 40 policies.

## The limitation it addresses

EditLocal and CarrierWindow fix a budget, so they can't adapt to how far an edit reaches. That reach differs per
document, and the path window from the edit to the dependent text was left untested. The erratum had not been
tested on derived facts at a distance either.

## How it is evaluated against the baseline

Every policy repairs the **same stale cache** of the **same items** with the **same operator**. We score:
- margin recovery;
- **answer accuracy**: the greedy answer contains the new code and not the old;
- tokens recomputed and time.

Every item must pass validity checks: the full re-read must improve the margin and generate the new code, and
the stale cache must not. Intervals are item-level bootstrap. A second run on a fresh pod reproduced every
item's numbers exactly.

## Headline results (see `report/` and `results/`)

| | Qwen3-8B | Llama-3.1-8B | Mistral-7B |
|---|---|---|---|
| Path window, edit-time index, explicit links (18 cells) | MR 0.99–1.00, 98–100% | 0.99–1.00, 98–100% | 0.99–1.00, 95–100% |
| EditLocal@32 at distance ≥ 250 | ≈0 | ≈0.03 | ≈0 |
| Fixed window at the path window's mean cost | 0.48–0.78 | 0.44–0.81 | 0.59–0.65 |
| CarrierWindow (oracle) | 0.92–0.95 | 0.30–0.46 | 0.56–0.69 |
| Random positions at the path's budget | ≤ 0.36 | ≤ 0.32 | ≤ 0.29 |
| Paraphrased links, gpt-4.1 graphs before + at edit time | 0.88–0.97 | 0.84–0.93 | 0.93–0.98 |
| Attention-picked, fixed 512 tokens | 0.98–1.00 | 0.99–1.02 | 0.98–1.03 |

**Main findings:**
- Repair needs to reach the dependent sentences and the text that carries the edit to them, not just enough
  budget.
- A word index built at edit time finds them for explicit links. Paraphrased links need a strong LLM.
- A dependency set must include the text the edit made **irrelevant**: an edit-time query alone scores 0.21
  when the new row comes first, against 1.01 when the old row comes first.

## Running it

All runs used RunPod pods with 3× L40S (one model per GPU), the PyTorch 2.8 template and a 150 GB container
disk:
- `RUN-main.md`: building the items, a smoke test, and the main run;
- `RUN-followup.md`: the matched-budget controls;
- `RUN-indirect.md`: the paraphrased cells. These need an OpenAI key for the LLM graphs.

```
pip install -r extension/requirements-gpu.txt
python extension/kvx.py selftest          # CPU only: builder, spans and word index, with a stub tokenizer
python extension/kvx.py build --n 50      # main items (data/items.jsonl is the exact set we ran)
python extension/kvx.py run --model qwen3 --items data/items.jsonl
python extension/kvx.py analyze --out-dir out
```

**Cost of the whole study:** about US$7.60 of GPU time and US$1.73 of API calls.

## What full validation would require

The study runs at full scale for its benchmark: 450 items per model on 3 models. It's still synthetic in one
respect: every dependency is an inserted template sentence in real background text. Full validation would
need:
- real documents with real edits, including edits that insert or delete text and shift positions;
- longer documents than about 3,500 tokens;
- larger models;
- a second rewording type for the paraphrased links.

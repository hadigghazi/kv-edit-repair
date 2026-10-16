# Follow-up controls (same items as the main run)

> These are the exact pod steps we used. On the pod, the bundle was unzipped to `/workspace/kv`, with `kvx.py` at its top level; in this repo the same script is `extension/kvx.py` and the items are in `data/`.

`--arms followup` adds the following, and re-runs a few reference arms that must match the main run:
- **stopshort:** recompute the gap from the edit up to the first dependent sentence, but not the dependent sentences themselves.
- **random_matched** and **random_blocks:** the path window's budget, spent on random positions or random 32-token blocks.
- **attn_k32/128/512** and **attn_blocks_k128/512:** attention-picked positions at fixed budgets, without the graph's budget.
- **attn_stop25** and **attn_stop10:** attention decides where to stop. The window runs from the edit to the furthest position whose attention to the edited sentence is at least 25% (or 10%) of the maximum.

Steps (3 GPUs, container disk 150 GB):

    cd /workspace && python -m zipfile -e kvx-followup.zip kv && cd kv
    export HF_HOME=/workspace/hf
    pip install -q -U "transformers>=4.56" accelerate datasets
    read -rsp "HF token (Enter to skip): " HF_TOKEN; echo; export HF_TOKEN
    python kvx.py run --model qwen3 --arms followup --limit 1
    for i in 0 1 2; do m=$(echo qwen3 llama mistral | cut -d' ' -f$((i+1))); CUDA_VISIBLE_DEVICES=$i nohup python kvx.py run --model $m --arms followup > fu_$m.out 2>&1 & done
    tail -n 2 fu_*.out
    python kvx.py analyze --tag _followup > /dev/null && cd /workspace && python -m zipfile -c kv-followup-results.zip kv/out/results_qwen3_followup.jsonl kv/out/results_llama_followup.jsonl kv/out/results_mistral_followup.jsonl kv/out/results_followup.md kv/out/results_followup.json kv/out/log_qwen3.txt kv/out/log_llama.txt kv/out/log_mistral.txt

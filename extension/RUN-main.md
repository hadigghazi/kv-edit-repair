# Ripple-aware KV-cache repair: GPU study

> These are the exact pod steps we used. On the pod, the bundle was unzipped to `/workspace/kv`, with `kvx.py` at its top level; in this repo the same script is `extension/kvx.py` and the items are in `data/`.

The full design is described at the top of `kvx.py`. Three models run one per GPU: Qwen3-8B, Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3.

## Pod
- **GPU:** 3 GPUs with 48 GB or more each, for example 3× L40S or 3× A100 80GB.
- **Template:** RunPod PyTorch, the newest version.
- **Volume:** 150 GB, mounted at `/workspace`. The three models total about 47 GB.

## Steps (Jupyter terminal)

    cd /workspace && python -m zipfile -e kvx.zip kv && cd kv
    export HF_HOME=/workspace/hf
    pip install -q -U "transformers>=4.56" accelerate datasets openai
    read -rsp "HF token: " HF_TOKEN; echo; export HF_TOKEN
    read -rsp "OpenAI key (Enter to skip the LLM graph): " OPENAI_API_KEY; echo; export OPENAI_API_KEY
    python kvx.py build --n 50

Smoke test, 2 items per cell, all three models in parallel:

    for i in 0 1 2; do m=$(echo qwen3 llama mistral | cut -d' ' -f$((i+1))); CUDA_VISIBLE_DEVICES=$i nohup python kvx.py run --model $m --limit 2 > smoke_$m.out 2>&1 & done
    tail -n 5 smoke_*.out

Full run, after the smoke test looks right:

    for i in 0 1 2; do m=$(echo qwen3 llama mistral | cut -d' ' -f$((i+1))); CUDA_VISIBLE_DEVICES=$i nohup python kvx.py run --model $m > run_$m.out 2>&1 & done
    tail -n 3 run_*.out

When all three logs end with `done`:

    python kvx.py analyze
    cd /workspace && python -m zipfile -c kv-results.zip kv/out kv/run_qwen3.out kv/run_llama.out kv/run_mistral.out

Download `kv-results.zip` from the Jupyter file panel, then **terminate the pod**.

The job can be restarted safely: `run` skips items already present in `out/results_<model>.jsonl`.

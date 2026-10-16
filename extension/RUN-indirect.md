# Indirect dependencies (paraphrased: "the sixth plan" vs "Plan six")

> These are the exact pod steps we used. On the pod, the bundle was unzipped to `/workspace/kv`, with `kvx.py` at its top level; in this repo the same script is `extension/kvx.py` and the items are in `data/`.

Two new cells, indirect_d250 and indirect_d1500, with 50 items each and the rows in random order. They are run on all three models with every main policy, the key controls, and four ways of finding the dependents:
- the edit-time word index;
- an LLM graph built before the edit;
- an LLM asked at edit time;
- the hybrids of the index with each LLM variant.

Each LLM variant uses both gpt-4o-mini and gpt-4.1.

Steps (3× L40S, container disk 150 GB):

    cd /workspace && python -m zipfile -e kvx-indirect.zip kv && cd kv
    export HF_HOME=/workspace/hf
    pip install -q -U "transformers>=4.56" accelerate datasets openai
    read -rsp "HF token (Enter to skip): " HF_TOKEN; echo; export HF_TOKEN
    read -rsp "OpenAI key: " OPENAI_API_KEY; echo; export OPENAI_API_KEY
    python kvx.py build --cells indirect --n 50
    python kvx.py run --model qwen3 --arms indirect --items out/items_indirect.jsonl --limit 1
    for i in 0 1 2; do m=$(echo qwen3 llama mistral | cut -d' ' -f$((i+1))); CUDA_VISIBLE_DEVICES=$i nohup python kvx.py run --model $m --arms indirect --items out/items_indirect.jsonl > ind_$m.out 2>&1 & done
    tail -n 2 ind_*.out
    python kvx.py analyze --tag _indirect > /dev/null && cd /workspace && python -m zipfile -c kv-indirect-results.zip kv/out

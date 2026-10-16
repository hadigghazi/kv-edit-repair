# KV repair results

## qwen3

350 items, 322 kept, 0 errors; rejected: {"stale_answer": 4, "gap": 12, "oracle_answer": 12}

### qwen3 / direct (n=50, median distance 0 tokens, median doc 1436 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.96 [0.94, 0.98] | 0.99 | 98 | 0 | 2 | 28 |
| el32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 31 |
| el64 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 66 | 33 |
| el128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 35 |
| el256 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 258 | 44 |
| el512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 62 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 753 | 83 |
| boundary | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 69 | 33 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 32 |
| attn_blocks | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 31 |
| erratum_bare | 0.78 [0.76, 0.79] | 0.78 | 100 | 0 | 27 | nan |
| erratum_field | 0.82 [0.81, 0.83] | 0.82 | 100 | 0 | 29 | nan |
| erratum_el32 | 0.85 [0.83, 0.86] | 0.84 | 100 | 0 | 61 | nan |
| gp_index | 0.96 [0.94, 0.98] | 0.99 | 98 | 0 | 2 | 28 |
| gp_llm | 0.99 [0.97, 1.00] | 1.00 | 100 | 0 | 41 | 31 |
| gp_hybrid | 0.99 [0.97, 1.00] | 1.00 | 100 | 0 | 41 | 31 |
| suffix | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 753 | 82 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1465 | 148 |

- gp_index minus el32: MR -0.04 [-0.06, -0.02]; accuracy -2 [-6, +0] points (n=50)
- gp_index minus erratum_field: MR +0.14 [+0.11, +0.16]; accuracy -2 [-6, +0] points (n=50)
- gp_index minus attn_blocks: MR -0.04 [-0.06, -0.02]; accuracy -2 [-6, +0] points (n=50)
- gp_hybrid minus gp_index: MR +0.03 [+0.01, +0.05]; accuracy +2 [+0, +6] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / derived_d0 (n=50, median distance 1 tokens, median doc 1480 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | -0.00 [-0.01, 0.00] | -0.00 | 0 | 100 | 1 | 26 |
| el32 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 33 | 31 |
| el64 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 65 | 33 |
| el128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 129 | 35 |
| el256 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 257 | 44 |
| el512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 62 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 774 | 84 |
| boundary | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 82 | 34 |
| carrier32 | 0.94 [0.92, 0.96] | 0.95 | 100 | 0 | 33 | 31 |
| carrier_rows | 0.94 [0.92, 0.96] | 0.95 | 100 | 0 | 17 | 30 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 33 | 31 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 33 | 31 |
| erratum_bare | 0.51 [0.45, 0.57] | 0.53 | 58 | 42 | 25 | nan |
| erratum_field | 0.43 [0.38, 0.49] | 0.41 | 50 | 50 | 26 | nan |
| erratum_el32 | 0.96 [0.93, 0.99] | 0.96 | 98 | 2 | 58 | nan |
| gp_index | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 18 | 30 |
| gp_llm | 0.85 [0.75, 0.94] | 1.00 | 84 | 16 | 18 | 29 |
| gp_hybrid | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 21 | 30 |
| gp_oracle | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 18 | 30 |
| suffix | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 774 | 84 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1484 | 149 |

- gp_index minus el32: MR +0.00 [-0.00, +0.01]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus carrier32: MR +0.06 [+0.04, +0.08]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus erratum_field: MR +0.57 [+0.51, +0.62]; accuracy +50 [+36, +64] points (n=50)
- gp_index minus attn_blocks: MR +0.00 [-0.00, +0.01]; accuracy +0 [+0, +0] points (n=50)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / derived_d250 (n=50, median distance 332 tokens, median doc 1879 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.02] | 0.00 | 0 | 100 | 1 | 26 |
| el32 | 0.01 [0.00, 0.03] | 0.01 | 0 | 100 | 33 | 31 |
| el64 | 0.02 [0.01, 0.03] | 0.01 | 0 | 100 | 65 | 33 |
| el128 | 0.02 [0.00, 0.03] | 0.01 | 0 | 100 | 129 | 35 |
| el256 | 0.02 [0.00, 0.03] | 0.01 | 0 | 100 | 257 | 44 |
| el512 | 0.96 [0.91, 1.00] | 1.00 | 96 | 4 | 513 | 62 |
| el1024 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1024 | 120 |
| boundary | 0.02 [0.00, 0.03] | 0.01 | 0 | 100 | 67 | 33 |
| carrier32 | 0.92 [0.90, 0.94] | 0.93 | 98 | 2 | 33 | 32 |
| carrier_rows | 0.92 [0.90, 0.94] | 0.93 | 98 | 2 | 17 | 30 |
| attn_topk | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 360 | 51 |
| attn_blocks | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 344 | 48 |
| erratum_bare | 0.59 [0.51, 0.67] | 0.61 | 62 | 38 | 25 | nan |
| erratum_field | 0.49 [0.41, 0.57] | 0.52 | 54 | 46 | 26 | nan |
| erratum_el32 | 0.41 [0.34, 0.48] | 0.43 | 40 | 58 | 58 | nan |
| gp_index | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 360 | 48 |
| gp_llm | 0.52 [0.39, 0.66] | 0.71 | 50 | 48 | 232 | 41 |
| gp_hybrid | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 360 | 48 |
| gp_oracle | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 360 | 48 |
| suffix | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1236 | 133 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1947 | 196 |

- gp_index minus el32: MR +0.98 [+0.97, +1.00]; accuracy +100 [+100, +100] points (n=50)
- gp_index minus carrier32: MR +0.08 [+0.06, +0.10]; accuracy +2 [+0, +6] points (n=50)
- gp_index minus erratum_field: MR +0.51 [+0.43, +0.59]; accuracy +46 [+32, +58] points (n=50)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=50)
- EditLocal at the path window's mean cost (360 tokens, log-interpolated): MR 0.48 vs gp_index 1.00
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / derived_d1500 (n=48, median distance 1556 tokens, median doc 3170 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 96 | 0 | 0 |
| edit_only | -0.02 [-0.07, 0.01] | -0.00 | 0 | 96 | 1 | 26 |
| el32 | -0.02 [-0.07, 0.01] | 0.01 | 0 | 96 | 33 | 31 |
| el64 | -0.02 [-0.07, 0.01] | 0.01 | 0 | 96 | 65 | 33 |
| el128 | -0.02 [-0.07, 0.01] | 0.00 | 0 | 96 | 129 | 35 |
| el256 | -0.02 [-0.07, 0.01] | 0.01 | 0 | 96 | 257 | 44 |
| el512 | -0.02 [-0.07, 0.01] | 0.00 | 0 | 96 | 513 | 62 |
| el1024 | -0.02 [-0.06, 0.02] | 0.01 | 0 | 96 | 1025 | 121 |
| boundary | -0.02 [-0.07, 0.01] | 0.01 | 0 | 96 | 67 | 33 |
| carrier32 | 0.93 [0.90, 0.96] | 0.93 | 94 | 2 | 33 | 35 |
| carrier_rows | 0.93 [0.90, 0.96] | 0.94 | 94 | 2 | 17 | 34 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1591 | 178 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1575 | 176 |
| erratum_bare | 0.65 [0.55, 0.76] | 0.66 | 44 | 44 | 25 | nan |
| erratum_field | 0.55 [0.44, 0.65] | 0.54 | 38 | 44 | 26 | nan |
| erratum_el32 | 0.48 [0.38, 0.57] | 0.44 | 27 | 52 | 58 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 98 | 0 | 1591 | 168 |
| gp_llm | 0.26 [0.13, 0.40] | 0.02 | 27 | 73 | 531 | 73 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 98 | 0 | 1591 | 168 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 98 | 0 | 1591 | 168 |
| suffix | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 2457 | 273 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3180 | 348 |

- gp_index minus el32: MR +1.02 [+0.98, +1.07]; accuracy +98 [+92, +100] points (n=48)
- gp_index minus carrier32: MR +0.07 [+0.04, +0.10]; accuracy +4 [+0, +10] points (n=48)
- gp_index minus erratum_field: MR +0.45 [+0.35, +0.56]; accuracy +60 [+46, +75] points (n=48)
- gp_index minus attn_blocks: MR +0.00 [-0.00, +0.01]; accuracy -2 [-8, +0] points (n=48)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=48)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=48)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / hop3 (n=36, median distance 323 tokens, median doc 2426 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 94 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.03] | 0.00 | 3 | 94 | 1 | 27 |
| el32 | 0.02 [0.00, 0.04] | 0.02 | 3 | 94 | 33 | 31 |
| el64 | 0.02 [0.01, 0.04] | 0.02 | 3 | 94 | 65 | 33 |
| el128 | 0.02 [0.01, 0.05] | 0.02 | 3 | 94 | 129 | 35 |
| el256 | 0.03 [0.01, 0.05] | 0.02 | 3 | 94 | 257 | 44 |
| el512 | 0.21 [0.12, 0.30] | 0.21 | 25 | 75 | 513 | 62 |
| el1024 | 0.94 [0.87, 0.99] | 1.00 | 92 | 8 | 1025 | 121 |
| boundary | 0.02 [0.01, 0.04] | 0.02 | 3 | 94 | 68 | 33 |
| carrier32 | 0.01 [-0.00, 0.03] | 0.00 | 3 | 94 | 33 | 33 |
| carrier_rows | 0.85 [0.80, 0.90] | 0.91 | 92 | 8 | 34 | 33 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 886 | 100 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 871 | 98 |
| erratum_bare | 0.31 [0.19, 0.41] | 0.31 | 36 | 64 | 25 | nan |
| erratum_field | 0.24 [0.13, 0.34] | 0.29 | 31 | 69 | 26 | nan |
| erratum_el32 | 0.22 [0.10, 0.32] | 0.25 | 33 | 67 | 58 | nan |
| gp_index | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 886 | 94 |
| gp_llm | 0.18 [0.06, 0.29] | 0.06 | 11 | 83 | 302 | 48 |
| gp_hybrid | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 889 | 94 |
| gp_oracle | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 886 | 94 |
| suffix | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1750 | 184 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2460 | 259 |

- gp_index minus el32: MR +0.98 [+0.96, +1.00]; accuracy +97 [+92, +100] points (n=36)
- gp_index minus carrier32: MR +0.99 [+0.97, +1.00]; accuracy +97 [+92, +100] points (n=36)
- gp_index minus erratum_field: MR +0.75 [+0.65, +0.87]; accuracy +69 [+56, +83] points (n=36)
- gp_index minus attn_blocks: MR +0.00 [-0.00, +0.01]; accuracy +0 [+0, +0] points (n=36)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=36)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=36)
- EditLocal at the path window's mean cost (886 tokens, log-interpolated): MR 0.78 vs gp_index 1.00
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / fanout3 (n=42, median distance 326 tokens, median doc 3031 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 93 | 0 | 0 |
| edit_only | -0.01 [-0.05, 0.02] | 0.01 | 0 | 95 | 1 | 26 |
| el32 | 0.00 [-0.05, 0.03] | 0.02 | 2 | 93 | 33 | 31 |
| el64 | 0.00 [-0.05, 0.03] | 0.02 | 5 | 88 | 65 | 33 |
| el128 | 0.00 [-0.05, 0.03] | 0.02 | 5 | 88 | 129 | 35 |
| el256 | 0.00 [-0.05, 0.03] | 0.02 | 2 | 93 | 257 | 44 |
| el512 | 0.51 [0.36, 0.65] | 0.77 | 50 | 43 | 513 | 62 |
| el1024 | 0.53 [0.37, 0.68] | 0.91 | 55 | 40 | 1025 | 121 |
| boundary | -0.00 [-0.05, 0.03] | 0.02 | 2 | 90 | 67 | 33 |
| carrier32 | 0.50 [0.38, 0.63] | 0.58 | 52 | 31 | 33 | 33 |
| carrier_rows | 0.92 [0.88, 0.95] | 0.96 | 98 | 2 | 44 | 35 |
| attn_topk | 1.00 [0.99, 1.01] | 1.01 | 100 | 0 | 1470 | 164 |
| attn_blocks | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1454 | 162 |
| erratum_bare | 0.35 [0.26, 0.43] | 0.35 | 33 | 62 | 25 | nan |
| erratum_field | 0.30 [0.22, 0.38] | 0.28 | 29 | 67 | 26 | nan |
| erratum_el32 | 0.28 [0.20, 0.35] | 0.25 | 26 | 69 | 58 | nan |
| gp_index | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1470 | 155 |
| gp_llm | 0.19 [0.05, 0.33] | 0.03 | 21 | 71 | 276 | 49 |
| gp_hybrid | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1470 | 155 |
| gp_oracle | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1470 | 155 |
| suffix | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 2329 | 256 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3057 | 333 |

- gp_index minus el32: MR +1.00 [+0.97, +1.05]; accuracy +98 [+93, +100] points (n=42)
- gp_index minus carrier32: MR +0.50 [+0.37, +0.62]; accuracy +48 [+33, +62] points (n=42)
- gp_index minus erratum_field: MR +0.70 [+0.63, +0.78]; accuracy +71 [+57, +83] points (n=42)
- gp_index minus attn_blocks: MR +0.00 [-0.00, +0.01]; accuracy +0 [+0, +0] points (n=42)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=42)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=42)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / noisy_d250 (n=46, median distance 344 tokens, median doc 1983 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 1 | 26 |
| el32 | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 33 | 31 |
| el64 | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 65 | 33 |
| el128 | 0.01 [-0.00, 0.02] | -0.00 | 0 | 100 | 129 | 35 |
| el256 | 0.01 [-0.00, 0.02] | 0.01 | 0 | 100 | 257 | 44 |
| el512 | 0.96 [0.90, 1.00] | 1.00 | 98 | 2 | 513 | 62 |
| el1024 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1025 | 121 |
| boundary | 0.01 [-0.00, 0.02] | 0.00 | 0 | 100 | 73 | 33 |
| carrier32 | 0.95 [0.92, 0.96] | 0.95 | 100 | 0 | 33 | 32 |
| carrier_rows | 0.94 [0.92, 0.96] | 0.95 | 100 | 0 | 17 | 31 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 376 | 52 |
| attn_blocks | 0.99 [0.96, 1.01] | 1.00 | 98 | 2 | 358 | 50 |
| erratum_bare | 0.54 [0.46, 0.62] | 0.51 | 50 | 50 | 25 | nan |
| erratum_field | 0.49 [0.41, 0.56] | 0.47 | 48 | 50 | 26 | nan |
| erratum_el32 | 0.45 [0.38, 0.52] | 0.45 | 48 | 50 | 58 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 376 | 49 |
| gp_llm | 0.09 [0.02, 0.18] | 0.01 | 9 | 91 | 120 | 35 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 385 | 49 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 376 | 49 |
| suffix | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1278 | 137 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2004 | 201 |

- gp_index minus el32: MR +0.99 [+0.98, +1.00]; accuracy +100 [+100, +100] points (n=46)
- gp_index minus carrier32: MR +0.05 [+0.03, +0.07]; accuracy +0 [+0, +0] points (n=46)
- gp_index minus erratum_field: MR +0.51 [+0.43, +0.59]; accuracy +52 [+39, +67] points (n=46)
- gp_index minus attn_blocks: MR +0.01 [-0.01, +0.04]; accuracy +2 [+0, +7] points (n=46)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=46)
- gp_hybrid minus gp_index: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=46)
- EditLocal at the path window's mean cost (376 tokens, log-interpolated): MR 0.53 vs gp_index 1.00
- index graph: dependent recall 1.00, extra sentences 0.0

## llama

350 items, 263 kept, 0 errors; rejected: {"oracle_answer": 21, "stale_answer": 26, "gap": 40}

### llama / direct (n=50, median distance 0 tokens, median doc 1388 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.93 [0.89, 0.96] | 0.98 | 96 | 4 | 2 | 26 |
| el32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| el64 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 66 | 30 |
| el128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 33 |
| el256 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 258 | 39 |
| el512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 59 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 727 | 74 |
| boundary | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 67 | 30 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| attn_blocks | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| erratum_bare | 0.68 [0.67, 0.70] | 0.69 | 100 | 0 | 27 | nan |
| erratum_field | 0.79 [0.78, 0.80] | 0.80 | 100 | 0 | 29 | nan |
| erratum_el32 | 0.83 [0.82, 0.84] | 0.82 | 100 | 0 | 61 | nan |
| gp_index | 0.93 [0.89, 0.96] | 0.98 | 96 | 4 | 2 | 26 |
| gp_llm | 0.98 [0.96, 0.99] | 1.00 | 100 | 0 | 40 | 28 |
| gp_hybrid | 0.98 [0.96, 0.99] | 1.00 | 100 | 0 | 40 | 28 |
| suffix | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 727 | 74 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1441 | 138 |

- gp_index minus el32: MR -0.07 [-0.11, -0.04]; accuracy -4 [-10, +0] points (n=50)
- gp_index minus erratum_field: MR +0.14 [+0.10, +0.18]; accuracy -4 [-10, +0] points (n=50)
- gp_index minus attn_blocks: MR -0.07 [-0.11, -0.04]; accuracy -4 [-10, +0] points (n=50)
- gp_hybrid minus gp_index: MR +0.05 [+0.02, +0.08]; accuracy +4 [+0, +10] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / derived_d0 (n=49, median distance 1 tokens, median doc 1438 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 98 | 0 | 0 |
| edit_only | -0.02 [-0.03, -0.00] | -0.00 | 0 | 100 | 1 | 24 |
| el32 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 33 | 29 |
| el64 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 65 | 30 |
| el128 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 129 | 33 |
| el256 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 257 | 39 |
| el512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 513 | 58 |
| el1024 | 1.00 [1.00, 1.01] | 1.01 | 100 | 0 | 745 | 76 |
| boundary | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 80 | 31 |
| carrier32 | 0.46 [0.40, 0.51] | 0.47 | 31 | 43 | 33 | 29 |
| carrier_rows | 0.46 [0.40, 0.51] | 0.47 | 29 | 41 | 17 | 27 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 33 | 29 |
| attn_blocks | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 33 | 29 |
| erratum_bare | 0.95 [0.83, 1.09] | 1.03 | 94 | 6 | 25 | nan |
| erratum_field | 0.92 [0.81, 1.06] | 1.01 | 92 | 6 | 26 | nan |
| erratum_el32 | 1.03 [0.96, 1.10] | 1.08 | 100 | 0 | 58 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 18 | 27 |
| gp_llm | 0.84 [0.74, 0.94] | 0.99 | 86 | 12 | 18 | 27 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 21 | 27 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 18 | 27 |
| suffix | 1.00 [1.00, 1.01] | 1.01 | 100 | 0 | 745 | 75 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1457 | 140 |

- gp_index minus el32: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_index minus carrier32: MR +0.54 [+0.48, +0.60]; accuracy +69 [+55, +82] points (n=49)
- gp_index minus erratum_field: MR +0.07 [-0.06, +0.19]; accuracy +8 [+2, +16] points (n=49)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / derived_d250 (n=31, median distance 317 tokens, median doc 1804 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 94 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.02] | 0.01 | 3 | 94 | 1 | 24 |
| el32 | 0.04 [0.01, 0.06] | 0.05 | 6 | 87 | 33 | 29 |
| el64 | 0.04 [0.01, 0.06] | 0.04 | 6 | 87 | 65 | 30 |
| el128 | 0.04 [0.02, 0.06] | 0.04 | 6 | 87 | 129 | 33 |
| el256 | 0.04 [0.01, 0.07] | 0.03 | 6 | 87 | 257 | 39 |
| el512 | 0.97 [0.90, 1.01] | 1.00 | 97 | 3 | 513 | 59 |
| el1024 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1023 | 111 |
| boundary | 0.04 [0.01, 0.06] | 0.04 | 6 | 87 | 65 | 30 |
| carrier32 | 0.30 [0.26, 0.34] | 0.29 | 19 | 61 | 33 | 30 |
| carrier_rows | 0.30 [0.26, 0.34] | 0.28 | 16 | 61 | 17 | 28 |
| attn_topk | 1.00 [0.99, 1.01] | 1.00 | 97 | 0 | 347 | 46 |
| attn_blocks | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 332 | 44 |
| erratum_bare | 1.12 [0.98, 1.24] | 1.26 | 94 | 0 | 25 | nan |
| erratum_field | 1.09 [0.96, 1.21] | 1.24 | 94 | 0 | 26 | nan |
| erratum_el32 | 0.86 [0.72, 0.98] | 0.90 | 68 | 6 | 58 | nan |
| gp_index | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 347 | 43 |
| gp_llm | 0.53 [0.37, 0.69] | 0.41 | 55 | 39 | 213 | 37 |
| gp_hybrid | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 347 | 43 |
| gp_oracle | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 347 | 43 |
| suffix | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1194 | 122 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1917 | 184 |

- gp_index minus el32: MR +0.96 [+0.94, +0.99]; accuracy +94 [+84, +100] points (n=31)
- gp_index minus carrier32: MR +0.70 [+0.66, +0.74]; accuracy +81 [+65, +94] points (n=31)
- gp_index minus erratum_field: MR -0.09 [-0.22, +0.05]; accuracy +6 [+0, +16] points (n=31)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.01]; accuracy +0 [+0, +0] points (n=31)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=31)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=31)
- EditLocal at the path window's mean cost (347 tokens, log-interpolated): MR 0.44 vs gp_index 1.00
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / derived_d1500 (n=28, median distance 1500 tokens, median doc 3023 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 82 | 0 | 0 |
| edit_only | 0.02 [-0.01, 0.05] | 0.01 | 4 | 86 | 1 | 24 |
| el32 | 0.02 [-0.03, 0.07] | 0.02 | 4 | 82 | 33 | 32 |
| el64 | 0.03 [-0.02, 0.07] | 0.01 | 0 | 86 | 65 | 30 |
| el128 | 0.03 [-0.02, 0.08] | 0.02 | 0 | 86 | 129 | 33 |
| el256 | 0.02 [-0.03, 0.07] | 0.01 | 0 | 86 | 257 | 39 |
| el512 | 0.02 [-0.03, 0.08] | 0.01 | 4 | 82 | 513 | 58 |
| el1024 | 0.03 [-0.02, 0.08] | 0.02 | 0 | 86 | 1025 | 112 |
| boundary | 0.03 [-0.02, 0.08] | 0.02 | 4 | 82 | 68 | 31 |
| carrier32 | 0.37 [0.32, 0.42] | 0.36 | 36 | 50 | 33 | 33 |
| carrier_rows | 0.37 [0.32, 0.42] | 0.37 | 32 | 54 | 17 | 31 |
| attn_topk | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1530 | 162 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1519 | 160 |
| erratum_bare | 1.21 [0.97, 1.48] | 1.13 | 100 | 0 | 25 | nan |
| erratum_field | 1.19 [0.95, 1.45] | 1.13 | 100 | 0 | 26 | nan |
| erratum_el32 | 0.96 [0.76, 1.17] | 0.79 | 86 | 0 | 58 | nan |
| gp_index | 0.99 [0.98, 1.00] | 0.98 | 100 | 0 | 1530 | 154 |
| gp_llm | 0.30 [0.14, 0.49] | 0.03 | 32 | 57 | 528 | 69 |
| gp_hybrid | 0.99 [0.98, 1.00] | 0.98 | 100 | 0 | 1530 | 154 |
| gp_oracle | 0.99 [0.98, 1.00] | 0.98 | 100 | 0 | 1530 | 154 |
| suffix | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 2357 | 249 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3067 | 328 |

- gp_index minus el32: MR +0.97 [+0.93, +1.01]; accuracy +96 [+89, +100] points (n=28)
- gp_index minus carrier32: MR +0.62 [+0.57, +0.67]; accuracy +64 [+46, +82] points (n=28)
- gp_index minus erratum_field: MR -0.20 [-0.46, +0.04]; accuracy +0 [+0, +0] points (n=28)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.01]; accuracy +0 [+0, +0] points (n=28)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=28)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=28)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / hop3 (n=32, median distance 320 tokens, median doc 2330 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.03 [0.01, 0.06] | 0.02 | 3 | 97 | 1 | 25 |
| el32 | 0.06 [0.01, 0.10] | 0.04 | 9 | 91 | 33 | 29 |
| el64 | 0.06 [0.02, 0.10] | 0.04 | 9 | 91 | 65 | 30 |
| el128 | 0.06 [0.03, 0.10] | 0.05 | 6 | 94 | 129 | 33 |
| el256 | 0.06 [0.02, 0.10] | 0.05 | 6 | 91 | 257 | 39 |
| el512 | 0.38 [0.27, 0.49] | 0.40 | 34 | 62 | 513 | 58 |
| el1024 | 0.97 [0.91, 1.01] | 1.00 | 97 | 3 | 1025 | 112 |
| boundary | 0.06 [0.02, 0.10] | 0.02 | 6 | 94 | 67 | 30 |
| carrier32 | 0.04 [0.02, 0.06] | 0.03 | 3 | 97 | 33 | 31 |
| carrier_rows | 0.27 [0.21, 0.34] | 0.25 | 31 | 69 | 34 | 31 |
| attn_topk | 0.99 [0.98, 1.01] | 1.00 | 100 | 0 | 851 | 91 |
| attn_blocks | 0.99 [0.98, 1.01] | 1.00 | 100 | 0 | 837 | 89 |
| erratum_bare | 0.94 [0.71, 1.18] | 0.75 | 84 | 12 | 25 | nan |
| erratum_field | 0.89 [0.70, 1.11] | 0.72 | 84 | 12 | 26 | nan |
| erratum_el32 | 0.59 [0.43, 0.77] | 0.41 | 53 | 47 | 58 | nan |
| gp_index | 1.00 [0.98, 1.01] | 1.00 | 100 | 0 | 851 | 86 |
| gp_llm | 0.29 [0.19, 0.40] | 0.20 | 19 | 78 | 284 | 42 |
| gp_hybrid | 1.00 [0.98, 1.02] | 1.00 | 100 | 0 | 855 | 86 |
| gp_oracle | 1.00 [0.98, 1.01] | 1.00 | 100 | 0 | 851 | 85 |
| suffix | 0.99 [0.98, 1.01] | 1.00 | 100 | 0 | 1670 | 169 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2376 | 241 |

- gp_index minus el32: MR +0.94 [+0.90, +0.98]; accuracy +91 [+78, +100] points (n=32)
- gp_index minus carrier32: MR +0.96 [+0.93, +0.98]; accuracy +97 [+91, +100] points (n=32)
- gp_index minus erratum_field: MR +0.10 [-0.12, +0.30]; accuracy +16 [+3, +28] points (n=32)
- gp_index minus attn_blocks: MR +0.01 [-0.01, +0.02]; accuracy +0 [+0, +0] points (n=32)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=32)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=32)
- EditLocal at the path window's mean cost (851 tokens, log-interpolated): MR 0.81 vs gp_index 1.00
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / fanout3 (n=31, median distance 322 tokens, median doc 2913 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 90 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.03] | 0.01 | 3 | 90 | 1 | 25 |
| el32 | 0.03 [-0.00, 0.06] | 0.06 | 3 | 90 | 33 | 29 |
| el64 | 0.03 [-0.00, 0.06] | 0.05 | 3 | 90 | 65 | 30 |
| el128 | 0.03 [-0.00, 0.06] | 0.03 | 3 | 90 | 129 | 33 |
| el256 | 0.06 [0.01, 0.13] | 0.04 | 3 | 87 | 257 | 39 |
| el512 | 0.60 [0.43, 0.75] | 0.87 | 55 | 26 | 513 | 59 |
| el1024 | 0.69 [0.53, 0.84] | 0.95 | 71 | 26 | 1025 | 112 |
| boundary | 0.03 [-0.00, 0.06] | 0.05 | 3 | 90 | 68 | 30 |
| carrier32 | 0.21 [0.15, 0.27] | 0.20 | 13 | 68 | 33 | 31 |
| carrier_rows | 0.32 [0.26, 0.37] | 0.31 | 29 | 65 | 44 | 33 |
| attn_topk | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1413 | 152 |
| attn_blocks | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1397 | 149 |
| erratum_bare | 0.81 [0.68, 0.94] | 0.73 | 71 | 3 | 25 | nan |
| erratum_field | 0.76 [0.64, 0.89] | 0.69 | 68 | 6 | 26 | nan |
| erratum_el32 | 0.70 [0.59, 0.82] | 0.61 | 65 | 13 | 58 | nan |
| gp_index | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1413 | 145 |
| gp_llm | 0.31 [0.17, 0.47] | 0.06 | 32 | 65 | 323 | 50 |
| gp_hybrid | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1413 | 145 |
| gp_oracle | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1413 | 145 |
| suffix | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 2241 | 233 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2960 | 306 |

- gp_index minus el32: MR +0.97 [+0.93, +1.00]; accuracy +97 [+90, +100] points (n=31)
- gp_index minus carrier32: MR +0.79 [+0.72, +0.84]; accuracy +87 [+74, +97] points (n=31)
- gp_index minus erratum_field: MR +0.24 [+0.11, +0.36]; accuracy +32 [+16, +48] points (n=31)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.01]; accuracy +0 [+0, +0] points (n=31)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=31)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=31)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / noisy_d250 (n=42, median distance 320 tokens, median doc 1902 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 98 | 0 | 0 |
| edit_only | 0.01 [-0.01, 0.02] | 0.00 | 0 | 100 | 1 | 25 |
| el32 | 0.01 [-0.01, 0.03] | 0.00 | 0 | 95 | 33 | 29 |
| el64 | 0.01 [-0.01, 0.02] | 0.00 | 0 | 95 | 65 | 30 |
| el128 | 0.01 [-0.01, 0.02] | 0.01 | 0 | 95 | 129 | 33 |
| el256 | 0.02 [0.00, 0.05] | 0.01 | 0 | 95 | 257 | 39 |
| el512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 513 | 59 |
| el1024 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1024 | 111 |
| boundary | 0.01 [-0.01, 0.02] | 0.00 | 0 | 95 | 70 | 31 |
| carrier32 | 0.32 [0.27, 0.37] | 0.31 | 36 | 55 | 33 | 30 |
| carrier_rows | 0.32 [0.27, 0.36] | 0.30 | 36 | 55 | 17 | 28 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 359 | 46 |
| attn_blocks | 0.99 [0.97, 1.00] | 1.00 | 98 | 0 | 342 | 45 |
| erratum_bare | 1.00 [0.86, 1.14] | 0.86 | 100 | 0 | 25 | nan |
| erratum_field | 0.97 [0.84, 1.12] | 0.79 | 100 | 0 | 26 | nan |
| erratum_el32 | 0.80 [0.67, 0.93] | 0.69 | 76 | 0 | 58 | nan |
| gp_index | 0.99 [0.99, 1.00] | 0.99 | 98 | 2 | 359 | 44 |
| gp_llm | 0.11 [0.04, 0.21] | 0.02 | 7 | 90 | 115 | 32 |
| gp_hybrid | 0.99 [0.98, 1.00] | 0.99 | 98 | 2 | 368 | 44 |
| gp_oracle | 0.99 [0.99, 1.00] | 0.99 | 98 | 2 | 359 | 43 |
| suffix | 1.00 [0.99, 1.00] | 1.00 | 98 | 2 | 1225 | 126 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1952 | 188 |

- gp_index minus el32: MR +0.98 [+0.96, +1.00]; accuracy +98 [+93, +100] points (n=42)
- gp_index minus carrier32: MR +0.67 [+0.62, +0.72]; accuracy +62 [+48, +76] points (n=42)
- gp_index minus erratum_field: MR +0.02 [-0.13, +0.16]; accuracy -2 [-7, +0] points (n=42)
- gp_index minus attn_blocks: MR +0.00 [-0.01, +0.02]; accuracy +0 [-7, +7] points (n=42)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=42)
- gp_hybrid minus gp_index: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=42)
- EditLocal at the path window's mean cost (359 tokens, log-interpolated): MR 0.49 vs gp_index 0.99
- index graph: dependent recall 1.00, extra sentences 0.0

## mistral

350 items, 260 kept, 0 errors; rejected: {"oracle_answer": 42, "gap": 26, "stale_answer": 22}

### mistral / direct (n=50, median distance 0 tokens, median doc 1588 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.91 [0.86, 0.96] | 0.99 | 90 | 10 | 2 | 26 |
| el32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| el64 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 66 | 31 |
| el128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 33 |
| el256 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 258 | 39 |
| el512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 57 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 831 | 82 |
| boundary | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 75 | 31 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| attn_blocks | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| erratum_bare | 0.76 [0.74, 0.78] | 0.76 | 100 | 0 | 32 | nan |
| erratum_field | 0.81 [0.80, 0.83] | 0.81 | 100 | 0 | 34 | nan |
| erratum_el32 | 0.82 [0.81, 0.83] | 0.81 | 100 | 0 | 66 | nan |
| gp_index | 0.91 [0.86, 0.96] | 0.99 | 90 | 10 | 2 | 26 |
| gp_llm | 0.97 [0.93, 1.00] | 1.00 | 98 | 2 | 45 | 29 |
| gp_hybrid | 0.97 [0.93, 1.00] | 1.00 | 98 | 2 | 45 | 29 |
| suffix | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 831 | 82 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1618 | 151 |

- gp_index minus el32: MR -0.09 [-0.14, -0.04]; accuracy -10 [-20, -2] points (n=50)
- gp_index minus erratum_field: MR +0.10 [+0.04, +0.15]; accuracy -10 [-20, -2] points (n=50)
- gp_index minus attn_blocks: MR -0.09 [-0.14, -0.04]; accuracy -10 [-20, -2] points (n=50)
- gp_hybrid minus gp_index: MR +0.06 [+0.02, +0.10]; accuracy +8 [+2, +16] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / derived_d0 (n=49, median distance 1 tokens, median doc 1626 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.00 [-0.00, 0.01] | 0.00 | 0 | 100 | 2 | 26 |
| el32 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| el64 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 66 | 31 |
| el128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 33 |
| el256 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 258 | 39 |
| el512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 57 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 854 | 83 |
| boundary | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 93 | 32 |
| carrier32 | 0.69 [0.63, 0.74] | 0.72 | 69 | 29 | 34 | 29 |
| carrier_rows | 0.69 [0.63, 0.75] | 0.72 | 69 | 29 | 22 | 28 |
| attn_topk | 0.86 [0.81, 0.91] | 0.98 | 90 | 10 | 34 | 29 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| erratum_bare | 0.64 [0.54, 0.74] | 0.63 | 53 | 37 | 32 | nan |
| erratum_field | 0.48 [0.41, 0.56] | 0.47 | 43 | 49 | 34 | nan |
| erratum_el32 | 0.99 [0.95, 1.04] | 0.95 | 98 | 0 | 66 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 23 | 28 |
| gp_llm | 0.84 [0.74, 0.93] | 0.99 | 84 | 16 | 23 | 27 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 26 | 28 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 23 | 28 |
| suffix | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 854 | 83 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1636 | 153 |

- gp_index minus el32: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_index minus carrier32: MR +0.30 [+0.25, +0.36]; accuracy +31 [+18, +43] points (n=49)
- gp_index minus erratum_field: MR +0.51 [+0.44, +0.59]; accuracy +57 [+43, +69] points (n=49)
- gp_index minus attn_blocks: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_hybrid minus gp_index: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / derived_d250 (n=38, median distance 362 tokens, median doc 2079 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.00 [-0.01, 0.02] | -0.00 | 3 | 97 | 2 | 26 |
| el32 | 0.02 [0.00, 0.03] | 0.01 | 5 | 95 | 34 | 29 |
| el64 | 0.02 [0.00, 0.03] | -0.00 | 3 | 97 | 66 | 31 |
| el128 | 0.02 [0.00, 0.04] | 0.00 | 3 | 97 | 130 | 33 |
| el256 | 0.02 [0.00, 0.04] | -0.00 | 5 | 95 | 258 | 39 |
| el512 | 0.92 [0.83, 1.00] | 1.00 | 89 | 11 | 514 | 57 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1026 | 110 |
| boundary | 0.02 [0.00, 0.03] | 0.00 | 5 | 95 | 73 | 31 |
| carrier32 | 0.62 [0.53, 0.71] | 0.67 | 66 | 24 | 34 | 30 |
| carrier_rows | 0.62 [0.53, 0.71] | 0.66 | 66 | 24 | 21 | 28 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 397 | 48 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 97 | 3 | 383 | 47 |
| erratum_bare | 0.56 [0.44, 0.69] | 0.49 | 32 | 18 | 32 | nan |
| erratum_field | 0.48 [0.37, 0.60] | 0.41 | 26 | 24 | 34 | nan |
| erratum_el32 | 0.34 [0.26, 0.43] | 0.30 | 16 | 37 | 66 | nan |
| gp_index | 0.99 [0.99, 1.00] | 0.99 | 97 | 3 | 397 | 46 |
| gp_llm | 0.42 [0.27, 0.57] | 0.11 | 45 | 55 | 229 | 37 |
| gp_hybrid | 0.99 [0.99, 1.00] | 0.99 | 97 | 3 | 397 | 46 |
| gp_oracle | 0.99 [0.99, 1.00] | 0.99 | 97 | 3 | 397 | 46 |
| suffix | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1366 | 136 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2159 | 209 |

- gp_index minus el32: MR +0.98 [+0.96, +0.99]; accuracy +92 [+82, +100] points (n=38)
- gp_index minus carrier32: MR +0.37 [+0.28, +0.46]; accuracy +32 [+16, +47] points (n=38)
- gp_index minus erratum_field: MR +0.52 [+0.40, +0.63]; accuracy +71 [+55, +87] points (n=38)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=38)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=38)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=38)
- EditLocal at the path window's mean cost (397 tokens, log-interpolated): MR 0.59 vs gp_index 0.99
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / derived_d1500 (n=39, median distance 1740 tokens, median doc 3536 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 82 | 0 | 0 |
| edit_only | -0.02 [-0.05, 0.02] | 0.00 | 15 | 79 | 2 | 26 |
| el32 | -0.01 [-0.07, 0.03] | 0.00 | 26 | 69 | 34 | 29 |
| el64 | -0.01 [-0.07, 0.03] | 0.00 | 26 | 69 | 66 | 31 |
| el128 | -0.01 [-0.07, 0.03] | -0.00 | 23 | 72 | 130 | 33 |
| el256 | -0.01 [-0.06, 0.03] | -0.01 | 26 | 69 | 258 | 39 |
| el512 | -0.01 [-0.06, 0.03] | -0.00 | 26 | 69 | 514 | 57 |
| el1024 | -0.01 [-0.07, 0.03] | 0.00 | 26 | 69 | 1026 | 110 |
| boundary | -0.01 [-0.07, 0.03] | -0.01 | 26 | 69 | 70 | 31 |
| carrier32 | 0.56 [0.46, 0.66] | 0.60 | 67 | 21 | 34 | 33 |
| carrier_rows | 0.56 [0.45, 0.66] | 0.60 | 67 | 21 | 21 | 32 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1763 | 182 |
| attn_blocks | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1747 | 180 |
| erratum_bare | 0.57 [0.44, 0.71] | 0.38 | 28 | 13 | 32 | nan |
| erratum_field | 0.44 [0.32, 0.57] | 0.32 | 21 | 15 | 34 | nan |
| erratum_el32 | 0.26 [0.16, 0.37] | 0.20 | 10 | 31 | 66 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1763 | 172 |
| gp_llm | 0.25 [0.11, 0.41] | 0.03 | 36 | 59 | 561 | 71 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1763 | 172 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1763 | 172 |
| suffix | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 2728 | 286 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3523 | 369 |

- gp_index minus el32: MR +1.01 [+0.97, +1.06]; accuracy +74 [+59, +87] points (n=39)
- gp_index minus carrier32: MR +0.44 [+0.34, +0.54]; accuracy +33 [+18, +49] points (n=39)
- gp_index minus erratum_field: MR +0.55 [+0.42, +0.67]; accuracy +79 [+67, +90] points (n=39)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=39)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=39)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=39)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / hop3 (n=22, median distance 356 tokens, median doc 2660 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 64 | 0 | 0 |
| edit_only | -0.02 [-0.14, 0.08] | 0.01 | 18 | 55 | 2 | 26 |
| el32 | -0.07 [-0.23, 0.07] | 0.03 | 14 | 59 | 34 | 30 |
| el64 | -0.06 [-0.21, 0.07] | 0.03 | 14 | 59 | 66 | 31 |
| el128 | -0.05 [-0.20, 0.07] | 0.03 | 14 | 59 | 130 | 33 |
| el256 | -0.05 [-0.20, 0.08] | 0.03 | 14 | 59 | 258 | 39 |
| el512 | 0.03 [-0.11, 0.15] | 0.06 | 9 | 59 | 514 | 57 |
| el1024 | 0.70 [0.48, 0.88] | 0.99 | 73 | 18 | 1026 | 110 |
| boundary | -0.06 [-0.21, 0.07] | 0.03 | 14 | 59 | 70 | 31 |
| carrier32 | -0.02 [-0.14, 0.09] | 0.03 | 18 | 55 | 34 | 31 |
| carrier_rows | 0.56 [0.45, 0.66] | 0.58 | 55 | 27 | 39 | 31 |
| attn_topk | 1.00 [0.98, 1.01] | 1.00 | 100 | 0 | 979 | 103 |
| attn_blocks | 0.99 [0.98, 1.01] | 1.00 | 100 | 0 | 962 | 100 |
| erratum_bare | 0.18 [-0.11, 0.47] | 0.23 | 27 | 41 | 32 | nan |
| erratum_field | 0.15 [-0.15, 0.43] | 0.19 | 23 | 41 | 34 | nan |
| erratum_el32 | 0.03 [-0.26, 0.27] | 0.20 | 23 | 50 | 66 | nan |
| gp_index | 0.99 [0.98, 1.01] | 1.00 | 95 | 0 | 979 | 97 |
| gp_llm | 0.29 [0.11, 0.47] | 0.09 | 41 | 36 | 417 | 54 |
| gp_hybrid | 0.99 [0.98, 1.01] | 1.00 | 95 | 0 | 979 | 97 |
| gp_oracle | 0.99 [0.98, 1.01] | 1.00 | 95 | 0 | 979 | 97 |
| suffix | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1924 | 190 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2705 | 268 |

- gp_index minus el32: MR +1.07 [+0.93, +1.22]; accuracy +82 [+64, +95] points (n=22)
- gp_index minus carrier32: MR +1.01 [+0.90, +1.14]; accuracy +77 [+59, +91] points (n=22)
- gp_index minus erratum_field: MR +0.85 [+0.57, +1.14]; accuracy +73 [+55, +91] points (n=22)
- gp_index minus attn_blocks: MR -0.00 [-0.02, +0.02]; accuracy -5 [-14, +0] points (n=22)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=22)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=22)
- EditLocal at the path window's mean cost (979 tokens, log-interpolated): MR 0.65 vs gp_index 0.99
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / fanout3 (n=18, median distance 394 tokens, median doc 3447 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 67 | 0 | 0 |
| edit_only | 0.01 [-0.02, 0.03] | 0.00 | 11 | 72 | 2 | 26 |
| el32 | 0.03 [0.00, 0.06] | 0.02 | 17 | 61 | 34 | 29 |
| el64 | 0.03 [0.01, 0.05] | 0.02 | 17 | 61 | 66 | 31 |
| el128 | 0.03 [0.01, 0.06] | 0.02 | 22 | 61 | 130 | 33 |
| el256 | 0.03 [0.01, 0.06] | 0.02 | 22 | 61 | 258 | 39 |
| el512 | 0.41 [0.19, 0.63] | 0.10 | 50 | 33 | 514 | 57 |
| el1024 | 0.48 [0.26, 0.69] | 0.26 | 56 | 33 | 1026 | 110 |
| boundary | 0.03 [-0.00, 0.06] | 0.02 | 17 | 61 | 80 | 31 |
| carrier32 | 0.33 [0.16, 0.51] | 0.15 | 39 | 33 | 34 | 32 |
| carrier_rows | 0.66 [0.56, 0.76] | 0.72 | 72 | 6 | 53 | 33 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1655 | 172 |
| attn_blocks | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1639 | 171 |
| erratum_bare | 0.35 [0.24, 0.47] | 0.34 | 28 | 39 | 32 | nan |
| erratum_field | 0.30 [0.17, 0.42] | 0.29 | 11 | 50 | 34 | nan |
| erratum_el32 | 0.27 [0.14, 0.40] | 0.28 | 17 | 44 | 66 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1655 | 162 |
| gp_llm | 0.31 [0.13, 0.52] | 0.07 | 44 | 50 | 376 | 53 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1655 | 162 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1655 | 162 |
| suffix | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 2602 | 269 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3410 | 351 |

- gp_index minus el32: MR +0.97 [+0.94, +0.99]; accuracy +83 [+67, +100] points (n=18)
- gp_index minus carrier32: MR +0.66 [+0.49, +0.84]; accuracy +61 [+39, +83] points (n=18)
- gp_index minus erratum_field: MR +0.70 [+0.57, +0.82]; accuracy +89 [+72, +100] points (n=18)
- gp_index minus attn_blocks: MR +0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=18)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=18)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=18)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / noisy_d250 (n=44, median distance 394 tokens, median doc 2182 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 98 | 0 | 0 |
| edit_only | 0.01 [-0.01, 0.03] | 0.01 | 0 | 98 | 2 | 26 |
| el32 | 0.02 [-0.01, 0.04] | 0.01 | 2 | 95 | 34 | 29 |
| el64 | 0.02 [-0.00, 0.04] | 0.01 | 2 | 95 | 66 | 31 |
| el128 | 0.02 [-0.00, 0.04] | 0.01 | 2 | 95 | 130 | 33 |
| el256 | 0.02 [0.00, 0.04] | 0.01 | 2 | 95 | 258 | 39 |
| el512 | 0.84 [0.74, 0.94] | 0.99 | 84 | 16 | 514 | 57 |
| el1024 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1026 | 110 |
| boundary | 0.02 [-0.00, 0.04] | 0.01 | 2 | 95 | 82 | 31 |
| carrier32 | 0.68 [0.61, 0.76] | 0.77 | 55 | 39 | 34 | 30 |
| carrier_rows | 0.68 [0.61, 0.76] | 0.77 | 55 | 39 | 21 | 29 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 427 | 52 |
| attn_blocks | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 411 | 50 |
| erratum_bare | 0.53 [0.40, 0.67] | 0.51 | 41 | 27 | 32 | nan |
| erratum_field | 0.49 [0.35, 0.62] | 0.43 | 34 | 27 | 34 | nan |
| erratum_el32 | 0.41 [0.28, 0.53] | 0.35 | 23 | 39 | 66 | nan |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 427 | 48 |
| gp_llm | 0.11 [0.03, 0.21] | 0.01 | 11 | 84 | 120 | 32 |
| gp_hybrid | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 427 | 48 |
| gp_oracle | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 427 | 48 |
| suffix | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1420 | 141 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2218 | 215 |

- gp_index minus el32: MR +0.98 [+0.96, +1.00]; accuracy +98 [+93, +100] points (n=44)
- gp_index minus carrier32: MR +0.31 [+0.24, +0.39]; accuracy +45 [+30, +61] points (n=44)
- gp_index minus erratum_field: MR +0.51 [+0.38, +0.65]; accuracy +66 [+52, +80] points (n=44)
- gp_index minus attn_blocks: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=44)
- gp_oracle minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=44)
- gp_hybrid minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=44)
- EditLocal at the path window's mean cost (427 tokens, log-interpolated): MR 0.62 vs gp_index 1.00
- index graph: dependent recall 1.00, extra sentences 0.0


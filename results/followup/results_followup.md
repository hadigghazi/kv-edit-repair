# KV repair results

## qwen3

350 items, 322 kept, 0 errors; rejected: {"stale_answer": 4, "gap": 12, "oracle_answer": 12}

### qwen3 / direct (n=50, median distance 0 tokens, median doc 1436 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.96 [0.94, 0.98] | 0.99 | 98 | 0 | 2 | 28 |
| el32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 31 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 32 |
| gp_index | 0.96 [0.94, 0.98] | 0.99 | 98 | 0 | 2 | 28 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1465 | 152 |
| random_matched | 0.96 [0.94, 0.98] | 0.99 | 98 | 0 | 34 | 33 |
| random_blocks | 0.96 [0.93, 0.98] | 0.99 | 98 | 0 | 34 | 32 |
| attn_k32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 32 |
| attn_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 37 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 65 |
| attn_blocks_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 35 |
| attn_blocks_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 64 |
| attn_stop25 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 20 | 30 |
| attn_stop10 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 180 | 40 |

- gp_index minus random_matched: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus random_blocks: MR +0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus attn_stop25: MR -0.04 [-0.06, -0.02]; accuracy -2 [-6, +0] points (n=50)
- gp_index minus attn_k512: MR -0.04 [-0.06, -0.02]; accuracy -2 [-6, +0] points (n=50)
- gp_index minus el32: MR -0.04 [-0.06, -0.02]; accuracy -2 [-6, +0] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / derived_d0 (n=50, median distance 1 tokens, median doc 1480 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | -0.00 [-0.01, 0.00] | -0.00 | 0 | 100 | 1 | 26 |
| el32 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 33 | 31 |
| carrier_rows | 0.94 [0.92, 0.96] | 0.95 | 100 | 0 | 17 | 30 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 33 | 31 |
| gp_index | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 18 | 30 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1484 | 154 |
| stopshort | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 2 | 28 |
| random_matched | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 33 | 33 |
| random_blocks | 0.09 [0.01, 0.17] | 0.00 | 10 | 90 | 33 | 32 |
| attn_k32 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 33 | 31 |
| attn_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 129 | 36 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 513 | 65 |
| attn_blocks_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 129 | 35 |
| attn_blocks_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 64 |
| attn_stop25 | 0.96 [0.91, 0.99] | 1.00 | 94 | 6 | 22 | 30 |
| attn_stop10 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 131 | 36 |

- gp_index minus random_matched: MR +1.00 [+0.99, +1.01]; accuracy +100 [+100, +100] points (n=50)
- gp_index minus random_blocks: MR +0.91 [+0.82, +0.99]; accuracy +90 [+82, +98] points (n=50)
- gp_index minus stopshort: MR +1.00 [+0.99, +1.01]; accuracy +100 [+100, +100] points (n=50)
- gp_index minus attn_stop25: MR +0.04 [+0.01, +0.09]; accuracy +6 [+0, +14] points (n=50)
- gp_index minus attn_k512: MR +0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus el32: MR +0.00 [-0.00, +0.01]; accuracy +0 [+0, +0] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / derived_d250 (n=50, median distance 332 tokens, median doc 1879 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.02] | 0.00 | 0 | 100 | 1 | 26 |
| el32 | 0.01 [0.00, 0.03] | 0.01 | 0 | 100 | 33 | 31 |
| carrier_rows | 0.92 [0.90, 0.94] | 0.93 | 98 | 2 | 17 | 31 |
| attn_topk | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 360 | 52 |
| gp_index | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 360 | 49 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1947 | 202 |
| stopshort | 0.02 [0.01, 0.03] | 0.01 | 0 | 100 | 344 | 48 |
| random_matched | 0.05 [0.02, 0.09] | 0.01 | 2 | 96 | 360 | 52 |
| random_blocks | 0.21 [0.11, 0.31] | 0.02 | 24 | 76 | 344 | 51 |
| attn_k32 | 0.14 [0.11, 0.18] | 0.13 | 0 | 80 | 33 | 32 |
| attn_k128 | 0.96 [0.93, 0.99] | 0.99 | 96 | 4 | 129 | 37 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 67 |
| attn_blocks_k128 | 0.78 [0.67, 0.88] | 0.99 | 74 | 22 | 129 | 36 |
| attn_blocks_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 65 |
| attn_stop25 | 0.02 [-0.01, 0.07] | 0.00 | 2 | 98 | 301 | 46 |
| attn_stop10 | 0.53 [0.44, 0.63] | 0.37 | 36 | 40 | 428 | 55 |

- gp_index minus random_matched: MR +0.95 [+0.91, +0.98]; accuracy +98 [+92, +100] points (n=50)
- gp_index minus random_blocks: MR +0.79 [+0.69, +0.89]; accuracy +76 [+64, +88] points (n=50)
- gp_index minus stopshort: MR +0.98 [+0.97, +0.99]; accuracy +100 [+100, +100] points (n=50)
- gp_index minus attn_stop25: MR +0.98 [+0.93, +1.01]; accuracy +98 [+94, +100] points (n=50)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus el32: MR +0.98 [+0.97, +1.00]; accuracy +100 [+100, +100] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / derived_d1500 (n=48, median distance 1556 tokens, median doc 3170 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 96 | 0 | 0 |
| edit_only | -0.02 [-0.07, 0.01] | -0.00 | 0 | 96 | 1 | 26 |
| el32 | -0.02 [-0.07, 0.01] | 0.01 | 0 | 96 | 33 | 31 |
| carrier_rows | 0.93 [0.90, 0.96] | 0.94 | 94 | 2 | 17 | 34 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1591 | 183 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 98 | 0 | 1591 | 172 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3180 | 356 |
| stopshort | -0.02 [-0.07, 0.01] | 0.01 | 0 | 96 | 1574 | 171 |
| random_matched | 0.36 [0.27, 0.44] | 0.34 | 31 | 56 | 1591 | 183 |
| random_blocks | 0.49 [0.34, 0.62] | 0.66 | 46 | 48 | 1575 | 182 |
| attn_k32 | 0.04 [-0.00, 0.08] | 0.05 | 0 | 77 | 33 | 36 |
| attn_k128 | 0.60 [0.51, 0.70] | 0.57 | 48 | 31 | 129 | 40 |
| attn_k512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 513 | 73 |
| attn_blocks_k128 | 0.76 [0.66, 0.85] | 0.97 | 65 | 23 | 129 | 39 |
| attn_blocks_k512 | 0.99 [0.99, 1.00] | 1.00 | 98 | 0 | 513 | 70 |
| attn_stop25 | -0.03 [-0.07, 0.01] | 0.01 | 0 | 94 | 284 | 54 |
| attn_stop10 | 0.54 [0.42, 0.66] | 0.30 | 44 | 42 | 1660 | 179 |

- gp_index minus random_matched: MR +0.64 [+0.56, +0.73]; accuracy +67 [+54, +79] points (n=48)
- gp_index minus random_blocks: MR +0.51 [+0.38, +0.66]; accuracy +52 [+38, +67] points (n=48)
- gp_index minus stopshort: MR +1.02 [+0.98, +1.07]; accuracy +98 [+92, +100] points (n=48)
- gp_index minus attn_stop25: MR +1.02 [+0.99, +1.07]; accuracy +98 [+92, +100] points (n=48)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy -2 [-8, +0] points (n=48)
- gp_index minus el32: MR +1.02 [+0.98, +1.07]; accuracy +98 [+92, +100] points (n=48)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / hop3 (n=36, median distance 323 tokens, median doc 2426 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 94 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.03] | 0.00 | 3 | 94 | 1 | 27 |
| el32 | 0.02 [0.00, 0.04] | 0.02 | 3 | 94 | 33 | 31 |
| carrier_rows | 0.85 [0.80, 0.90] | 0.91 | 92 | 8 | 34 | 33 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 886 | 103 |
| gp_index | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 886 | 97 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2460 | 267 |
| stopshort | 0.03 [0.01, 0.05] | 0.02 | 3 | 94 | 336 | 47 |
| random_matched | 0.14 [0.09, 0.19] | 0.11 | 11 | 89 | 886 | 103 |
| random_blocks | 0.24 [0.13, 0.35] | 0.07 | 25 | 75 | 871 | 103 |
| attn_k32 | 0.07 [0.02, 0.12] | 0.04 | 8 | 92 | 33 | 32 |
| attn_k128 | 0.40 [0.29, 0.49] | 0.46 | 33 | 58 | 129 | 38 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 70 |
| attn_blocks_k128 | 0.26 [0.15, 0.37] | 0.21 | 22 | 75 | 129 | 36 |
| attn_blocks_k512 | 0.99 [0.97, 1.01] | 1.00 | 100 | 0 | 513 | 67 |
| attn_stop25 | 0.03 [0.00, 0.06] | 0.02 | 3 | 94 | 309 | 46 |
| attn_stop10 | 0.28 [0.16, 0.41] | 0.16 | 25 | 75 | 549 | 67 |

- gp_index minus random_matched: MR +0.86 [+0.81, +0.91]; accuracy +89 [+78, +97] points (n=36)
- gp_index minus random_blocks: MR +0.76 [+0.65, +0.87]; accuracy +75 [+61, +89] points (n=36)
- gp_index minus stopshort: MR +0.97 [+0.95, +0.99]; accuracy +97 [+92, +100] points (n=36)
- gp_index minus attn_stop25: MR +0.97 [+0.94, +0.99]; accuracy +97 [+92, +100] points (n=36)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=36)
- gp_index minus el32: MR +0.98 [+0.96, +1.00]; accuracy +97 [+92, +100] points (n=36)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / fanout3 (n=42, median distance 326 tokens, median doc 3031 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 93 | 0 | 0 |
| edit_only | -0.01 [-0.05, 0.02] | 0.01 | 0 | 95 | 1 | 26 |
| el32 | 0.00 [-0.05, 0.03] | 0.02 | 2 | 93 | 33 | 31 |
| carrier_rows | 0.92 [0.88, 0.95] | 0.96 | 98 | 2 | 44 | 35 |
| attn_topk | 1.00 [0.99, 1.01] | 1.01 | 100 | 0 | 1470 | 169 |
| gp_index | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1470 | 159 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3057 | 343 |
| stopshort | 0.00 [-0.05, 0.03] | 0.03 | 2 | 90 | 342 | 48 |
| random_matched | 0.26 [0.18, 0.35] | 0.18 | 19 | 62 | 1470 | 169 |
| random_blocks | 0.56 [0.44, 0.68] | 0.62 | 52 | 36 | 1454 | 168 |
| attn_k32 | 0.06 [0.00, 0.10] | 0.06 | 2 | 83 | 33 | 33 |
| attn_k128 | 0.56 [0.43, 0.69] | 0.59 | 60 | 40 | 129 | 39 |
| attn_k512 | 0.98 [0.96, 1.00] | 1.00 | 98 | 2 | 513 | 73 |
| attn_blocks_k128 | 0.41 [0.27, 0.55] | 0.14 | 38 | 50 | 129 | 36 |
| attn_blocks_k512 | 0.95 [0.88, 0.99] | 1.00 | 95 | 2 | 513 | 69 |
| attn_stop25 | 0.01 [-0.05, 0.04] | 0.01 | 5 | 90 | 249 | 42 |
| attn_stop10 | 0.35 [0.19, 0.51] | 0.12 | 36 | 55 | 722 | 84 |

- gp_index minus random_matched: MR +0.74 [+0.66, +0.82]; accuracy +81 [+69, +93] points (n=42)
- gp_index minus random_blocks: MR +0.44 [+0.32, +0.56]; accuracy +48 [+31, +62] points (n=42)
- gp_index minus stopshort: MR +1.00 [+0.97, +1.05]; accuracy +98 [+93, +100] points (n=42)
- gp_index minus attn_stop25: MR +1.00 [+0.96, +1.05]; accuracy +95 [+88, +100] points (n=42)
- gp_index minus attn_k512: MR +0.02 [+0.00, +0.05]; accuracy +2 [+0, +7] points (n=42)
- gp_index minus el32: MR +1.00 [+0.97, +1.05]; accuracy +98 [+93, +100] points (n=42)
- index graph: dependent recall 1.00, extra sentences 0.0

### qwen3 / noisy_d250 (n=46, median distance 344 tokens, median doc 1983 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 1 | 26 |
| el32 | 0.00 [-0.01, 0.01] | 0.00 | 0 | 100 | 33 | 31 |
| carrier_rows | 0.94 [0.92, 0.96] | 0.95 | 100 | 0 | 17 | 31 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 376 | 53 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 376 | 49 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2004 | 206 |
| stopshort | 0.01 [-0.00, 0.02] | 0.00 | 0 | 100 | 360 | 49 |
| random_matched | 0.07 [0.04, 0.12] | 0.03 | 9 | 91 | 376 | 53 |
| random_blocks | 0.21 [0.11, 0.33] | 0.01 | 22 | 78 | 358 | 52 |
| attn_k32 | 0.03 [0.01, 0.05] | 0.04 | 0 | 100 | 33 | 33 |
| attn_k128 | 0.85 [0.77, 0.91] | 0.98 | 91 | 9 | 129 | 37 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 67 |
| attn_blocks_k128 | 0.80 [0.68, 0.89] | 0.99 | 78 | 22 | 129 | 36 |
| attn_blocks_k512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 513 | 66 |
| attn_stop25 | -0.00 [-0.02, 0.01] | 0.01 | 0 | 100 | 253 | 43 |
| attn_stop10 | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 768 | 86 |

- gp_index minus random_matched: MR +0.92 [+0.88, +0.96]; accuracy +91 [+83, +98] points (n=46)
- gp_index minus random_blocks: MR +0.78 [+0.66, +0.89]; accuracy +78 [+65, +89] points (n=46)
- gp_index minus stopshort: MR +0.99 [+0.98, +1.00]; accuracy +100 [+100, +100] points (n=46)
- gp_index minus attn_stop25: MR +1.00 [+0.98, +1.01]; accuracy +100 [+100, +100] points (n=46)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=46)
- gp_index minus el32: MR +0.99 [+0.98, +1.00]; accuracy +100 [+100, +100] points (n=46)
- index graph: dependent recall 1.00, extra sentences 0.0

## llama

350 items, 263 kept, 0 errors; rejected: {"oracle_answer": 21, "stale_answer": 26, "gap": 40}

### llama / direct (n=50, median distance 0 tokens, median doc 1388 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.93 [0.89, 0.96] | 0.98 | 96 | 4 | 2 | 26 |
| el32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| gp_index | 0.93 [0.89, 0.96] | 0.98 | 96 | 4 | 2 | 26 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1441 | 144 |
| random_matched | 0.94 [0.90, 0.97] | 0.98 | 96 | 4 | 34 | 31 |
| random_blocks | 0.93 [0.89, 0.97] | 0.98 | 96 | 4 | 34 | 30 |
| attn_k32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| attn_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 35 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 61 |
| attn_blocks_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 33 |
| attn_blocks_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 61 |
| attn_stop25 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 21 | 27 |
| attn_stop10 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 91 | 32 |

- gp_index minus random_matched: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus random_blocks: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus attn_stop25: MR -0.07 [-0.11, -0.04]; accuracy -4 [-10, +0] points (n=50)
- gp_index minus attn_k512: MR -0.07 [-0.11, -0.04]; accuracy -4 [-10, +0] points (n=50)
- gp_index minus el32: MR -0.07 [-0.11, -0.04]; accuracy -4 [-10, +0] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / derived_d0 (n=49, median distance 1 tokens, median doc 1438 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 98 | 0 | 0 |
| edit_only | -0.02 [-0.03, -0.00] | -0.00 | 0 | 100 | 1 | 25 |
| el32 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 33 | 29 |
| carrier_rows | 0.46 [0.40, 0.51] | 0.47 | 29 | 41 | 17 | 27 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 33 | 29 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 18 | 27 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1457 | 144 |
| stopshort | 0.00 [-0.02, 0.02] | 0.01 | 0 | 98 | 2 | 26 |
| random_matched | -0.02 [-0.04, 0.00] | -0.00 | 0 | 100 | 33 | 30 |
| random_blocks | 0.07 [-0.01, 0.15] | -0.00 | 8 | 92 | 33 | 30 |
| attn_k32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 33 | 29 |
| attn_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 129 | 34 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 61 |
| attn_blocks_k128 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 129 | 33 |
| attn_blocks_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 61 |
| attn_stop25 | 0.94 [0.89, 0.99] | 1.00 | 98 | 2 | 23 | 28 |
| attn_stop10 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 61 | 30 |

- gp_index minus random_matched: MR +1.01 [+1.00, +1.03]; accuracy +100 [+100, +100] points (n=49)
- gp_index minus random_blocks: MR +0.93 [+0.85, +1.00]; accuracy +92 [+84, +98] points (n=49)
- gp_index minus stopshort: MR +0.99 [+0.98, +1.02]; accuracy +100 [+100, +100] points (n=49)
- gp_index minus attn_stop25: MR +0.05 [+0.01, +0.11]; accuracy +2 [+0, +6] points (n=49)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_index minus el32: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=49)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / derived_d250 (n=31, median distance 317 tokens, median doc 1804 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 94 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.02] | 0.01 | 3 | 94 | 1 | 24 |
| el32 | 0.04 [0.01, 0.06] | 0.05 | 6 | 87 | 33 | 29 |
| carrier_rows | 0.30 [0.26, 0.34] | 0.28 | 16 | 61 | 17 | 28 |
| attn_topk | 1.00 [0.99, 1.01] | 1.00 | 97 | 0 | 347 | 47 |
| gp_index | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 347 | 44 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1917 | 190 |
| stopshort | 0.04 [0.02, 0.06] | 0.04 | 6 | 87 | 331 | 43 |
| random_matched | 0.07 [0.03, 0.12] | 0.05 | 10 | 81 | 347 | 47 |
| random_blocks | 0.14 [0.07, 0.24] | 0.05 | 13 | 84 | 332 | 46 |
| attn_k32 | 0.12 [0.08, 0.17] | 0.12 | 16 | 55 | 33 | 30 |
| attn_k128 | 0.92 [0.87, 0.96] | 0.98 | 77 | 16 | 129 | 35 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 97 | 0 | 513 | 64 |
| attn_blocks_k128 | 0.82 [0.71, 0.92] | 1.00 | 81 | 13 | 129 | 34 |
| attn_blocks_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 62 |
| attn_stop25 | 0.09 [0.01, 0.19] | 0.05 | 10 | 81 | 115 | 32 |
| attn_stop10 | 0.76 [0.65, 0.87] | 0.99 | 71 | 10 | 378 | 47 |

- gp_index minus random_matched: MR +0.93 [+0.88, +0.97]; accuracy +90 [+77, +100] points (n=31)
- gp_index minus random_blocks: MR +0.86 [+0.76, +0.93]; accuracy +87 [+74, +97] points (n=31)
- gp_index minus stopshort: MR +0.96 [+0.93, +0.99]; accuracy +94 [+84, +100] points (n=31)
- gp_index minus attn_stop25: MR +0.91 [+0.80, +0.99]; accuracy +90 [+77, +100] points (n=31)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +3 [+0, +10] points (n=31)
- gp_index minus el32: MR +0.96 [+0.94, +0.99]; accuracy +94 [+84, +100] points (n=31)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / derived_d1500 (n=28, median distance 1500 tokens, median doc 3023 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 82 | 0 | 0 |
| edit_only | 0.02 [-0.01, 0.05] | 0.01 | 4 | 86 | 1 | 24 |
| el32 | 0.02 [-0.03, 0.07] | 0.02 | 4 | 82 | 33 | 29 |
| carrier_rows | 0.37 [0.32, 0.42] | 0.37 | 32 | 54 | 17 | 31 |
| attn_topk | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1530 | 168 |
| gp_index | 0.99 [0.98, 1.00] | 0.98 | 100 | 0 | 1530 | 160 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3067 | 326 |
| stopshort | 0.03 [-0.02, 0.07] | 0.02 | 0 | 86 | 1514 | 158 |
| random_matched | 0.32 [0.21, 0.44] | 0.23 | 18 | 46 | 1530 | 168 |
| random_blocks | 0.44 [0.29, 0.58] | 0.45 | 32 | 54 | 1519 | 168 |
| attn_k32 | 0.15 [0.07, 0.22] | 0.12 | 4 | 57 | 33 | 33 |
| attn_k128 | 0.65 [0.54, 0.76] | 0.69 | 54 | 32 | 129 | 37 |
| attn_k512 | 0.99 [0.98, 1.00] | 0.99 | 100 | 0 | 513 | 69 |
| attn_blocks_k128 | 0.75 [0.65, 0.85] | 0.97 | 71 | 14 | 129 | 36 |
| attn_blocks_k512 | 0.99 [0.99, 1.00] | 0.99 | 96 | 4 | 513 | 66 |
| attn_stop25 | 0.03 [-0.02, 0.08] | 0.03 | 4 | 82 | 22 | 27 |
| attn_stop10 | 0.79 [0.65, 0.91] | 0.99 | 71 | 7 | 1589 | 165 |

- gp_index minus random_matched: MR +0.67 [+0.56, +0.78]; accuracy +82 [+68, +93] points (n=28)
- gp_index minus random_blocks: MR +0.55 [+0.41, +0.70]; accuracy +68 [+50, +86] points (n=28)
- gp_index minus stopshort: MR +0.97 [+0.92, +1.01]; accuracy +100 [+100, +100] points (n=28)
- gp_index minus attn_stop25: MR +0.96 [+0.92, +1.01]; accuracy +96 [+89, +100] points (n=28)
- gp_index minus attn_k512: MR +0.00 [-0.01, +0.01]; accuracy +0 [+0, +0] points (n=28)
- gp_index minus el32: MR +0.97 [+0.93, +1.01]; accuracy +96 [+89, +100] points (n=28)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / hop3 (n=32, median distance 320 tokens, median doc 2330 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.03 [0.01, 0.06] | 0.02 | 3 | 97 | 1 | 25 |
| el32 | 0.06 [0.01, 0.10] | 0.04 | 9 | 91 | 33 | 29 |
| carrier_rows | 0.27 [0.21, 0.34] | 0.25 | 31 | 69 | 34 | 31 |
| attn_topk | 0.99 [0.98, 1.01] | 1.00 | 100 | 0 | 851 | 93 |
| gp_index | 1.00 [0.98, 1.01] | 1.00 | 100 | 0 | 851 | 88 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2376 | 249 |
| stopshort | 0.05 [0.02, 0.09] | 0.04 | 6 | 94 | 326 | 42 |
| random_matched | 0.12 [0.08, 0.17] | 0.12 | 6 | 91 | 851 | 94 |
| random_blocks | 0.15 [0.06, 0.24] | 0.05 | 9 | 88 | 837 | 93 |
| attn_k32 | 0.11 [-0.04, 0.25] | 0.13 | 12 | 84 | 33 | 30 |
| attn_k128 | 0.48 [0.41, 0.56] | 0.46 | 47 | 50 | 129 | 36 |
| attn_k512 | 1.00 [0.98, 1.01] | 1.00 | 100 | 0 | 513 | 66 |
| attn_blocks_k128 | 0.36 [0.19, 0.50] | 0.41 | 41 | 56 | 129 | 34 |
| attn_blocks_k512 | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 513 | 63 |
| attn_stop25 | 0.14 [0.07, 0.22] | 0.12 | 6 | 84 | 230 | 38 |
| attn_stop10 | 0.36 [0.17, 0.52] | 0.28 | 47 | 47 | 488 | 57 |

- gp_index minus random_matched: MR +0.87 [+0.82, +0.92]; accuracy +94 [+84, +100] points (n=32)
- gp_index minus random_blocks: MR +0.85 [+0.75, +0.93]; accuracy +91 [+81, +100] points (n=32)
- gp_index minus stopshort: MR +0.94 [+0.91, +0.98]; accuracy +94 [+84, +100] points (n=32)
- gp_index minus attn_stop25: MR +0.86 [+0.78, +0.93]; accuracy +94 [+84, +100] points (n=32)
- gp_index minus attn_k512: MR -0.00 [-0.02, +0.02]; accuracy +0 [+0, +0] points (n=32)
- gp_index minus el32: MR +0.94 [+0.90, +0.98]; accuracy +91 [+78, +100] points (n=32)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / fanout3 (n=31, median distance 322 tokens, median doc 2913 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 90 | 0 | 0 |
| edit_only | 0.01 [-0.00, 0.03] | 0.01 | 3 | 90 | 1 | 25 |
| el32 | 0.03 [-0.00, 0.06] | 0.06 | 3 | 90 | 33 | 29 |
| carrier_rows | 0.32 [0.26, 0.37] | 0.31 | 29 | 65 | 44 | 33 |
| attn_topk | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 1413 | 158 |
| gp_index | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 1413 | 150 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2960 | 316 |
| stopshort | 0.03 [-0.00, 0.06] | 0.04 | 3 | 90 | 330 | 43 |
| random_matched | 0.17 [0.12, 0.24] | 0.14 | 6 | 77 | 1413 | 158 |
| random_blocks | 0.36 [0.21, 0.52] | 0.12 | 35 | 58 | 1397 | 157 |
| attn_k32 | 0.01 [-0.03, 0.05] | 0.02 | 3 | 87 | 33 | 31 |
| attn_k128 | 0.68 [0.53, 0.82] | 0.89 | 61 | 32 | 129 | 37 |
| attn_k512 | 1.00 [0.99, 1.01] | 1.01 | 100 | 0 | 513 | 68 |
| attn_blocks_k128 | 0.55 [0.40, 0.72] | 0.86 | 58 | 26 | 129 | 34 |
| attn_blocks_k512 | 1.00 [0.99, 1.01] | 1.00 | 97 | 0 | 513 | 65 |
| attn_stop25 | 0.03 [-0.00, 0.07] | 0.05 | 3 | 90 | 49 | 28 |
| attn_stop10 | 0.50 [0.33, 0.66] | 0.30 | 48 | 32 | 549 | 63 |

- gp_index minus random_matched: MR +0.83 [+0.76, +0.88]; accuracy +94 [+84, +100] points (n=31)
- gp_index minus random_blocks: MR +0.63 [+0.48, +0.79]; accuracy +65 [+48, +81] points (n=31)
- gp_index minus stopshort: MR +0.97 [+0.94, +1.00]; accuracy +97 [+90, +100] points (n=31)
- gp_index minus attn_stop25: MR +0.97 [+0.93, +1.00]; accuracy +97 [+90, +100] points (n=31)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.01]; accuracy +0 [+0, +0] points (n=31)
- gp_index minus el32: MR +0.97 [+0.93, +1.00]; accuracy +97 [+90, +100] points (n=31)
- index graph: dependent recall 1.00, extra sentences 0.0

### llama / noisy_d250 (n=42, median distance 320 tokens, median doc 1902 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 98 | 0 | 0 |
| edit_only | 0.01 [-0.01, 0.02] | 0.00 | 0 | 100 | 1 | 25 |
| el32 | 0.01 [-0.01, 0.03] | 0.00 | 0 | 95 | 33 | 29 |
| carrier_rows | 0.32 [0.27, 0.36] | 0.30 | 36 | 55 | 17 | 28 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 359 | 47 |
| gp_index | 0.99 [0.99, 1.00] | 0.99 | 98 | 2 | 359 | 44 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1952 | 194 |
| stopshort | 0.01 [-0.01, 0.02] | 0.01 | 0 | 95 | 342 | 43 |
| random_matched | 0.06 [0.02, 0.09] | 0.03 | 5 | 86 | 359 | 47 |
| random_blocks | 0.11 [0.05, 0.19] | 0.03 | 10 | 86 | 342 | 47 |
| attn_k32 | 0.06 [0.03, 0.09] | 0.06 | 7 | 88 | 33 | 30 |
| attn_k128 | 0.80 [0.73, 0.87] | 0.92 | 64 | 31 | 129 | 35 |
| attn_k512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 513 | 64 |
| attn_blocks_k128 | 0.69 [0.57, 0.79] | 0.96 | 64 | 29 | 129 | 34 |
| attn_blocks_k512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 513 | 62 |
| attn_stop25 | 0.00 [-0.01, 0.02] | 0.00 | 0 | 95 | 128 | 33 |
| attn_stop10 | 0.95 [0.88, 1.00] | 1.00 | 93 | 5 | 612 | 66 |

- gp_index minus random_matched: MR +0.94 [+0.90, +0.97]; accuracy +93 [+83, +100] points (n=42)
- gp_index minus random_blocks: MR +0.88 [+0.80, +0.94]; accuracy +88 [+79, +98] points (n=42)
- gp_index minus stopshort: MR +0.98 [+0.96, +1.00]; accuracy +98 [+93, +100] points (n=42)
- gp_index minus attn_stop25: MR +0.99 [+0.97, +1.00]; accuracy +98 [+93, +100] points (n=42)
- gp_index minus attn_k512: MR -0.01 [-0.01, -0.00]; accuracy -2 [-7, +0] points (n=42)
- gp_index minus el32: MR +0.98 [+0.96, +1.00]; accuracy +98 [+93, +100] points (n=42)
- index graph: dependent recall 1.00, extra sentences 0.0

## mistral

350 items, 260 kept, 0 errors; rejected: {"oracle_answer": 42, "gap": 26, "stale_answer": 22}

### mistral / direct (n=50, median distance 0 tokens, median doc 1588 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.91 [0.86, 0.96] | 0.99 | 90 | 10 | 2 | 26 |
| el32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| gp_index | 0.91 [0.86, 0.96] | 0.99 | 90 | 10 | 2 | 26 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1618 | 155 |
| random_matched | 0.92 [0.87, 0.97] | 0.99 | 90 | 10 | 34 | 31 |
| random_blocks | 0.92 [0.87, 0.97] | 0.99 | 90 | 10 | 34 | 30 |
| attn_k32 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| attn_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 35 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 60 |
| attn_blocks_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 33 |
| attn_blocks_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 60 |
| attn_stop25 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 43 | 29 |
| attn_stop10 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 156 | 35 |

- gp_index minus random_matched: MR -0.01 [-0.03, +0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus random_blocks: MR -0.01 [-0.02, -0.00]; accuracy +0 [+0, +0] points (n=50)
- gp_index minus attn_stop25: MR -0.09 [-0.14, -0.04]; accuracy -10 [-20, -2] points (n=50)
- gp_index minus attn_k512: MR -0.08 [-0.14, -0.04]; accuracy -10 [-20, -2] points (n=50)
- gp_index minus el32: MR -0.09 [-0.14, -0.04]; accuracy -10 [-20, -2] points (n=50)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / derived_d0 (n=49, median distance 1 tokens, median doc 1626 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.00 [-0.00, 0.01] | 0.00 | 0 | 100 | 2 | 26 |
| el32 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 34 | 29 |
| carrier_rows | 0.69 [0.63, 0.75] | 0.72 | 69 | 29 | 22 | 28 |
| attn_topk | 0.86 [0.81, 0.91] | 0.98 | 90 | 10 | 34 | 29 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 23 | 28 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1636 | 158 |
| stopshort | 0.00 [-0.00, 0.01] | 0.00 | 0 | 100 | 3 | 26 |
| random_matched | 0.00 [-0.01, 0.01] | -0.00 | 0 | 100 | 34 | 31 |
| random_blocks | 0.05 [0.00, 0.11] | 0.00 | 4 | 96 | 34 | 30 |
| attn_k32 | 0.86 [0.81, 0.91] | 0.98 | 90 | 10 | 34 | 29 |
| attn_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 34 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 60 |
| attn_blocks_k128 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 130 | 33 |
| attn_blocks_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 60 |
| attn_stop25 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 37 | 28 |
| attn_stop10 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 107 | 33 |

- gp_index minus random_matched: MR +0.99 [+0.98, +1.01]; accuracy +100 [+100, +100] points (n=49)
- gp_index minus random_blocks: MR +0.95 [+0.89, +1.00]; accuracy +96 [+90, +100] points (n=49)
- gp_index minus stopshort: MR +0.99 [+0.98, +1.00]; accuracy +100 [+100, +100] points (n=49)
- gp_index minus attn_stop25: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=49)
- gp_index minus el32: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=49)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / derived_d250 (n=38, median distance 362 tokens, median doc 2079 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.00 [-0.01, 0.02] | -0.00 | 3 | 97 | 2 | 26 |
| el32 | 0.02 [0.00, 0.03] | 0.01 | 5 | 95 | 34 | 29 |
| carrier_rows | 0.62 [0.53, 0.71] | 0.66 | 66 | 24 | 21 | 29 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 397 | 49 |
| gp_index | 0.99 [0.99, 1.00] | 0.99 | 97 | 3 | 397 | 46 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2159 | 213 |
| stopshort | 0.02 [0.01, 0.04] | 0.00 | 5 | 95 | 378 | 46 |
| random_matched | 0.01 [-0.00, 0.03] | -0.00 | 5 | 95 | 397 | 50 |
| random_blocks | 0.21 [0.11, 0.32] | 0.01 | 18 | 76 | 383 | 49 |
| attn_k32 | 0.01 [-0.02, 0.03] | -0.01 | 8 | 89 | 34 | 30 |
| attn_k128 | 0.85 [0.76, 0.93] | 0.99 | 82 | 13 | 130 | 35 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 97 | 3 | 514 | 62 |
| attn_blocks_k128 | 0.90 [0.83, 0.97] | 0.99 | 84 | 11 | 130 | 34 |
| attn_blocks_k512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 514 | 61 |
| attn_stop25 | 0.05 [0.00, 0.11] | 0.00 | 8 | 92 | 266 | 40 |
| attn_stop10 | 0.51 [0.39, 0.63] | 0.36 | 53 | 29 | 442 | 51 |

- gp_index minus random_matched: MR +0.98 [+0.96, +1.00]; accuracy +92 [+82, +100] points (n=38)
- gp_index minus random_blocks: MR +0.78 [+0.67, +0.89]; accuracy +79 [+66, +92] points (n=38)
- gp_index minus stopshort: MR +0.97 [+0.96, +0.99]; accuracy +92 [+82, +100] points (n=38)
- gp_index minus attn_stop25: MR +0.94 [+0.88, +0.99]; accuracy +89 [+79, +97] points (n=38)
- gp_index minus attn_k512: MR -0.01 [-0.01, -0.00]; accuracy +0 [+0, +0] points (n=38)
- gp_index minus el32: MR +0.98 [+0.96, +0.99]; accuracy +92 [+82, +100] points (n=38)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / derived_d1500 (n=39, median distance 1740 tokens, median doc 3536 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 82 | 0 | 0 |
| edit_only | -0.02 [-0.05, 0.02] | 0.00 | 15 | 79 | 2 | 26 |
| el32 | -0.01 [-0.07, 0.03] | 0.00 | 26 | 69 | 34 | 29 |
| carrier_rows | 0.56 [0.45, 0.66] | 0.60 | 67 | 21 | 21 | 32 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1763 | 188 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1763 | 177 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3523 | 380 |
| stopshort | -0.01 [-0.07, 0.03] | 0.00 | 26 | 69 | 1744 | 176 |
| random_matched | 0.29 [0.18, 0.41] | 0.16 | 44 | 49 | 1763 | 189 |
| random_blocks | 0.44 [0.28, 0.59] | 0.32 | 54 | 38 | 1747 | 188 |
| attn_k32 | -0.02 [-0.07, 0.03] | -0.00 | 31 | 64 | 34 | 33 |
| attn_k128 | 0.62 [0.54, 0.70] | 0.62 | 59 | 15 | 130 | 38 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 69 |
| attn_blocks_k128 | 0.82 [0.71, 0.92] | 0.99 | 82 | 10 | 130 | 37 |
| attn_blocks_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 514 | 65 |
| attn_stop25 | -0.01 [-0.07, 0.03] | -0.01 | 26 | 67 | 569 | 75 |
| attn_stop10 | 0.40 [0.29, 0.51] | 0.30 | 67 | 28 | 1769 | 178 |

- gp_index minus random_matched: MR +0.70 [+0.59, +0.81]; accuracy +56 [+41, +72] points (n=39)
- gp_index minus random_blocks: MR +0.56 [+0.41, +0.71]; accuracy +46 [+31, +62] points (n=39)
- gp_index minus stopshort: MR +1.01 [+0.97, +1.06]; accuracy +74 [+59, +87] points (n=39)
- gp_index minus attn_stop25: MR +1.01 [+0.97, +1.06]; accuracy +74 [+59, +87] points (n=39)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +0 [+0, +0] points (n=39)
- gp_index minus el32: MR +1.01 [+0.97, +1.06]; accuracy +74 [+59, +87] points (n=39)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / hop3 (n=22, median distance 356 tokens, median doc 2660 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 64 | 0 | 0 |
| edit_only | -0.02 [-0.14, 0.08] | 0.01 | 18 | 55 | 2 | 26 |
| el32 | -0.07 [-0.23, 0.07] | 0.03 | 14 | 59 | 34 | 29 |
| carrier_rows | 0.56 [0.45, 0.66] | 0.58 | 55 | 27 | 39 | 31 |
| attn_topk | 1.00 [0.98, 1.01] | 1.00 | 100 | 0 | 979 | 107 |
| gp_index | 0.99 [0.98, 1.01] | 1.00 | 95 | 0 | 979 | 100 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2705 | 278 |
| stopshort | -0.05 [-0.20, 0.08] | 0.02 | 14 | 59 | 375 | 45 |
| random_matched | -0.00 [-0.12, 0.10] | 0.05 | 23 | 55 | 979 | 107 |
| random_blocks | 0.14 [-0.06, 0.39] | 0.07 | 14 | 59 | 962 | 105 |
| attn_k32 | -0.14 [-0.32, 0.01] | -0.03 | 9 | 68 | 34 | 30 |
| attn_k128 | 0.35 [0.20, 0.50] | 0.50 | 23 | 50 | 130 | 36 |
| attn_k512 | 0.99 [0.97, 1.00] | 1.00 | 100 | 0 | 514 | 65 |
| attn_blocks_k128 | 0.11 [-0.05, 0.28] | 0.11 | 23 | 50 | 130 | 34 |
| attn_blocks_k512 | 0.96 [0.89, 1.00] | 1.00 | 95 | 5 | 514 | 62 |
| attn_stop25 | -0.04 [-0.19, 0.09] | 0.02 | 18 | 64 | 310 | 42 |
| attn_stop10 | -0.03 [-0.20, 0.12] | 0.04 | 14 | 55 | 562 | 62 |

- gp_index minus random_matched: MR +0.99 [+0.89, +1.11]; accuracy +73 [+50, +91] points (n=22)
- gp_index minus random_blocks: MR +0.85 [+0.59, +1.06]; accuracy +82 [+64, +95] points (n=22)
- gp_index minus stopshort: MR +1.04 [+0.92, +1.18]; accuracy +82 [+64, +95] points (n=22)
- gp_index minus attn_stop25: MR +1.03 [+0.91, +1.17]; accuracy +77 [+55, +95] points (n=22)
- gp_index minus attn_k512: MR +0.00 [-0.00, +0.01]; accuracy -5 [-14, +0] points (n=22)
- gp_index minus el32: MR +1.07 [+0.93, +1.22]; accuracy +82 [+64, +95] points (n=22)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / fanout3 (n=18, median distance 394 tokens, median doc 3447 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 67 | 0 | 0 |
| edit_only | 0.01 [-0.02, 0.03] | 0.00 | 11 | 72 | 2 | 26 |
| el32 | 0.03 [0.00, 0.06] | 0.02 | 17 | 61 | 34 | 29 |
| carrier_rows | 0.66 [0.56, 0.76] | 0.72 | 72 | 6 | 53 | 34 |
| attn_topk | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1655 | 178 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 1655 | 167 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3410 | 362 |
| stopshort | 0.03 [0.01, 0.06] | 0.02 | 22 | 61 | 396 | 47 |
| random_matched | 0.21 [0.11, 0.32] | 0.18 | 22 | 61 | 1655 | 178 |
| random_blocks | 0.33 [0.17, 0.52] | 0.14 | 39 | 33 | 1639 | 177 |
| attn_k32 | 0.01 [-0.04, 0.06] | -0.02 | 11 | 67 | 34 | 30 |
| attn_k128 | 0.40 [0.21, 0.60] | 0.27 | 33 | 39 | 130 | 37 |
| attn_k512 | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 514 | 68 |
| attn_blocks_k128 | 0.38 [0.17, 0.59] | 0.11 | 39 | 33 | 130 | 34 |
| attn_blocks_k512 | 0.95 [0.86, 1.00] | 1.00 | 94 | 0 | 514 | 65 |
| attn_stop25 | 0.06 [0.01, 0.13] | 0.02 | 22 | 56 | 245 | 39 |
| attn_stop10 | 0.38 [0.18, 0.58] | 0.24 | 44 | 33 | 715 | 76 |

- gp_index minus random_matched: MR +0.79 [+0.68, +0.88]; accuracy +78 [+61, +94] points (n=18)
- gp_index minus random_blocks: MR +0.66 [+0.48, +0.83]; accuracy +61 [+39, +83] points (n=18)
- gp_index minus stopshort: MR +0.96 [+0.94, +0.99]; accuracy +78 [+61, +94] points (n=18)
- gp_index minus attn_stop25: MR +0.94 [+0.86, +0.99]; accuracy +78 [+56, +94] points (n=18)
- gp_index minus attn_k512: MR -0.00 [-0.00, +0.00]; accuracy +0 [+0, +0] points (n=18)
- gp_index minus el32: MR +0.97 [+0.94, +0.99]; accuracy +83 [+67, +100] points (n=18)
- index graph: dependent recall 1.00, extra sentences 0.0

### mistral / noisy_d250 (n=44, median distance 394 tokens, median doc 2182 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 98 | 0 | 0 |
| edit_only | 0.01 [-0.01, 0.03] | 0.01 | 0 | 98 | 2 | 26 |
| el32 | 0.02 [-0.01, 0.04] | 0.01 | 2 | 95 | 34 | 29 |
| carrier_rows | 0.68 [0.61, 0.76] | 0.77 | 55 | 39 | 21 | 29 |
| attn_topk | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 427 | 53 |
| gp_index | 1.00 [0.99, 1.00] | 1.00 | 100 | 0 | 427 | 49 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2218 | 222 |
| stopshort | 0.02 [0.00, 0.05] | 0.01 | 2 | 95 | 408 | 47 |
| random_matched | 0.07 [0.03, 0.12] | 0.03 | 2 | 93 | 427 | 53 |
| random_blocks | 0.18 [0.09, 0.28] | 0.02 | 16 | 82 | 411 | 52 |
| attn_k32 | 0.02 [-0.01, 0.04] | -0.00 | 2 | 95 | 34 | 30 |
| attn_k128 | 0.68 [0.60, 0.76] | 0.71 | 70 | 25 | 130 | 36 |
| attn_k512 | 1.00 [1.00, 1.00] | 1.00 | 98 | 2 | 514 | 63 |
| attn_blocks_k128 | 0.76 [0.66, 0.86] | 0.98 | 68 | 25 | 130 | 34 |
| attn_blocks_k512 | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 514 | 61 |
| attn_stop25 | 0.02 [-0.00, 0.05] | 0.01 | 2 | 95 | 285 | 41 |
| attn_stop10 | 0.98 [0.93, 1.01] | 1.00 | 98 | 0 | 822 | 84 |

- gp_index minus random_matched: MR +0.93 [+0.88, +0.97]; accuracy +98 [+93, +100] points (n=44)
- gp_index minus random_blocks: MR +0.82 [+0.72, +0.91]; accuracy +84 [+73, +93] points (n=44)
- gp_index minus stopshort: MR +0.98 [+0.95, +1.00]; accuracy +98 [+93, +100] points (n=44)
- gp_index minus attn_stop25: MR +0.98 [+0.95, +1.00]; accuracy +98 [+93, +100] points (n=44)
- gp_index minus attn_k512: MR -0.00 [-0.01, +0.00]; accuracy +2 [+0, +7] points (n=44)
- gp_index minus el32: MR +0.98 [+0.96, +1.00]; accuracy +98 [+93, +100] points (n=44)
- index graph: dependent recall 1.00, extra sentences 0.0


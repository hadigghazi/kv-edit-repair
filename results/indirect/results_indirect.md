# KV repair results

## qwen3

100 items, 61 kept, 0 errors; rejected: {"stale_answer": 15, "gap": 24}

### qwen3 / indirect_d250 (n=35, median distance 327 tokens, median doc 1944 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | -0.01 [-0.05, 0.03] | 0.01 | 3 | 97 | 1 | 29 |
| el32 | -0.02 [-0.08, 0.03] | 0.02 | 0 | 100 | 33 | 32 |
| el64 | -0.02 [-0.08, 0.03] | 0.01 | 0 | 100 | 65 | 33 |
| el128 | -0.02 [-0.08, 0.03] | 0.02 | 0 | 100 | 129 | 36 |
| el256 | -0.02 [-0.08, 0.03] | 0.01 | 0 | 100 | 257 | 44 |
| el512 | 0.94 [0.85, 1.01] | 1.00 | 94 | 6 | 513 | 62 |
| el1024 | 1.00 [0.99, 1.01] | 1.01 | 100 | 0 | 1025 | 121 |
| boundary | -0.02 [-0.07, 0.03] | 0.01 | 0 | 100 | 63 | 33 |
| carrier32 | 0.54 [0.37, 0.79] | 0.44 | 40 | 60 | 33 | 32 |
| carrier_rows | 0.54 [0.37, 0.79] | 0.45 | 40 | 60 | 17 | 31 |
| attn_topk | 0.37 [0.22, 0.52] | 0.17 | 34 | 66 | 362 | 60 |
| attn_blocks | 0.32 [0.16, 0.48] | 0.04 | 31 | 69 | 358 | 58 |
| erratum_bare | 0.42 [0.28, 0.54] | 0.47 | 46 | 54 | 25 | nan |
| erratum_field | 0.40 [0.28, 0.51] | 0.43 | 43 | 57 | 26 | nan |
| erratum_el32 | 0.18 [0.07, 0.29] | 0.12 | 29 | 71 | 58 | nan |
| gp_index | 0.32 [0.17, 0.47] | 0.04 | 34 | 66 | 341 | 56 |
| gp_llm | 0.06 [-0.02, 0.17] | 0.02 | 9 | 91 | 84 | 33 |
| gp_hybrid | 0.39 [0.24, 0.55] | 0.08 | 40 | 60 | 405 | 60 |
| gp_oracle | 1.00 [0.99, 1.01] | 1.00 | 100 | 0 | 376 | 50 |
| suffix | 1.00 [0.99, 1.01] | 1.01 | 100 | 0 | 1263 | 137 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1982 | 200 |
| stopshort | -0.01 [-0.07, 0.04] | 0.01 | 0 | 100 | 360 | 49 |
| random_matched | 0.23 [0.08, 0.44] | 0.04 | 20 | 80 | 362 | 61 |
| attn_k128 | 0.84 [0.74, 0.93] | 0.99 | 74 | 23 | 129 | 37 |
| attn_k512 | 1.00 [1.00, 1.01] | 1.00 | 100 | 0 | 513 | 66 |
| gp_edit_41 | 0.55 [0.39, 0.70] | 0.41 | 63 | 37 | 372 | 49 |
| gp_edit_4omini | -0.01 [-0.05, 0.03] | 0.01 | 3 | 97 | 2 | 29 |
| gp_edithyb_41 | 0.69 [0.56, 0.82] | 0.98 | 74 | 26 | 596 | 71 |
| gp_edithyb_4omini | 0.32 [0.17, 0.47] | 0.04 | 34 | 66 | 341 | 56 |
| gp_pre_41 | 0.88 [0.78, 0.97] | 0.99 | 86 | 14 | 367 | 49 |
| gp_pre_4omini | 0.06 [-0.02, 0.17] | 0.02 | 9 | 91 | 84 | 33 |
| gp_prehyb_41 | 0.90 [0.81, 0.98] | 1.00 | 89 | 11 | 591 | 70 |
| gp_prehyb_4omini | 0.39 [0.24, 0.55] | 0.08 | 40 | 60 | 405 | 60 |

- gp_index minus random_matched: MR +0.09 [-0.07, +0.23]; accuracy +14 [+3, +26] points (n=35)
- gp_index minus stopshort: MR +0.33 [+0.16, +0.50]; accuracy +34 [+20, +51] points (n=35)
- gp_index minus attn_k512: MR -0.69 [-0.84, -0.53]; accuracy -66 [-80, -49] points (n=35)
- gp_index minus el32: MR +0.34 [+0.17, +0.52]; accuracy +34 [+20, +51] points (n=35)
- gp_index minus carrier32: MR -0.23 [-0.48, +0.01]; accuracy -6 [-29, +17] points (n=35)
- gp_index minus erratum_field: MR -0.08 [-0.28, +0.14]; accuracy -9 [-31, +14] points (n=35)
- gp_index minus attn_blocks: MR -0.00 [-0.02, +0.02]; accuracy +3 [+0, +9] points (n=35)
- gp_oracle minus gp_index: MR +0.68 [+0.53, +0.83]; accuracy +66 [+49, +80] points (n=35)
- gp_hybrid minus gp_index: MR +0.07 [+0.01, +0.16]; accuracy +6 [+0, +14] points (n=35)
- gp_edithyb_4omini minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=35)
- gp_edithyb_41 minus gp_index: MR +0.37 [+0.24, +0.52]; accuracy +40 [+23, +57] points (n=35)
- gp_edithyb_41 minus gp_prehyb_41: MR -0.21 [-0.37, -0.05]; accuracy -14 [-34, +3] points (n=35)
- gp_oracle minus gp_edithyb_41: MR +0.31 [+0.18, +0.44]; accuracy +26 [+11, +43] points (n=35)
- gp_oracle minus gp_edithyb_4omini: MR +0.68 [+0.53, +0.83]; accuracy +66 [+49, +80] points (n=35)
- EditLocal at the path window's mean cost (341 tokens, log-interpolated): MR 0.37 vs gp_index 0.32
- rows new first (n=18): gp_index 0.28; gp_llm -0.02; gp_hybrid 0.30; gp_oracle 1.00; gp_edit_41 0.13; gp_edit_4omini -0.01; gp_edithyb_41 0.40; gp_edithyb_4omini 0.28; gp_pre_41 0.95; gp_pre_4omini -0.02; gp_prehyb_41 0.94; gp_prehyb_4omini 0.30
- rows old first (n=17): gp_index 0.36; gp_llm 0.15; gp_hybrid 0.48; gp_oracle 0.99; gp_edit_41 0.99; gp_edit_4omini -0.00; gp_edithyb_41 1.00; gp_edithyb_4omini 0.36; gp_pre_41 0.81; gp_pre_4omini 0.15; gp_prehyb_41 0.87; gp_prehyb_4omini 0.48
- index graph: dependent recall 0.00, extra sentences 2.3

### qwen3 / indirect_d1500 (n=26, median distance 1559 tokens, median doc 3096 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.04 [-0.02, 0.11] | 0.01 | 8 | 92 | 1 | 28 |
| el32 | 0.05 [-0.09, 0.18] | 0.02 | 12 | 88 | 33 | 31 |
| el64 | 0.04 [-0.10, 0.18] | 0.01 | 15 | 85 | 65 | 33 |
| el128 | 0.04 [-0.10, 0.17] | 0.01 | 12 | 88 | 129 | 35 |
| el256 | 0.04 [-0.10, 0.17] | 0.00 | 12 | 88 | 257 | 44 |
| el512 | 0.05 [-0.09, 0.18] | 0.01 | 12 | 88 | 513 | 62 |
| el1024 | 0.04 [-0.11, 0.17] | 0.00 | 12 | 88 | 1025 | 122 |
| boundary | 0.03 [-0.11, 0.16] | 0.02 | 12 | 88 | 62 | 32 |
| carrier32 | 0.43 [0.34, 0.53] | 0.39 | 46 | 54 | 33 | 36 |
| carrier_rows | 0.43 [0.33, 0.53] | 0.40 | 46 | 54 | 17 | 34 |
| attn_topk | 0.45 [0.24, 0.67] | 0.43 | 46 | 54 | 945 | 122 |
| attn_blocks | 0.48 [0.27, 0.69] | 0.38 | 50 | 50 | 938 | 118 |
| erratum_bare | 0.85 [0.45, 1.29] | 0.60 | 58 | 38 | 25 | nan |
| erratum_field | 0.61 [0.35, 0.90] | 0.51 | 54 | 46 | 26 | nan |
| erratum_el32 | 0.30 [0.02, 0.60] | 0.24 | 35 | 65 | 58 | nan |
| gp_index | 0.42 [0.24, 0.62] | 0.13 | 42 | 58 | 928 | 115 |
| gp_llm | 0.01 [-0.14, 0.13] | 0.00 | 12 | 88 | 38 | 31 |
| gp_hybrid | 0.41 [0.20, 0.63] | 0.22 | 42 | 58 | 951 | 117 |
| gp_oracle | 1.01 [0.99, 1.03] | 1.00 | 100 | 0 | 1594 | 169 |
| suffix | 0.99 [0.97, 1.02] | 0.99 | 100 | 0 | 2436 | 270 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3136 | 343 |
| stopshort | 0.04 [-0.10, 0.17] | 0.00 | 12 | 88 | 1578 | 168 |
| random_matched | 0.28 [0.13, 0.45] | 0.08 | 23 | 77 | 945 | 123 |
| attn_k128 | 0.41 [0.19, 0.59] | 0.36 | 54 | 46 | 129 | 40 |
| attn_k512 | 0.99 [0.97, 1.01] | 1.00 | 100 | 0 | 513 | 72 |
| gp_edit_41 | 0.61 [0.43, 0.77] | 0.80 | 58 | 42 | 1590 | 168 |
| gp_edit_4omini | 0.04 [-0.02, 0.11] | 0.01 | 8 | 92 | 1 | 29 |
| gp_edithyb_41 | 0.66 [0.49, 0.82] | 0.96 | 65 | 35 | 1809 | 194 |
| gp_edithyb_4omini | 0.42 [0.24, 0.62] | 0.13 | 42 | 58 | 928 | 115 |
| gp_pre_41 | 0.75 [0.54, 0.92] | 0.99 | 81 | 19 | 1350 | 147 |
| gp_pre_4omini | 0.01 [-0.14, 0.13] | 0.00 | 12 | 88 | 38 | 31 |
| gp_prehyb_41 | 0.80 [0.61, 0.96] | 0.99 | 85 | 15 | 1630 | 178 |
| gp_prehyb_4omini | 0.41 [0.20, 0.63] | 0.22 | 42 | 58 | 951 | 117 |

- gp_index minus random_matched: MR +0.14 [+0.05, +0.25]; accuracy +19 [+4, +35] points (n=26)
- gp_index minus stopshort: MR +0.39 [+0.18, +0.61]; accuracy +31 [+8, +50] points (n=26)
- gp_index minus attn_k512: MR -0.56 [-0.75, -0.37]; accuracy -58 [-77, -38] points (n=26)
- gp_index minus el32: MR +0.37 [+0.17, +0.60]; accuracy +31 [+8, +50] points (n=26)
- gp_index minus carrier32: MR -0.01 [-0.23, +0.23]; accuracy -4 [-35, +27] points (n=26)
- gp_index minus erratum_field: MR -0.19 [-0.46, +0.08]; accuracy -12 [-35, +15] points (n=26)
- gp_index minus attn_blocks: MR -0.05 [-0.14, +0.03]; accuracy -8 [-19, +0] points (n=26)
- gp_oracle minus gp_index: MR +0.58 [+0.39, +0.76]; accuracy +58 [+38, +77] points (n=26)
- gp_hybrid minus gp_index: MR -0.01 [-0.08, +0.04]; accuracy +0 [+0, +0] points (n=26)
- gp_edithyb_4omini minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=26)
- gp_edithyb_41 minus gp_index: MR +0.24 [+0.10, +0.40]; accuracy +23 [+8, +42] points (n=26)
- gp_edithyb_41 minus gp_prehyb_41: MR -0.13 [-0.33, +0.10]; accuracy -19 [-38, +0] points (n=26)
- gp_oracle minus gp_edithyb_41: MR +0.35 [+0.19, +0.51]; accuracy +35 [+15, +54] points (n=26)
- gp_oracle minus gp_edithyb_4omini: MR +0.58 [+0.39, +0.76]; accuracy +58 [+38, +77] points (n=26)
- EditLocal at the path window's mean cost (928 tokens, log-interpolated): MR 0.04 vs gp_index 0.42
- rows new first (n=13): gp_index 0.22; gp_llm 0.04; gp_hybrid 0.25; gp_oracle 0.99; gp_edit_41 0.19; gp_edit_4omini 0.01; gp_edithyb_41 0.33; gp_edithyb_4omini 0.22; gp_pre_41 0.69; gp_pre_4omini 0.04; gp_prehyb_41 0.75; gp_prehyb_4omini 0.25
- rows old first (n=13): gp_index 0.63; gp_llm -0.03; gp_hybrid 0.57; gp_oracle 1.03; gp_edit_41 1.03; gp_edit_4omini 0.08; gp_edithyb_41 1.00; gp_edithyb_4omini 0.63; gp_pre_41 0.80; gp_pre_4omini -0.03; gp_prehyb_41 0.85; gp_prehyb_4omini 0.57
- index graph: dependent recall 0.04, extra sentences 4.7

## llama

100 items, 25 kept, 0 errors; rejected: {"stale_answer": 9, "gap": 63, "oracle_answer": 3}

### llama / indirect_d250 (n=15, median distance 332 tokens, median doc 1882 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.04 [0.00, 0.08] | 0.04 | 0 | 100 | 1 | 25 |
| el32 | 0.07 [-0.01, 0.17] | 0.02 | 13 | 80 | 33 | 29 |
| el64 | 0.08 [-0.00, 0.17] | 0.03 | 13 | 80 | 65 | 31 |
| el128 | 0.07 [-0.01, 0.17] | 0.02 | 13 | 80 | 129 | 35 |
| el256 | 0.14 [0.00, 0.30] | 0.03 | 20 | 73 | 257 | 39 |
| el512 | 1.02 [1.00, 1.03] | 1.02 | 100 | 0 | 513 | 59 |
| el1024 | 1.02 [1.00, 1.04] | 1.02 | 100 | 0 | 1025 | 113 |
| boundary | 0.07 [-0.02, 0.16] | 0.02 | 13 | 80 | 60 | 30 |
| carrier32 | 0.39 [0.27, 0.52] | 0.38 | 27 | 73 | 33 | 30 |
| carrier_rows | 0.39 [0.26, 0.52] | 0.42 | 27 | 73 | 17 | 29 |
| attn_topk | 0.14 [-0.01, 0.32] | 0.04 | 33 | 67 | 108 | 36 |
| attn_blocks | 0.14 [0.01, 0.29] | 0.02 | 20 | 73 | 106 | 35 |
| erratum_bare | 1.07 [0.55, 1.75] | 0.64 | 80 | 20 | 25 | nan |
| erratum_field | 0.96 [0.53, 1.54] | 0.73 | 80 | 20 | 26 | nan |
| erratum_el32 | 0.59 [0.33, 0.85] | 0.42 | 60 | 40 | 58 | nan |
| gp_index | 0.11 [0.01, 0.25] | 0.05 | 7 | 93 | 78 | 31 |
| gp_llm | 0.05 [-0.05, 0.15] | 0.03 | 13 | 80 | 58 | 29 |
| gp_hybrid | 0.12 [-0.03, 0.28] | 0.04 | 20 | 73 | 134 | 35 |
| gp_oracle | 0.99 [0.97, 1.01] | 1.00 | 100 | 0 | 356 | 44 |
| suffix | 1.02 [1.01, 1.05] | 1.00 | 100 | 0 | 1234 | 126 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 1947 | 185 |
| stopshort | 0.07 [-0.02, 0.17] | 0.03 | 13 | 80 | 340 | 43 |
| random_matched | 0.07 [0.01, 0.16] | 0.03 | 7 | 93 | 108 | 38 |
| attn_k128 | 0.69 [0.46, 0.91] | 0.99 | 73 | 27 | 129 | 35 |
| attn_k512 | 1.02 [1.00, 1.04] | 1.00 | 100 | 0 | 513 | 62 |
| gp_edit_41 | 0.38 [0.14, 0.63] | 0.16 | 60 | 40 | 350 | 43 |
| gp_edit_4omini | 0.11 [0.01, 0.25] | 0.05 | 7 | 93 | 20 | 26 |
| gp_edithyb_41 | 0.44 [0.19, 0.69] | 0.25 | 60 | 40 | 399 | 48 |
| gp_edithyb_4omini | 0.17 [0.03, 0.35] | 0.06 | 13 | 87 | 97 | 32 |
| gp_pre_41 | 0.86 [0.67, 0.99] | 0.98 | 87 | 13 | 326 | 42 |
| gp_pre_4omini | 0.05 [-0.05, 0.15] | 0.03 | 13 | 80 | 58 | 29 |
| gp_prehyb_41 | 0.86 [0.67, 1.00] | 0.99 | 87 | 13 | 374 | 46 |
| gp_prehyb_4omini | 0.12 [-0.03, 0.28] | 0.04 | 20 | 73 | 134 | 35 |

- gp_index minus random_matched: MR +0.04 [-0.00, +0.10]; accuracy +0 [+0, +0] points (n=15)
- gp_index minus stopshort: MR +0.03 [-0.10, +0.20]; accuracy -7 [-33, +13] points (n=15)
- gp_index minus attn_k512: MR -0.91 [-1.01, -0.77]; accuracy -93 [-100, -80] points (n=15)
- gp_index minus el32: MR +0.03 [-0.10, +0.20]; accuracy -7 [-33, +13] points (n=15)
- gp_index minus carrier32: MR -0.29 [-0.43, -0.15]; accuracy -20 [-40, +0] points (n=15)
- gp_index minus erratum_field: MR -0.85 [-1.44, -0.36]; accuracy -73 [-93, -47] points (n=15)
- gp_index minus attn_blocks: MR -0.03 [-0.11, +0.04]; accuracy -13 [-33, +0] points (n=15)
- gp_oracle minus gp_index: MR +0.88 [+0.74, +0.97]; accuracy +93 [+80, +100] points (n=15)
- gp_hybrid minus gp_index: MR +0.01 [-0.07, +0.10]; accuracy +13 [+0, +33] points (n=15)
- gp_edithyb_4omini minus gp_index: MR +0.06 [+0.00, +0.19]; accuracy +7 [+0, +20] points (n=15)
- gp_edithyb_41 minus gp_index: MR +0.33 [+0.08, +0.59]; accuracy +53 [+27, +80] points (n=15)
- gp_edithyb_41 minus gp_prehyb_41: MR -0.42 [-0.72, -0.10]; accuracy -27 [-53, +0] points (n=15)
- gp_oracle minus gp_edithyb_41: MR +0.55 [+0.31, +0.79]; accuracy +40 [+20, +67] points (n=15)
- gp_oracle minus gp_edithyb_4omini: MR +0.82 [+0.64, +0.96]; accuracy +87 [+67, +100] points (n=15)
- EditLocal at the path window's mean cost (78 tokens, log-interpolated): MR 0.08 vs gp_index 0.11
- rows new first (n=10): gp_index 0.14; gp_llm 0.06; gp_hybrid 0.16; gp_oracle 0.98; gp_edit_41 0.07; gp_edit_4omini 0.04; gp_edithyb_41 0.16; gp_edithyb_4omini 0.14; gp_pre_41 0.88; gp_pre_4omini 0.06; gp_prehyb_41 0.88; gp_prehyb_4omini 0.16
- rows old first (n=5): gp_index 0.05; gp_llm 0.03; gp_hybrid 0.03; gp_oracle 1.01; gp_edit_41 1.01; gp_edit_4omini 0.24; gp_edithyb_41 1.01; gp_edithyb_4omini 0.24; gp_pre_41 0.82; gp_pre_4omini 0.03; gp_prehyb_41 0.82; gp_prehyb_4omini 0.03
- index graph: dependent recall 0.00, extra sentences 0.2

### llama / indirect_d1500 (n=10, median distance 1508 tokens, median doc 2976 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.06 [-0.05, 0.16] | 0.07 | 0 | 90 | 1 | 25 |
| el32 | 0.21 [0.02, 0.40] | 0.23 | 10 | 80 | 33 | 29 |
| el64 | 0.21 [0.02, 0.41] | 0.20 | 10 | 80 | 65 | 31 |
| el128 | 0.21 [0.02, 0.41] | 0.21 | 10 | 80 | 129 | 33 |
| el256 | 0.22 [0.02, 0.42] | 0.22 | 10 | 80 | 257 | 39 |
| el512 | 0.22 [0.02, 0.42] | 0.23 | 10 | 80 | 513 | 59 |
| el1024 | 0.23 [0.03, 0.42] | 0.23 | 10 | 80 | 1025 | 113 |
| boundary | 0.21 [0.02, 0.42] | 0.22 | 10 | 80 | 59 | 30 |
| carrier32 | 0.26 [0.13, 0.37] | 0.34 | 20 | 70 | 33 | 33 |
| carrier_rows | 0.25 [0.12, 0.37] | 0.33 | 10 | 80 | 17 | 32 |
| attn_topk | 0.53 [0.18, 0.84] | 0.67 | 50 | 40 | 868 | 108 |
| attn_blocks | 0.54 [0.21, 0.85] | 0.62 | 50 | 50 | 859 | 106 |
| erratum_bare | 1.55 [0.96, 2.45] | 1.18 | 90 | 10 | 24 | nan |
| erratum_field | 1.54 [0.86, 2.51] | 1.44 | 80 | 20 | 25 | nan |
| erratum_el32 | 1.21 [0.65, 2.01] | 0.90 | 80 | 20 | 57 | nan |
| gp_index | 0.39 [0.09, 0.69] | 0.10 | 40 | 60 | 852 | 101 |
| gp_llm | 0.31 [0.09, 0.56] | 0.26 | 20 | 70 | 190 | 41 |
| gp_hybrid | 0.49 [0.16, 0.81] | 0.54 | 50 | 50 | 1021 | 115 |
| gp_oracle | 1.01 [0.97, 1.04] | 1.00 | 100 | 0 | 1551 | 157 |
| suffix | 1.00 [0.97, 1.04] | 1.00 | 100 | 0 | 2398 | 255 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3103 | 322 |
| stopshort | 0.22 [0.03, 0.42] | 0.24 | 10 | 80 | 1535 | 155 |
| random_matched | 0.32 [0.08, 0.59] | 0.09 | 30 | 70 | 868 | 109 |
| attn_k128 | 0.56 [0.33, 0.75] | 0.67 | 30 | 60 | 129 | 38 |
| attn_k512 | 0.99 [0.91, 1.04] | 1.02 | 90 | 0 | 513 | 68 |
| gp_edit_41 | 0.71 [0.49, 0.93] | 0.93 | 60 | 40 | 1548 | 156 |
| gp_edit_4omini | 0.06 [-0.05, 0.16] | 0.07 | 0 | 90 | 1 | 25 |
| gp_edithyb_41 | 0.78 [0.55, 0.97] | 0.97 | 70 | 30 | 1749 | 179 |
| gp_edithyb_4omini | 0.39 [0.09, 0.69] | 0.10 | 40 | 60 | 852 | 101 |
| gp_pre_41 | 0.73 [0.44, 0.98] | 0.95 | 70 | 30 | 1077 | 116 |
| gp_pre_4omini | 0.31 [0.09, 0.56] | 0.26 | 20 | 70 | 190 | 41 |
| gp_prehyb_41 | 0.80 [0.49, 1.02] | 0.99 | 80 | 20 | 1531 | 159 |
| gp_prehyb_4omini | 0.49 [0.16, 0.81] | 0.54 | 50 | 50 | 1021 | 116 |

- gp_index minus random_matched: MR +0.07 [-0.03, +0.19]; accuracy +10 [+0, +30] points (n=10)
- gp_index minus stopshort: MR +0.16 [-0.01, +0.36]; accuracy +30 [+10, +60] points (n=10)
- gp_index minus attn_k512: MR -0.61 [-0.92, -0.26]; accuracy -50 [-90, +0] points (n=10)
- gp_index minus el32: MR +0.17 [-0.00, +0.38]; accuracy +30 [+10, +60] points (n=10)
- gp_index minus carrier32: MR +0.13 [-0.18, +0.48]; accuracy +20 [-30, +70] points (n=10)
- gp_index minus erratum_field: MR -1.16 [-2.00, -0.52]; accuracy -40 [-70, -10] points (n=10)
- gp_index minus attn_blocks: MR -0.16 [-0.39, +0.01]; accuracy -10 [-30, +0] points (n=10)
- gp_oracle minus gp_index: MR +0.62 [+0.32, +0.90]; accuracy +60 [+30, +90] points (n=10)
- gp_hybrid minus gp_index: MR +0.11 [-0.02, +0.31]; accuracy +10 [+0, +30] points (n=10)
- gp_edithyb_4omini minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=10)
- gp_edithyb_41 minus gp_index: MR +0.39 [+0.14, +0.67]; accuracy +30 [+0, +60] points (n=10)
- gp_edithyb_41 minus gp_prehyb_41: MR -0.02 [-0.28, +0.27]; accuracy -10 [-40, +20] points (n=10)
- gp_oracle minus gp_edithyb_41: MR +0.23 [+0.02, +0.45]; accuracy +30 [+0, +60] points (n=10)
- gp_oracle minus gp_edithyb_4omini: MR +0.62 [+0.32, +0.90]; accuracy +60 [+30, +90] points (n=10)
- EditLocal at the path window's mean cost (852 tokens, log-interpolated): MR 0.22 vs gp_index 0.39
- rows new first (n=4): gp_index 0.28; gp_llm 0.36; gp_hybrid 0.56; gp_oracle 1.03; gp_edit_41 0.29; gp_edit_4omini 0.09; gp_edithyb_41 0.46; gp_edithyb_4omini 0.28; gp_pre_41 0.59; gp_pre_4omini 0.36; gp_prehyb_41 0.79; gp_prehyb_4omini 0.56
- rows old first (n=6): gp_index 0.45; gp_llm 0.28; gp_hybrid 0.45; gp_oracle 0.99; gp_edit_41 0.99; gp_edit_4omini 0.05; gp_edithyb_41 0.99; gp_edithyb_4omini 0.45; gp_pre_41 0.81; gp_pre_4omini 0.28; gp_prehyb_41 0.81; gp_prehyb_4omini 0.45
- index graph: dependent recall 0.00, extra sentences 5.3

## mistral

100 items, 32 kept, 0 errors; rejected: {"stale_answer": 18, "oracle_answer": 8, "gap": 42}

### mistral / indirect_d250 (n=13, median distance 352 tokens, median doc 2134 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 100 | 0 | 0 |
| edit_only | 0.04 [0.01, 0.07] | 0.03 | 0 | 100 | 1 | 25 |
| el32 | -0.16 [-0.35, -0.01] | -0.04 | 0 | 100 | 33 | 30 |
| el64 | -0.18 [-0.37, -0.01] | -0.04 | 0 | 100 | 65 | 31 |
| el128 | -0.19 [-0.39, -0.01] | -0.03 | 0 | 100 | 129 | 34 |
| el256 | -0.19 [-0.39, -0.02] | -0.03 | 0 | 100 | 257 | 40 |
| el512 | 0.95 [0.79, 1.04] | 1.00 | 85 | 8 | 513 | 59 |
| el1024 | 1.01 [0.99, 1.02] | 1.00 | 100 | 0 | 1025 | 113 |
| boundary | -0.14 [-0.27, -0.02] | -0.04 | 0 | 100 | 68 | 31 |
| carrier32 | 0.49 [0.32, 0.68] | 0.45 | 46 | 54 | 33 | 30 |
| carrier_rows | 0.49 [0.32, 0.68] | 0.44 | 46 | 54 | 17 | 29 |
| attn_topk | 0.22 [-0.08, 0.54] | 0.04 | 31 | 69 | 330 | 54 |
| attn_blocks | 0.24 [-0.05, 0.56] | -0.00 | 31 | 69 | 324 | 52 |
| erratum_bare | 0.55 [0.13, 0.92] | 0.60 | 23 | 38 | 30 | nan |
| erratum_field | 0.64 [0.36, 0.90] | 0.68 | 15 | 23 | 31 | nan |
| erratum_el32 | 0.29 [0.05, 0.52] | 0.33 | 0 | 38 | 63 | nan |
| gp_index | 0.24 [0.02, 0.49] | 0.03 | 23 | 77 | 307 | 50 |
| gp_llm | -0.11 [-0.24, 0.01] | -0.00 | 0 | 100 | 46 | 29 |
| gp_hybrid | 0.13 [-0.15, 0.42] | -0.00 | 23 | 77 | 347 | 53 |
| gp_oracle | 1.02 [0.98, 1.07] | 0.99 | 85 | 8 | 399 | 47 |
| suffix | 1.02 [1.00, 1.04] | 1.00 | 92 | 8 | 1384 | 141 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 2175 | 211 |
| stopshort | -0.19 [-0.39, -0.02] | -0.05 | 0 | 100 | 383 | 46 |
| random_matched | 0.24 [0.05, 0.47] | 0.02 | 15 | 85 | 330 | 56 |
| attn_k128 | 0.78 [0.60, 0.93] | 0.90 | 69 | 15 | 129 | 36 |
| attn_k512 | 1.03 [1.01, 1.06] | 1.02 | 100 | 0 | 513 | 63 |
| gp_edit_41 | 0.57 [0.35, 0.78] | 0.51 | 62 | 38 | 394 | 47 |
| gp_edit_4omini | 0.11 [0.01, 0.27] | 0.03 | 8 | 92 | 26 | 26 |
| gp_edithyb_41 | 0.66 [0.41, 0.89] | 0.98 | 69 | 31 | 567 | 63 |
| gp_edithyb_4omini | 0.31 [0.06, 0.57] | 0.03 | 31 | 69 | 332 | 51 |
| gp_pre_41 | 0.94 [0.77, 1.06] | 0.99 | 77 | 15 | 362 | 45 |
| gp_pre_4omini | -0.11 [-0.24, 0.01] | -0.00 | 0 | 100 | 46 | 29 |
| gp_prehyb_41 | 0.93 [0.76, 1.03] | 0.99 | 77 | 15 | 533 | 61 |
| gp_prehyb_4omini | 0.13 [-0.15, 0.42] | -0.00 | 23 | 77 | 347 | 53 |

- gp_index minus random_matched: MR -0.00 [-0.09, +0.09]; accuracy +8 [+0, +23] points (n=13)
- gp_index minus stopshort: MR +0.43 [+0.16, +0.79]; accuracy +23 [+0, +46] points (n=13)
- gp_index minus attn_k512: MR -0.79 [-1.01, -0.54]; accuracy -77 [-100, -54] points (n=13)
- gp_index minus el32: MR +0.40 [+0.13, +0.78]; accuracy +23 [+0, +46] points (n=13)
- gp_index minus carrier32: MR -0.25 [-0.57, +0.09]; accuracy -23 [-62, +15] points (n=13)
- gp_index minus erratum_field: MR -0.40 [-0.79, -0.01]; accuracy +8 [+0, +23] points (n=13)
- gp_index minus attn_blocks: MR -0.00 [-0.28, +0.20]; accuracy -8 [-23, +0] points (n=13)
- gp_oracle minus gp_index: MR +0.78 [+0.54, +0.99]; accuracy +62 [+38, +85] points (n=13)
- gp_hybrid minus gp_index: MR -0.11 [-0.23, -0.02]; accuracy +0 [+0, +0] points (n=13)
- gp_edithyb_4omini minus gp_index: MR +0.07 [+0.00, +0.21]; accuracy +8 [+0, +23] points (n=13)
- gp_edithyb_41 minus gp_index: MR +0.42 [+0.16, +0.71]; accuracy +46 [+23, +77] points (n=13)
- gp_edithyb_41 minus gp_prehyb_41: MR -0.26 [-0.54, -0.04]; accuracy -8 [-38, +15] points (n=13)
- gp_oracle minus gp_edithyb_41: MR +0.36 [+0.15, +0.59]; accuracy +15 [+0, +38] points (n=13)
- gp_oracle minus gp_edithyb_4omini: MR +0.71 [+0.45, +0.95]; accuracy +54 [+31, +77] points (n=13)
- EditLocal at the path window's mean cost (307 tokens, log-interpolated): MR 0.10 vs gp_index 0.24
- rows new first (n=8): gp_index 0.29; gp_llm -0.19; gp_hybrid 0.13; gp_oracle 1.02; gp_edit_41 0.29; gp_edit_4omini 0.04; gp_edithyb_41 0.44; gp_edithyb_4omini 0.29; gp_pre_41 0.89; gp_pre_4omini -0.19; gp_prehyb_41 0.87; gp_prehyb_4omini 0.13
- rows old first (n=5): gp_index 0.16; gp_llm 0.02; gp_hybrid 0.13; gp_oracle 1.03; gp_edit_41 1.03; gp_edit_4omini 0.23; gp_edithyb_41 1.02; gp_edithyb_4omini 0.34; gp_pre_41 1.03; gp_pre_4omini 0.02; gp_prehyb_41 1.02; gp_prehyb_4omini 0.13
- index graph: dependent recall 0.00, extra sentences 2.3

### mistral / indirect_d1500 (n=19, median distance 1705 tokens, median doc 3430 tokens)

| arm | MR mean [95% CI] | MR median | accuracy % | old answer % | tokens recomputed (mean) | ms (mean) |
|---|---|---|---|---|---|---|
| none | 0.00 [0.00, 0.00] | 0.00 | 0 | 63 | 0 | 0 |
| edit_only | 0.14 [-0.06, 0.34] | 0.07 | 16 | 63 | 1 | 25 |
| el32 | 0.08 [-0.15, 0.28] | 0.12 | 21 | 58 | 33 | 30 |
| el64 | -0.00 [-0.29, 0.27] | 0.15 | 21 | 58 | 65 | 31 |
| el128 | 0.01 [-0.29, 0.29] | 0.13 | 21 | 58 | 129 | 35 |
| el256 | 0.01 [-0.29, 0.28] | 0.13 | 21 | 58 | 257 | 40 |
| el512 | 0.02 [-0.28, 0.28] | 0.12 | 21 | 58 | 513 | 59 |
| el1024 | 0.00 [-0.30, 0.28] | 0.16 | 21 | 58 | 1025 | 112 |
| boundary | 0.03 [-0.24, 0.27] | 0.14 | 21 | 58 | 73 | 31 |
| carrier32 | 0.46 [0.25, 0.68] | 0.40 | 47 | 32 | 33 | 34 |
| carrier_rows | 0.45 [0.24, 0.66] | 0.40 | 42 | 37 | 17 | 32 |
| attn_topk | 0.47 [0.21, 0.71] | 0.48 | 53 | 37 | 977 | 121 |
| attn_blocks | 0.49 [0.27, 0.71] | 0.38 | 53 | 42 | 968 | 118 |
| erratum_bare | 0.74 [0.09, 1.41] | 0.68 | 47 | 11 | 30 | nan |
| erratum_field | 0.81 [0.41, 1.34] | 0.69 | 26 | 5 | 31 | nan |
| erratum_el32 | 0.43 [0.04, 0.83] | 0.45 | 16 | 16 | 63 | nan |
| gp_index | 0.42 [0.17, 0.66] | 0.50 | 42 | 42 | 960 | 113 |
| gp_llm | 0.12 [-0.16, 0.37] | 0.19 | 26 | 53 | 64 | 30 |
| gp_hybrid | 0.43 [0.17, 0.67] | 0.31 | 47 | 37 | 995 | 116 |
| gp_oracle | 0.98 [0.96, 1.00] | 0.99 | 95 | 5 | 1741 | 174 |
| suffix | 0.99 [0.97, 1.02] | 1.00 | 100 | 0 | 2688 | 289 |
| full | 1.00 [1.00, 1.00] | 1.00 | 100 | 0 | 3508 | 374 |
| stopshort | -0.00 [-0.31, 0.28] | 0.13 | 21 | 58 | 1725 | 172 |
| random_matched | 0.27 [0.02, 0.51] | 0.23 | 32 | 53 | 977 | 123 |
| attn_k128 | 0.26 [-0.06, 0.57] | 0.40 | 37 | 47 | 129 | 38 |
| attn_k512 | 0.98 [0.93, 1.02] | 1.00 | 95 | 0 | 513 | 69 |
| gp_edit_41 | 0.77 [0.62, 0.90] | 0.96 | 74 | 16 | 1738 | 174 |
| gp_edit_4omini | 0.14 [-0.06, 0.34] | 0.07 | 16 | 63 | 1 | 25 |
| gp_edithyb_41 | 0.83 [0.71, 0.94] | 0.96 | 79 | 16 | 1940 | 197 |
| gp_edithyb_4omini | 0.42 [0.17, 0.66] | 0.50 | 42 | 42 | 960 | 113 |
| gp_pre_41 | 0.91 [0.80, 0.98] | 0.97 | 89 | 11 | 1553 | 158 |
| gp_pre_4omini | 0.12 [-0.16, 0.37] | 0.19 | 26 | 53 | 64 | 30 |
| gp_prehyb_41 | 0.93 [0.82, 0.99] | 0.97 | 89 | 11 | 1756 | 182 |
| gp_prehyb_4omini | 0.43 [0.17, 0.67] | 0.31 | 47 | 37 | 995 | 116 |

- gp_index minus random_matched: MR +0.15 [+0.02, +0.34]; accuracy +11 [+0, +26] points (n=19)
- gp_index minus stopshort: MR +0.42 [+0.05, +0.84]; accuracy +21 [+0, +42] points (n=19)
- gp_index minus attn_k512: MR -0.56 [-0.83, -0.31]; accuracy -53 [-79, -26] points (n=19)
- gp_index minus el32: MR +0.34 [+0.05, +0.68]; accuracy +21 [+0, +42] points (n=19)
- gp_index minus carrier32: MR -0.04 [-0.25, +0.18]; accuracy -5 [-32, +21] points (n=19)
- gp_index minus erratum_field: MR -0.39 [-0.90, +0.05]; accuracy +16 [-5, +37] points (n=19)
- gp_index minus attn_blocks: MR -0.07 [-0.24, +0.11]; accuracy -11 [-32, +11] points (n=19)
- gp_oracle minus gp_index: MR +0.56 [+0.33, +0.82]; accuracy +53 [+32, +74] points (n=19)
- gp_hybrid minus gp_index: MR +0.01 [-0.11, +0.09]; accuracy +5 [+0, +16] points (n=19)
- gp_edithyb_4omini minus gp_index: MR +0.00 [+0.00, +0.00]; accuracy +0 [+0, +0] points (n=19)
- gp_edithyb_41 minus gp_index: MR +0.41 [+0.17, +0.69]; accuracy +37 [+11, +63] points (n=19)
- gp_edithyb_41 minus gp_prehyb_41: MR -0.09 [-0.19, -0.01]; accuracy -11 [-32, +11] points (n=19)
- gp_oracle minus gp_edithyb_41: MR +0.15 [+0.05, +0.26]; accuracy +16 [+0, +32] points (n=19)
- gp_oracle minus gp_edithyb_4omini: MR +0.56 [+0.33, +0.82]; accuracy +53 [+32, +74] points (n=19)
- EditLocal at the path window's mean cost (960 tokens, log-interpolated): MR 0.01 vs gp_index 0.42
- rows new first (n=8): gp_index 0.48; gp_llm 0.25; gp_hybrid 0.41; gp_oracle 0.96; gp_edit_41 0.45; gp_edit_4omini 0.29; gp_edithyb_41 0.62; gp_edithyb_4omini 0.48; gp_pre_41 0.85; gp_pre_4omini 0.25; gp_prehyb_41 0.84; gp_prehyb_4omini 0.41
- rows old first (n=11): gp_index 0.38; gp_llm 0.01; gp_hybrid 0.44; gp_oracle 1.00; gp_edit_41 1.00; gp_edit_4omini 0.03; gp_edithyb_41 0.99; gp_edithyb_4omini 0.38; gp_pre_41 0.96; gp_pre_4omini 0.01; gp_prehyb_41 0.99; gp_prehyb_4omini 0.44
- index graph: dependent recall 0.00, extra sentences 4.7


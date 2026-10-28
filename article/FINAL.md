---
title: "Do RAG chunking strategies actually differ? Error bars, 2 embedding models and an overlap sweep"
subtitle: "64 documents, 215 questions, five strategies, sizes in tokens, a dev/test split and paired bootstrap confidence intervals. Code and raw results included."
canonical_url: ""
tags: rag, retrieval, llm, benchmarking
---

# Do RAG chunking strategies actually differ? Error bars, 2 embedding models and an overlap sweep

Chunking is the step everyone has an opinion about and almost nobody measures with error bars.
Blog posts rank the strategies confidently; the gaps they report are often two or three points,
reported once, from a single run, with no interval around them.

I went looking for how much of that advice survives a significance test. Five strategies, a corpus
of 64 documents, 215 questions, 2 embedding models, chunk sizes in tokens, and the
part that matters: **every setting chosen on a held-out dev split and every number reported on test
questions the tuning never saw**, with paired bootstrap confidence intervals over 5,000 resamples.

**The short answer: on one embedding model two of the four alternatives beat plain
fixed-size chunking, and on a second model none of those still do.** Against the
fixed 200 baseline on MRR@10 with bge-small, only 2 of the other four strategies
beat it with an interval clear of zero: **Sentence-based** +0.093 [+0.032, +0.155]; **Fixed + overlap** +0.073 [+0.017, +0.131]. The others (Recursive, Semantic) have
point estimates above the baseline but intervals that include it.

Then I ran the **identical chunks** through minilm, and the picture did not hold:
**Fixed + overlap** +0.037 [-0.016, +0.093] (not distinguishable); **Recursive** +0.068 [+0.019, +0.116]; **Semantic** +0.010 [-0.050, +0.075] (not distinguishable); **Sentence-based** +0.025 [-0.021, +0.071] (not distinguishable). No strategy beats plain fixed-size with an interval clear of zero on both models. What does survive the model change is weaker but more
useful: the worst strategy is the same on both models (Fixed-size) but the best is not, and 3 of the five strategies hold their rank throughout
(Fixed + overlap, Semantic, Fixed-size).

That is the finding I would actually stand behind, and it is a warning about every chunking
comparison you have read, including the first half of this one: **a chunking result measured on one
embedding model mostly describes that model.** Three further things came out of it:

1. **Strategy may matter more than size, on both models.** Switching strategy at a fixed size moves
   MRR by 0.029 to 0.121 (mean 0.081); changing size within a strategy moves it
   by 0.035 to 0.064 (mean 0.052). And this replicates on the second model
   (strategy 0.050 vs size 0.036), which is mild evidence that it is not purely an artefact of one encoder, though two small models are not the world.
2. **Overlap helps, and nothing beyond the smallest step is resolvable.** Going from no overlap to
   20 tokens (10%) is worth +0.066 MRR. Going from there all the way to 80 tokens (40%) is
   +0.007 MRR (95% CI [-0.054, +0.066]), which is not distinguishable from zero.
3. **The published way of measuring overlap's cost is partly an artefact.** The standard
   implementation counts text appearing in two overlapping chunks twice, which penalises overlap by
   construction rather than by evidence. Details below.

**What this is not:** a new finding about which chunker wins. That ground is covered (see
[Prior work](#prior-work)). What I believe is genuinely missing from the published work, and what
this adds, is narrow: **confidence intervals and paired significance tests between strategies**, and
**an actual sweep over overlap values**. I could not find either in the evaluations I read.

**Disclosure:** I am a final-year CS student. Nobody paid for this, I am not affiliated with any
vector database or embedding vendor, and I have no stake in which strategy wins. Repo:
**https://github.com/vaishnavi-sonawane27/RAG-Chunking-Strategies**.

## The setup

| | |
|---|---|
| **Corpus** | *Pro Git* (2nd ed.), Chacon & Straub, 64 sections, ~107,000 words (~175,000 tokens), CC BY-NC-SA 3.0 |
| **Questions** | 215 questions, each tied to one evidence passage that occurs exactly once |
| **Split** | 64 dev (chooses settings) / 151 test (reported). Stratified by document, seed 0 |
| **Chunk sizes** | 100, 200, 400 tokens, measured with the bge-small WordPiece vocabulary |
| **Overlap sweep** | 20, 40, 80 tokens at a 200-token chunk size |
| **Embedding models** | bge-small and minilm, ONNX, cosine similarity, top-10 |
| **Baselines** | BM25 over the identical chunks; fixed 200 as the reference configuration |
| **Metrics** | Recall@1/3, MRR@10, recall at a fixed 1000-token budget, and token-level recall / precision / IoU at k=5 |
| **Statistics** | 5,000 paired bootstrap resamples over the test questions |
| **Platform** | Python 3.13.17, 2 CPU cores, Linux-6.18.44-fc-v180-x86_64-with-glibc2.39. One model: ~16 min |

Four design choices do most of the work.

**Sizes are in tokens, not words.** Every serious evaluation in this space reports token sizes, so
word-based sizes cannot be compared with any of them. One canonical tokenizer is used for sizing no
matter which model is being scored, so chunk boundaries stay identical across models and a
difference between models is a difference in the model.

**A relevance rule that does not depend on chunking.** A retrieved chunk counts as relevant if it
lies in the right document and covers at least half of the question's evidence passage. That rule is
identical for every strategy, so a strategy that slices the answer in half is penalised. I also
report how often the evidence survives *whole* inside a single chunk.

**A fixed context budget.** Comparing at the same `k` quietly favours small chunks: ten 70-token
chunks is a different amount of context than ten 370-token chunks. So alongside recall@k I report
recall at a fixed 1000-token budget: fill the context window and see who got the answer in.

**Context efficiency, not just recall.** Recall@k cannot tell a tight chunk that is mostly answer
from a long one with the answer buried in padding, and in production you pay per token. Token-level
precision is the share of everything you retrieved that was actually the answer. Across the sizes
tried it ranges from 3.58% at 100 tokens to 1.13% at 400 tokens for fixed-size chunking, a larger relative swing
than anything in the recall numbers.

Settings chosen on dev: `fixed 200`, `fixed_overlap 200+80`, `recursive 200`, `semantic 85`, `sentence 200`.

## Results

<!-- generated by scripts/make_report.py from results/bge-small; do not edit by hand -->

**Run:** bge-small · 64 documents · 215 questions · 5,000 bootstrap resamples. Sizes are in bge-small WordPiece tokens.

**Protocol:** chunk sizes, overlaps and thresholds were chosen on 64 dev questions; every number below is measured on the 151 held-out test questions (split seed 0). Selected on dev: `fixed 200`, `fixed_overlap 200+80`, `recursive 200`, `semantic 85`, `sentence 200`.

### Headline comparison (dense retrieval)

![Headline comparison](chart_headline.png)

| Strategy | Setting | Chunks | Mean tokens | Evidence intact | Recall@1 | Recall@3 | MRR@10 | Recall @1000 tok | Token precision@5 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fixed-size | `200` | 904 | 194 | 0.89 | 0.30 (0.23 to 0.37) | 0.52 (0.44 to 0.60) | 0.43 (0.36 to 0.49) | 0.62 (0.54 to 0.69) | 2.06% |
| Fixed + overlap | `200+80` | 1451 | 197 | 1.00 | 0.36 (0.28 to 0.43) | 0.63 (0.55 to 0.71) | 0.50 (0.44 to 0.56) | 0.72 (0.65 to 0.80) | 2.32% |
| Sentence-based | `200` | 963 | 182 | 0.99 | 0.42 (0.34 to 0.50) | 0.57 (0.49 to 0.65) | 0.52 (0.45 to 0.59) | 0.65 (0.57 to 0.72) | 2.26% |
| Recursive | `200` | 1114 | 157 | 1.00 | 0.36 (0.28 to 0.44) | 0.57 (0.49 to 0.65) | 0.49 (0.42 to 0.55) | 0.69 (0.61 to 0.76) | 2.79% |
| Semantic | `p85` | 1002 | 175 | 1.00 | 0.36 (0.28 to 0.44) | 0.54 (0.46 to 0.62) | 0.46 (0.39 to 0.53) | 0.56 (0.48 to 0.64) | 2.02% |

### Same chunks, BM25 instead of embeddings

| Strategy | Setting | Chunks | Mean tokens | Evidence intact | Recall@1 | Recall@3 | MRR@10 | Recall @1000 tok | Token precision@5 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fixed-size | `200` | 904 | 194 | 0.89 | 0.29 (0.22 to 0.36) | 0.48 (0.40 to 0.56) | 0.40 (0.33 to 0.47) | 0.54 (0.46 to 0.62) | 1.79% |
| Fixed + overlap | `200+80` | 1451 | 197 | 1.00 | 0.30 (0.23 to 0.37) | 0.48 (0.40 to 0.56) | 0.40 (0.34 to 0.47) | 0.53 (0.45 to 0.61) | 1.78% |
| Sentence-based | `200` | 963 | 182 | 0.99 | 0.30 (0.23 to 0.37) | 0.47 (0.39 to 0.55) | 0.40 (0.33 to 0.47) | 0.53 (0.45 to 0.61) | 1.89% |
| Recursive | `200` | 1114 | 157 | 1.00 | 0.29 (0.22 to 0.36) | 0.44 (0.36 to 0.52) | 0.39 (0.32 to 0.46) | 0.52 (0.44 to 0.60) | 2.06% |
| Semantic | `p85` | 1002 | 175 | 1.00 | 0.35 (0.28 to 0.43) | 0.44 (0.36 to 0.52) | 0.43 (0.36 to 0.50) | 0.46 (0.38 to 0.54) | 1.53% |

### Dense versus BM25, paired on the same questions

| Strategy | Metric | Dense minus BM25 | 95% CI |
|---|---|---:|---|
| Fixed-size | recall@3 | +0.046 | [-0.053, +0.146] |
| Fixed-size | mrr@10 | +0.028 | [-0.047, +0.102] |
| Sentence-based | recall@3 | +0.099 | [+0.007, +0.192] |
| Sentence-based | mrr@10 | +0.122 | [+0.045, +0.197] |
| Recursive | recall@3 | +0.126 | [+0.033, +0.218] |
| Recursive | mrr@10 | +0.099 | [+0.021, +0.175] |
| Fixed + overlap | recall@3 | +0.146 | [+0.046, +0.238] |
| Fixed + overlap | mrr@10 | +0.101 | [+0.030, +0.169] |
| Semantic | recall@3 | +0.106 | [+0.007, +0.205] |
| Semantic | mrr@10 | +0.033 | [-0.050, +0.118] |

### Is any strategy actually different from the fixed 200 baseline?

![Paired differences](chart_paired.png)

| Strategy | Metric | Change vs baseline | 95% CI | Distinguishable? |
|---|---|---:|---|---|
| Fixed + overlap | mrr@10 | +0.073 | [+0.017, +0.131] | **yes** |
| Fixed + overlap | recall@1000tok | +0.106 | [+0.040, +0.172] | **yes** |
| Fixed + overlap | recall@3 | +0.106 | [+0.033, +0.179] | **yes** |
| Fixed + overlap | token_iou@5 | +0.0026 | [+0.0004, +0.0049] | **yes** |
| Fixed + overlap | token_precision@5 | +0.0026 | [+0.0005, +0.0049] | **yes** |
| Fixed + overlap | token_precision_union@5 | +0.0052 | [+0.0030, +0.0075] | **yes** |
| Sentence-based | mrr@10 | +0.093 | [+0.032, +0.155] | **yes** |
| Sentence-based | recall@1000tok | +0.033 | [-0.033, +0.106] | no, CI includes 0 |
| Sentence-based | recall@3 | +0.046 | [-0.026, +0.126] | no, CI includes 0 |
| Sentence-based | token_iou@5 | +0.0021 | [-0.0005, +0.0047] | no, CI includes 0 |
| Sentence-based | token_precision@5 | +0.0021 | [-0.0005, +0.0047] | no, CI includes 0 |
| Sentence-based | token_precision_union@5 | +0.0021 | [-0.0005, +0.0047] | no, CI includes 0 |
| Recursive | mrr@10 | +0.058 | [-0.009, +0.122] | no, CI includes 0 |
| Recursive | recall@1000tok | +0.073 | [+0.000, +0.146] | no, CI includes 0 |
| Recursive | recall@3 | +0.046 | [-0.033, +0.126] | no, CI includes 0 |
| Recursive | token_iou@5 | +0.0074 | [+0.0041, +0.0107] | **yes** |
| Recursive | token_precision@5 | +0.0074 | [+0.0041, +0.0107] | **yes** |
| Recursive | token_precision_union@5 | +0.0074 | [+0.0041, +0.0107] | **yes** |
| Semantic | mrr@10 | +0.035 | [-0.033, +0.102] | no, CI includes 0 |
| Semantic | recall@1000tok | -0.053 | [-0.139, +0.033] | no, CI includes 0 |
| Semantic | recall@3 | +0.020 | [-0.066, +0.113] | no, CI includes 0 |
| Semantic | token_iou@5 | -0.0004 | [-0.0036, +0.0027] | no, CI includes 0 |
| Semantic | token_precision@5 | -0.0004 | [-0.0036, +0.0027] | no, CI includes 0 |
| Semantic | token_precision_union@5 | -0.0004 | [-0.0036, +0.0027] | no, CI includes 0 |

### The overlap sweep

![Overlap sweep](chart_overlap.png)

| Overlap | Chunks | Tokens indexed | Recall@3 | Recall @1000 tok | Token precision@5 (duplicates counted) | Token precision@5 (counted once) |
|---|---:|---:|---:|---:|---:|---:|
| 0 tok (0%) | 904 | 174,963 | 0.52 (0.44 to 0.60) | 0.62 (0.54 to 0.69) | 2.06% | 2.06% |
| 20 tok (10%) | 1000 | 193,690 | 0.57 (0.49 to 0.65) | 0.64 (0.56 to 0.71) | 2.13% | 2.17% |
| 40 tok (20%) | 1111 | 216,852 | 0.56 (0.48 to 0.64) | 0.66 (0.58 to 0.73) | 2.12% | 2.22% |
| 80 tok (40%) | 1451 | 285,914 | 0.63 (0.55 to 0.71) | 0.72 (0.65 to 0.80) | 2.32% | 2.57% |

### Every configuration tried

![Size sweep](chart_size_sweep.png)

| Configuration | Chunks | Mean tokens | Evidence intact | Recall@3 | MRR@10 | Token precision@5 |
|---|---:|---:|---:|---:|---:|---:|
| `fixed 100` | 1782 | 98 | 0.71 | 0.49 | 0.42 | 3.58% |
| `fixed 200` | 904 | 194 | 0.89 | 0.52 | 0.43 | 2.06% |
| `fixed 400` | 469 | 373 | 0.95 | 0.56 | 0.45 | 1.13% |
| `fixed_overlap 200+20` | 1000 | 194 | 0.95 | 0.57 | 0.49 | 2.13% |
| `fixed_overlap 200+40` | 1111 | 195 | 0.99 | 0.56 | 0.47 | 2.12% |
| `fixed_overlap 200+80` | 1451 | 197 | 1.00 | 0.63 | 0.50 | 2.32% |
| `sentence 100` | 2051 | 85 | 0.99 | 0.56 | 0.47 | 4.68% |
| `sentence 200` | 963 | 182 | 0.99 | 0.57 | 0.52 | 2.26% |
| `sentence 400` | 483 | 362 | 1.00 | 0.50 | 0.46 | 1.12% |
| `recursive 100` | 2513 | 70 | 1.00 | 0.61 | 0.54 | 6.13% |
| `recursive 200` | 1114 | 157 | 1.00 | 0.57 | 0.49 | 2.79% |
| `recursive 400` | 519 | 337 | 1.00 | 0.54 | 0.48 | 1.20% |
| `semantic p75` | 1310 | 134 | 0.99 | 0.56 | 0.47 | 2.64% |
| `semantic p85` | 1002 | 175 | 1.00 | 0.54 | 0.46 | 2.02% |
| `semantic p95` | 604 | 290 | 1.00 | 0.57 | 0.48 | 1.37% |

### Indexing cost

| Strategy | Tokens embedded to build the index | Relative cost |
|---|---:|---:|
| Fixed-size | 174,963 | 1.00× |
| Fixed + overlap | 285,914 | 1.63× |
| Sentence-based | 174,979 | 1.00× |
| Recursive | 174,979 | 1.00× |
| Semantic | 349,958 | 2.00× |

### Where retrieval failed

| Configuration | Misses (not in top 5) | Evidence split across chunks | Right document, wrong passage | Wrong document |
|---|---:|---:|---:|---:|
| `fixed 200` | 59 | 0 | 23 | 36 |
| `fixed_overlap 200+80` | 42 | 0 | 14 | 28 |
| `sentence 200` | 53 | 0 | 19 | 34 |
| `recursive 200` | 51 | 0 | 18 | 33 |
| `semantic p85` | 61 | 0 | 16 | 45 |

### Same chunks, 2 embedding models

![Model comparison](chart_models.png)

| Strategy | Configuration | bge-small | rank | minilm | rank |
|---|---|---:|---:|---:|---:|
| Fixed-size | `fixed 200` | 0.43 | 5 | 0.38 | 5 |
| Fixed + overlap | `fixed_overlap 200+80` | 0.50 | 2 | 0.42 | 2 |
| Sentence-based | `sentence 200` | 0.52 | 1 | 0.40 | 3 |
| Recursive | `recursive 200` | 0.49 | 3 | 0.45 | 1 |
| Semantic | `semantic p85` | 0.46 | 4 | 0.39 | 4 |

Strategies holding the same rank across all 2 models: Fixed-size, Fixed + overlap, Semantic.


## What I take from this

- **Dense retrieval beat BM25 on 3 of the 5 chunkings**, by as much as
  +0.122 MRR on Sentence-based. The exceptions are Fixed-size, Semantic: on the plain fixed-size
  baseline the dense-versus-BM25 interval still includes zero (+0.028 MRR (95% CI [-0.047, +0.102])). A chunking bad
  enough that a better retriever cannot exploit it is itself worth noticing.
- **Sentence-based had the best point estimate** (0.52 (95% CI 0.45 to 0.59)) and Fixed-size the worst
  (0.43 (95% CI 0.36 to 0.49)), a spread of 0.09 MRR, though the most context-efficient is Recursive at 2.79% token precision against this one's 2.26%. Both of those are point estimates on one model: its gaps to the one other strategy that beat the baseline do not clear zero,
  and it is not necessarily the strategy that held up on minilm.
- **two of the 4 other strategies beat the baseline on MRR with intervals clear
  of zero on bge-small.** Not every comparison separates: on recall@3 several intervals still
  include zero, and the widest paired interval spans 0.13 MRR. Across all
  24 paired comparisons, 10 separated.
- **The ordering among the winners is not resolvable.** Sentence-based has the highest point estimate,
  but its gaps to the one other strategy that beat the baseline do not clear zero: **Sentence-based** vs **Fixed + overlap** +0.019 [-0.041, +0.080]. So read the table as "these two beat fixed-size" and not as a
  ranking.
- **Splitting the answer is a real failure mode only at small sizes.** At 100 tokens,
  fixed-size chunking left the answer passage intact in 71.5% of questions. At the selected
  settings: Fixed-size 88.7%, Fixed + overlap 100.0%, Sentence-based 99.3%, Recursive 100.0%, Semantic 100.0%.
- **Semantic chunking cost the most and bought the least.** It reached 0.46 (95% CI 0.39 to 0.53) on
  bge-small, not distinguishable from the baseline (+0.035 [-0.033, +0.102]), for 2.0× the embedding work to build
  the index. Cheaper strategies landed in the same place for the same indexing cost as plain
  fixed-size, and on minilm it is not distinguishable from the baseline either (+0.010 [-0.050, +0.075]). The published literature
  keeps reaching the same verdict.

### The overlap sweep

Overlap is the one setting the literature openly disagrees about, and I could not find a published
sweep of it. Here is one, at a 200-token chunk size.

Adding any overlap helps. MRR across the sweep runs 0.429 then 0.495 then 0.473 then 0.502 and recall@3 runs
0.52, 0.57, 0.56, 0.63. Note that recall@3 is **not monotonic**: it peaks at the largest overlap tried (80 tokens), but dips at 40 tokens on the way there, so the series is not a clean trend.

**The useful finding is that nothing beyond the first step is resolvable.** The first
20 tokens (10%) buys +0.066 MRR. Going from there to 80 tokens (40%) is +0.007 MRR (95% CI [-0.054, +0.066]), which is
not distinguishable from zero. So the honest statement is not "more overlap keeps helping", and not even
"the benefit saturates", but "I cannot resolve any difference above 20 tokens (10%), and it costs
more to index": 20 tokens (10%) costs 1.11× the tokens of no overlap, while 80 tokens (40%)
costs 1.63×. The common default of 50% overlap buys nothing I can measure here and
charges for it.

**One caution about the cost side.** The widely used implementation of token-level precision sums
the length of every retrieved chunk in the denominator *without de-duplicating*. Text appearing in
two overlapping chunks is counted twice: it inflates the denominator while contributing nothing to
the numerator, so that denominator penalises overlap by arithmetic rather than by evidence.

I computed precision both ways to see how much that matters. Counting duplicate text twice,
precision rises from no overlap to the largest tried (2.06% to 2.32%), though not at
every step. Counting each piece of source text once, it rises (2.06% to 2.57%). So on this corpus both denominators agree on the direction: the choice of denominator changes
the size of the effect, not its sign, and precision goes up with overlap either way because the
recall gain outruns the extra context. I expected the two to disagree and they did not, which is
worth saying plainly rather than quietly dropping.

The caution still stands for anyone comparing strategies with very different redundancy: check
which denominator your harness implements before reading much into a precision or IoU gap.

### Does any of this survive a change of embedding model?

This is the question that decides whether a chunking result means anything, and most evaluations
cannot answer it because they test one model. Running the identical chunks through minilm
instead of bge-small, the strategy ranking is **different**.

On bge-small: Sentence-based > Fixed + overlap > Recursive > Semantic > Fixed-size.
On minilm, same chunks: Recursive > Fixed + overlap > Sentence-based > Semantic > Fixed-size.

Rank changes: Sentence-based 1 to 3, Recursive 3 to 1, and the worst strategy is the same on both models (Fixed-size) but the best is not. The spread between best and worst goes from 0.09
MRR to 0.07.

Tested against the same baseline on the second model, **Fixed + overlap** +0.037 [-0.016, +0.093] (not distinguishable); **Recursive** +0.068 [+0.019, +0.116]; **Semantic** +0.010 [-0.050, +0.075] (not distinguishable); **Sentence-based** +0.025 [-0.021, +0.071] (not distinguishable). So of the
2 strategies that beat plain fixed-size on bge-small, **none** still does so
on minilm.

Across all 2 models (bge-small, minilm), a different strategy wins depending on the model. Best strategy per model:
bge-small: Sentence-based, minilm: Recursive. 3 of the five strategies hold the same rank on every model
(Fixed + overlap, Semantic, Fixed-size), and no strategy beats plain fixed-size with an interval clear of zero on every model. The strategies that hold their rank are the ones worth
taking from this article, because they are the only claims here that do not depend on which encoder
you happen to use.

This is the single most useful thing I found, and it is uncomfortable, because it undercuts the
first half of my own article. A chunking comparison run on one embedding model is largely a
measurement of that model. If you are choosing a chunker from someone's table, check how many
retrievers they tested. Usually the answer is one.

### Where retrieval actually failed

Pooling the 5 selected configurations over the same 151 test questions gives
266 miss-events, so a question that defeats every strategy is counted
5 times. Of those, 0 were caused by the evidence being split across
chunks. 176 had their top hit in the wrong document entirely and 90
in the right document but the wrong passage.

A caveat on that split count, because it is partly definitional: a miss is filed that way only when
*no* chunk anywhere in the index covers at least half the evidence, and in this corpus
`answerable` = 1.00 in all 30 rows of summary.csv. The stricter evidence-intact measure is the one to trust on whether splitting
hurts, and it does move with size.

Once chunks are large enough to hold an answer, chunking stops being the bottleneck. What is left
are retrieval failures: the model confidently fetching a different section about a genuinely related
thing. That is the best explanation I have for why the strategies are so hard to separate on ranking.

## Prior work

This question has been studied properly and my results mostly agree with the existing consensus. If
you are choosing a chunker for real work, read these rather than me:

- **Chroma, "Evaluating Chunking Strategies for Retrieval"** (Smith & Troynikov, July 2024). The
  most thorough public evaluation: 5 corpora, 472 LLM-generated queries with exact-match excerpt
  grounding, and the token-level recall / precision / IoU family that this article borrows. Found
  `RecursiveCharacterTextSplitter` at 200 tokens with no overlap consistently strong and
  off-the-shelf semantic chunking weaker than its reputation.
  https://research.trychroma.com/evaluating-chunking
  Two things worth knowing if you build on it: the metrics are described as token-level but are
  implemented over character offsets, and the precision denominator does not de-duplicate
  overlapping retrieved spans (see the overlap section above). It reports standard deviations rather
  than confidence intervals, and those deviations are large relative to the gaps being discussed.
- **"Is Semantic Chunking Worth the Computational Cost?"** (Qu, Tu & Bao, *Findings of ACL: NAACL
  2025*, pp. 2155-2177; arXiv:2410.13070). The key negative result. Semantic chunking won mainly on
  corpora artificially stitched from short documents, and fixed-size won on naturally long ones.
- **"Chunking Methods on Retrieval-Augmented Generation"** (Śmigielski et al., arXiv:2606.00881, May
  2026). The broadest method sweep I found: 8 methods across 8 datasets with wall-clock cost. On
  Accuracy@5 the cheap classical methods win; on Recall@10 the expensive LLM-based one leads. One
  embedding model, no intervals, chunk sizes not normalised across methods.
- **"Late Chunking"** (Günther et al., arXiv:2409.04701). Embed the whole document first, then pool
  token embeddings per chunk. Roughly +1.8 nDCG@10 with no retraining.
- **Anthropic, "Contextual Retrieval"** (Sept 2024). Not a boundary method but chunk enrichment.
  Cut retrieval failure rate from 5.7% to 3.7% at top-20, a better-evidenced return than boundary tricks.

The honest summary of that literature: **respecting structure that already exists in the document
helps; inferring new boundaries from embedding similarity usually does not pay for itself.** My
results are consistent with that, which is reassuring but not independent evidence, since I read
them first.

## Limitations

Specific enough to be falsifiable:

- **One corpus, one genre, one language.** A technical book in English with clean headings. Expect
  different numbers on PDFs with tables, transcripts, or multilingual corpora.
- **151 test questions.** That is why so many intervals include zero. This experiment can show
  that differences are *not resolvable*; it cannot prove they are absent.
- **Questions were drafted with AI assistance and audited, not reviewed by a second person.**
  `scripts/analyse_questions.py` measures the things that decide whether a question set is sound,
  and its output is in the repo. On this set: 0 near-duplicate questions, 0 with
  verbatim leakage from their own evidence, 0 with heavy lexical overlap, mean
  question-to-evidence similarity 0.729. 0 of the 215 evidence passages
  open with an anaphor ("This is...", "In that case..."), which matters because a passage that starts
  with a back-reference cannot be judged relevant on its own. Coverage is even: 64 documents
  carry questions and the busiest single document holds 2% of them. An earlier version of
  this set failed both of those checks, with 19 anaphoric passages and 130 questions crowded onto 20
  of the 64 documents, so it was rebuilt from scratch before these results were produced.
- **Some questions are genuinely ambiguous.** For 67 of the 215 questions
  (31%), another question's evidence passage matches the question better than its own
  does. Most of that is a good sign, since it means the questions are paraphrased rather than
  lookups, but part of it is real ambiguity: a passage I score as wrong may be a defensible answer.
  That depresses every strategy equally, so the comparisons stand, but the absolute recall and MRR
  numbers should be read as a floor rather than a ceiling.
- **The cross-model numbers are at bge-small's dev-selected settings, not minilm's.** That is
  deliberate: holding the configuration fixed is the only way to attribute a difference to the model
  rather than to a different set of chunks. But it does mean the minilm column is not that
  model's own best showing. Run separately, minilm's dev split picks `fixed 100`, `fixed_overlap 200+80`, `recursive 100`, `semantic 95`, `sentence 100`,
  and against its own reference no strategy clears zero on MRR either. Both readings are in the
  repo. The comparisons quoted above live in `results/bge-small/paired_cross_model.csv`, because
  `paired_vs_reference.csv` holds each model's comparison against its own reference and so cannot
  answer the cross-model question.
- **2 embedding models, all small.** Better models may behave differently again. The
  repo takes `--compare` any number of times, so adding more is one command per model.
- **Retrieval only.** I did not measure whether any of this survives to the generated answer. Qu et
  al. found retrieval differences largely washed out in generation.
- **Context windows differ between models, and this is a confound.** bge-small reads at
  most 512 tokens; minilm reads at most 256. On bge-small the selected
  configurations are affected as follows: Fixed-size 0/904, Sentence-based 0/963, Recursive 0/1114, Fixed + overlap 0/1451, Semantic 0/1002, so no selected configuration on this model is affected. On minilm the shorter
  window bites harder: Semantic 218/985 (22%). Any minilm number for an affected configuration is partly
  a context-window artefact and not purely a verdict on its boundaries. I did not separate the two
  effects, and it is one reason the cross-model section should be read as "these results are
  fragile" rather than as a clean ranking of models.
- **Some settings were chosen on a near-tie.** The dev split picks one configuration per strategy,
  and 2 of them were decided by a hair: Recursive (recursive 200 over recursive 100 by 0.009 dev MRR); Fixed + overlap (fixed_overlap 200+80 over fixed_overlap 200+40 by 0.004 dev MRR). A different split seed could
  select a different row and move that strategy several places. The protocol is honest but the
  resulting ordering is not robust.
- **Chunk boundaries are identical across models for every strategy except semantic**, which places
  its boundaries using the embedding model itself, so its chunks genuinely differ between the two
  runs. The cross-model comparison is like-for-like for the other four.
- **No correction for multiple comparisons.** I report 24 paired comparisons and
  highlight the 10 whose intervals clear zero. At a 5% threshold across that many
  tests you would expect roughly one to clear by chance. Treat them as suggestive.
- **My token-level metrics are computed over real tokens**, whereas the implementation this family
  of metrics comes from works over character offsets. The numbers are therefore close cousins of
  the published ones, not the same quantity.

## If you just want a decision rule

For prose documents like this one, on this evidence:

1. **Stop using plain fixed-size chunking with no overlap.** It was the worst of the five on both
   embedding models. 3 rank positions survived the model change (Fixed + overlap, Semantic, Fixed-size), but
   this is the only one you can act on, because the others tell you where a strategy lands rather
   than that you should switch to it. Everything else on this list is weaker than it looks.
2. **Prefer recursive splitting as the default, but hold it loosely.** No strategy beats plain fixed-size with an interval clear of zero on both models. The
   highest scorer was Sentence-based on bge-small and Recursive on minilm, so the winner
   is model-dependent; recursive is the one I would start from because it was never the worst on
   either model, costs nothing extra to build, and is what Chroma's much larger evaluation
   independently landed on. Re-run the comparison on your own encoder before trusting any ranking,
   including this one. That is a day of work and it changed the answer here.
3. **Add a little overlap, not a lot.** The first 20 tokens (10%) was worth +0.066 MRR;
   everything beyond it was inside the noise and cost real index size. Ignore precision-based
   arguments against overlap until you have checked how your harness counts duplicated text.
4. **Do not reach for semantic chunking first.** On bge-small it was not distinguishable from the baseline
   (+0.035 [-0.033, +0.102]) while costing 2.0× the indexing work of the cheaper strategies, and it
   placed fourth of five on both models. The published literature reaches the same verdict outside
   artificially stitched corpora.
5. **Spend the effort on your retriever.** Dense versus BM25 had the largest point estimate of
   anything measured here (+0.122 MRR on Sentence-based), though its interval overlaps the
   larger chunking effects, so I would not claim a strict ordering.
6. **Measure on your own documents.** Every source above, including this one, finds the winner depends
   on the corpus.

## Reproduce it

```bash
git clone https://github.com/vaishnavi-sonawane27/RAG-Chunking-Strategies
cd RAG-Chunking-Strategies
pip install -r requirements.txt
python scripts/fetch_corpus.py        # downloads Pro Git, converts to text
python scripts/validate_questions.py  # checks every evidence passage resolves uniquely
python scripts/fetch_models.py        # ONNX weights, hash-pinned
python run_experiment.py --embedder onnx:bge-small --tag bge-small
python run_experiment.py --embedder onnx:minilm --tag minilm
python scripts/make_report.py   --tag bge-small --compare minilm
python scripts/build_article.py --tag bge-small --compare minilm
```

Raw per-question results, the failure taxonomy and the paired comparisons are all in
`results/bge-small/`. Every number in this article is generated from those files by
`scripts/build_article.py`; none is typed by hand.

## Corrections

I would rather be corrected than cited. If you find a bug, a bad question or a methodological
mistake, open an issue on the repo and I will update this post and note the change here.

*Corpus: Pro Git, Scott Chacon and Ben Straub, CC BY-NC-SA 3.0, https://github.com/progit/progit2*

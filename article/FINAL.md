---
title: "Do RAG chunking strategies actually differ? Error bars, two embedding models and an overlap sweep"
subtitle: "64 documents, 130 questions, five strategies, sizes in tokens, a dev/test split and paired bootstrap confidence intervals. Code and raw results included."
canonical_url: ""
tags: rag, retrieval, llm, benchmarking
---

# Do RAG chunking strategies actually differ? Error bars, two embedding models and an overlap sweep

Chunking is the step everyone has an opinion about and almost nobody measures with error bars.
Blog posts rank the strategies confidently; the gaps they report are often two or three points,
reported once, from a single run, with no interval around them.

I went looking for how much of that advice survives a significance test. Five strategies, a corpus
of 64 documents, 130 questions, two embedding models, chunk sizes in tokens, and the
part that matters: **every setting chosen on a held-out dev split and every number reported on test
questions the tuning never saw**, with paired bootstrap confidence intervals over 5,000 resamples.

**The short answer: the differences are real, and plain fixed-size chunking is the worst option
tested.** Against the fixed 200 baseline on MRR@10, every single one of the other four
strategies beat it with a confidence interval clear of zero: **Sentence-based** +0.181 [+0.078, +0.285]; **Semantic** +0.138 [+0.037, +0.242]; **Fixed + overlap** +0.126 [+0.051, +0.204]; **Recursive** +0.090 [+0.007, +0.171]. Fixed-size came last at
every chunk size I tried.

That is a stronger result than I expected, and it only showed up once sizes were measured in tokens
rather than words. Three further things came out of it:

1. **Strategy matters more than size.** Switching strategy at a fixed size moves MRR by
   0.081 to 0.157 (mean 0.116); changing size within a strategy moves it by
   0.042 to 0.119 (mean 0.080). So strategy is the thing to get right first, and
   that is the opposite of the advice usually given.
2. **Overlap helps, and its benefit saturates almost immediately.** Going from no overlap to
   20 tokens (10%) is worth +0.125 MRR. Going all the way up to 80 tokens (40%) adds
   +0.001 on top of that.
3. **The published way of measuring overlap's cost is partly an artefact.** The standard
   implementation counts text appearing in two overlapping chunks twice, which penalises overlap by
   construction rather than by evidence. Details below.

**What this is not:** a new finding about which chunker wins. That ground is covered (see
[Prior work](#prior-work)). What I believe is genuinely missing from the published work, and what
this adds, is narrow: **confidence intervals and paired significance tests between strategies**, and
**an actual sweep over overlap values**. I could not find either in the evaluations I read.

**Disclosure:** I am a final-year CS student. Nobody paid for this, I am not affiliated with any
vector database or embedding vendor, and I have no stake in which strategy wins. Repo:
**[REPO LINK]**.

## The setup

| | |
|---|---|
| **Corpus** | *Pro Git* (2nd ed.), Chacon & Straub, 64 sections, ~107,000 words (~175,000 tokens), CC BY-NC-SA 3.0 |
| **Questions** | 130 questions, each tied to one evidence passage that occurs exactly once |
| **Split** | 42 dev (chooses settings) / 88 test (reported). Stratified by document, seed 0 |
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
precision is the share of everything you retrieved that was actually the answer. At the selected
settings it ranges from 3.98% at 100 tokens to 1.12% at 400 tokens for fixed-size chunking, which is a larger
relative swing than anything in the recall numbers.

Settings chosen on dev: `fixed 200`, `fixed_overlap 200+80`, `recursive 200`, `semantic 85`, `sentence 100`.

## Results

<!-- generated by scripts/make_report.py from results/bge-small; do not edit by hand -->

**Run:** bge-small · 64 documents · 130 questions · 5,000 bootstrap resamples. Sizes are in bge-small WordPiece tokens.

**Protocol:** chunk sizes, overlaps and thresholds were chosen on 42 dev questions; every number below is measured on the 88 held-out test questions (split seed 0). Selected on dev: `fixed 200`, `fixed_overlap 200+80`, `recursive 200`, `semantic 85`, `sentence 100`.

### Headline comparison (dense retrieval)

![Headline comparison](chart_headline.png)

| Strategy | Setting | Chunks | Mean tokens | Evidence intact | Recall@1 | Recall@3 | MRR@10 | Recall @1000 tok | Token precision@5 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fixed-size | `200` | 904 | 194 | 0.88 | 0.29 (0.20–0.40) | 0.57 (0.47–0.67) | 0.46 (0.38–0.54) | 0.68 (0.58–0.77) | 2.07% |
| Fixed + overlap | `200+80` | 1451 | 197 | 1.00 | 0.46 (0.35–0.56) | 0.70 (0.60–0.80) | 0.59 (0.50–0.67) | 0.76 (0.67–0.85) | 2.23% |
| Sentence-based | `100` | 2051 | 85 | 0.92 | 0.57 (0.47–0.67) | 0.68 (0.59–0.77) | 0.64 (0.56–0.73) | 0.84 (0.76–0.91) | 5.14% |
| Recursive | `200` | 1114 | 157 | 0.95 | 0.40 (0.29–0.50) | 0.65 (0.55–0.75) | 0.55 (0.47–0.63) | 0.80 (0.70–0.88) | 2.65% |
| Semantic | `p85` | 1002 | 175 | 0.99 | 0.46 (0.35–0.56) | 0.69 (0.59–0.80) | 0.60 (0.52–0.68) | 0.75 (0.66–0.84) | 2.28% |

### Same chunks, BM25 instead of embeddings

| Strategy | Setting | Chunks | Mean tokens | Evidence intact | Recall@1 | Recall@3 | MRR@10 | Recall @1000 tok | Token precision@5 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fixed-size | `200` | 904 | 194 | 0.88 | 0.32 (0.23–0.42) | 0.44 (0.34–0.55) | 0.41 (0.32–0.50) | 0.53 (0.43–0.64) | 1.77% |
| Fixed + overlap | `200+80` | 1451 | 197 | 1.00 | 0.35 (0.25–0.46) | 0.46 (0.35–0.56) | 0.44 (0.35–0.53) | 0.59 (0.49–0.69) | 1.94% |
| Sentence-based | `100` | 2051 | 85 | 0.92 | 0.28 (0.19–0.38) | 0.39 (0.28–0.49) | 0.37 (0.28–0.46) | 0.61 (0.51–0.72) | 3.41% |
| Recursive | `200` | 1114 | 157 | 0.95 | 0.28 (0.19–0.38) | 0.49 (0.39–0.59) | 0.39 (0.30–0.48) | 0.58 (0.48–0.68) | 1.81% |
| Semantic | `p85` | 1002 | 175 | 0.99 | 0.34 (0.25–0.44) | 0.55 (0.44–0.65) | 0.46 (0.37–0.55) | 0.55 (0.44–0.65) | 1.71% |

### Dense versus BM25, paired on the same questions

| Strategy | Metric | Dense minus BM25 | 95% CI |
|---|---|---:|---|
| Fixed-size | recall@3 | +0.125 | [+0.000, +0.239] |
| Fixed-size | mrr@10 | +0.052 | [-0.049, +0.151] |
| Sentence-based | recall@3 | +0.295 | [+0.182, +0.409] |
| Sentence-based | mrr@10 | +0.272 | [+0.185, +0.362] |
| Recursive | recall@3 | +0.159 | [+0.034, +0.284] |
| Recursive | mrr@10 | +0.161 | [+0.057, +0.262] |
| Fixed + overlap | recall@3 | +0.250 | [+0.125, +0.375] |
| Fixed + overlap | mrr@10 | +0.150 | [+0.041, +0.261] |
| Semantic | recall@3 | +0.148 | [+0.011, +0.284] |
| Semantic | mrr@10 | +0.143 | [+0.047, +0.241] |

### Is any strategy actually different from the fixed 200 baseline?

![Paired differences](chart_paired.png)

| Strategy | Metric | Change vs baseline | 95% CI | Distinguishable? |
|---|---|---:|---|---|
| Fixed + overlap | mrr@10 | +0.126 | [+0.051, +0.204] | **yes** |
| Fixed + overlap | recall@1000tok | +0.080 | [-0.011, +0.171] | no, CI includes 0 |
| Fixed + overlap | recall@3 | +0.136 | [+0.045, +0.227] | **yes** |
| Fixed + overlap | token_iou@5 | +0.0016 | [-0.0009, +0.0042] | no, CI includes 0 |
| Fixed + overlap | token_precision@5 | +0.0016 | [-0.0009, +0.0042] | no, CI includes 0 |
| Fixed + overlap | token_precision_union@5 | +0.0045 | [+0.0019, +0.0073] | **yes** |
| Sentence-based | mrr@10 | +0.181 | [+0.078, +0.285] | **yes** |
| Sentence-based | recall@1000tok | +0.159 | [+0.057, +0.261] | **yes** |
| Sentence-based | recall@3 | +0.114 | [-0.000, +0.239] | no, CI includes 0 |
| Sentence-based | token_iou@5 | +0.0303 | [+0.0235, +0.0375] | **yes** |
| Sentence-based | token_precision@5 | +0.0307 | [+0.0238, +0.0380] | **yes** |
| Sentence-based | token_precision_union@5 | +0.0307 | [+0.0238, +0.0380] | **yes** |
| Recursive | mrr@10 | +0.090 | [+0.007, +0.171] | **yes** |
| Recursive | recall@1000tok | +0.114 | [+0.023, +0.216] | **yes** |
| Recursive | recall@3 | +0.080 | [-0.034, +0.193] | no, CI includes 0 |
| Recursive | token_iou@5 | +0.0057 | [+0.0022, +0.0090] | **yes** |
| Recursive | token_precision@5 | +0.0057 | [+0.0022, +0.0090] | **yes** |
| Recursive | token_precision_union@5 | +0.0057 | [+0.0022, +0.0090] | **yes** |
| Semantic | mrr@10 | +0.138 | [+0.037, +0.242] | **yes** |
| Semantic | recall@1000tok | +0.068 | [-0.045, +0.182] | no, CI includes 0 |
| Semantic | recall@3 | +0.125 | [+0.000, +0.250] | no, CI includes 0 |
| Semantic | token_iou@5 | +0.0021 | [-0.0029, +0.0069] | no, CI includes 0 |
| Semantic | token_precision@5 | +0.0020 | [-0.0030, +0.0068] | no, CI includes 0 |
| Semantic | token_precision_union@5 | +0.0020 | [-0.0030, +0.0068] | no, CI includes 0 |

### The overlap sweep

![Overlap sweep](chart_overlap.png)

| Overlap | Chunks | Tokens indexed | Recall@3 | Recall @1000 tok | Token precision@5 (duplicates counted) | Token precision@5 (counted once) |
|---|---:|---:|---:|---:|---:|---:|
| 0 tok (0%) | 904 | 174,963 | 0.57 (0.47–0.67) | 0.68 (0.58–0.77) | 2.07% | 2.07% |
| 20 tok (10%) | 1000 | 193,690 | 0.73 (0.64–0.82) | 0.77 (0.68–0.85) | 2.23% | 2.28% |
| 40 tok (20%) | 1111 | 216,852 | 0.66 (0.56–0.76) | 0.73 (0.64–0.82) | 2.11% | 2.22% |
| 80 tok (40%) | 1451 | 285,914 | 0.70 (0.60–0.80) | 0.76 (0.67–0.85) | 2.23% | 2.52% |

### Every configuration tried

![Size sweep](chart_size_sweep.png)

| Configuration | Chunks | Mean tokens | Evidence intact | Recall@3 | MRR@10 | Token precision@5 |
|---|---:|---:|---:|---:|---:|---:|
| `fixed 100` | 1782 | 98 | 0.74 | 0.56 | 0.49 | 3.98% |
| `fixed 200` | 904 | 194 | 0.88 | 0.57 | 0.46 | 2.07% |
| `fixed 400` | 469 | 373 | 0.94 | 0.58 | 0.50 | 1.12% |
| `fixed_overlap 200+20` | 1000 | 194 | 0.94 | 0.73 | 0.59 | 2.23% |
| `fixed_overlap 200+40` | 1111 | 195 | 0.94 | 0.66 | 0.58 | 2.11% |
| `fixed_overlap 200+80` | 1451 | 197 | 1.00 | 0.70 | 0.59 | 2.23% |
| `sentence 100` | 2051 | 85 | 0.92 | 0.68 | 0.64 | 5.14% |
| `sentence 200` | 963 | 182 | 0.93 | 0.66 | 0.57 | 2.34% |
| `sentence 400` | 483 | 362 | 0.97 | 0.60 | 0.52 | 1.23% |
| `recursive 100` | 2513 | 70 | 0.94 | 0.67 | 0.63 | 5.73% |
| `recursive 200` | 1114 | 157 | 0.95 | 0.65 | 0.55 | 2.65% |
| `recursive 400` | 519 | 337 | 1.00 | 0.62 | 0.58 | 1.33% |
| `semantic p75` | 1310 | 134 | 0.99 | 0.73 | 0.59 | 2.82% |
| `semantic p85` | 1002 | 175 | 0.99 | 0.69 | 0.60 | 2.28% |
| `semantic p95` | 604 | 290 | 1.00 | 0.67 | 0.53 | 1.51% |

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
| `fixed 200` | 27 | 0 | 8 | 19 |
| `fixed_overlap 200+80` | 21 | 0 | 5 | 16 |
| `sentence 100` | 22 | 0 | 12 | 10 |
| `recursive 200` | 23 | 0 | 10 | 13 |
| `semantic p85` | 19 | 0 | 7 | 12 |

### Does the ranking survive a change of embedding model?

![Model comparison](chart_models.png)

| Strategy | MRR@10 (bge-small) | rank | MRR@10 (minilm) | rank |
|---|---:|---:|---:|---:|
| Fixed-size | 0.46 | 5 | 0.49 | 5 |
| Fixed + overlap | 0.59 | 3 | 0.51 | 4 |
| Sentence-based | 0.64 | 1 | 0.59 | 1 |
| Recursive | 0.55 | 4 | 0.58 | 2 |
| Semantic | 0.60 | 2 | 0.54 | 3 |


## What I take from this

- **Dense retrieval beat BM25 on 4 of the 5 chunkings**, by as much as
  +0.272 MRR on Sentence-based. The exception is Fixed-size: on the plain fixed-size
  baseline the dense-versus-BM25 interval still includes zero (+0.052 MRR (95% CI [-0.049, +0.151])). A chunking bad
  enough that a better retriever cannot exploit it is itself worth noticing.
- **Sentence-based came first** (0.64 (95% CI 0.56–0.73)) and Fixed-size last (0.46 (95% CI 0.38–0.54)), a spread of 0.18
  MRR. Sentence-based is also the most context-efficient at 5.14% token precision, so on this
  corpus it wins on both axes at once.
- **All 4 other strategies beat the baseline on MRR with intervals clear of zero.** Not every comparison separates: on recall@3 several intervals still include zero, and the
  widest paired interval spans 0.21 MRR. Across all 24 paired comparisons,
  14 separated. So the headline is solid and the fine-grained ordering below the top
  is not.
- **Splitting the answer is a real failure mode only at small sizes.** At 100 tokens,
  fixed-size chunking left the answer passage intact in 74% of questions. At the selected
  settings: Fixed-size 88%, Fixed + overlap 100%, Sentence-based 92%, Recursive 96%, Semantic 99%.
- **Semantic chunking works, but it is not worth what it costs.** It reached 0.60 (95% CI 0.52–0.68), a real
  improvement on the baseline, for 2.0× the embedding work to build the index. Sentence
  chunking beat it at 0.64 (95% CI 0.56–0.73) for the same indexing cost as plain fixed-size. Paying double to
  come second is the trade the published literature keeps finding, and this run agrees.

### The overlap sweep

Overlap is the one setting the literature openly disagrees about, and I could not find a published
sweep of it. Here is one, at a 200-token chunk size.

Coverage rises with overlap: recall@3 goes from 0.57 at no overlap to 0.70 at
80 tokens (40%), and recall at the 1000-token budget from 0.68 to 0.76. That
is the expected result and it is what overlap is for. It also costs 1.63× the tokens to
index, which is the part people forget.

**The useful finding is where the benefit stops.** MRR across the sweep runs 0.462 then 0.587 then 0.585 then 0.588. The
first 20 tokens (10%) buys +0.125; going all the way to 80 tokens (40%) adds +0.001 on top
of that. Almost the entire benefit arrives with the smallest overlap tested, and the rest is index
size you are paying for and not getting back. The common default of 50% overlap looks like a poor
trade on this evidence.

**One caution about the cost side.** The widely used implementation of token-level precision sums
the length of every retrieved chunk in the denominator *without de-duplicating*. Text appearing in
two overlapping chunks is counted twice: it inflates the denominator while contributing nothing to
the numerator, so that denominator penalises overlap by arithmetic rather than by evidence.

I computed precision both ways to see how much that matters. Counting duplicate text twice,
precision rises across the sweep (2.07% to 2.23%). Counting each piece of source text once,
it rises (2.07% to 2.52%). So on this corpus both denominators agree on the direction: the choice of denominator changes
the size of the effect, not its sign, and precision goes up with overlap either way because the
recall gain outruns the extra context. I expected the two to disagree and they did not, which is
worth saying plainly rather than quietly dropping.

The caution still stands for anyone comparing strategies with very different redundancy: check
which denominator your harness implements before reading much into a precision or IoU gap.

### Does any of this survive a change of embedding model?

This is the question that decides whether a chunking result means anything, and most evaluations
cannot answer it because they test one model. Running the identical chunks through minilm
instead of bge-small, the strategy ranking is **different** (Fixed + overlap 3→4, Recursive 4→2, Semantic 2→3).

The part that holds is the part worth acting on: the best and worst strategies are the same on both models. Sentence-based is first on both and
Fixed-size is last on both, so "use something structure-aware, not plain fixed-size" survives the
model change. What does not hold is the ordering in the middle (Fixed + overlap, Recursive, Semantic), where the spread
between strategies is 0.10 MRR on the second model against 0.18 on the first.

So: trust the top and the bottom of a chunking table, and treat the middle as noise unless the
author tested more than one retriever. Most do not.

### Where retrieval actually failed

Pooling the 5 selected configurations over the same 88 test questions gives
112 miss-events, so a question that defeats every strategy is counted
5 times. Of those, 0 were caused by the evidence being split across
chunks. 70 had their top hit in the wrong document entirely and 42
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
  2025*, pp. 2155–2177; arXiv:2410.13070). The key negative result. Semantic chunking won mainly on
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
- **88 test questions.** That is why so many intervals include zero. This experiment can show
  that differences are *not resolvable*; it cannot prove they are absent.
- **Questions were drafted with AI assistance** and verified programmatically (each evidence passage
  occurs exactly once; questions are checked for verbatim leakage), but not reviewed by a second
  person. They are paraphrased by construction, which favours embeddings over lexical matching.
- **Two embedding models, both small.** Better models may behave differently again.
- **Retrieval only.** I did not measure whether any of this survives to the generated answer. Qu et
  al. found retrieval differences largely washed out in generation.
- **Long chunks get truncated, and this is a confound.** The models read at most 512 tokens. Chunks
  over that limit, by selected configuration: Sentence-based 0/2051, Fixed-size 0/904, Recursive 0/1114, Fixed + overlap 0/1451, Semantic 0/1002. Sentence-based (0% of its chunks) is the most affected, so
  part of its deficit is a context-window artefact rather than a verdict on its boundaries.
- **No correction for multiple comparisons.** I report 24 paired comparisons and
  highlight the 14 whose intervals clear zero. At a 5% threshold across that many
  tests you would expect roughly one to clear by chance. Treat them as suggestive.
- **My token-level metrics are computed over real tokens**, whereas the implementation this family
  of metrics comes from works over character offsets. The numbers are therefore close cousins of
  the published ones, not the same quantity.

## If you just want a decision rule

For prose documents like this one, on this evidence:

1. **Start with recursive or sentence-aware splitting at a small-to-moderate token size.** It
   respects boundaries that already exist, costs nothing extra, and was the most context-efficient
   option here.
2. **Fix the strategy before you tune the size.** Strategy moved the numbers more than size did
   here, and plain fixed-size was worst at every size tested.
3. **Add a little overlap, not a lot.** The first 20 tokens (10%) captured almost all of the
   benefit here; going further mostly bought index size. Ignore precision-based arguments against
   overlap until you have checked how your harness counts duplicated text.
4. **Do not reach for semantic chunking first.** It cost 2.0× the indexing work here for
   no defensible gain, and the published literature finds the same outside artificially stitched corpora.
5. **Spend the effort on your retriever.** Dense versus BM25 was a bigger effect than any chunking choice.
6. **Measure on your own documents.** Every source above, including this one, finds the winner depends
   on the corpus.

## Reproduce it

```bash
git clone [REPO LINK]
cd rag-chunking-experiment
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

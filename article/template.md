---
title: "Do RAG chunking strategies actually differ? Error bars, {n_models} embedding models and an overlap sweep"
subtitle: "{n_docs} documents, {n_questions} questions, five strategies, sizes in tokens, a dev/test split and paired bootstrap confidence intervals. Code and raw results included."
canonical_url: ""
tags: rag, retrieval, llm, benchmarking
---

# Do RAG chunking strategies actually differ? Error bars, {n_models} embedding models and an overlap sweep

Chunking is the step everyone has an opinion about and almost nobody measures with error bars.
Blog posts rank the strategies confidently; the gaps they report are often two or three points,
reported once, from a single run, with no interval around them.

I went looking for how much of that advice survives a significance test. Five strategies, a corpus
of {n_docs} documents, {n_questions} questions, {n_models} embedding models, chunk sizes in tokens, and the
part that matters: **every setting chosen on a held-out dev split and every number reported on test
questions the tuning never saw**, with paired bootstrap confidence intervals over {n_boot} resamples.

**The short answer: on one embedding model {n_beat_word} of the four alternatives beat plain
fixed-size chunking, and on a second model {n_replicate_word} of those still do.** Against the
{reference} baseline on MRR@10 with {embedder}, {all_beat_baseline} of the other four strategies
beat it with an interval clear of zero: {beat_baseline_detail}. The others ({losers_list}) have
point estimates above the baseline but intervals that include it.

Then I ran the **identical chunks** through {embedder2}, and the picture did not hold:
{replication_detail}. {robust_sentence} What does survive the model change is weaker but more
useful: {ends_stable}, and {n_rank_stable} of the five strategies hold their rank throughout
({rank_stable}).

That is the finding I would actually stand behind, and it is a warning about every chunking
comparison you have read, including the first half of this one: **a chunking result measured on one
embedding model mostly describes that model.** Three further things came out of it:

1. **Strategy may matter more than size, {strategy_size_scope}.** Switching strategy at a fixed size moves
   MRR by {strategy_spread} (mean {mean_strategy_spread}); changing size within a strategy moves it
   by {size_spread} (mean {mean_size_spread}). {replicates_conj} {replicates} on the second model
   (strategy {model2_strategy_spread} vs size {model2_size_spread}), {replicates_caveat}.
2. **Overlap helps, and nothing beyond the smallest step is resolvable.** Going from no overlap to
   {ov_first_step} is worth {ov_first_gain} MRR. Going from there all the way to {ov_max} is
   {ov_tail_ci}, which is {ov_tail_resolvable}.
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
| **Corpus** | *Pro Git* (2nd ed.), Chacon & Straub, {n_docs} sections, ~107,000 words (~175,000 tokens), CC BY-NC-SA 3.0 |
| **Questions** | {n_questions} questions, each tied to one evidence passage that occurs exactly once |
| **Split** | {n_dev} dev (chooses settings) / {n_test} test (reported). Stratified by document, seed 0 |
| **Chunk sizes** | {sizes} tokens, measured with the {tokenizer} vocabulary |
| **Overlap sweep** | {overlaps} tokens at a {ov_size}-token chunk size |
| **Embedding models** | {embedder} and {embedder2}, ONNX, cosine similarity, top-10 |
| **Baselines** | BM25 over the identical chunks; {reference} as the reference configuration |
| **Metrics** | Recall@1/3, MRR@10, recall at a fixed {budget_tokens}-token budget, and token-level recall / precision / IoU at k={token_k} |
| **Statistics** | {n_boot} paired bootstrap resamples over the test questions |
| **Platform** | Python {python}, {cpu_count} CPU cores, {os}. One model: ~{runtime_min} min |

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
recall at a fixed {budget_tokens}-token budget: fill the context window and see who got the answer in.

**Context efficiency, not just recall.** Recall@k cannot tell a tight chunk that is mostly answer
from a long one with the answer buried in padding, and in production you pay per token. Token-level
precision is the share of everything you retrieved that was actually the answer. Across the sizes
tried it ranges from {tprec_small} to {tprec_large} for fixed-size chunking, a larger relative swing
than anything in the recall numbers.

Settings chosen on dev: {selected}.

## Results

{results_section}

## What I take from this

- **Dense retrieval beat BM25 on {dvb_n_sig} of the {dvb_n_total} chunkings**, by as much as
  {dvb_best_val} MRR on {dvb_best_name}. The exception is {dvb_exceptions}: on the plain fixed-size
  baseline the dense-versus-BM25 interval still includes zero ({dense_vs_bm25}). A chunking bad
  enough that a better retriever cannot exploit it is itself worth noticing.
- **{best_name} had the best point estimate** ({best_mrr}) and {worst_name} the worst
  ({worst_mrr}), a spread of {spread} MRR, and {best_name} is also the most context-efficient at
  {best_tprec} token precision. Both of those are point estimates on one model: {best_gap_note},
  and it is not necessarily the strategy that held up on {embedder2}.
- **{n_beat_word} of the {n_compared} other strategies beat the baseline on MRR with intervals clear
  of zero on {embedder}.** Not every comparison separates: on recall@3 several intervals still
  include zero, and the widest paired interval spans {widest_ci} MRR. Across all
  {n_all_comparisons} paired comparisons, {n_all_separated} separated.
- **The ordering among the winners is not resolvable.** {best_name} has the highest point estimate,
  but {best_gap_note}: {best_vs_winners}. So read the table as "{winners_verdict}" and not as a
  ranking.
- **Splitting the answer is a real failure mode only at small sizes.** At {small_size} tokens,
  fixed-size chunking left the answer passage intact in {intact_small} of questions. At the selected
  settings: {intact_table}.
- **Semantic chunking works, but it is the most expensive way to get there.** It reached
  {semantic_mrr} on {embedder}, {semantic_verdict} ({semantic_ci}), for {semantic_cost} the
  embedding work to build the index. Cheaper strategies reached the same place for the same indexing
  cost as plain fixed-size, and on {embedder2} its advantage over the baseline is no longer
  distinguishable. The published literature keeps reaching the same verdict.

### The overlap sweep

Overlap is the one setting the literature openly disagrees about, and I could not find a published
sweep of it. Here is one, at a {ov_size}-token chunk size.

Adding any overlap helps. MRR across the sweep runs {ov_mrr_path} and recall@3 runs
{ov_recall_path}. Note that recall@3 is **not monotonic**: it peaks at {ov_recall_peak}, not at the
largest overlap, so this is a step change at the first increment rather than a trend.

**The useful finding is that nothing beyond the first step is resolvable.** The first
{ov_first_step} buys {ov_first_gain} MRR. Going from there to {ov_max} is {ov_tail_ci}, which is
{ov_tail_resolvable}. So the honest statement is not "more overlap keeps helping", and not even
"the benefit saturates", but "I cannot resolve any difference above {ov_first_step}, and it costs
more to index": {ov_first_step} costs {ov_cost_first} the tokens of no overlap, while {ov_max}
costs {ov_index_growth}. The common default of 50% overlap buys nothing I can measure here and
charges for it.

**One caution about the cost side.** The widely used implementation of token-level precision sums
the length of every retrieved chunk in the denominator *without de-duplicating*. Text appearing in
two overlapping chunks is counted twice: it inflates the denominator while contributing nothing to
the numerator, so that denominator penalises overlap by arithmetic rather than by evidence.

I computed precision both ways to see how much that matters. Counting duplicate text twice,
precision {ov_dup_dir} across the sweep ({ov_tprec_dup}). Counting each piece of source text once,
it {ov_uni_dir} ({ov_tprec_uni}). So on this corpus {ov_verdict}: the choice of denominator changes
the size of the effect, not its sign, and precision goes up with overlap either way because the
recall gain outruns the extra context. I expected the two to disagree and they did not, which is
worth saying plainly rather than quietly dropping.

The caution still stands for anyone comparing strategies with very different redundancy: check
which denominator your harness implements before reading much into a precision or IoU gap.

### Does any of this survive a change of embedding model?

This is the question that decides whether a chunking result means anything, and most evaluations
cannot answer it because they test one model. Running the identical chunks through {embedder2}
instead of {embedder}, the strategy ranking is **{ranking_same}**.

On {embedder}: {model1_order}.
On {embedder2}, same chunks: {model2_order}.

Rank changes: {rank_moves}, and {ends_stable}. The spread between best and worst goes from {spread}
MRR to {model2_spread}.

Tested against the same baseline on the second model, {replication_detail}. So of the
{n_beat_baseline} strategies that beat plain fixed-size on {embedder}, **{n_replicate_word}** still does so
on {embedder2}.

Across all {n_models} models ({model_names}), {winners_differ}. Best strategy per model:
{model_best_each}. {n_rank_stable} of the five strategies hold the same rank on every model
({rank_stable}), and {robust_all_sentence}. The strategies that hold their rank are the ones worth
taking from this article, because they are the only claims here that do not depend on which encoder
you happen to use.

This is the single most useful thing I found, and it is uncomfortable, because it undercuts the
first half of my own article. A chunking comparison run on one embedding model is largely a
measurement of that model. If you are choosing a chunker from someone's table, check how many
retrievers they tested. Usually the answer is one.

### Where retrieval actually failed

Pooling the {n_selected_configs} selected configurations over the same {n_test} test questions gives
{total_misses} miss-events, so a question that defeats every strategy is counted
{n_selected_configs} times. Of those, {split_misses} were caused by the evidence being split across
chunks. {wrongdoc_misses} had their top hit in the wrong document entirely and {wrongpassage_misses}
in the right document but the wrong passage.

A caveat on that split count, because it is partly definitional: a miss is filed that way only when
*no* chunk anywhere in the index covers at least half the evidence, and in this corpus
{answerable_note}. The stricter evidence-intact measure is the one to trust on whether splitting
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
- **{n_test} test questions.** That is why so many intervals include zero. This experiment can show
  that differences are *not resolvable*; it cannot prove they are absent.
- **Questions were drafted with AI assistance and audited, not reviewed by a second person.**
  `scripts/analyse_questions.py` measures the things that decide whether a question set is sound,
  and its output is in the repo. On this set: {qa_dups} near-duplicate questions, {qa_leak} with
  verbatim leakage from their own evidence, {qa_overlap} with heavy lexical overlap, mean
  question-to-evidence similarity {qa_sim}. {qa_anaphoric} of the {n_questions} evidence passages
  open with an anaphor ("This is...", "In that case..."), which matters because a passage that starts
  with a back-reference cannot be judged relevant on its own. Coverage is even: {qa_docs} documents
  carry questions and the busiest single document holds {qa_maxshare} of them. An earlier version of
  this set failed both of those checks, with 19 anaphoric passages and 130 questions crowded onto 20
  of the 64 documents, so it was rebuilt from scratch before these results were produced.
- **Some questions are genuinely ambiguous.** For {qa_ambiguous} of the {n_questions} questions
  ({qa_ambiguous_pct}), another question's evidence passage matches the question better than its own
  does. Most of that is a good sign, since it means the questions are paraphrased rather than
  lookups, but part of it is real ambiguity: a passage I score as wrong may be a defensible answer.
  That depresses every strategy equally, so the comparisons stand, but the absolute recall and MRR
  numbers should be read as a floor rather than a ceiling.
- **{n_models} embedding models, all small.** Better models may behave differently again. The
  repo takes `--compare` any number of times, so adding more is one command per model.
- **Retrieval only.** I did not measure whether any of this survives to the generated answer. Qu et
  al. found retrieval differences largely washed out in generation.
- **Context windows differ between models, and this is a confound.** {embedder} reads at
  most {max_len} tokens; {embedder2} reads at most {model2_maxlen}. On {embedder} the selected
  configurations are affected as follows: {truncation}, so {worst_trunc}. On {embedder2} the shorter
  window bites harder: {truncation2}. Any {embedder2} number for an affected configuration is partly
  a context-window artefact and not purely a verdict on its boundaries. I did not separate the two
  effects, and it is one reason the cross-model section should be read as "these results are
  fragile" rather than as a clean ranking of models.
- **Some settings were chosen on a near-tie.** The dev split picks one configuration per strategy,
  and {n_fragile} of them were decided by a hair: {fragile_selections}. A different split seed could
  select a different row and move that strategy several places. The protocol is honest but the
  resulting ordering is not robust.
- **Chunk boundaries are identical across models for every strategy except semantic**, which places
  its boundaries using the embedding model itself, so its chunks genuinely differ between the two
  runs. The cross-model comparison is like-for-like for the other four.
- **No correction for multiple comparisons.** I report {n_all_comparisons} paired comparisons and
  highlight the {n_all_separated} whose intervals clear zero. At a 5% threshold across that many
  tests you would expect roughly one to clear by chance. Treat them as suggestive.
- **My token-level metrics are computed over real tokens**, whereas the implementation this family
  of metrics comes from works over character offsets. The numbers are therefore close cousins of
  the published ones, not the same quantity.

## If you just want a decision rule

For prose documents like this one, on this evidence:

1. **Stop using plain fixed-size chunking with no overlap.** That is the one recommendation here
   that survived the change of embedding model: {ends_stable}. Everything else on this list is
   weaker than it looks.
2. **Prefer recursive splitting as the default, but hold it loosely.** {robust_sentence} The
   highest scorer was {model1_best} on {embedder} and {model2_best} on {embedder2}, so the winner
   is model-dependent; recursive is the one I would start from because it was never the worst on
   either model, costs nothing extra to build, and is what Chroma's much larger evaluation
   independently landed on. Re-run the comparison on your own encoder before trusting any ranking,
   including this one. That is a day of work and it changed the answer here.
3. **Add a little overlap, not a lot.** The first {ov_first_step} was worth {ov_first_gain} MRR;
   everything beyond it was inside the noise and cost real index size. Ignore precision-based
   arguments against overlap until you have checked how your harness counts duplicated text.
4. **Do not reach for semantic chunking first.** On {embedder} it was {semantic_verdict}
   ({semantic_ci}) while costing {semantic_cost} the indexing work of the cheaper strategies, and it
   placed fourth of five on both models. The published literature reaches the same verdict outside
   artificially stitched corpora.
5. **Spend the effort on your retriever.** Dense versus BM25 had the largest point estimate of
   anything measured here ({dvb_best_val} MRR on {dvb_best_name}), though its interval overlaps the
   larger chunking effects, so I would not claim a strict ordering.
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
python run_experiment.py --embedder onnx:{tag} --tag {tag}
python run_experiment.py --embedder onnx:minilm --tag minilm
python scripts/make_report.py   --tag {tag} --compare minilm
python scripts/build_article.py --tag {tag} --compare minilm
```

Raw per-question results, the failure taxonomy and the paired comparisons are all in
`results/{tag}/`. Every number in this article is generated from those files by
`scripts/build_article.py`; none is typed by hand.

## Corrections

I would rather be corrected than cited. If you find a bug, a bad question or a methodological
mistake, open an issue on the repo and I will update this post and note the change here.

*Corpus: Pro Git, Scott Chacon and Ben Straub, CC BY-NC-SA 3.0, https://github.com/progit/progit2*

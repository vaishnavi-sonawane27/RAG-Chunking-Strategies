---
title: "Do RAG chunking strategies actually differ? I re-ran the comparison with error bars"
subtitle: "{n_docs} documents, {n_questions} questions, five chunking strategies, paired bootstrap confidence intervals and a dev/test split. Code and raw results included."
canonical_url: ""
tags: rag, retrieval, llm, benchmarking
---

# Do RAG chunking strategies actually differ? I re-ran the comparison with error bars

Chunking is the step everyone has an opinion about and almost nobody measures with error bars.
Blog posts rank the strategies confidently; the gaps they report are often two or three points,
reported once, from a single run, with no interval around them.

So I rebuilt the comparison with the statistics attached. Five strategies, one corpus of
{n_docs} documents, {n_questions} questions, a real embedding model ({embedder}), and, most importantly, **every chunk size chosen on a held-out dev split and every number reported on test
questions the tuning never saw**, with paired bootstrap confidence intervals over {n_boot}
resamples.

**The short answer: it depends which question you ask, and most of the gaps are smaller than the
noise.** Against the {reference} baseline on MRR@10, all {n_compared} strategies had confidence
intervals that still contained zero, so none is distinguishable from plain fixed-size chunking on that
metric, and the widest of those intervals spans {widest_ci} MRR.

But MRR is not the only thing that matters, and across all {n_all_comparisons} paired comparisons
(three metrics × four strategies), **{n_all_separated} did separate from the baseline**:
{sep_detail}.

Every one of those is a *coverage* win (getting the answer into the context you send the model at
all), not a *ranking* win. Fixed + overlap appears twice because at ~150-word chunks a 450-word
budget holds about three chunks, so the two metrics coincide there; they come apart wherever chunk
sizes differ.

So the honest summary is: **how you split the text changes how often the answer makes it into the
context window, and barely changes how well it ranks once it is there.**

**What this is not:** a new finding about chunking. That ground is well covered (see
[Prior work](#prior-work)). What I think is worth your time is the method: a fully reproducible
harness, a dev/test split, and intervals, because it shows how much of the usual chunking advice
survives contact with a significance test.

**Disclosure:** I am a final-year CS student. Nobody paid for this, I am not affiliated with any
vector database or embedding vendor, and I have no stake in which strategy wins. Repo:
**[REPO LINK]**.

## The setup, in brief

| | |
|---|---|
| **Corpus** | *Pro Git* (2nd ed.), Chacon & Straub, chapters 1–8 and 10, {n_docs} sections, ~107,000 words, CC BY-NC-SA 3.0 |
| **Questions** | {n_questions} questions, each tied to one evidence passage that occurs exactly once |
| **Split** | {n_dev} dev (chooses settings) / {n_test} test (reported). Stratified by document, seed 0 |
| **Embedding model** | {embedder}, ONNX, cosine similarity, top-10 |
| **Baselines** | BM25 over the identical chunks; {reference} as the reference configuration |
| **Metrics** | Recall@1, Recall@3, MRR@10, and recall at a fixed {budget_words}-word context budget (Recall@5 is in `summary.csv` and defines the failure analysis) |
| **Statistics** | {n_boot} paired bootstrap resamples over the test questions |
| **Platform** | Python {python}, {cpu_count} CPU cores, {os}. Full run: ~{runtime_min} min |

Two design choices do most of the work.

**A relevance rule that does not depend on chunking.** A retrieved chunk counts as relevant if it
lies in the right document and covers at least half of the question's evidence passage. That rule is
identical for every strategy, so a strategy that slices the answer in half is penalised, which is
the whole thing we are trying to measure. I also report how often the evidence survives *whole*
inside a single chunk.

**A fixed context budget.** Comparing strategies at the same `k` quietly favours small chunks: ten
50-word chunks is a different amount of context than ten 300-word chunks. So alongside recall@k I
report recall at a fixed {budget_words}-word budget: fill the context window and see who got the
answer in. Note that for chunks of roughly 150 words a {budget_words}-word budget fits about three
of them, so for those configurations this metric nearly coincides with recall@3; it diverges exactly
where chunk sizes differ, which is the point. Settings chosen on dev: {selected}.

## Results

{results_section}

## What I take from this

- **Dense retrieval beat BM25 on the same chunks** ({ref_name}: {ref_mrr} dense vs {bm25_ref_mrr}
  BM25). Paired on the same test questions, that difference is {dense_vs_bm25_paired}. It clears
  zero, though not by much, and it is the largest single effect measured here. Worth stating because an earlier version of this
  experiment used weak static word-vector embeddings, and BM25 beat *them* on every strategy. The
  embedding model changes the conclusion, so any chunking result is conditional on it.
- **The point-estimate ranking puts {best_name} first** ({best_mrr}) and {worst_name} last
  ({worst_mrr}), a spread of {spread} MRR.
- **On MRR@10, none of the {n_compared} strategies separated from the baseline**: every interval
  contains zero. On coverage metrics ({sep_metrics}), {n_all_separated} of {n_all_comparisons}
  comparisons did. No paired MRR difference was larger than its own interval, so with {n_test} test
  questions a point-estimate ranking on MRR is not informative here.
- **Splitting the answer is a real failure mode, at small chunk sizes.** At {small_size} words,
  fixed-size chunking left the answer passage intact in only {intact_fixed_small} of questions,
  against {intact_sentence_small} for sentence-based. If the answer is cut in half, no embedding
  model can retrieve it whole.
- **But at the sizes the dev split actually chose, that problem is already solved.** Evidence-intact
  at the selected settings: {intact_table}. This is the part I did not expect, and it
  reframes the whole comparison: see below.
- **Overlap buys coverage, not ranking.** Adding overlap to fixed-size chunking raised
  evidence-intact to {overlap_intact} and was one of the few changes that separated from the
  baseline on recall@3 and the budget metric. On MRR it moved {overlap_delta} ({overlap_ci}), i.e.
  not detectably. It makes the answer more likely to be *present*, not better *ranked*. **This is a
  dense-retrieval result only:** with the identical chunks under BM25, overlap changed recall@3 by
  {ov_bm25}, exactly nothing.
- **Semantic chunking cost {semantic_cost} the embedding work** of fixed-size chunking to build the
  index, for {semantic_mrr}, the worst MRR in the set. On this corpus that is not a good trade,
  which matches the published literature (below). **But see the caveat about truncation in
  Limitations: semantic chunks were the longest, and {worst_trunc_pct} of them exceeded the model's
  512-token window, so part of its deficit may be truncation rather than bad boundaries.** I did not
  separate the two effects.

### The thing I did not expect

Pooling the {n_selected_configs} selected configurations over the same {n_test} test questions gives
{total_misses} miss-events (so a question that defeats every strategy is counted {n_selected_configs}
times). Of those, **{split_misses} were caused by the evidence being split across chunks.**
{wrongdoc_misses} had their top hit in the wrong document entirely and {wrongpassage_misses} in the
right document but the wrong passage.

Once chunks are large enough to hold an answer, chunking stops being the bottleneck. What is left
are retrieval failures: the embedding model confidently fetching a different section that is
genuinely about a related thing. The sections it landed on most often were {top_wrong_docs}, which
are exactly the near-neighbours of the questions being asked. That is the best explanation I have
for the headline result: the strategies are hard to tell apart on ranking because, at sensible sizes,
**they are no longer the thing that is failing.**

**One caveat on that zero, because it is partly definitional.** A miss is filed as "evidence split"
only when *no* chunk anywhere in the index covers at least half the evidence passage, and in this
corpus {answerable_note}. So that bucket could not have come out non-zero at any chunk size I tried,
and the honest reading is narrower than it first looks: the ≥50% rule is lenient, and under it
splitting never made an answer wholly unreachable. The stricter *evidence-intact* measure does move
(it is {intact_fixed_small} at {small_size} words for fixed-size), which is the number to trust on
whether splitting hurts.

## Prior work

This question has been studied properly, and my results mostly agree with the existing consensus.
If you are choosing a chunker for real work, read these rather than me:

- **Chroma, "Evaluating Chunking Strategies for Retrieval"** (Smith & Troynikov, July 2024).
  The most thorough public evaluation. Introduces token-level recall/precision and IoU, which penalise
  dragging in padding around the answer, and a clever *Precision_Ω* that isolates boundary quality
  from retriever quality. Found `RecursiveCharacterTextSplitter` at 200 tokens with no overlap
  consistently strong, and off-the-shelf semantic chunking weaker than its reputation.
  https://research.trychroma.com/evaluating-chunking
- **"Is Semantic Chunking Worth the Computational Cost?"** (Qu, Tu & Bao, *Findings of ACL: NAACL
  2025*, pp. 2155–2177; arXiv:2410.13070). The key negative result. Semantic chunking won mainly on
  corpora *artificially stitched* from short documents, and fixed-size won on naturally long ones.
  Their conclusion is that the costs are not justified by consistent gains.
- **"Late Chunking"** (Günther et al., arXiv:2409.04701). Embed the whole document first, then pool
  token embeddings per chunk. Reports roughly +1.8 nDCG@10 with no retraining, and notes overlapping
  chunks neither clearly helped nor hurt.
- **Anthropic, "Contextual Retrieval"** (Sept 2024). Not a boundary method but chunk *enrichment*:
  prepend generated context before embedding. Cut retrieval failure rate from 5.7% to 3.7% at top-20.
  Orthogonal to everything measured here, and a better-evidenced return than boundary tricks.
- **"A Systematic Investigation of Document Chunking Strategies and Embedding Sensitivity"**
  (Shaukat, Adnan & Kuhn, arXiv:2603.06976). 36 strategies, and the only one I found that reports
  runtime, memory and index size next to quality.
- **Śmigielski et al., arXiv:2606.00881** (May 2026) describes itself as the first systematic
  evaluation across a wide range of chunking methods.

The honest summary of that literature: **respecting structure that already exists in the document
helps; inferring new boundaries from embedding similarity usually does not pay for itself.** My
results are consistent with that, which is reassuring but not independent evidence; I went looking
after reading them.

## Limitations

Specific enough to be falsifiable:

- **One corpus, one genre, one language.** A technical book in English with clean headings. Results
  may not transfer to PDFs with tables, transcripts, or multilingual corpora.
- **{n_test} test questions.** That is why so many intervals include zero. This experiment can show
  that differences are *not resolvable*; it cannot prove they are absent. A larger question set would
  narrow the intervals and might separate strategies this one cannot.
- **Questions were drafted with AI assistance** and verified programmatically (each evidence passage
  occurs exactly once; questions are checked for verbatim leakage), but they have not been
  independently reviewed by a second person. They are also paraphrased by construction, which favours
  embeddings over lexical matching.
- **Retrieval only.** I did not measure whether any of this survives to the generated answer. Qu et
  al. found retrieval differences largely washed out in generation, so assume they might here too.
- **Chunk size is measured in words, not model tokens.** Roughly 1.3 tokens per word for this text.
- **One embedding model.** Chroma found the ranking changed between embedding models; so should you
  expect it to here.
- **Long chunks get truncated, and this is a confound.** bge-small reads at most 512 word pieces.
  Chunks exceeding that, by selected configuration: {truncation}. {worst_trunc_name} is the most
  affected at {worst_trunc_pct}, so its lower score is partly a context-window artefact and not
  purely a verdict on its boundaries. It is worse in the size sweep ({worst_sweep_trunc}), so the
  flat-to-declining large-chunk results there are partly a truncation artefact too. Capping chunk
  length below the model window, or using a longer-context encoder, would separate those effects.
  I did not do that here.
- **No correction for multiple comparisons.** I report {n_all_comparisons} paired comparisons and
  highlight the {n_all_separated} whose intervals clear zero. At a 5% threshold across that many
  tests you would expect roughly one to clear by chance, and two of the three are the same underlying
  result on two metrics that coincide at this chunk size. Treat them as suggestive, not as
  {n_all_separated} independent findings.
- **Evidence-intact, answerable and mean-words-in-budget are diagnostics of the chunking itself**,
  not retrieval scores. They are computed on the test questions like everything else, but they do not
  depend on the retriever, so they carry no tuning signal either way.
- **The ONNX weights came from an npm redistribution**, not from the official model repository,
  because the machine I ran this on could not reach Hugging Face. The hashes are pinned in the repo.
  Re-run with `--embedder st:BAAI/bge-small-en-v1.5` against official weights if that matters to you,
  and tell me if the numbers move.

## If you just want a decision rule

For prose documents like this one, on this evidence:

1. **Start with recursive or sentence-aware splitting at a moderate size** and move on. It respects
   boundaries that already exist, costs nothing extra, and nothing here beat it by a margin I can
   defend.
2. **Add overlap if the answers you need are short.** This is the opposite of what I assumed before
   looking. Overlap moved recall@3 from {ov_short_r3} on short evidence and from {ov_long_r3} on long
   evidence. All of its measured benefit is on short passages, and on long ones MRR actually went
   {ov_long_mrr}. It is cheap, but it is not a general fix, and it is not a fix for the dominant
   failure mode here (see below).
3. **Do not reach for semantic chunking first.** It cost {semantic_cost} the indexing work here for no
   defensible gain, and the published literature finds the same outside of artificially stitched corpora.
4. **Spend the effort on your embedding model and on evaluation instead.** Switching from weak static
   embeddings to a real model moved my numbers far more than any chunking choice did.
5. **Measure on your own documents.** Every source above, including this one, finds that the winner
   depends on the corpus.

## Reproduce it

```bash
git clone [REPO LINK]
cd rag-chunking-experiment
pip install -r requirements.txt
python scripts/fetch_corpus.py        # downloads Pro Git, converts to text
python scripts/validate_questions.py  # checks every evidence passage resolves uniquely
python scripts/fetch_models.py        # ONNX weights, hash-pinned
python run_experiment.py --embedder onnx:{tag} --tag {tag}
python scripts/make_report.py --tag {tag}
```

Raw per-question results, the failure taxonomy and the paired comparisons are all in `results/{tag}/`.
Every number in this article is generated from those files by `scripts/build_article.py`; none of
them is typed by hand.

## Corrections

I would rather be corrected than cited. If you find a bug, a bad question, or a methodological
mistake, open an issue on the repo and I will update this post and note the change here.

*Corpus: Pro Git, Scott Chacon and Ben Straub, CC BY-NC-SA 3.0, https://github.com/progit/progit2*

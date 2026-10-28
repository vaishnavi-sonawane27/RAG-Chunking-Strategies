# RAG chunking strategies, with confidence intervals

A small, fully reproducible comparison of five document chunking strategies for retrieval in a RAG
pipeline, run with a **held-out dev/test split** and **paired bootstrap confidence intervals**, so
that differences can be assessed for significance instead of ranked on point estimates.

| Strategy | What it does |
|---|---|
| Fixed-size | cut every N tokens, ignoring structure |
| Fixed + overlap | the same, with an overlapping window (swept at 10% / 20% / 40%) |
| Sentence-based | pack whole sentences up to N tokens |
| Recursive | split on paragraph → line → sentence → word, then merge back up to N tokens |
| Semantic | start a new chunk where embedding distance between neighbouring sentences jumps |

## This is a replication, not a discovery

Chunking has been evaluated carefully by others, and this repo agrees with their consensus. Read
these first: [Chroma's chunking evaluation](https://research.trychroma.com/evaluating-chunking)
(Smith & Troynikov, 2024); [*Is Semantic Chunking Worth the Computational
Cost?*](https://arxiv.org/abs/2410.13070) (Qu, Tu & Bao, Findings of ACL: NAACL 2025);
[*Late Chunking*](https://arxiv.org/abs/2409.04701) (Günther et al.);
[*A Systematic Investigation of Document Chunking Strategies*](https://arxiv.org/abs/2603.06976)
(Shaukat et al.); and [arXiv:2606.00881](https://arxiv.org/abs/2606.00881) (Śmigielski et al.).

What this adds is narrow and methodological: a dev/test split so chunk sizes are not tuned on the
reported numbers, paired bootstrap intervals on every comparison, a fixed-context-budget metric, and
cost reported next to quality. These are gaps several of those authors name themselves.

## What makes the measurement trustworthy

* **Relevance is chunking-independent.** A chunk counts as relevant if it is in the right document
  and covers ≥50% of the question's evidence passage. The same rule applies to every strategy, so a
  strategy that slices the answer in half is penalised. `evidence_intact` separately reports how
  often the passage survives *whole*.
* **Settings are chosen on dev, reported on test.** Chunk sizes and semantic thresholds are picked
  using 30% of the questions; every headline number comes from the other 70%, which the tuning never
  saw. Without this, sweeping sizes and reporting the best is tuning on the test set.
* **Comparisons are paired.** All configurations are scored on the same questions using one shared
  set of bootstrap resamples, so `paired_vs_reference.csv` gives the difference against the baseline
  with an interval, which is the right way to ask "is this actually better?"
* **Sizes are in model tokens, not words.** Every published chunking evaluation reports token
  sizes, so word-based sizes cannot be compared with them. One canonical tokenizer is used for
  sizing regardless of which model is being evaluated, so chunk boundaries stay identical across
  models and a model difference is a model difference.
* **Equal context budgets.** Comparing at the same `k` favours small chunks. `recall@1000tok` fills
  a fixed token budget instead and asks who got the answer in.
* **Context efficiency is measured.** Recall cannot tell a tight chunk from a long one with the
  answer buried in padding. Token-level precision and IoU measure how much of what you retrieved
  was actually the answer. Both are reported two ways: counting text that appears in two
  overlapping chunks twice (which is what Chroma's published implementation does) and counting it
  once. The choice changes the verdict on overlap.
* **Two embedding models.** Published work shows the strategy ranking can change between models,
  so a single-model result cannot support a general claim.
* **Cost is reported.** `index_embed_words` counts the embedding work to build each index, including
  the extra sentence pass semantic chunking needs.
* **Distractors.** Questions cover 20 of 64 documents; the other 44 exist to be wrongly retrieved.

## Reproduce

```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python scripts/fetch_corpus.py            # downloads Pro Git, converts to plain text
python scripts/validate_questions.py      # every evidence passage must resolve uniquely
python scripts/analyse_questions.py       # question-set quality audit -> data/question_audit.json
python -m pytest -q                       # unit tests + an end-to-end sanity check

python scripts/fetch_models.py            # ONNX weights, pinned by SHA-512
python run_experiment.py --embedder onnx:bge-small --tag bge-small
python run_experiment.py --embedder onnx:minilm    --tag minilm
python scripts/make_report.py   --tag bge-small --compare minilm
python scripts/build_article.py --tag bge-small --compare minilm
```

`results/bge-small/` then contains `summary.csv`, `paired_vs_reference.csv`, `per_question.csv`,
`failure_taxonomy.csv`, `failures.md`, four charts and `results_section.md`.
`article/FINAL.md` is the written article with every number injected from those files. The build
**fails** rather than emit a hand-typed number.

### Running official Hugging Face weights instead

`scripts/fetch_models.py` pulls ONNX exports from npm because the machine this was developed on
could not reach `huggingface.co`. Those are **third-party redistributions**: the hashes are pinned,
which proves the bytes have not changed, not that the publisher is trustworthy. If you can reach
Hugging Face, prefer the official weights:

```bash
pip install sentence-transformers
python run_experiment.py --embedder st:BAAI/bge-small-en-v1.5 --tag bge-official
```

### Without any model download

```bash
python run_experiment.py --embedder none --tag smoke --smoke   # BM25 only, ~2 s
```

This is what CI runs on every push.

## Layout

```
run_experiment.py         the experiment: strategies × sizes × retrievers
src/chunkers.py           the five chunkers (every chunk keeps its character span)
src/retrieval.py          ONNX encoder, dense retriever, BM25
src/dataset.py            corpus + question loading, evidence resolution, dev/test split
src/models.py             model provenance and pinned hashes
scripts/                  fetch_corpus, fetch_models, validate_questions, make_report, build_article
tests/                    chunker unit tests, evidence-as-query sanity check
data/questions.json       130 questions with evidence passages  (see data/README.md)
article/template.md       article prose with {placeholders}
article/FINAL.md          generated article
results/<tag>/            CSVs, charts, failure analysis
```

## Licensing

Code is MIT. **`data/questions.json` is CC BY-NC-SA 3.0**, because its evidence fields quote *Pro
Git*. The book text itself is never committed; `scripts/fetch_corpus.py` downloads it. See
[`LICENSE`](LICENSE) and [`data/README.md`](data/README.md).

## Limitations

One corpus, one language, one embedding model, retrieval only (no generation), chunk size in words
rather than model tokens, and a question set drafted with AI assistance that has been verified
programmatically but not reviewed by a second person. The test split is deliberately small enough
that many differences are *not* resolvable. That is the finding, not a defect, but it does mean
this cannot prove two strategies are equivalent.

Corrections welcome as issues.

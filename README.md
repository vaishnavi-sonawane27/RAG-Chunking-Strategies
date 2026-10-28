# RAG chunking strategies, with confidence intervals

[![CI](https://github.com/vaishnavi-sonawane27/RAG-Chunking-Strategies/actions/workflows/ci.yml/badge.svg)](https://github.com/vaishnavi-sonawane27/RAG-Chunking-Strategies/actions)

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
* **More than one embedding model.** Published work shows the strategy ranking can change between
  models, so a single-model result cannot support a general claim. The committed run uses two; the
  pipeline accepts any number, and the article reports which strategies survive *all* of them.
* **Cost is reported.** `index_embed_words` counts the embedding work to build each index, including
  the extra sentence pass semantic chunking needs.
* **Every document is a target and a distractor.** All 64 documents carry questions (3 or 4 each, no
  document holding more than 2% of the set), and for any one question the other 63 are there to be
  wrongly retrieved. An earlier version of this set put 130 questions on just 20 documents, which
  both concentrated the result on a fifth of the corpus and left the rest as mere decoration.

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

`--compare` takes any number of tags, so a six-model comparison is
`--compare minilm e5-base-v2 gte-base ...`. Chunk boundaries never change between models, because
sizing always uses one canonical tokenizer, so a difference between two columns is a difference
between the models rather than between two different sets of chunks.

`results/bge-small/` then contains `summary.csv`, `paired_vs_reference.csv`, `per_question.csv`,
`paired_cross_model.csv`, `failure_taxonomy.csv`, `failures.md`, five charts and
`results_section.md`. Note that `paired_vs_reference.csv` compares each model against *its own*
dev-selected reference, so the cross-model comparisons, which hold the configuration fixed across
models, live in `paired_cross_model.csv`.
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

To sweep several official models and rebuild the report and article in one go:

```bash
python scripts/run_models.py          # six popular English encoders, bge-small as reference
python scripts/run_models.py BAAI/bge-base-en-v1.5 intfloat/e5-base-v2 thenlper/gte-base
```

A model that fails to download is reported and skipped rather than taking the whole run down.

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
data/questions.json       215 questions with evidence passages  (see data/README.md)
article/template.md       article prose with {placeholders}
article/FINAL.md          generated article
results/<tag>/            CSVs, charts, failure analysis
```

## Licensing

Code is MIT. **`data/questions.json` is CC BY-NC-SA 3.0**, because its evidence fields quote *Pro
Git*. The book text itself is never committed; `scripts/fetch_corpus.py` downloads it. See
[`LICENSE`](LICENSE) and [`data/README.md`](data/README.md).

## Limitations

One corpus, one language, two embedding models, retrieval only (no generation), and a question set
drafted with AI assistance that has been verified programmatically but not reviewed by a second
person. On 31% of questions some other labelled passage in the set is a closer embedding match than
the question's own evidence; Git's chapters overlap in subject matter, so this is a property of the
corpus rather than a bug, but it does put a ceiling on achievable recall. The test split is deliberately small enough
that many differences are *not* resolvable. That is the finding, not a defect, but it does mean
this cannot prove two strategies are equivalent.

Corrections welcome as issues.

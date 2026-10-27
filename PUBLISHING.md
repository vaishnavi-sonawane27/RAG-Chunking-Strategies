# Publishing checklist

## 1. Push the repo

I could not push from the sandbox (no valid GitHub credentials there), so the repo is committed
locally and ready. From the project folder:

```bash
git remote add origin https://github.com/vaishnavi-sonawane27/rag-chunking-experiment.git
git push -u origin main
```

Create the empty repo on GitHub first (no README, no .gitignore — this repo has both).
Then in the repo settings add a description and these topics: `rag`, `retrieval`, `benchmark`,
`information-retrieval`, `reproducible-research`, `llm`.

Check after pushing:
- the CI badge goes green (Actions tab) — CI fetches the corpus, validates all 130 questions and
  runs the tests on every push
- `data/_models/` and `data/docs/` are **not** in the repo (they are gitignored; the repo is ~300 KB)
- the README renders and the links resolve

Add the badge to the top of README.md once the repo exists:

```markdown
[![CI](https://github.com/vaishnavi-sonawane27/rag-chunking-experiment/actions/workflows/ci.yml/badge.svg)](https://github.com/vaishnavi-sonawane27/rag-chunking-experiment/actions)
```

## 2. Before you publish the article — read these

- **Read the questions.** Skim `data/questions.json`. They were drafted with AI help and verified
  programmatically, and the article says so, but you are putting your name on them. Fix any you
  disagree with, re-run, and the article regenerates.
- **Re-run on official weights if you can.** The ONNX files come from third-party npm
  redistributions because the build machine could not reach Hugging Face. On your own machine:
  `pip install sentence-transformers && python run_experiment.py --embedder st:BAAI/bge-small-en-v1.5 --tag bge-official`
  then `make_report.py` and `build_article.py` with `--tag bge-official`. If the numbers hold, say so
  in the article and drop the caveat. If they move, that is itself worth reporting.
- **Fill in `[REPO LINK]`** in `article/FINAL.md` (two places).
- **Decide the title.** The current one is a question the article answers in the first screen, which
  is the safest honest shape. Avoid superlatives you cannot test.

## 3. Where to publish

Own the canonical URL. Publish first on the blog you control, then syndicate.

1. **Day 0 — your own blog** (Hashnode on a custom domain, or your own site). This is the canonical.
2. **Day 0–2 — Hacker News**, submitted with the canonical URL and the title unedited. HN guidelines:
   no all-caps, no exclamation marks, no editorialising, don't add the site name.
3. **Day 2–7 — dev.to**, with `canonical_url:` set in the front matter to your own URL, so your
   domain keeps the ranking. The template already has an empty `canonical_url` field.
4. **LinkedIn** — one post: the question, the one-line answer, the chart, the link.

On Hashnode the canonical field is under the editor's **Draft/Article Settings → "Are you
republishing?" → Add Original URL**.

## 4. What will get attacked, and what protects you

From how benchmark posts usually get torn apart:

| Likely objection | Already handled |
|---|---|
| "No error bars" | paired bootstrap CIs on every comparison |
| "You tuned on your test set" | sizes chosen on dev, reported on test, split seed in `run_info.json` |
| "Small chunks win because you retrieve more of them" | `recall@450w` at a fixed context budget |
| "Unrepresentative corpus" | stated plainly in Limitations; corpus is public and licensed |
| "What hardware/versions?" | platform block in `run_info.json` and in the article |
| "Cherry-picked baseline" | BM25 on identical chunks, plus a declared reference config |
| "No cost accounting" | `index_embed_words` per strategy, including semantic's extra pass |
| "You're claiming novelty that isn't there" | the article says outright this is a replication and cites the prior work |

The one you cannot fully answer is sample size — 130 questions is small, and that is exactly why so
many intervals include zero. Say it first, before a commenter does.

## 5. After publishing

Respond to corrections and update the post with a dated changelog at the bottom. Benchmark posts
that visibly get corrected are the ones people keep linking to.

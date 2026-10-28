"""Run the experiment across several Hugging Face embedding models, then build the report.

The sandbox this was developed in could not reach huggingface.co, so the committed results use
ONNX redistributions fetched from npm (see src/models.py). On a machine with normal network access,
this script runs the official weights instead, which is the better provenance story.

    pip install sentence-transformers
    python scripts/run_models.py

Chunk boundaries do not change between models: sizing always uses the one canonical tokenizer in
data/_models/bge-small/tokenizer.json. So a difference between two columns of the output is a
difference between the models, not between two different sets of chunks.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DEFAULT = [
    "BAAI/bge-small-en-v1.5",
    "BAAI/bge-base-en-v1.5",
    "intfloat/e5-base-v2",
    "thenlper/gte-base",
    "sentence-transformers/all-mpnet-base-v2",
    "sentence-transformers/all-MiniLM-L6-v2",
]


def tag_for(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.split("/")[-1].lower()).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("models", nargs="*", default=DEFAULT,
                    help="Hugging Face model names (default: six popular English encoders)")
    ap.add_argument("--reference", default=None,
                    help="which model is the reference column (default: the first one)")
    args = ap.parse_args()
    models = args.models or DEFAULT
    tags = [tag_for(m) for m in models]
    if len(set(tags)) != len(tags):
        sys.exit("two models reduce to the same tag; pass distinct models")

    done = []
    for name, tag in zip(models, tags):
        print(f"\n=== {name}  ->  results/{tag} ===", flush=True)
        r = subprocess.run([sys.executable, "run_experiment.py",
                            "--embedder", f"st:{name}", "--tag", tag], cwd=ROOT)
        if r.returncode:
            print(f"!! {name} failed (exit {r.returncode}); continuing without it", flush=True)
            continue
        done.append(tag)

    if len(done) < 2:
        sys.exit("\nfewer than two models succeeded, so there is nothing to compare")

    ref = tag_for(args.reference) if args.reference else done[0]
    if ref not in done:
        sys.exit(f"reference {ref} is not among the models that succeeded: {', '.join(done)}")
    others = [t for t in done if t != ref]

    for script in ("make_report.py", "build_article.py"):
        cmd = [sys.executable, f"scripts/{script}", "--tag", ref, "--compare", *others]
        print("\n$ " + " ".join(cmd[1:]), flush=True)
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode:
            return r.returncode

    print(f"\n{len(done)} models: {', '.join(done)}")
    print(f"reference column: {ref}")
    print("article/FINAL.md and results/%s/results_section.md are regenerated." % ref)
    return 0


if __name__ == "__main__":
    sys.exit(main())

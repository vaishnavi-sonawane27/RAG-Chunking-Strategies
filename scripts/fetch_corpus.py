"""Download Pro Git (CC BY-NC-SA 3.0) chapters 1-3 and convert them to clean plain text.

The book text is NOT committed to this repo; run this script to recreate data/docs/.
Source: https://github.com/progit/progit2  (Scott Chacon and Ben Straub)
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "data" / "docs"
CLONE = ROOT / "data" / "_progit2"
CHAPTERS = [
    "01-introduction", "02-git-basics", "03-git-branching", "04-git-server",
    "05-distributed-git", "06-github", "07-git-tools", "08-customizing-git",
    "10-git-internals",
]


def clone():
    if not CLONE.exists():
        subprocess.run(
            ["git", "clone", "--depth", "1", "https://github.com/progit/progit2.git", str(CLONE)],
            check=True,
        )


def clean_asciidoc(text: str) -> str:
    out = []
    in_block = False
    for line in text.splitlines():
        s = line.rstrip()
        if re.match(r"^(ifdef|ifndef|endif)::", s):
            continue
        if re.match(r"^(image|include)::", s):
            continue
        if re.match(r"^\[\[.*\]\]$", s):          # anchors
            continue
        if re.match(r"^\[(source|quote|NOTE|TIP|WARNING|CAUTION|IMPORTANT|cols|options|%|role).*\]$", s) or s.startswith("[["):
            continue
        if re.match(r"^(\[.*\])$", s) and not s.startswith("[["):   # other block attributes
            continue
        if s.strip() in ("----", "====", "....", "____", "|===", "****"):
            in_block = not in_block if s.strip() == "----" else in_block
            continue
        if s.startswith("//"):
            continue
        m = re.match(r"^(=+)\s+(.*)$", s)
        if m:
            out.append("")
            out.append(m.group(2).strip())
            out.append("")
            continue
        s = re.sub(r"\(\(\(.*?\)\)\)", "", s)        # AsciiDoc index terms
        if not s.strip() and line.strip():           # line was only index terms
            continue
        s = re.sub(r"\[\[[^\]]*\]\]", "", s)
        s = re.sub(r"<<[^,>]*,([^>]*)>>", r"\1", s)
        s = re.sub(r"<<([^>]*)>>", r"\1", s)
        s = re.sub(r"(https?://\S+?)\[([^\]]*)\]", r"\2 (\1)", s)
        s = re.sub(r"link:[^\[]*\[([^\]]*)\]", r"\1", s)
        s = re.sub(r"(?<![\w*])\*\*?([^*\n]+?)\*\*?(?![\w*])", r"\1", s)
        s = re.sub(r"(?<![\w_])_([^_\n]+?)_(?![\w_])", r"\1", s)
        s = s.replace("`", "")
        s = re.sub(r"^\*+\s+", "- ", s)
        s = re.sub(r"^\.\s+", "- ", s)
        s = re.sub(r"^\.([A-Za-z])", r"\1", s)   # block titles
        out.append(s)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main():
    clone()
    DOCS.mkdir(parents=True, exist_ok=True)
    for f in DOCS.glob("*.txt"):
        f.unlink()
    n = 0
    for ch in CHAPTERS:
        for f in sorted((CLONE / "book" / ch / "sections").glob("*.asc")):
            t = clean_asciidoc(f.read_text(encoding="utf-8"))
            (DOCS / f"{ch[:2]}_{f.stem}.txt").write_text(t, encoding="utf-8")
            n += 1
    words = sum(len(p.read_text().split()) for p in DOCS.glob("*.txt"))
    print(f"wrote {n} documents, {words} words -> {DOCS}")


if __name__ == "__main__":
    sys.exit(main())

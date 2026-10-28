"""Every source file must parse under the oldest Python the project claims to support.

This exists because of a real failure: `f"{row[f"key"]}"` nests the same quote character inside
an f-string, which PEP 701 made legal in Python 3.12 but is a SyntaxError on 3.11. The sandbox the
project was developed in runs 3.13, so it imported fine there and only broke in CI, at import time,
which took the whole test suite down with it. A syntax error cannot be caught by a test that has to
import the module first, so this parses the files as data instead.
"""
import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
MIN_VERSION = (3, 11)       # keep in step with .github/workflows/ci.yml

SOURCES = sorted(
    p for p in ROOT.rglob("*.py")
    if not any(part in {".git", "__pycache__", ".venv", "venv", ".pytest_cache"} for part in p.parts)
)


def test_sources_were_found():
    assert len(SOURCES) > 10, "source discovery is broken; this test would pass vacuously"


@pytest.mark.parametrize("path", SOURCES, ids=lambda p: str(p.relative_to(ROOT)))
def test_parses_on_oldest_supported_python(path):
    source = path.read_text(encoding="utf-8")
    try:
        ast.parse(source, filename=str(path), feature_version=MIN_VERSION)
    except SyntaxError as err:                      # pragma: no cover - the failure message is the point
        pytest.fail(f"{path.relative_to(ROOT)}:{err.lineno} is not valid on Python "
                    f"{MIN_VERSION[0]}.{MIN_VERSION[1]}: {err.msg}")

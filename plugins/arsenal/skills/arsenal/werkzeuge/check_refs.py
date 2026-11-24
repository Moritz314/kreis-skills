#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Arsenal reference check: no outside-skill pointers, no dead links, replacement table complete.

Three checks, all must be green (exit code 0), otherwise exit code 1:
  (i)   The names of the former outside skills ("impeccable", "frontend-design")
        appear nowhere in the skill folder except on lines that contain "Quelle:".
  (ii)  Every relative Markdown link and every ${SKILL_PATH}/... path in the
        skill folder points to an existing file or folder.
  (iii) Every row of the replacement table (verweise-v2.md) has at least one
        existing target path, and the row count equals the "Anzahl Treffer"
        line of the table.

Usage:
  uv run werkzeuge/check_refs.py [--table PATH]
Die Ersetzungstabelle (iii) ist optional: nur mit --table PATH.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent          # skills/arsenal
ROOT = SKILL.parent                                     # skills (nur für die Anzeige der Pfade)

# Folders and suffixes that hold no text we check (data dumps, images, indexes).
SKIP_PARTS = {"gallery", "techdb", "images", "node_modules", ".git", "__pycache__"}
TEXT_SUFFIX = {".md", ".js", ".py", ".html", ".yaml", ".yml", ".txt", ".json", ".svg", ".css"}

# Files that a workflow creates at run time; they need not exist in the repository.
RUNTIME_CREATED: set[str] = set()

NAMES = re.compile(r"impeccable|frontend-design", re.I)
MD_LINK = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKILL_PATH = re.compile(r"\$\{SKILL_PATH\}/([^\s`'\"),\]}]+)")


def text_files() -> list[Path]:
    """All text files of the skill folder that are worth checking."""
    out = []
    for p in sorted(SKILL.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIX:
            continue
        if SKIP_PARTS & set(p.relative_to(SKILL).parts):
            continue
        if p.stat().st_size > 3_000_000 or p.name == "check_refs.py":
            continue
        out.append(p)
    return out


def check_names(files: list[Path]) -> list[str]:
    """(i) outside skill names only on 'Quelle:' lines (HERKUNFT.md ist die Herkunftsliste und ausgenommen)."""
    bad = []
    for p in files:
        if p.name == "HERKUNFT.md":
            continue
        for n, line in enumerate(p.read_text("utf-8", "ignore").splitlines(), 1):
            if NAMES.search(line) and "Quelle:" not in line:
                bad.append(f"{p.relative_to(ROOT)}:{n}: {line.strip()[:120]}")
    return bad


def check_links(files: list[Path]) -> list[str]:
    """(ii) relative Markdown links and ${SKILL_PATH} paths exist."""
    bad = []
    for p in files:
        for n, line in enumerate(p.read_text("utf-8", "ignore").splitlines(), 1):
            if p.suffix == ".md":
                for m in MD_LINK.finditer(line):
                    t = m.group(1)
                    if re.match(r"(https?:|mailto:|#|tel:)", t) or "<" in t:
                        continue
                    t = t.split("#")[0]
                    if t and not (p.parent / t).exists():
                        bad.append(f"{p.relative_to(ROOT)}:{n}: dead link {m.group(1)}")
            for m in SKILL_PATH.finditer(line):
                t = m.group(1).rstrip(".,;:")
                if "<" in t or "*" in t or "$" in t or t in RUNTIME_CREATED:
                    continue
                if not (SKILL / t).exists():
                    bad.append(f"{p.relative_to(ROOT)}:{n}: dead SKILL_PATH {t}")
    return bad


def check_table(path: Path) -> list[str]:
    """(iii) each table row has an existing target; row count matches the stated hit count."""
    if not path.exists():
        return [f"table missing: {path}"]
    text = path.read_text("utf-8")
    m = re.search(r"Anzahl Treffer:\s*(\d+)", text)
    if not m:
        return ["table has no line 'Anzahl Treffer: <n>'"]
    expected = int(m.group(1))
    bad, rows = [], 0
    for n, line in enumerate(text.splitlines(), 1):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.startswith("|") or not re.fullmatch(r"\d+", cells[0] if cells else ""):
            continue
        rows += 1
        # target column = 5th cell (nr | old | pointed to | decision | new target | size)
        target = cells[4] if len(cells) > 4 else ""
        paths = re.findall(r"`([^`]+)`", target)
        ok = False
        for t in paths:
            t = t.split("#")[0].split(" ")[0]
            if t and ((ROOT / t).exists() or (SKILL / t).exists()):
                ok = True
        if not ok:
            bad.append(f"{path.name}:{n}: no existing target in '{target[:80]}'")
    if rows != expected:
        bad.append(f"row count {rows} != Anzahl Treffer {expected}")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--table", type=Path, default=None)
    a = ap.parse_args()
    files = text_files()
    results = {"(i) outside names": check_names(files), "(ii) links and paths": check_links(files)}
    if a.table:
        results["(iii) replacement table"] = check_table(a.table)
    fail = 0
    for name, bad in results.items():
        print(f"{name}: {'OK' if not bad else str(len(bad)) + ' problems'} ({len(files)} files)")
        for b in bad[:40]:
            print("   ", b)
        fail += bool(bad)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())

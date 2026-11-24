#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Arsenal website check: the three delivery rules of a website, read from the source.

Usage:
  website_check.py <page.html | folder>... [--konzept KONZEPT.md] [--json]

Checks (Auslieferungsregeln der Website, Verfahren in regeln/website-idee.md):
  platzhalter  stand-in words, digit dummies and bracketed gaps in visible text and link targets (W3)
  schrift      every family that leads a font stack is shipped: @font-face with a data: source or an existing file (W5)
  abdeckung    with --konzept: every line of "## Auftragsabdeckung" names a section id or heading that exists (W1)
  idee         with --konzept: "## Tragende Idee" with the line "Proben:" (Tausch, Kulisse, Erstgriff, Nutzen),
               "## Annahmen" present (W6)

An element marked data-entwurf (the one draft sentence in the footer) is skipped by "platzhalter" and reported as a note.
Stufe "muss" blocks delivery, "pruefen" is a prompt to look. Reads source only: it cannot see whether a font renders.
Exit: 0 no finding, 1 at least one "muss", 2 file unreadable, 3 only "pruefen".
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

GENERIC = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "ui-serif", "ui-sans-serif",
           "ui-monospace", "ui-rounded", "math", "emoji", "fangsong", "-apple-system", "blinkmacsystemfont"}
KEYWORD = {"inherit", "initial", "unset", "revert", "revert-layer"}
OS_ONLY = {
    "bahnschrift": "Windows", "segoe ui": "Windows", "calibri": "Windows", "cambria": "Windows", "candara": "Windows",
    "consolas": "Windows", "corbel": "Windows", "constantia": "Windows", "franklin gothic medium": "Windows",
    "tahoma": "Windows", "impact": "Windows and macOS", "arial black": "Windows and macOS",
    "georgia": "Windows and macOS", "verdana": "Windows and macOS", "trebuchet ms": "Windows and macOS",
    "helvetica neue": "Apple", "helvetica": "Apple", "sf pro": "Apple", "sf pro text": "Apple",
    "sf pro display": "Apple", "avenir": "Apple", "avenir next": "Apple", "futura": "Apple", "gill sans": "Apple",
    "optima": "Apple", "palatino": "Apple", "didot": "Apple", "baskerville": "Apple", "menlo": "Apple",
    "monaco": "Apple", "din alternate": "Apple", "din condensed": "Apple", "roboto": "Android",
    "ubuntu": "Linux", "cantarell": "Linux",
}

# (level, label, pattern). Matched against visible text and link targets, never against code.
STANDINS = [
    ("muss", "stand-in compound", re.compile(r"\bBeispiel(?!sweise|haft)[a-zäöüß]{3,}\w*")),
    ("muss", "stand-in name", re.compile(r"\b(?:Max|Erika|Anna|Hans|Herr|Frau|Inhaber(?:in)?|Familie)\s+(?:Beispiel|Muster|Mustermann|Musterfrau|Test|Tester)\b")),
    ("muss", "stand-in compound", re.compile(r"\bMuster(?:mann|frau|firma|straße|strasse|stadt|weg|gasse|platz|name|text|adresse|hausen|dorf)\w*", re.I)),
    ("muss", "stand-in name", re.compile(r"\b(?:John|Jane) Doe\b|\bfoo ?bar\b|\bAcme (?:Inc|Corp|GmbH|Ltd)\b", re.I)),
    ("muss", "filler text", re.compile(r"\blorem ipsum\b|\bdolor sit amet\b", re.I)),
    ("muss", "stand-in word", re.compile(r"\bPlatzhalter\w*|\bplaceholder\b|\bBlindtext\w*", re.I)),
    ("muss", "open marker", re.compile(r"\b(?:TODO|TBD|FIXME)\b|\bx{3,}\b|\?{3,}")),
    ("muss", "bracketed gap", re.compile(r"\[[^\]\n]{0,40}(?:folgt|einfügen|einsetzen|insert|hier|here|todo|tbd|name|text|\.\.\.|…)[^\]\n]{0,40}\]", re.I)),
    ("muss", "stand-in phrase", re.compile(r"\b(?:Ihr|Dein|Your) (?:Text|Firmenname|Company|Logo)(?: hier| here)?\b|\bYour Name Here\b|\bHier steht (?:Ihr|dein|ein)\b|\bCompany Name\b", re.I)),
    ("muss", "digit dummy", re.compile(r"(?<![\d.,])(?<!\d )(?:0{3}[ .\-/]?){2,}0*(?![\d.,])|(?<!\d)0{5,}(?!\d)|\b123 ?456(?: ?789)?\b|\b0123[ /\-]?456\b")),
    ("muss", "stand-in domain", re.compile(r"@(?:test|beispiel|muster\w*|domain|email|mail|firma|example)\.(?:de|at|ch)\b|\.(?:beispiel|test|invalid|localhost)\b", re.I)),
    ("pruefen", "possible stand-in", re.compile(r"\((?:Beispiel|Muster|Demo|Test)\)|\bDemo(?:daten|firma|kunde)\w*|\bTest(?:firma|kunde|eintrag)\w*")),
]
RESERVED_MAIL = re.compile(r"[\w.+-]+@[\w.-]+\.example(?:\.(?:com|org|net))?\b|[\w.+-]+@example\.(?:com|org|net)\b", re.I)

FONT_FACE = re.compile(r"@font-face\s*\{([^}]*)\}", re.I | re.S)
DATA_URI = re.compile(r"url\(\s*['\"]?data:[^)]*\)", re.I)
SIZE = r"(?:\d*\.?\d+(?:px|rem|em|%|vw|vh|pt|ch)|clamp\([^;{}]*?\)|calc\([^;{}]*?\)|var\([^)]*\))"


def read(p: Path) -> str:
    return p.read_text("utf-8", "ignore")


def collect(paths: list[Path]) -> tuple[list[Path], list[Path]]:
    """HTML pages and stylesheets under the given files and folders."""
    pages, sheets = [], []
    for p in paths:
        if p.is_dir():
            for q in sorted(p.rglob("*")):
                if {"node_modules", ".git", "dist", "build"} & set(q.parts):
                    continue
                if q.suffix.lower() in (".html", ".htm"):
                    pages.append(q)
                elif q.suffix.lower() == ".css":
                    sheets.append(q)
        elif p.suffix.lower() == ".css":
            sheets.append(p)
        else:
            pages.append(p)
    return pages, sheets


def visible(html: str) -> tuple[str, int]:
    """Visible text plus the attribute values a visitor meets. Returns (text, number of data-entwurf elements)."""
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    html = re.sub(r"<(script|style|template)\b.*?</\1\s*>", " ", html, flags=re.S | re.I)
    html, drafts = re.subn(r"<(\w+)\b[^>]*\bdata-entwurf\b[^>]*>.*?</\1\s*>", " ", html, flags=re.S | re.I)
    attrs = re.findall(r"\b(?:alt|title|aria-label|placeholder|content|href|value)\s*=\s*\"([^\"]*)\"", html, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text + " " + " ".join(attrs)), drafts


def check_standins(page: Path, html: str) -> tuple[list[dict], list[str]]:
    text, drafts = visible(html)
    notes = []
    if drafts:
        notes.append(f"{page.name}: {drafts} element(s) marked data-entwurf, remove before launch")
    reserved = sorted(set(RESERVED_MAIL.findall(text)))
    if reserved:
        notes.append(f"{page.name}: mail on a reserved domain ({', '.join(reserved[:3])}), replace before launch")
    text = RESERVED_MAIL.sub(" ", text)
    found, seen = [], set()
    for level, label, rx in STANDINS:
        for m in rx.finditer(text):
            hit = m.group(0).strip()
            if (label, hit.lower()) in seen:
                continue
            seen.add((label, hit.lower()))
            around = text[max(0, m.start() - 30):m.end() + 30].strip()
            found.append({"art": "platzhalter", "stufe": level, "ort": page.name, "befund": f"{label}: \"{hit}\" in \"{around}\""})
    return found, notes


def families(value: str) -> list[str]:
    return [f.strip().strip("'\"") for f in value.split(",") if f.strip()]


def check_fonts(page: Path, html: str, sheets: list[Path]) -> list[dict]:
    css_parts = [(page, c) for c in re.findall(r"<style\b[^>]*>(.*?)</style\s*>", html, flags=re.S | re.I)]
    css_parts += [(page, c) for c in re.findall(r"\bstyle\s*=\s*\"([^\"]*)\"", html, flags=re.I)]
    found = []
    for href in re.findall(r"<link\b[^>]*\bhref\s*=\s*\"([^\"]+)\"", html, flags=re.I):
        if re.match(r"https?://(?:fonts\.googleapis|fonts\.gstatic|use\.typekit|fonts\.bunny|api\.fontshare)", href, re.I):
            found.append({"art": "schrift", "stufe": "muss", "ort": page.name, "befund": f"font loaded from a foreign host: {href[:80]}"})
        elif href.lower().split("?")[0].endswith(".css") and not re.match(r"(https?:)?//", href):
            q = (page.parent / href.split("?")[0]).resolve()
            if q.exists() and q not in [s.resolve() for s in sheets]:
                css_parts.append((q, read(q)))
    css_parts += [(s, read(s)) for s in sheets]

    shipped, variables, stacks = {}, {}, []
    for origin, css in css_parts:
        css = re.sub(r"/\*.*?\*/", " ", css, flags=re.S)
        for block in FONT_FACE.findall(css):
            fam = re.search(r"font-family\s*:\s*([^;]+)", block, re.I)
            if not fam:
                continue
            name = families(fam.group(1))[0].lower()
            if DATA_URI.search(block):
                shipped[name] = "embedded"
                continue
            urls = re.findall(r"url\(\s*['\"]?([^'\")]+)", block)
            local = [u for u in urls if not re.match(r"(https?:)?//", u)]
            if any((origin.parent / u.split("?")[0].split("#")[0]).exists() for u in local):
                shipped[name] = "file"
            elif urls and not local:
                shipped.setdefault(name, "foreign host")
            else:
                shipped.setdefault(name, "file missing")
        css = FONT_FACE.sub(" ", css)
        css = DATA_URI.sub("url(data:)", css)
        for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;{}]+)", css):
            variables[name] = value.strip()
        for value in re.findall(r"(?<![\w-])font-family\s*:\s*([^;{}]+)", css, flags=re.I):
            stacks.append(value.strip())
        for value in re.findall(r"(?<![\w-])font\s*:\s*([^;{}]+)", css, flags=re.I):
            m = re.search(SIZE + r"(?:\s*/\s*[^\s,]+)?\s+([^;{}]+)$", value.strip())
            if m:
                stacks.append(m.group(1).strip())

    seen = set()
    for stack in stacks:
        for _ in range(4):                                   # resolve var(--x) at the head of the stack
            m = re.match(r"var\(\s*(--[\w-]+)\s*(?:,[^)]*)?\)\s*(.*)$", stack, flags=re.S)
            if not m or m.group(1) not in variables:
                break
            stack = variables[m.group(1)] + m.group(2)
        fams = families(stack)
        if not fams or fams[0].lower() in KEYWORD or fams[0].startswith("var(") or fams[0].lower() in seen:
            continue
        head = fams[0].lower()
        seen.add(head)
        if head in GENERIC:
            found.append({"art": "schrift", "stufe": "pruefen", "ort": page.name,
                          "befund": f"stack starts with the system family \"{fams[0]}\": allowed only as the stated equivalent substitute (## Annahmen lists the member per platform)"})
        elif shipped.get(head) in ("embedded", "file"):
            continue
        elif shipped.get(head) == "foreign host":
            found.append({"art": "schrift", "stufe": "muss", "ort": page.name, "befund": f"\"{fams[0]}\" is loaded from a foreign host, ship the file with the page"})
        elif shipped.get(head) == "file missing":
            found.append({"art": "schrift", "stufe": "muss", "ort": page.name, "befund": f"\"{fams[0]}\" has an @font-face, but its file is not there"})
        else:
            where = OS_ONLY.get(head)
            why = f"exists only on {where}" if where else "is named but not shipped (no @font-face)"
            found.append({"art": "schrift", "stufe": "muss", "ort": page.name, "befund": f"\"{fams[0]}\" leads a font stack and {why}"})
    return found


def section(md: str, title: str) -> str | None:
    m = re.search(r"^##\s+" + re.escape(title) + r"\s*$(.*?)(?=^##\s|\Z)", md, flags=re.M | re.S | re.I)
    return m.group(1) if m else None


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip().lower()


def check_konzept(konzept: Path, pages: list[tuple[Path, str]]) -> list[dict]:
    md, found, ort = read(konzept), [], konzept.name
    ids, heads = set(), []
    for _, html in pages:
        ids |= {i.lower() for i in re.findall(r"\bid\s*=\s*\"([^\"]+)\"", html, flags=re.I)}
        heads += [norm(h) for h in re.findall(r"<h[1-4]\b[^>]*>(.*?)</h[1-4]\s*>", html, flags=re.S | re.I)]
    cover = section(md, "Auftragsabdeckung")
    lines = [l.strip() for l in (cover or "").splitlines() if l.strip().startswith("-")]
    if not lines:
        found.append({"art": "abdeckung", "stufe": "muss", "ort": ort, "befund": "section \"## Auftragsabdeckung\" is missing or has no line"})
    for line in lines:
        parts = re.split(r"\s*(?:->|→)\s*", line.lstrip("- ").strip(), maxsplit=1)
        if len(parts) < 2 or not parts[1].strip():
            found.append({"art": "abdeckung", "stufe": "muss", "ort": ort, "befund": f"line names no section: \"{line[:80]}\""})
            continue
        target = parts[1].strip().strip("`\"")
        ok = target.lstrip("#").lower() in ids if target.startswith("#") else any(norm(target) in h for h in heads)
        if not ok:
            found.append({"art": "abdeckung", "stufe": "muss", "ort": ort, "befund": f"\"{parts[0][:50]}\" has no section \"{target[:60]}\" in the page"})
    idea = section(md, "Tragende Idee")
    if idea is None or not idea.strip():
        found.append({"art": "idee", "stufe": "muss", "ort": ort, "befund": "section \"## Tragende Idee\" is missing or empty"})
    else:
        proben = re.search(r"^\s*Proben:(.*)$", idea, flags=re.M)
        missing = [w for w in ("Tausch", "Kulisse", "Erstgriff", "Nutzen") if not proben or w.lower() not in proben.group(1).lower()]
        if missing:
            found.append({"art": "idee", "stufe": "muss", "ort": ort, "befund": "line \"Proben:\" lacks " + ", ".join(missing)})
        if re.search(r"\b(?:Die Seite ist|The page is)\b", idea):
            found.append({"art": "idee", "stufe": "pruefen", "ort": ort, "befund": "\"The page is ...\" names a look: say what the visitor does"})
    if section(md, "Annahmen") is None:
        found.append({"art": "idee", "stufe": "muss", "ort": ort, "befund": "section \"## Annahmen\" is missing (write \"keine\" when nothing was assumed)"})
    if not re.search(r"^\s*-?\s*Arsenal-Reflex:", md, flags=re.M):
        found.append({"art": "idee", "stufe": "pruefen", "ort": ort, "befund": "line \"Arsenal-Reflex:\" is missing"})
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--konzept", type=Path)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    missing = [str(p) for p in a.paths + ([a.konzept] if a.konzept else []) if not p.exists()]
    pages, sheets = collect([p for p in a.paths if p.exists()])
    if missing or not pages:
        print("unreadable: " + (", ".join(missing) or "no HTML page found"), file=sys.stderr)
        return 2
    found, notes, loaded = [], [], []
    for page in pages:
        html = read(page)
        loaded.append((page, html))
        f, n = check_standins(page, html)
        found += f + check_fonts(page, html, sheets)
        notes += n
    if a.konzept:
        found += check_konzept(a.konzept, loaded)
    muss = [f for f in found if f["stufe"] == "muss"]
    if a.json:
        print(json.dumps({"ok": not muss, "seiten": [p.name for p in pages], "funde": found, "hinweise": notes}, ensure_ascii=False, indent=1))
    else:
        for f in found:
            print(f"{f['stufe']:8} {f['art']:12} {f['ort']}: {f['befund']}")
        for n in notes:
            print(f"hinweis  {n}")
        print(f"{len(pages)} page(s): {len(muss)} muss, {len(found) - len(muss)} pruefen")
    return 1 if muss else (3 if found else 0)


if __name__ == "__main__":
    sys.exit(main())

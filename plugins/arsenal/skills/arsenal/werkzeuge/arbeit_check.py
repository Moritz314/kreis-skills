#!/usr/bin/env python3
"""Arsenal work check: ARBEIT.md (work analysis) and durchgang.json (work walkthrough of a software surface).

Usage:
  arbeit_check.py ARBEIT.md [--json]
  arbeit_check.py ARBEIT.md --durchgang durchgang.json [--alle] [--json]
  arbeit_check.py --durchgang durchgang.json [--json]     no budget: form and recount only

ARBEIT.md (art "form"): abschnitt, platzhalter, groesse, szene, aufgaben, budget, vorgaben, kern, daten, annahmen.
durchgang.json: form, zaehlung (sums are recomputed from the protocol), proben, urteil (art "form": the walkthrough
report is wrong, the checker repeats it) and budget, fehlt (art "arbeit": the surface fails, the design is reworked).
--alle demands every core task of ARBEIT.md in the walkthrough (built state); without it only K1 (draft).

Output: text lines, or with --json one object: ok, funde [{art, kennung, ort, befund}], warnungen, kernaufgaben
[{id, name, pflicht, heute, budget, handwechsel}], annahmen, bytes, kurzteil_bytes, durchgang.
Exit: 0 no finding, 1 findings, 2 file unreadable, 3 nothing wrong but the walkthrough says "ungeprueft".
Standard library only.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SECTIONS = ["Szene", "Budget", "Aufbau-Vorgaben", "Aufgaben", "Kernaufgaben heute", "Daten und Mengen",
            "Annahmen und offene Fragen"]
MAX_BYTES, MAX_KURZ = 3072, 1536            # whole file; the first three sections (read by variants, build and critique)
VAGE = re.compile(r"\b(modern\w*|übersichtlich\w*|intuitiv\w*|benutzerfreundlich\w*|ansprechend\w*|aufgeräumt\w*|clean|"
                  r"schlank\w*|einfach zu bedienen)\b", re.I)
PROBEN = ["wiederholung", "neuladen", "falscheingabe", "zerstoerung", "zustaende", "sammelaktion"]
ERGEBNIS = {"bestanden", "durchgefallen", "entfaellt", "ungeprueft"}
URTEIL = {"freigabe", "nacharbeit", "verwerfen", "ungeprueft"}
EINGABE = {"tastatur", "zeiger", "touch"}
ZAHL = re.compile(r"\d[\d.]*")


def split_sections(text: str) -> dict:
    """Body per '## heading', in file order."""
    parts = re.split(r"(?m)^##[ \t]+(.+?)[ \t]*$", text)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def table(body: str) -> list:
    """Rows of the first Markdown table as cell lists, header first, separator dropped."""
    out = []
    for ln in body.splitlines():
        if ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                out.append(cells)
    return out


def bullets(body: str) -> list:
    return [m.group(1).strip() for m in re.finditer(r"(?m)^[-*][ \t]+(.+)$", body)]


def zahl(cell: str):
    m = ZAHL.search(cell or "")
    return int(m.group(0).replace(".", "")) if m else None


def check_arbeit(text: str) -> dict:
    """Findings and the parsed core tasks of one ARBEIT.md."""
    funde, warn, kern = [], [], []
    add = lambda k, ort, befund: funde.append({"art": "form", "kennung": k, "ort": ort, "befund": befund})  # noqa: E731
    sec = split_sections(text)
    names = [n for n in sec if n in SECTIONS]
    for n in SECTIONS:
        if n not in sec:
            add("abschnitt", n, "Abschnitt fehlt")
    if names != [n for n in SECTIONS if n in sec]:
        add("abschnitt", "Reihenfolge", "Abschnitte stehen nicht in der Reihenfolge der Vorlage")
    for m in re.finditer(r"<[A-Za-zÄÖÜäöü][^>\n]*>|\[TODO\]", text):
        add("platzhalter", m.group(0)[:40], "Platzhalter der Vorlage steht noch da")
    size = len(text.encode("utf-8"))
    kurz = sum(len(("## " + n + "\n" + sec[n]).encode("utf-8")) for n in SECTIONS[:3] if n in sec)
    if size > MAX_BYTES:
        add("groesse", "Datei", f"{size} Bytes, erlaubt {MAX_BYTES}")
    if kurz > MAX_KURZ:
        add("groesse", "Kurzteil", f"Szene, Budget und Aufbau-Vorgaben haben {kurz} Bytes, erlaubt {MAX_KURZ}")

    rollen = bullets(sec.get("Szene", ""))
    if "Szene" in sec and not rollen:
        add("szene", "Szene", "keine Rolle (eine Zeile je Rolle)")
    for i, b in enumerate(rollen, 1):
        if not re.search(r"\d{3,4}\s*px", b):
            add("szene", f"Szene Zeile {i}", "Bildschirmbreite in px fehlt")
        if not re.search(r"Tastatur|Maus|Zeiger|Touch|Hand|Stift", b):
            add("szene", f"Szene Zeile {i}", "Eingabe fehlt (Tastatur, Maus, Touch, eine freie Hand)")
        if not re.search(r"\d+\s*(Stunden?\b|h\b|Minuten am Tag)", b):
            add("szene", f"Szene Zeile {i}", "Dauer am Tag als Zahl fehlt (zum Beispiel 8 Stunden oder 20 Minuten am Tag)")

    rows = table(sec.get("Aufgaben", ""))[1:]
    if "Aufgaben" in sec and not 3 <= len(rows) <= 7:
        add("aufgaben", "Aufgaben", f"{len(rows)} Zeilen, verlangt sind 3 bis 7")
    feste = 0
    for i, r in enumerate(rows, 1):
        ort = f"Aufgaben Zeile {i}"
        if len(r) != 9 or any(not c for c in r):
            add("aufgaben", ort, "neun gefüllte Spalten verlangt")
            continue
        if zahl(r[3]) is None or not re.search(r"je (Stunde|Tag|Woche|Monat|Jahr)", r[3]):
            add("aufgaben", ort, "Häufigkeit braucht eine Zahl je Tag, Woche oder Monat")
        for c, name in ((r[4], "Schritte heute"), (r[5], "Dauer heute")):
            if zahl(c) is None and "neu" not in c.lower():
                add("aufgaben", ort, f"{name} braucht eine Zahl oder 'neu'")
        if len(ZAHL.findall(r[7])) < 2:
            add("aufgaben", ort, "Menge braucht zwei Zahlen: üblich und höchstens")
        feste += sum("Annahme:" not in c for c in (r[3], r[7]))
    if rows and not feste:
        warn.append("alle Häufigkeiten und Mengen sind Annahmen: beim Auftraggeber oder am Bestand belegen")

    for i, r in enumerate(table(sec.get("Budget", ""))[1:], 1):
        ort = f"Budget Zeile {i}"
        m = re.match(r"(K\d)\s+(.+)", r[0]) if r else None
        if not m or len(r) != 5:
            add("budget", ort, "Zeile beginnt mit K1, K2 oder K3 und einem Namen und hat fünf Spalten")
            continue
        pflicht, heute, budget, hand = zahl(r[1]), zahl(r[2]), zahl(r[3]), zahl(r[4])
        if None in (pflicht, budget, hand) or (heute is None and "neu" not in r[2].lower()):
            add("budget", ort, "Pflichteingaben, Schritte heute (oder 'neu'), Schrittbudget und Handwechsel als Zahl")
            continue
        if m.group(1) != f"K{len(kern) + 1}":
            add("budget", ort, f"Kennung {m.group(1)}, erwartet K{len(kern) + 1}")
        if budget > pflicht + 4:
            add("budget", ort, f"Schrittbudget {budget} über Pflichteingaben plus 4 ({pflicht + 4})")
        if heute is not None and budget > heute:
            add("budget", ort, f"Schrittbudget {budget} über den Schritten heute ({heute})")
        if budget < min(pflicht + 2, heute if heute is not None else pflicht + 2):
            add("budget", ort, f"Schrittbudget {budget} unter der Untergrenze (Pflichteingaben plus 2)")
        kern.append({"id": m.group(1), "name": m.group(2), "pflicht": pflicht, "heute": heute, "budget": budget,
                     "handwechsel": hand})
    if "Budget" in sec and not 1 <= len(kern) <= 3:
        add("budget", "Budget", f"{len(kern)} gültige Kernaufgaben, verlangt sind 1 bis 3")

    vorgaben = [b for b in bullets(sec.get("Aufbau-Vorgaben", "")) if re.match(r"A\d+\b", b)]
    if "Aufbau-Vorgaben" in sec and len(vorgaben) < 3:
        add("vorgaben", "Aufbau-Vorgaben", f"{len(vorgaben)} Vorgaben, verlangt sind mindestens 3 (A1, A2, A3)")
    for i, b in enumerate(vorgaben, 1):
        if not b.startswith(f"A{i} "):
            add("vorgaben", b[:30], f"Nummer nicht fortlaufend, erwartet A{i}")
        if "(aus " not in b:
            add("vorgaben", f"A{i}", "Herkunft fehlt: (aus K1, Aufgabe oder Szene)")
        if VAGE.search(b):
            add("vorgaben", f"A{i}", f"nicht prüfbar: '{VAGE.search(b).group(0)}'; nenne Form, Ort oder Zahl")

    heute_body = sec.get("Kernaufgaben heute", "")
    blocks = re.split(r"(?m)^###[ \t]+", heute_body)[1:]
    for k in kern:
        block = next((b for b in blocks if b.startswith(k["id"])), None)
        if block is None:
            add("kern", k["id"], "Block '### " + k["id"] + " ...' fehlt unter Kernaufgaben heute")
            continue
        steps = len(re.findall(r"(?m)^\d+\.[ \t]+\S", block))
        if k["heute"] is not None and steps != k["heute"]:
            add("kern", k["id"], f"Ablauf nennt {steps} Schritte, die Budgettabelle {k['heute']}: zählen, nicht schätzen")
        if not re.search(r"(?m)^Teuerste Stelle:[ \t]*\S.{9,}", block):
            add("kern", k["id"], "Zeile 'Teuerste Stelle:' mit Schritt, Grund und Beleg fehlt")

    daten = bullets(sec.get("Daten und Mengen", ""))
    if "Daten und Mengen" in sec and not daten:
        add("daten", "Daten und Mengen", "kein Datenobjekt")
    for i, b in enumerate(daten, 1):
        if not re.search(r"längster Wert", b, re.I) or zahl(b.split("ängster Wert", 1)[-1]) is None:
            add("daten", f"Daten Zeile {i}", "längster Wert mit Zeichenzahl fehlt")

    last = SECTIONS[-1]
    annahmen = text.count("Annahme:")
    if last in sec and annahmen - sec[last].count("Annahme:") > 0 and not bullets(sec[last]):
        add("annahmen", last, "Annahmen stehen im Text, aber nicht in der Liste am Ende")
    return {"funde": funde, "warnungen": warn, "kernaufgaben": kern, "annahmen": annahmen, "bytes": size, "kurzteil_bytes": kurz}


def recount(protokoll: list) -> dict:
    """Sums that follow from the protocol lines."""
    hand = blick = 0
    for a, b in zip(protokoll, protokoll[1:]):
        hand += {a.get("eingabe"), b.get("eingabe")} == {"tastatur", "zeiger"}
        blick += a.get("bereich") != b.get("bereich")
    return {"schritte": len(protokoll), "handwechsel": hand, "blickwechsel": blick,
            "wartepunkte": sum(bool(p.get("warten")) for p in protokoll),
            "fehlgriffe": sum(bool(p.get("fehlgriff")) for p in protokoll)}


def check_durchgang(d, kern: list, alle: bool) -> dict:
    """Findings of one durchgang.json against the budgets of ARBEIT.md (kern may be empty)."""
    funde = []
    add = lambda art, k, ort, befund: funde.append({"art": art, "kennung": k, "ort": ort, "befund": befund})  # noqa: E731
    if not isinstance(d, dict) or d.get("urteil") not in URTEIL or not isinstance(d.get("aufgaben"), list) \
            or not isinstance(d.get("proben"), list) or not isinstance(d.get("befunde"), list) or not d.get("richtung"):
        add("form", "form", "durchgang.json", "richtung, urteil, aufgaben, proben, befunde nach werkzeuge/vorlagen/durchgang.schema.json")
        return {"funde": funde, "urteil": d.get("urteil") if isinstance(d, dict) else None, "aufgaben": []}
    urteil, kurz, budgets = d["urteil"], [], {k["id"]: k for k in kern}
    for a in d["aufgaben"]:
        name = str(a.get("aufgabe", "?")) if isinstance(a, dict) else "?"
        prot = a.get("protokoll") if isinstance(a, dict) else None
        if not isinstance(prot, list) or not prot or any(
                not isinstance(p, dict) or p.get("eingabe") not in EINGABE or not p.get("handlung") or not p.get("bereich")
                or "rueckmeldung" not in p for p in prot):
            add("form", "form", name, "Protokoll fehlt oder eine Zeile ohne handlung, eingabe (tastatur, zeiger, touch), bereich, rueckmeldung")
            continue
        soll = recount(prot)
        for key, val in soll.items():
            if a.get(key) != val:
                add("form", "zaehlung", name, f"{key} gemeldet {a.get(key)}, aus dem Protokoll folgt {val}")
        k = budgets.get(name.split()[0])
        budget = k["budget"] if k else a.get("budget")
        if k and a.get("budget") != k["budget"]:
            add("form", "zaehlung", name, f"budget gemeldet {a.get('budget')}, ARBEIT.md nennt {k['budget']}")
        ok = None
        if isinstance(budget, int):
            ok = soll["schritte"] <= budget and (not k or soll["handwechsel"] <= k["handwechsel"])
            if soll["schritte"] > budget:
                add("arbeit", "budget", name, f"{soll['schritte']} Schritte, Budget {budget}: Aufbau ändern, nicht das Budget")
            if k and soll["handwechsel"] > k["handwechsel"]:
                add("arbeit", "budget", name, f"{soll['handwechsel']} Handwechsel, erlaubt {k['handwechsel']}")
            if a.get("bestanden") is not ok:
                add("form", "zaehlung", name, f"bestanden gemeldet {a.get('bestanden')}, aus den Zahlen folgt {ok}")
        kurz.append({"aufgabe": name, "budget": budget, **soll, "bestanden": ok})
    da = {x["aufgabe"].split()[0] for x in kurz}
    if urteil != "ungeprueft":
        for k in kern[: None if alle else 1]:
            if k["id"] not in da:
                add("arbeit", "fehlt", k["id"], "Kernaufgabe wurde nicht durchgespielt")
    proben = {p.get("probe"): p for p in d["proben"] if isinstance(p, dict)}
    for name in PROBEN:
        p = proben.get(name)
        if urteil == "ungeprueft":
            break
        if not p or p.get("ergebnis") not in ERGEBNIS or len(str(p.get("beleg", ""))) < 5:
            add("form", "proben", name, "Probe fehlt oder ohne ergebnis und beleg")
    for i, b in enumerate(d["befunde"], 1):
        if not isinstance(b, dict) or any(not b.get(x) for x in ("stufe", "regel", "ort", "befund", "korrektur")):
            add("form", "form", f"Befund {i}", "stufe, regel, ort, befund, korrektur verlangt")
    durch = [n for n, p in proben.items() if p.get("ergebnis") == "durchgefallen"]
    if len(d["befunde"]) < len(durch):
        add("form", "proben", ", ".join(durch), "jede durchgefallene Probe braucht einen Befund")
    if urteil == "freigabe":
        gruende = [f["ort"] for f in funde if f["art"] == "arbeit"] + durch \
            + [n for n, p in proben.items() if p.get("ergebnis") == "ungeprueft"] \
            + [f"Befund muss: {b.get('ort')}" for b in d["befunde"] if isinstance(b, dict) and b.get("stufe") == "muss"]
        if gruende:
            add("form", "urteil", "urteil", "freigabe trotz: " + "; ".join(dict.fromkeys(str(g) for g in gruende)))
    return {"funde": funde, "urteil": urteil, "aufgaben": kurz}


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Check ARBEIT.md and durchgang.json")
    ap.add_argument("arbeit", nargs="?", help="ARBEIT.md")
    ap.add_argument("--durchgang", help="durchgang.json of one direction")
    ap.add_argument("--alle", action="store_true", help="every core task must be in the walkthrough")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if not a.arbeit and not a.durchgang:
        ap.error("ARBEIT.md oder --durchgang angeben")
    out = {"ok": True, "funde": [], "warnungen": [], "kernaufgaben": [], "annahmen": 0, "bytes": 0, "kurzteil_bytes": 0}
    try:
        if a.arbeit:
            out.update(check_arbeit(Path(a.arbeit).read_text(encoding="utf-8")))
        if a.durchgang:
            d = check_durchgang(json.loads(Path(a.durchgang).read_text(encoding="utf-8")), out["kernaufgaben"], a.alle)
            out["funde"] += d.pop("funde")
            out["durchgang"] = d
    except (OSError, ValueError) as exc:
        print(json.dumps({"ok": False, "fehler": str(exc)}, ensure_ascii=False) if a.json else f"arbeit_check: {exc}")
        return 2
    out["ok"] = not out["funde"]
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for f in out["funde"]:
            print(f"{f['art']} {f['kennung']}: {f['ort']}: {f['befund']}")
        for w in out["warnungen"]:
            print("Warnung:", w)
        for x in out.get("durchgang", {}).get("aufgaben", []):
            print(f"{x['aufgabe']}: {x['schritte']} Schritte (Budget {x['budget']}), {x['handwechsel']} Handwechsel, "
                  f"{x['blickwechsel']} Blickwechsel")
    offen = not out["funde"] and out.get("durchgang", {}).get("urteil") == "ungeprueft"
    if not a.json:
        print("arbeit_check:", "ungeprueft, nichts gemessen" if offen else "OK" if out["ok"] else f"{len(out['funde'])} Funde")
    return 1 if out["funde"] else 3 if offen else 0


if __name__ == "__main__":
    sys.exit(main())

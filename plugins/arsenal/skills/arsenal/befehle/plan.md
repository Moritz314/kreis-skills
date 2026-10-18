# plan (Schritte 1 bis 3)

Legt einen Lauf an: Start, Befund, SOUL und ARMOURY. `plan --bestand` übernimmt ein bestehendes Projekt (früher `register`).

**Aufruf:** `plan [ordner] [brief]`, `plan --bestand [ordner|adresse]`
**Wer:** Leitung und Gestaltung, Opus (Aufwand xhigh); Befund Sonnet.
**Laufordner** `L/` = `<Kundenordner>/webdesign-<JJJJ-MM-TT>/`. Alles eines Laufs liegt dort.

## 1 Start

- Eingabe: Kunde in <internal-project> gewählt (`betrieb_id`), Paket, Stufe, Website-Art, Lauf-Art (`regler.md`). Bei eigenen Vorhaben (Hausseite, plasmind) die Vault-Notiz statt der <internal-project>-Akte.
- Ergebnis: `L/lauf.md` (Kunde, Art, Lauf, Stufe, Budget in Tokens, Termin) und `L/stand.log`. Der Projektordner ist ein Git-Repository: prüfen, sonst anlegen (keine Zugangsdaten im ersten Commit).
- Halt: Kundenlauf ohne <internal-project>-Akte.

## 2 Befund

- Eingabe: <internal-project>-Akte, alte Website (nur lesen), Vault-Notiz, Sync-Ordner des Kunden.
- Ergebnis: `L/befund.md` mit Inventar (8 bis 12 Merkmale, die nur dieser Kunde hat), Leistungen, allen Projekten mit Quelle, vorhandenen Fotos, fünf Aufgaben der Besucher mit benanntem Ziel (KO07); Lücken als `[FEHLT]`. Dazu `L/befund/alt-1440.png` und `alt-390.png` (`deviceScaleFactor` 2).
- Abnahme: jede Leistung und jedes Projekt hat eine Quelle.

## 3 SOUL und ARMOURY

- Fehlt Wesentliches, fragen: höchstens drei bis vier Fragen je Runde, nur was Akte und Befund nicht beantworten. Ein Satz Brief ist keine Antwort; nie selbst ergänzen. Vor dem Schreiben die Zusammenfassung bestätigen lassen.
- `L/SOUL.md` (wer und warum): Identität, Positionierung in einem Satz, Versprechen, Zielgruppe, Nutzungsszene (wer, wo, welches Licht; S31), Inventar mit Quelle, 3 bis 5 Referenzen mit je einem Merkmal, Anti-Referenzen, tragender Satz, Wortliste, „Die Seite sieht so aus, weil …“.
- `L/ARMOURY.md` (womit gebaut wird): Block aus `regler.md` mit Art, Lauf, Branche, Stufe und zehn Reglern, je ein Satz Grund. Startwerte aus `branchen/<name>.json` (bei `anwendung`: `regler.md`), Rahmen der Stufe, Leitplanken prüfen. Dazu: geladene Module, gewählte Techniken (höchstens zwei), Bausteine, Ausnahmen mit Datum.
- Abnahme: Der Satz „… weil …“ nennt die Leistung des Kunden (S02); keine Behauptung ohne Beleg in `befund.md`; alle zehn Regler gesetzt.

`MASK.md` entsteht erst nach der Wahl (`entwurf`).

## --bestand

1. Projekt lesen: Adresse (Seiten, Fotos, Konsole) und Code (Gerüst, Token, Komponenten).
2. SOUL, MASK und ARMOURY aus dem ableiten, was da ist, nicht aus Wünschen. Regler nur aus Beobachtetem (vorhandene Bewegung, Dichte, Skript, Tonfall).
3. Mehrere Vorgaben im Projekt: Es gilt die, die das Projekt als verbindlich führt. Entwürfe und Überholtes gelten nicht. Genutzte und verworfene Quellen nennen.
4. Beim Überführen bleibt jeder Inhalt mit Norm erhalten: Grenzwerte, Verbote, Nutzungsregeln an Token, datierte Anweisungen einer Person, Verweise. Fehlt einer, nicht schreiben.
5. Alte ARMOURY-Dateien nach `regler.md` (Block im ARMOURY) ergänzen.
6. Lücken erfragen wie in Schritt 3, bestätigen lassen, schreiben. Git-Repository wie in Schritt 1.

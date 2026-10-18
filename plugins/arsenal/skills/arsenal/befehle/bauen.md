# bauen (Schritt 6)

Baut die gewählte Seite oder Anwendung. Die Reihenfolge ist Regel.

**Aufruf:** `bauen [laufordner]` (Alias `build`)
**Wer:** Gestaltung Opus (Aufwand xhigh); Umsetzung Sonnet, kleine Änderungen Haiku.
**Tore:** `SOUL.md`, `MASK.md` und `ARMOURY.md` vollständig (alle zehn Regler, keine Platzhalter), sonst Halt mit Verweis auf `plan` oder `entwurf`. Der Projektordner ist ein Git-Repository.

## Schritte

1. **Laden** nach dem Ladeplan in `SKILL.md`: Stamm, `regler.md`, Branche, die Module der Art und der Regler, Rezepte nur für die gewählten Techniken.
2. **Inhalt vor Layout:** echte Texte und Daten für jeden Abschnitt und jeden Zustand, bevor gestaltet wird (S05). Fehlendes bleibt `[FEHLT]` und wird gemeldet, nie erfunden (S06).
3. **Bausteine zuerst:** `library/galerie/_index.md` und die mitgelieferten Vorlagen in `bausteine/_index.md` lesen und nur Kacheln öffnen, deren Art, Unterart, Branchen und Beschreibung (`ki`) zu Art und Reglern passen; dazu Muster aus `library/muster/`. Die Gestalt kommt aus dem MASK (PR15).
4. **Bau:** zuerst die gewählte erste Ansicht, dann die Abschnitte, dann die Unterseiten. Website: Startseite als Weiche (PR05), alle Projekte (PR10). Gerüst nach TE01.
5. **Zusammenbau in getrennten Dateien:** Jeder Bau-Agent schreibt nur seine Abschnitte oder Komponenten. Geteilte Dateien (Grundstil, Token, Layout, Routen) ändert nur die Integration.
6. **Vorschau:** `app.plasmind.dev/mockups-<zufall>/<code>/lp-n/` mit `noindex` und sperrender `robots.txt`, Adresse in `L/lp-n/VORSCHAU.md`. Leserechte setzen, jede verwiesene Datei auf Status 200 prüfen.

Bewegung baut `bewegung` im selben Schritt.

## Arbeitsweise

- Ein Auftrag je Agent zur Zeit. Die Leitung prüft nach jeder Zeile im Stand-Log, ob der nächste Schritt läuft, und legt einen hängenden Auftrag nach 15 Minuten um.
- Zwischenstände als Dateien im Laufordner, damit ein Neustart nicht alles wiederholt.
- Liefert ein Agent nichts, einmal wiederholen, dann die Lücke melden.
- Kleine Dateien und das Stand-Log schreibt die Leitung selbst.
- Token-Budget je Lauf in `lauf.md`. Richtwert aus den Läufen vom 15./16.10.: Plan und Material 1,0 bis 1,5 Mio., je Seite Gestaltung 1,0 bis 1,2, Bau und Messung 0,5 bis 0,8, Kritik 1,0, Politur 0,8 bis 1,0, Leitung 0,5; ein Lauf mit Wahl und einer Seite 4,8 bis 6,0 Mio. Die Läufe hatten drei Kritiker; der Posten Kritik und die Summe sind für sechs Kritiker ungeprüft. Bei 80 % eines Postens Meldung an die Leitung, nie Abbruch mitten im Schreiben.

## Ergebnis und Abnahme

`L/lp-n/site/`, `L/lp-n/VORSCHAU.md`. Jede Leistung mit einem Klick erreichbar; Zahl der gezeigten Projekte gleich der Liste in `befund.md`; kein Platzhalter.

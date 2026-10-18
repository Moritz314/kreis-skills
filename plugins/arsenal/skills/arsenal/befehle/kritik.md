# kritik (Schritt 8)

Sechs frische Kritiker prüfen blind und unabhängig. Drei vergeben Noten, drei suchen Mängel.

**Aufruf:** `kritik [laufordner] [lp-n]`, `kritik --datei <pfad|adresse> "<art, stufe, regler>"` für einzelne Entwürfe und fremde Seiten (ohne ARMOURY; fehlende Regler als Annahme im Bericht).
**Eingabe je Kritiker, nur lesend:** `AUDIT.md`, `bilder/`, `SOUL.md`, `MASK.md`, `ARMOURY.md`, `lauf.md`, zwei Referenzen, die alte Seite. Kein eigener Shell-Lauf; fehlt eine Datei, ist das ein Befund an die Leitung.

## Die sechs

| | Rolle | Modell | Ausgabe |
|---|---|---|---|
| G | Gestaltung und Marke gegen die Referenzen | Opus | 8 Noten |
| B | Bewegung und Detail, mit Liste „roh“ | Opus | 8 Noten |
| K | Kunde und Wirkung: zwei bis drei Personas aus der Zielgruppe (bei örtlichen Betrieben Laien, nie Fachpublikum), Fachwortliste, Budget Zeile für Zeile | Sonnet | 6 Noten |
| T | Technik und Vorgabentreue: jede Vorgabe aus Brief und ARMOURY einzeln, Attrappen statt echter Funktion | Sonnet | Mängel |
| M | Muster und KI-Reflex: Häufung der Merkmale aus S04, Befunde von `detect`, Farbe aus dem Branchenklischee | Sonnet | Mängel |
| R | Website: Recht und Vertrauen (S06 bis S11, KO06; Zähler mit 0, Stimme als Platzhalter, Bewertung ohne Quelle, Zoom gesperrt, Superlativ ohne Beleg). Anwendung: Bedienung (Modul `software`) | Sonnet | Mängel |

**Noten** gibt es ab Stufe `kunde-hochwertig`; auf `betrieb` liefern G, B und K Mängellisten. Skala: 10 besser als beide Referenzen, 8 gleiche Liga, 5 Agentur, 3 Vorlage, 1 Formular. Jede Note nennt Fundstelle (Bild und Ausschnitt) und den einen Schritt auf 8. „Gleiche Liga“ (G) und „poliert“ (B) heißen: alle Noten ab 8.

- **G:** erste Ansicht und Blickfang, Markenidentität, Typografie, Material und Bild, Komposition und Raum, Farbe und Licht, Durchgängigkeit (mit Unterseiten), Eigenständigkeit (PR15).
- **B:** Ladefolge, Wortwechsel und Anzeigen, Scroll-Choreografie, Hover, Fokus und Druck, Timing und Kurven, Typografie im Detail, Übergänge und Rhythmus, reduziert und mobil.
- **K:** Fünf-Sekunden-Klarheit, Weg zum eigenen Anliegen (Weiche), Vertrauen, als Zielgruppe gemeint, Wertigkeit, Weg zur Anfrage (mit Telefon). Dazu: Versteht er jedes Bild (S35)? Was hält ihn ab?

## Regeln

- Alle sechs starten in einer Nachricht als getrennte Agenten, nie als Abzweig derselben Sitzung, nie nacheinander in einer Sitzung. Gilt eine Grenze gleichzeitiger Agenten, laufen sie paarweise nacheinander mit eigenem Browser-Kontext.
- Ein Befund misst sich an den Reglern (`regler.md`, letzter Abschnitt).
- Mangel: Schwere, Fundstelle, Befund, Korrektur. Fehlt ein Feld, entfällt er.
- Die Leitung führt zusammen: Doppeltes zusammenlegen (mehrfach gefunden ist ein starkes Zeichen), Widersprüche entscheiden, einordnen als **notwendig** (Pflicht, Budget, kaputt), **empfohlen** oder **Geschmack**.
- Liegt eine Note nach der ersten Runde unter 6 (auf `betrieb`: ein Mangel an der Grundentscheidung, etwa Leitmotiv, Farbordnung oder Schrift), braucht es eine neue Grundentscheidung (zurück zu `entwurf`), keine Politur.

## Ergebnis

`L/lp-n/KRITIK-G.md`, `-B.md`, `-K.md`, `-T.md`, `-M.md`, `-R.md`; letzte Zeile das Urteil wie in `audit` (bei K: „würde anfragen“ ja oder nein, „im Budget“ ja oder nein). Dazu `L/lp-n/KRITIK.md` mit der zusammengeführten Liste.

# bibliothek

Legt Muster und Bausteine in die Bibliothek. Die Heimat aller neuen Bausteine ist die Galerie; im Skill liegen nur die mitgelieferten Vorlagen (`bausteine/`).

**Aufruf:** `bibliothek <adresse|bild>` (Muster, Alias `loot`), `bibliothek --baustein <ordner> [laufordner]` (Kachel), `bibliothek --medium <datei>` (Medium)
**Ort:** `library/` im Zustandsordner (Pfade in `SKILL.md`).

## Muster aus einer fremden Seite

1. Abschnitt für Abschnitt in fester Folge: erste Ansicht, Navigation, Typografie, Farbe, Bewegung, Komponenten, Tonfall. Fehlt einer, sagen.
2. Nach jedem Abschnitt fragen: „Was genau gefällt dir daran?“ Nur bestätigte, genaue Antworten (die Kurve, die Paarung, der Ton) werden gespeichert.
3. Eintrag `library/muster/<slug>.md`: Beschreibung und Analyse, der bestätigte Grund, Adresse, Datum, Schlagworte, Website oder Anwendung. Nie fremden Code oder fremde Dateien.
4. Eine Zeile in `library/muster/_index.md`. Ohne Zeile findet ihn kein Bau.

## Baustein in die Galerie

1. Ordner `library/galerie/<slug>/` mit `kachel.html`, `kachel.css`, `kachel.json` und `HERKUNFT.md`, nach den Galerie-Vorgaben der Arsenal-App (`<dein-ordner>`, Abschnitte 9 und 14.4).
2. `kachel.json` mit den Pflichtfeldern und den Feldern für die Auswahl: `art` und `unterart` (Schlüssel aus `library/galerie/_ordnung.json`), `branchen`, `stichworte`, `wofuer`, `parameter`; die Galerie-Werkzeuge bilden daraus die Beschreibung `ki` (Format: `SCHEMA.md`, Pfad in `SKILL.md`).
3. Die Gestalt ist neutral oder per Parameter anpassbar; Kundennamen und Kundenmaterial nur mit Freigabe.
4. Probe: Kachel öffnet ohne Konsolenfehler, reduzierte Fassung sichtbar, `groesse_kb` gemessen.

## Medium in die Galerie

Nur kommerziell frei Nutzbares (ME12), mit Lizenz, Quelle, Urheber, Auflösung und Herkunftsnachweis; KI-Fotos mit Datum der Freigabe durch <dein-name>.

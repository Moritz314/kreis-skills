# Modul Medien

Laden nach `regler.md` (Module nach Reglern). Grundlagen im Stamm: scharf (S34), Bezug (S35), Einbindung (S36), Herkunft und Lizenz (S11), nichts vortäuschen (S06). Selbst Erzeugtes: Modul `erzeugt`.

## Quellen, in dieser Reihenfolge

- **ME01 Eigenes zuerst.** Fotos und Arbeiten des Kunden, eigene Websites und Aufnahmen. Eigenes Material führt in die oberste Liga; Stock allein endete in der Kalibrierung bei Note 7.
- **ME02 Stock ist erlaubt, wenn es passt** (E11). Prüffragen: Zeigt es die Leistung erkennbar (S35)? Passt es zur Zielgruppe, nicht nur zur Leistung? Widerspricht das erste Bild der Bühne dem Text daneben? Quellen ohne Namensnennung: Pixabay (Pixabay Content License; Filme in der Fassung `large` oder 4K; Fotos über den Holdienst nur bis 1280 px, siehe Zugänge), Pexels (Fotos und Filme), Coverr (Filme). Unsplash ist frei, verlangt über die API aber Namensnennung. Mixkit mischt Lizenzen je Clip und liefert höchstens 720p, darum nie für große Flächen.
- **ME03 Selbst erzeugt** (Modul `erzeugt`): SVG, Motion Graphics, Linien, Texturen, Shader, 3D.
- **ME04 Echte KI-Fotos** aus Bildgeneratoren (Higgsfield, Leonardo) nach Ermessen, aber erst nach einer Frage an <dein-name> (E11). Keine erkennbare echte Person ohne Einwilligung, keine fremde Marke im Bild. Den Zugang vor der ersten Nutzung prüfen, nicht annehmen.
- **ME05 Icons:** ein Satz je Vorhaben. Lucide (ISC), Phosphor, Tabler, Heroicons (je MIT), oder ein eigener Satz auf einem Raster mit gleicher Strichstärke. SVG statt Icon-Schrift. Prüffrage: Bleibt jedes Icon ohne geladene Schrift sichtbar und für Screenreader richtig benannt?
- **ME06 Schriften** mit geprüfter Lizenz: Google Fonts (fast alle SIL OFL), Fontshare (ITF Free Font License), Velvetyne (frei, Bedingungen je Schrift prüfen). Open Foundry ist nur ein Verzeichnis, die Lizenz kommt von der Quelle. Immer selbst gehostet (S09).

## Prüfen und ablegen

- **ME07 Medientabelle `material/MEDIEN.md`:** eine Tabelle für alles: je Datei Quelle, Urheber, Lizenz, Suchbegriff, Bearbeitung (S11), Quellpixel, geplantes Anzeigemaß, Gewicht, Bezugssatz („zeigt …, für …“, S35). Jede Zeile erfüllt Quelle ≥ Anzeigemaß × 2. Dazu ein Kontaktbogen, gesichtet vor jeder Kodierung.
- **ME08 Ordnen nach Nähe zum Zielkunden:** Eigene Arbeiten stehen in der Reihenfolge, in der sie dem Zielkunden am nächsten sind.
- **ME09 Gewicht und Schärfe zugleich.** Einzelbild bis 250 KB; das Budget der Stufe in `regler.md` geht vor. Geht beides nicht, wird das Motiv einfacher (ruhiger, Maske), nicht kleiner skaliert. `srcset` mit drei bis fünf Breiten.
- **ME10 Naht- und Wiederholungsprobe** für gekachelte oder gespiegelte Flächen: keine sichtbare Spiegelachse, kein Merkmal zweimal in einer Bildschirmhöhe. Geprüft am Standbild, nicht an der Datei.
- **ME11 Farbe des Materials.** Filme und Fotos der Bühne werden auf die Hausfarben gegradet; Glanzlichter bleiben. Körnung nur mit Absicht; Prüffrage: Verdeckt sie Glanzlichter oder Schärfe (S34)?
- **ME12 Galerie:** In die Bibliothek (`library/galerie`) kommt nur, was kommerziell frei nutzbar ist, mit Lizenz, Quelle, Auflösung und Herkunftsnachweis (Format: `SCHEMA.md` Abschnitt 4.1, Feld `medium`; Pfad in `SKILL.md`).

## Video

- **ME13 Klassen:** Größe nach S34: Jede ausgelieferte Datei ist mindestens so breit wie ihre größte Anzeige × 2, der Master ebenso (Vollbild bei 1440 CSS-px: 2880 px, also eine 4K-Quelle). Drei Klassen nach Fensterbreite (ab 1280 px je Datei bis 8 MB, Tablet und Telefon je bis 3 MB), gewählt über `media` an den `source`-Elementen. Gehen Schärfe und Gewicht nicht zugleich, wird das Motiv ruhiger, nicht die Datei kleiner (ME09). Das Videobudget je Seite in `regler.md` geht vor; auf `betrieb` ist es enger.
- **ME14 Poster** ist genau Bild 0 des ausgelieferten Films, je Fensterklasse eines (`picture` und `preload` mit `media`), mobil unter 30 KB. Abschnitte, die dasselbe Material nutzen, nutzen dieselbe Posterdatei. Probe: PSNR gegen Bild 0 über 35 dB (`rezepte/erzeugt.md`).
- **ME15 Laden:** Bühne `preload="metadata"`, unter der ersten Ansicht `preload="none"`; immer `width` und `height`. Der Film startet nach `load` und nach der Ladefolge ab Bild 0. `autoplay` nur stumm und mit Pause-Knopf fest am Bühnenrand. Außerhalb des Fensters pausiert er (IntersectionObserver). Bei reduzierter Bewegung steht das Poster. Video statt GIF.
- **ME16 Kein Mischmodus über laufendem Film im Pin** (`mix-blend-mode`): Chromium zeichnet dort weiße und schwarze Rechtecke. Licht auf Material kommt aus Ebenen mit Deckkraft oder aus dem Film selbst.

## Zugänge

Pixabay über den Holdienst: eine Zeile `video<TAB>begriff<TAB>anzahl[<TAB>mindestbreite]` oder `bild<TAB>…` an `<dein-ordner>`; Ergebnis in `<dein-ordner>` mit `treffer.json`. Einwortbegriffe treffen besser. Fotos kommen dort nur in Vorschaugröße (1280 px breit); das reicht nach S34 für höchstens 640 px Anzeigebreite. Größere Fotos auf einem anderen Weg (etwa Pexels in Originalgröße); fehlt einer, <dein-name> fragen (über den Overseer).

# Regler, Stufen, Arten

Wird immer geladen. Ein Vorhaben läuft mit zehn Reglern, einer Stufe, einer Website-Art und einer Lauf-Art. Die Regler sind Grenzen, kein Stilkatalog: Sie sagen, was erlaubt ist. Was innerhalb der Grenzen gut ist, sagen Stamm und Module.

## Woher die Werte kommen

1. **Branche** (`branchen/<name>.json`): Startwerte aller zehn Regler und kurze Branchenregeln. Gepflegt in der Arsenal-App. Die Art `anwendung` hat keine Branche (`branche: keine`): `plan` setzt die Startwerte aus dem Modul `software` (SW02, SW10, SW16) und S50, jeden mit Grund.
2. **Stufe** (unten): Rahmen für einzelne Regler. Liegt ein Startwert außerhalb, gilt die nächste Grenze des Rahmens.
3. **ARMOURY.md** des Vorhabens: die endgültigen Werte, je mit einem Satz Grund. Eine Abweichung von Branche oder Rahmen steht dort mit Datum und Grund. Ein Regler ändert sich mitten im Vorhaben nur so; danach prüft `kritik` gegen die neue Stellung.

„Nicht auf dieser Stufe“ heißt: Wer es braucht, stellt den Regler um. Es ist kein Verbot.

## Die zehn Regler

**auftreten** (wie die Seite klingt; regelt nicht die Qualität)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `werkstatt` | echte Fotos echter Arbeit, schlichte Hauptwörter, Preise oder Lieferzeiten im Text | Bilder fremder Menschen im Büro, Aussagen über sich ohne Beleg |
| `haus` | Struktur und Vollständigkeit, Rechtsklarheit, Referenzen, sichtbare Verantwortung | lauter Szene-Look |
| `studio` | bewusste Typografie, redaktionelles Layout, Zurückhaltung als Signal, Arbeiten als Fälle | Merkmallisten statt Fällen |
| `labor` | Vorführung vor Beschreibung, dichte Produktfläche, technische Sicherheit | Beschreibung, wo eine Vorführung geht |

**bewegung** (wie viel Bewegung das Vorhaben ausgibt; Stamm S42 bis S51 gelten auf jeder Stufe)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `0` | Sofortwechsel von Zuständen, sichtbarer Fokus | Übergänge, Einblendungen |
| `1` | Bewegung mit Funktion: Rückmeldung, Fokus, Auf und Zu, Seiten- und Ortswechsel | Schmuckbewegung, Einblendungen beim Scrollen |
| `2` | dazu wenige Akzente (typisch einer je Seite), das bewegte Leitmotiv (BE08), selbstlaufende Wechsel nach BE18 | Dauerbewegung im Hintergrund, Parallax über lange Seiten, Scroll-Szenen mit Pin |
| `3` | volle Choreografie: Scroll-Szenen, Pins, Zerlegung, Hintergrundbewegung | nichts vom Regler her; Ermessen und Budgets gelten |

**dichte** (wie viel auf einem Bildschirm steht; Weißraum ist die Gegenrichtung, darum kein eigener Regler)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `luftig` | ein Gedanke je Abschnitt, große Schritte der Schriftskala, großzügiges Zeilenmaß | mehrere gleichrangige Aussagen in einem Abschnitt |
| `ausgewogen` | zwei bis drei verwandte Gedanken je Abschnitt, Standardskala | – |
| `verdichtet` | enger Rhythmus, kleinere Schritte, Tabellenziffern (für täglich Bedientes) | Schmuck-Weißraum, der Daten aus dem Bild schiebt; Gedränge ohne Struktur |

**technik** (was die Seite ausliefert; Video ist auf jeder Stufe erlaubt)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `statisch` | HTML und CSS, wenige Zeilen Skript als Verbesserung, CSS- und SVG-Bewegung, Video | Skript-Bibliotheken, Inseln, WebGL |
| `inseln` | Inseln nur für die Teile, die sie brauchen (z. B. GSAP, Canvas, Lottie) | Shader- und 3D-Ebenen |
| `webgl` | dazu Shader und 3D, nie im kritischen Pfad, mit Standbild und Telefonfassung | nichts vom Regler her; Budgets gelten |

**tonfall** (wie der Text spricht)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `nuechtern` | Tatsachen, Zahlen, nur prüfbare Eigenschaften | Superlative, Versprechen, Ausrufe |
| `direkt` | spricht den Leser an, nennt den nächsten Schritt, kurze Sätze | Absicherungsfloskeln, Passiv |
| `selbstbewusst` | bezieht Stellung, nennt, was es nicht tut, starke Aussage mit Beleg | Getöse ohne Beleg, geliehenes Startup-Vokabular |

**material** (Bildanteil gegen Typografie; woher das Bild kommt, regelt das Modul Medien)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `typografisch` | Schrift, Raster und Fläche tragen die Seite; Bilder als Beleg in Abschnitten; selbst erzeugte Linien und Texturen | Foto oder Film im Vollbild als Bühne |
| `ausgewogen` | Bild oder Film in Bühne und Abschnitten neben starker Typografie | – |
| `bildstark` | Foto oder Film tragen Bühne und Abschnitte, Vollbild, Bildfolgen | – |

**farbe** (Farbstrategie)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `zurueckhaltend` | getönte Neutraltöne plus ein Akzent | Farbflächen über ganze Bereiche |
| `bekennend` | eine satte Farbe trägt 30 bis 60 % der Fläche | mehrere gleich starke Farben |
| `voll` | drei bis vier benannte Farbrollen, jede mit fester Aufgabe | Farbe ohne feste Aufgabe |
| `getraenkt` | die Fläche ist die Farbe | – |

**inszenierung** (wie stark Leistung oder Produkt vorgeführt wird)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `zeigen` | Leistung als Bild mit Klartext, Fälle, Listen mit Beleg | Pins, Vorführstrecken |
| `vorfuehren` | Ablauf in Schritten, Vorher-Nachher, Live-Probe, Bildfolge zum Ziehen | Bühnen über mehrere Bildschirmhöhen |
| `buehne` | Leitmotiv als Inszenierung, kühne Stelle mit dem Versprechen, Pins (ab `bewegung: 3`) | – |

**konversionsdruck** (wie direkt die Aufforderung ist; Täuschung ist auf keiner Stufe erlaubt, siehe Modul Konversion)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `leise` | Kontakt sichtbar in Kopf und Fuß, eine Einladung am Ende | feste Handlungsleiste, Hauptaktion in jedem Abschnitt |
| `klar` | eine Hauptaktion je Seite mit Mikrotext zur Hürde, in der ersten Ansicht, wiederholt nach KO01 | zwei konkurrierende Hauptaktionen |
| `direkt` | dazu feste mobile Handlungsleiste, Telefon als Knopf, Funnel, Rückruf oder Terminwahl in der Seite | – |

**schrift** (Charakter der Typografie; höchstens zwei Familien auf jeder Stufe)

| Stufe | erlaubt | nicht auf dieser Stufe |
|---|---|---|
| `sachlich` | eine ruhige Familie oder Paarung, Hierarchie über Größe und Gewicht | Anzeigeschrift, Plakatwörter |
| `redaktionell` | Paarung mit Kontrast in einer Achse (etwa Antiqua zu Grotesk), redaktionelle Skala, Zitate | Plakatwörter |
| `ausdruck` | Anzeigeschrift als Stimme, Plakatwörter über 150 px, kinetische Typografie | – |

## Leitplanken (die Planung hält an und fragt)

| Kombination | Warum |
|---|---|
| `bewegung: 3` mit `technik: statisch` | Choreografie dieser Art braucht eine Zeitleiste mit Skript |
| `bewegung: 3` mit `dichte: verdichtet` | Bewegung konkurriert auf täglich bedienten Flächen mit den Daten |
| `inszenierung: buehne` mit `bewegung` 0 oder 1 | eine Bühne ohne Bewegung ist ein Standbild |
| `auftreten: werkstatt` mit `tonfall: selbstbewusst` | erlaubt, braucht einen Grund im ARMOURY; sonst wirkt es wie geliehene Kleidung |
| lauter Szene-Look (harter Kontrast, Verzerrung, kurze Szenetexte) für breites örtliches Publikum | trägt nur bei kleiner, klar umrissener Zielgruppe |

Ein Brief, der Bewegung ganz verbietet, ist auf den Stufen `kunde-hochwertig` und `award` der Fehler, nicht der Regler.

Der Rahmen der Regler je Stufe (unten) gilt für Websites (`website`, `onepage`, `landingpage`). Für die Art `anwendung` sind die Regler auf jeder Stufe frei; dort gelten SW02 und S50.

## Stufen

<dein-name> wählt die Stufe je Lauf. Sie steht im ARMOURY über den Reglern. Gleiches Handwerk, gleiche Politur und gleicher Stamm auf jeder Stufe; nur Anspruch, Rahmen und Maßstab unterscheiden sich.

| | `betrieb` | `kunde-hochwertig` | `award` |
|---|---|---|---|
| für wen | Demos örtlicher Betriebe (Akquise) | Handwerk, kleine Betriebe, Vereine, Praxen | Hausseite kreis.systems, plasmind, Agenturkategorie |
| Rahmen der Regler | frei | `bewegung` ab 2, `inszenierung` ab `vorfuehren` | `bewegung` 3, `inszenierung` `buehne`, `technik` ab `inseln` |
| Leitmotiv | nach Ermessen | verlangt, aus dem Gewerk des Kunden | verlangt, mit eigenem Material |
| Prüfmaßstab | Mängelliste, keine Noten | Noten 1 bis 10 gegen zwei hochwertige Kundenseiten | Noten 1 bis 10 gegen die Seite der German Web Awards und eine zweite Referenz; die alte eigene Seite liegt daneben |

**Budgets** (eine Zahl je Stufe; Betrieb streng, Award weiter; Messung nach Stamm S38)

| Wert | `betrieb` | `kunde-hochwertig` | `award` |
|---|---|---|---|
| Lighthouse Leistung mobil | ≥ 90 | ≥ 70 | ≥ 70 |
| Lighthouse Leistung Desktop | ≥ 90 | ≥ 85 | ≥ 85 |
| Lighthouse Barrierefreiheit, Best Practices | ≥ 95 | ≥ 95 | ≥ 95 |
| Lighthouse SEO (ohne `noindex`-Demos) | ≥ 90 | ≥ 90 | ≥ 90 |
| LCP / CLS / INP | 2,5 s / 0,05 / 200 ms | gleich | gleich |
| TBT | ≤ 200 ms | ≤ 300 ms | ≤ 300 ms |
| LCP-Bild | ≤ 200 KB | ≤ 250 KB | ≤ 250 KB |
| erste Ansicht ohne Video | ≤ 1 MB | ≤ 1,5 MB | ≤ 1,5 MB |
| Videos je Seite | ≤ 5 MB | ≤ 15 MB, mobil ≤ 6 MB | ≤ 15 MB, mobil ≤ 6 MB |
| Schriften | ≤ 150 KB, ≤ 4 Dateien | ≤ 200 KB | ≤ 200 KB |
| Long Task bei 4-facher CPU-Drosselung | ≤ 100 ms | ≤ 100 ms | ≤ 100 ms |
| WebGL Pixeldichte (DPR) | ≤ 1,5, mobil 1 | ≤ 1,5, mobil 1 | ≤ 1,5, mobil 1 |

## Website-Arten und Lauf-Arten

| Art | Was | geladene Module (zusätzlich zum Stamm) |
|---|---|---|
| `website` | mehrseitig; die Startseite ist eine Weiche zu den Unterseiten | praesentation, text, konversion |
| `onepage` | eine Seite mit Abschnitten (Pakete Onepage, Schausteller-Seite); die erste Ansicht führt mit Sprungzielen wie Türen weiter (KONFLIKTE K3) | praesentation, text, konversion |
| `landingpage` | Kampagnenseite mit einem Ziel (Funnel) | praesentation, text, konversion |
| `anwendung` | Software im Browser (<internal-project>, plasmind) | software, text |

Was die Kalibrierung „Landingpage“ nannte, ist hier die Startseite der Art `website`.

| Lauf | Zweck | Ergebnis |
|---|---|---|
| `demo` | Akquise: zeigen, bevor der Kunde fragt (Stufe meist `betrieb`) | gewählte Startseite als Vorschau |
| `mockup` | Entwurf zur Wahl, gehostet | erste Ansichten oder Seiten unter `app.plasmind.dev/mockups-<zufall>/` |
| `bau` | fertige Website oder Ausbau einer gewählten Demo | ausgelieferte Seite |

**Module nach Reglern** (zusätzlich zur Art): `bewegung` ab `bewegung: 1`; `medien`, sobald Fotos, Filme oder fremde Dateien vorkommen; `erzeugt`, sobald Material selbst erzeugt wird (SVG, Film, Shader, 3D, Textur); `technik` ab `technik: inseln`, bei Video und bei `bauen` und `audit`. Dazu die Liste `module` der Branche.

## Block im ARMOURY

```markdown
## Vorhaben
art: website
lauf: bau
branche: handwerk
stufe: kunde-hochwertig

## Regler
auftreten: werkstatt        # Grund in einem Satz
bewegung: 2
dichte: luftig
technik: inseln
tonfall: nuechtern
material: bildstark
farbe: zurueckhaltend
inszenierung: vorfuehren
konversionsdruck: direkt
schrift: sachlich
```

Fehlt der Block oder ein Regler, halten `material`, `entwurf`, `bauen`, `bewegung`, `audit`, `kritik` (ohne `--datei`) und `politur` an und verweisen auf `plan`. Alte ARMOURY-Dateien mit `## Dials` (fünf Regler) gelten weiter; `plan --bestand` ergänzt die fünf neuen.

## Wie die Kritik die Regler nutzt

Ein Befund misst sich an den Reglern, nie an einem allgemeinen Ideal: „keine Animation“ ist bei `bewegung: 0` kein Befund. Immer zählen: Pflichtregeln (Lesart in `regeln/stamm.md`), das Budget der Stufe und Falsches (Behauptung ohne Beleg, erfundene Zahl, fehlende Rechtsangabe).

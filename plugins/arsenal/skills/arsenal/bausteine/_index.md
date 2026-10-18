# Bausteine (mitgelieferte Vorlagen)

Status: **ungeprüft**. Art, Unterart, `braucht` und Größe sind aus Kopfkommentar und Code abgeleitet (18.10.2026), nicht im Browser geprüft.

Die Heimat aller Bausteine ist die Galerie im Zustandsordner (`library/galerie/`, Index `library/galerie/_index.md`; Arten und Unterarten wie dort und in `library/galerie/_ordnung.json`). Hier liegen nur zwei Sätze als Vorlagen: der **plasmind-Satz** (Kennungen H, E, F, B; Hausmarke plasmind, aus der Elementeschau vom 03.10.2026) und die **Kunden-Bausteine** K1 bis K4 (eigene Gestalt, angeregt durch Seiten der German Web Awards 2026, BAUPLAN G5 bis G11 in `<dein-ordner>`). Die Planung wählt per `wofür` und `braucht`; die Gestalt kommt aus dem MASK (PR15).

- Jede Datei ist in sich geschlossen: CSS und JS inline, keine fremden Abrufe, keine Abhängigkeiten (Ausnahme: F2 und F3 lesen kleine Medien aus `plasmind/medien/`, K2 aus `kunden/medien/`). Schrift fällt auf Systemschrift zurück; Martian Mono (OFL) bei Bedarf selbst einbinden.
- Beim Einbau ins Projekt: CSS und JS in eigene Dateien (S10), Kurven und Dauern aus dem Satz des Projekts (BE04), die Gestalt aus dem MASK.
- Thema: dunkel als Standard, hell über `[data-theme=light]` (Demo: `?theme=light`); im Projekt gilt das Thema-Skript nach TE08. H- und E-Dateien pausieren außerhalb des Bildes und zeigen bei reduzierter Bewegung ein Standbild.
- Vorschau: `<ordner>/vorschau/<Kennung>.webp` (F1 bis F12: `.png`). Bildquellen: `plasmind/bilder/QUELLEN.md` (eigenes Werk).
- ★ = von <dein-name> ausgewählt. `braucht` = niedrigste passende Reglerstufe (Vorschlag).
- Zeiger-Effekte: Flächen, die auf den Zeiger reagieren (H2, H6, H8, H11), und Tooltips mit Information (E5) sind erlaubt. Schmuck, der als Form oder Spur am Zeiger hängt (E15, H1, H3, H4, H12), ist ein eigener Zeiger und darum nur Muster (S20).
- `ux`/`vorfuehrung` (F1, F3, F6 bis F12) gibt es in der Galerie noch nicht; Vorschlag an die Bauleitung.

## UI-Elemente (`ui`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| E21 | `formular` | Theme switch | Hell-Dunkel-Schalter: Eine Zelle gleitet über die Bahn und flacht dabei ab; zeigt beide Themen. | `PMEL.E21.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.2 | bewegung 1, inseln | `plasmind/E21-theme-switch.html` |
| E2 | `karte` | Card with cell outline ★ | Der Rand der Karte ist eine langsam lebende Kurve, die sich unter dem Zeiger regt. | `PMEL.E2.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.1 | bewegung 2, inseln | `plasmind/E2-card-with-cell-outline.html` |
| E17 | `karte` | Quote box ★ | Zitat in einem Kasten mit Zellenecke, für eine Regel des Produkts oder eine Stimme. | `PMEL.E17.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 14.5 | bewegung 1, inseln | `plasmind/E17-quote-box.html` |
| E18 | `karte` | Comparison table ★ | Zwei Pakete nebeneinander, die empfohlene Spalte auf umgekehrter Fläche; am Telefon als Stapel lesbar. | `PMEL.E18.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.1 | bewegung 1, inseln | `plasmind/E18-comparison-table.html` |
| F4 | `karussell` | Vorher/nachher | Ein Regler blendet zwischen zwei Zuständen eines Briefings über. | Demo, Thema über `data-theme` | 13.5 | bewegung 1, statisch | `plasmind/F4-compare-slider.html` |
| K1 | `knopf` | Telefonnummer als Knopf mit Telefonzeiten | Die Nummer selbst ist die Beschriftung eines tel:-Knopfs, die Telefonzeiten stehen direkt darunter; Haupt- oder Nebenknopf. | Kein Skript: echter Link `a[href^="tel:"]` mit Klasse `knopf--haupt` oder `knopf--neben`, darunter `p.tel-zeiten`. Der zugängliche Name enthält die sichtbare Nummer. | 14.7 | bewegung 0, statisch | `kunden/K1-telefonnummer-als-knopf.html` |
| E1 | `knopf` | Buttons with cell edge ★ | Haupt-, Neben- und stille Knöpfe; die Kontur wabert bei Hover wie eine Zelle und staucht beim Druck. | `PMEL.E1.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.0 | bewegung 1, inseln | `plasmind/E1-buttons-with-cell-edge.html` |
| E9 | `knopf` | Window buttons W8b2 | Drei kleine Zellen in der Titelleiste; das Zeichen erscheint bei Hover oder Fokus, Minimieren sind zwei Pfeile zur Mitte. | `PMEL.E9.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.5 | bewegung 1, inseln | `plasmind/E9-window-buttons-w8b2.html` |
| K4 | `navigation` | Feste Handlungsleiste unten mobil | Unter 768 px eine feste Zeile mit Anrufen und Hauptaktion, weicht der Bildschirmtastatur. | `aside.leiste` am Ende von `body` mit zwei Knöpfen. Das Skript blendet sie nur aus, solange ein Eingabefeld den Fokus hat und die Bildschirmtastatur offen ist (`visualViewport` unter 75 % der Fensterhöhe). Über 767 px Breite und unter 400 px Fensterhöhe unsichtbar. | 16.6 | bewegung 0, statisch | `kunden/K4-handlungsleiste-mobil.html` |
| E3 | `navigation` | Scrollbar W1b | Scrollbalken: dünne wabernde Zelle als Griff, größer bei Hover, breiter und lebendig beim Ziehen. | `PMEL.E3.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.4 | bewegung 1, inseln | `plasmind/E3-scrollbar-w1b.html` |

## UX-Muster (`ux`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| E6 | `bestaetigen` | Notification W5b | Meldungen gleiten von rechts mit einer kleinen Zelle herein; wichtige bleiben als umgekehrte Fläche stehen. | `PMEL.E6.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.1 | bewegung 1, inseln | `plasmind/E6-notification-w5b.html` |
| E7 | `laden` | Sleeping cell W6c | Leerzustand: eine Zelle mit geschlossenen Augen, die kaum atmet, dazu ein Satz, was sie weckt. | `PMEL.E7.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.3 | bewegung 1, inseln | `plasmind/E7-sleeping-cell-w6c.html` |
| E10 | `laden` | Taskbar liquid W10a | Die App-Zelle füllt sich von unten mit dem Fortschritt, die Oberfläche wellt sich langsam, die Augen bleiben oben. | `PMEL.E10.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.0 | bewegung 1, inseln | `plasmind/E10-taskbar-liquid-w10a.html` |
| E12 | `laden` | Loader LF3 | Lebendiges Ladezeichen: zwei Zellen ziehen sich auseinander und finden wieder zusammen. | `PMEL.E12.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 25.9 | bewegung 1, inseln | `plasmind/E12-loader-lf3.html` |
| E13 | `laden` | Loader LK2 | Mittlerer Ladering: Eine Zelle auf einem Kreis teilt sich und findet im Umlauf wieder zusammen. | `PMEL.E13.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 25.9 | bewegung 1, inseln | `plasmind/E13-loader-lk2.html` |
| E14 | `laden` | Wave bar | Fortschrittsbalken als ein ruhiger Körper, eine Welle läuft durch seine Dicke, nichts löst sich von der Front. | `PMEL.E14.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 26.4 | bewegung 1, inseln | `plasmind/E14-wave-bar.html` |
| E22 | `laden` | Budget ring | Fortschrittsring für den verbrauchten Teil eines Budgets; der Kopf ist eine kleine Zelle, der Stand steht auch als Text. | `PMEL.E22.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.7 | bewegung 1, inseln | `plasmind/E22-budget-ring.html` |
| F1 | `vorfuehrung` | Mini-Overseer | Ein Overseer-Blob zerlegt einen getippten Auftrag in Briefings für Agenten; einer wartet auf ein Ja. | Demo, Thema über `data-theme` | 18.7 | bewegung 1, statisch | `plasmind/F1-mini-overseer.html` |
| F3 | `vorfuehrung` | Schritte auf Bildschirmfotos | Vier Schritte führen mit Hervorhebung, Zoom und Lupe über Fotos eines App-Fensters. | Demo, Thema über `data-theme` | 17.5 | bewegung 1, statisch | `plasmind/F3-screenshot-steps.html` |
| F6 | `vorfuehrung` | Freigabe-Probe | Zeigt, dass der Agent vor jedem Senden neu um ein einmaliges Ja bittet. | Demo, Thema über `data-theme` | 12.0 | bewegung 1, statisch | `plasmind/F6-approval-rehearsal.html` |
| F7 | `vorfuehrung` | Ablaufprotokoll | Ein Beispiel-Lauf wird Zeile für Zeile abgespielt, drei Prüfpunkte leuchten auf. | Demo, Thema über `data-theme` | 13.2 | bewegung 1, statisch | `plasmind/F7-run-log.html` |
| F8 | `vorfuehrung` | Agentenkarte mit Budget | Ein Regler füllt den Budgetring, bei 80 % Warnung, bei 100 % Stopp. | Demo, Thema über `data-theme` | 16.7 | bewegung 1, statisch | `plasmind/F8-budget-card.html` |
| F9 | `vorfuehrung` | Dateiraster | Pakete werden Dateien zugewiesen, jede Datei gehört genau einem Paket. | Demo, Thema über `data-theme` | 15.8 | bewegung 1, statisch | `plasmind/F9-file-grid.html` |
| F10 | `vorfuehrung` | Schlafender Resident | Ein schlafender Agent wacht für eine kleine Aufgabe auf und schläft wieder ein. | Demo, Thema über `data-theme` | 16.8 | bewegung 1, statisch | `plasmind/F10-sleeping-resident.html` |
| F11 | `vorfuehrung` | Maskierung | Zeigt live, was ein Modell statt eines getippten Schlüssels oder Passworts sieht. | Demo, Thema über `data-theme` | 10.5 | bewegung 1, statisch | `plasmind/F11-key-masking.html` |
| F12 | `vorfuehrung` | Begleiter | Ein ziehbarer Blob rastet an einem Rand des Beispielfensters ein und zeigt Meldungen. | Demo, Thema über `data-theme` | 19.7 | bewegung 1, inseln | `plasmind/F12-companion.html` |

## Layouts (`layout`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| E19 | `seite` | Footer with cell pattern ★ | Fuß mit einem Raster kleiner Zellen, die nahe dem Zeiger anschwellen und wabern. | `PMEL.E19.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.1 | bewegung 2, inseln | `plasmind/E19-footer-with-cell-pattern.html` |

## Animationsarten (`animation`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| H10 | `bahn` | Colony with threads ★ | Agenten treiben als kleine Zellen, Fäden verbinden Nachbarn, Signale laufen darauf. | `PMEL.H10.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.3 | bewegung 2, inseln | `plasmind/H10-colony-with-threads.html` |
| H7 | `scroll` | Depth parallax | Blobs in fünf Ebenen verschieben sich beim Scrollen verschieden schnell. | `PMEL.H7.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 14.6 | bewegung 3, inseln | `plasmind/H7-depth-parallax.html` |
| H13 | `scroll` | Built: CSS 3D to WebGL | Scroll-Abschnitt mit vier Schritten (Design, Agenten, Kern, Fenster): Die Drahtkugel zieht sich zusammen, der echte Blob wächst heraus; rückwärts läuft es umgekehrt. Folgt dem Seitenthema. | `PMEL.H13.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 34.0 | bewegung 3, webgl | `plasmind/H13-built-css-3d-to-webgl.html` |
| E8 | `uebergang` | Drag preview W7b/c/d | Ziehen: Platzhalter und Neigung am Ursprung, Geisterspur am gezogenen Teil, Einfügemarke am Ziel. | `PMEL.E8.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 17.9 | bewegung 1, inseln | `plasmind/E8-drag-preview-w7b-c-d.html` |
| E20 | `uebergang` | Section transitions ★ | Drei Arten des Abschnittswechsels als Vorschau: Verwandlung, Wischen, Teilen. | `PMEL.E20.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.6 | bewegung 2, inseln | `plasmind/E20-section-transitions.html` |

## Effekte (`effekt`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| H1 | `hover` | Blobs follow the pointer | Weiche Zellen folgen dem Zeiger mit verschiedener Verzögerung und strecken sich in Bewegungsrichtung. **Nur als Muster in der Bibliothek; auf Seiten kein eigener Zeiger (S20).** | `PMEL.H1.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 14.4 | bewegung 2, inseln | `plasmind/H1-blobs-follow-the-pointer.html` |
| H2 | `hover` | Blobs dodge the pointer | Zellen bleiben an ihrem Platz und weichen aus, wenn der Zeiger nahe kommt. | `PMEL.H2.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 14.8 | bewegung 2, inseln | `plasmind/H2-blobs-dodge-the-pointer.html` |
| H3 | `hover` | Metaball fusion | Zellen verschmelzen bei Berührung zu einem Körper und lösen sich wieder; der Zeiger ist eine von ihnen. **Nur als Muster in der Bibliothek; auf Seiten kein eigener Zeiger (S20).** | `PMEL.H3.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.4 | bewegung 2, inseln | `plasmind/H3-metaball-fusion.html` |
| H4 | `hover` | Inversion surface ★ | Ein Blob am Zeiger kehrt alle Farben darunter um; die Fläche bleibt lesbar. **Nur als Muster in der Bibliothek; auf Seiten kein eigener Zeiger (S20).** | `PMEL.H4.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.0 | bewegung 2, inseln | `plasmind/H4-inversion-surface.html` |
| H8 | `hover` | 3D blob with light ★ | Geraymarchte, verformte Kugel mit Führungs- und Randlicht; sie blickt zum Zeiger und folgt ihm gedämpft. | `PMEL.H8.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 19.6 | bewegung 2, webgl | `plasmind/H8-3d-blob-with-light.html` |
| H11 | `hover` | Contour lines | Höhenlinien eines bewegten Felds; der Zeiger hebt einen Hügel, um den sich die Linien legen. | `PMEL.H11.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.4 | bewegung 2, inseln | `plasmind/H11-contour-lines.html` |
| H12 | `hover` | Cell trail ★ | Der Zeiger legt kleine Zellen ab, die anschwellen, zu einem Strang verschmelzen und vergehen. **Nur als Muster in der Bibliothek; auf Seiten kein eigener Zeiger (S20).** | `PMEL.H12.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 14.3 | bewegung 2, inseln | `plasmind/H12-cell-trail.html` |
| E5 | `hover` | Tooltip W4d | Tooltip folgt dem Zeiger seitlich, zeigt Bezeichnung und Wert in Mono, erscheint auch bei Tastaturfokus. | `PMEL.E5.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.0 | bewegung 1, inseln | `plasmind/E5-tooltip-w4d.html` |
| E15 | `hover` | Cursor CU1 | Ruhiger, straffer Blob am Zeiger: folgt, staucht beim Klick, verschmilzt mit Zellen. **Nur als Muster in der Bibliothek; auf Seiten kein eigener Zeiger (S20).** | `PMEL.E15.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 38.6 | bewegung 1, inseln | `plasmind/E15-cursor-cu1.html` |
| H5 | `klick` | Cell division on click | Ein Klick teilt eine Zelle über einen schmaler werdenden Hals; ein Klick ins Leere setzt eine neue. | `PMEL.H5.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.4 | bewegung 2, inseln | `plasmind/H5-cell-division-on-click.html` |
| E11 | `klick` | Tones W11d | Drei kurze Dreieckstöne durch einen Tiefpass wie ein Messgerät: Klick, Bestätigung, Hinweis. Nur nach einem Druck. | `PMEL.E11.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.4 | bewegung 1, inseln | `plasmind/E11-tones-w11d.html` |

## Typografie (`typo`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| K3 | `akzent` | Zeichen am Wort der H1 | Ein selbst gezeichnetes Gewerk-Zeichen (Fuge, Glühbirne, Zollstock) an genau einem Wort der H1, in der Markenfarbe. | Kein Skript: `span.zw` um das Wort, darin `svg.zeichen` (`aria-hidden`, `currentColor`) mit `zeichen--unter` oder `zeichen--hinter`. Größe in `em`, wächst mit der Schrift. | 14.6 | bewegung 0, statisch | `kunden/K3-zeichen-am-wort.html` |
| E4 | `akzent` | Text selection W2d2 | Markierter Text bekommt eine Leuchtspur mit weicher, klar sichtbarer Kante an beiden Enden. | `PMEL.E4.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.3 | bewegung 1, inseln | `plasmind/E4-text-selection-w2d2.html` |
| E16 | `wechsel` | Counting numbers | Zahlen zählen hoch, sobald sie ins Bild kommen, mit Wiederholung; reduziert sofort der Endwert. Geprüft 14.10.2026: Das Skript baut die Zahlen erst zur Laufzeit, der Endwert steht nicht im HTML. Nur mit Endwert im HTML einsetzen (S19, BE21). | `PMEL.E16.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 15.1 | bewegung 1, inseln | `plasmind/E16-counting-numbers.html` |
| F5 | `wechsel` | Zahlentafel | Vier Kacheln mit zählenden Beispielzahlen und Verlaufslinien. | Demo, Thema über `data-theme` | 15.2 | bewegung 1, inseln | `plasmind/F5-live-board.html` |

## Farbe und Material (`farbe`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| H6 | `textur` | Soft noise | Langsames Wolkenrauschen in den Palettentönen mit feinem Korn; der Zeiger schiebt es beiseite. | `PMEL.H6.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 14.8 | bewegung 3, inseln | `plasmind/H6-soft-noise.html` |
| B4 | `textur` | Cell pattern | Wabenraster aus kleinen Zellen für Fußzeilen und Flächen. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 159.4 | bewegung 0, statisch | `plasmind/bilder/B4-dark.svg (+ -light, .png)` |

## Art-Styles (`artstyle`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| H9 | `wireframe` | CSS 3D blob | Drahtkugel aus Ringen in CSS 3D mit leuchtendem Kern; leichte Alternative ohne WebGL. | `PMEL.H9.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 16.1 | bewegung 2, inseln | `plasmind/H9-css-3d-blob.html` |

## Medien (`medien`)

| Kennung | Unterart | Name | wofür | Parameter | KB | braucht | Datei |
|---|---|---|---|---|---|---|---|
| B1 | `grafik` | Hero mit Logo W12 ★ | Logo W12 (gestapelt) auf einem Feld aus weichen Zellen. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 10.2 | bewegung 0, statisch | `plasmind/bilder/B1-dark.svg (+ -light, .png)` |
| B1a | `grafik` | Hero with logo, alive | Logo W12 auf der hellen Fläche: Der Blob atmet, die Augen folgen dem Zeiger ein wenig, die Zeile erscheint Reihe für Reihe, der erste Klick teilt den Blob. | `PMEL.B1a.init(el,{theme})`, `setTheme`, `destroy`; Farben als CSS-Variablen | 13.6 | bewegung 2, inseln | `plasmind/B1a-hero-with-logo-alive.html` |
| B2 | `grafik` | Colony field | 34 Zellen mit Augen, Fäden zu Nachbarn, Signalpunkte. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 23.9 | bewegung 0, statisch | `plasmind/bilder/B2-dark.svg (+ -light, .png)` |
| B3 | `grafik` | Growth rings | Wachstumsringe aus ineinanderliegenden Zellkonturen. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 38.1 | bewegung 0, statisch | `plasmind/bilder/B3-dark.svg (+ -light, .png)` |
| B5 | `grafik` | Rendered blob ★ | Glänzender Blob mit Augen, Verläufe für Licht, Randlicht, Glanz, Schatten. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 2.6 | bewegung 0, statisch | `plasmind/bilder/B5-dark.svg (+ -light, .png)` |
| B6 | `grafik` | Inversion plane | Dieselbe Szene zweimal, die zweite mit vertauschten Farben, mit drei Blobformen beschnitten. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 103.6 | bewegung 0, statisch | `plasmind/bilder/B6-dark.svg (+ -light, .png)` |
| B7 | `grafik` | Division strip | Fünf Phasen einer Zellteilung über einen schmaler werdenden Hals. SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 8.8 | bewegung 0, statisch | `plasmind/bilder/B7-dark.svg (+ -light, .png)` |
| B8 | `grafik` | Metaball merge | Verschmelzende Zellen per SVG-Filter (Weichzeichnen plus Schwellwert). SVG und PNG, dunkel und hell. | SVG und PNG, `-dark` und `-light` | 0.9 | bewegung 0, statisch | `plasmind/bilder/B8-dark.svg (+ -light, .png)` |
| K2 | `video` | Pause-Knopf mit Dauer am Video | Stummer Film als Schleife, links unten Pause und Ganzer Film mit der Dauer aus der Datei; bei reduzierter Bewegung steht das Standbild. | `figure[data-g8]` mit `video`, `button[data-g8-pause]` und `button[data-g8-ganz]`. Das Skript startet den Film (kein `autoplay`), hält ihn außerhalb des Bildes (unter 25 %) und im verdeckten Tab an und liest die Dauer aus der Datei. Ohne Skript steht das Poster. | 19.5 | bewegung 0, statisch | `kunden/K2-pause-knopf-am-video.html` |
| F2 | `video` | Video bei Hover | Standbild der Blob-Ansicht, das bei Hover oder Fokus als stummes Video läuft (Bildfolge als Rückfall). | Demo, Thema über `data-theme` | 13.8 | bewegung 1, inseln | `plasmind/F2-video-hover.html` |

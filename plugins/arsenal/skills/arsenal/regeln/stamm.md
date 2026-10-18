# Stamm

Gilt für jede Website und jede Anwendung, auf jeder Stufe. Wird immer geladen. Für die Art `anwendung` gelten nicht: S03, der Teil „ohne Skript“ von S19 (dort S17 und SW03), S39 (dort SW02, SW07, SW12, SW13) und S41.

**Lesart.** Jede Regel ist Ermessen mit Prüffrage. Wer abweicht, schreibt den Grund mit Datum ins ARMOURY. **Pflicht** steht nur bei Recht, Datenschutz, Sicherheit, Barrierefreiheit und Lizenz sowie bei den festen Regeln von <dein-name> (Bilder S34, S35; Startseite als Weiche PR05; alle Projekte PR10; KI-Fotos nur nach Frage S06; Systemzeiger S20; Bewegung S42 bis S50). Zahlen sind Richtwerte, außer bei Pflicht und Budget. Regeln aus den Entscheidungen E1 bis E11, die hier nicht als Pflicht stehen (etwa S23, S25), sind Ermessen nach dem Grundsatz von <dein-name>; Abweichung mit Grund im ARMOURY. Budgets je Stufe stehen in `regler.md`. Im Zweifel <dein-name> fragen (über den Overseer), nicht selbst festlegen.

## Haltung

- **S01 Einfachheit.** Viel Weißraum, in jeder Farbe. Nichts Überladenes, nichts Reißerisches. Prüffrage: Was kann weg, ohne dass die Seite schwächer wird?
- **S02 Eine Idee aus der Sache.** Die Gestaltung folgt einer Idee aus Leistung oder Gewerk (Werkstoff, Werkzeug, Arbeit), nicht aus einem Trend. Prüffragen: Lässt sich „Die Seite sieht so aus, weil …“ mit der Leistung beenden? Passt die Bühne noch, wenn man das Logo eines Wettbewerbers einsetzt (Austauschprobe)? Dann ist sie zu allgemein.
- **S03 Eine kühne Stelle.** Jede Seite hat genau eine benannte kühne Stelle. Die Politur bewahrt sie. Wer sie streicht, baut eine neue.
- **S04 KI-Reflex prüfen.** Merkmale des KI-Looks sind nicht verboten: Lila-Blau-Verlauf, Verlaufstext, Glas als Schmuck, gleiche Icon-Karten, Karte in Karte, Akzentbalken an Karten, Pille über der Hauptzeile, Hero-Kennzahl-Vorlage, Mono als Kostüm, Emoji als Icons. Prüffrage: Hat das Element hier eine Aufgabe, oder ist es Gewohnheit? Erst die Häufung verrät die Vorlage. Werkzeug: `npx impeccable detect` (Befehl `audit`).

## Inhalt und Wahrheit

- **S05 Inhalt vor Layout.** Gestaltet wird mit echtem Text und echtem Material. „Fertig“ heißt: kein Platzhalter, auch kein versteckter.
- **S06 Pflicht (Recht): nichts erfinden.** Keine Zahl, kein Name, keine Kundenstimme, kein Siegel und keine Bewertung ohne Quelle. Kundenstimmen nur echt und freigegeben; kein Kundenname und keine Kundenarbeit als Referenz ohne Freigabe des Kunden. Kein Bild gibt sich als echte Kundenarbeit, Werkstatt oder Person aus, wenn es das nicht ist. Echte KI-Fotos erst nach einer Frage an <dein-name> (E11, ME04).

## Recht, Datenschutz, Sicherheit

- **S07 Pflicht (Recht).** Impressum (DDG § 5) und Datenschutz (DSGVO Art. 13) sind höchstens zwei Klicks entfernt, verlinkt im Fuß jeder Seite. Jedes Formular trägt einen Hinweis mit Link zur Datenschutzerklärung. Die Texte entstehen aus den Angaben des Kunden; <dein-name> gibt sie frei.
- **S08 Pflicht (Recht).** Eine Einwilligung (TDDDG § 25) kommt vor dem ersten nicht nötigen Aufruf. Ablehnen und Annehmen sind gleich stark, nichts ist vorab angehakt. Besser: Die Seite braucht keinen. Richtwert (kein Teil der Pflicht): Der Hinweis deckt höchstens ein Drittel der Fläche, mobil eine schmale Leiste. Prüffrage: Verdeckt er mehr Inhalt als nötig?
- **S09 Pflicht (Datenschutz).** Schriften, Skripte und Bilder liegen auf dem eigenen Server. Ausgenommen ist nur die Vorschau als Claude-Artefakt (TE16); was ausgeliefert wird, folgt S09. Keine Tracker. Formulare laufen über <internal-project>-Formulare; Fremddienste nur mit Freigabe je Fall.
- **S10 Pflicht (Sicherheit).** `Content-Security-Policy` mit `script-src 'self'` und `frame-ancestors 'self'` (als Kopfzeile oder auf dem `<meta>`-Weg nach TE05; `frame-ancestors` immer als Kopfzeile), dazu die Kopfzeilen `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`. Kein Inline-Skript (Thema- und Intro-Skript: Vorliebe in `behavior.md`, TE08). Probe: Antwortkopf und `<meta>` prüfen, Konsole ohne „Refused“.
- **S11 Pflicht (Lizenz).** Jede fremde Datei hat Quelle, Urheber, Lizenz, Suchbegriff und Bearbeitung in der Medientabelle des Laufs (`material/MEDIEN.md`, ME07); in der Galerie steht das in `HERKUNFT.md` der Kachel. Die Lizenz wird vor der Nutzung neu geprüft.

## Barrierefreiheit (Pflicht)

- **S12 WCAG 2.2 AA.** Grundgerüst: genau ein `main`, genau eine `h1`, Skip-Link als erstes Fokusziel, `lang`, Überschriften in Reihenfolge, Zoom frei. Echte `button` und `a`, Labels an Feldern, Alt-Texte, `aria-label` an Symbolknöpfen. Probe: axe vollständig (mit `region` und `landmark-*`) ohne Verstoß, ein Tastaturdurchlauf und die Probe Textabstand (WCAG 1.4.12: Test-CSS mit Zeilenhöhe 1,5, Absatzabstand 2, Buchstabenabstand 0,12 und Wortabstand 0,16 je Schriftgröße; nichts abgeschnitten).
- **S13 Fokus** ist sichtbar und nie verdeckt: `:focus-visible`, nie `outline: none` ohne Ersatz.
- **S14 Kontrast** 4,5 : 1, große Schrift 3 : 1, ungerundet. Er gilt auch auf Bildern, im hellsten und dunkelsten Bild einer Bewegung und in Hell und Dunkel. Ein knapper Wert bei dünner Schrift gilt als nicht bestanden.
- **S15 Farbe allein** trägt nie Bedeutung (Graustufenprobe).
- **S16 Tippziele** sind mindestens 44 × 44 px groß.
- **S17 Reduzierte Bewegung** ist eine vollständige Gestalt: Poster, Endzustände, alle Inhalte sichtbar. Große Bewegung wird Überblenden oder Stand, Rückmeldung bleibt. Die Abfrage wirkt je Effekt, auch in Skripten (`matchMedia`). Probe: Unter `reduce` laufen höchstens 20 % der Animationen des Normalwerts oder höchstens zwei, Videos 0.
- **S18 Pause.** Was länger als 5 s von selbst läuft, hat einen Pause-Knopf (WCAG 2.2.2). Nichts blitzt öfter als dreimal je Sekunde (2.3.1).
- **S19 Inhalt ohne Skript.** Jeder Text und jede Zahl steht mit Endwert im HTML. Eine Einblendung von Inhalt startet nie unsichtbar: Deckkraft 0, Maske, `clip-path`, `stroke-dashoffset`, `scale` unter 0,5 und ein Bild oder Video, das beim Eintritt ins Bild noch fehlt (ohne Poster oder Grundfläche), zählen als unsichtbar; natives `loading="lazy"` mit `width`, `height` und Grundfarbe ist erlaubt (S36). Ausgenommen sind Schmuck und der Wortwechsel nach BE19: Alle Wörter stehen im HTML, das Wort mit dem Versprechen steht bei reduzierter Bewegung. Beim Zurückscrollen verschwindet nichts. Probe: Fotos nach `load` und Ladefolge Abschnitt für Abschnitt beim Scrollen gegen das Foto nach vollem Scrollen, 0 fehlende Inhalte; dazu ein Ganzseitenfoto mit abgeschaltetem JavaScript, jeder Text und jede Zahl mit Endwert da.
- **S20 Pflicht (<dein-name>): Der Systemzeiger bleibt.** Kein eigener animierter Zeiger, weder als Ersatz noch daneben: kein Schmuck, der als Punkt, Form oder Spur am Zeiger hängt und ihm folgt. Flächen, die auf den Zeiger reagieren (Spotlicht, ausweichende Formen), und ein Tooltip mit Information sind kein Zeiger.

## Ordnung

- **S21 Keine zufällige Platzierung.** Jedes Element steht auf einem Raster und hängt an einer sichtbaren Ordnung (Linie, Kante, Achse). Symmetrie ist frei. Prüffrage: Kann jedes Element seine Achse nennen?
- **S22 Abstände.** Grundeinheit 4 oder 8 px. Innen kleiner als außen (Richtwert Faktor 2), über einer Überschrift mehr als darunter. Richtwert: etwa acht Abstandswerte je Seite.
- **S23 Eckenradius** ist frei, höchstens drei Werte je Seite.
- **S24 Weißraum ist Gestaltung, ein Loch ist ein Mangel.** Ein Loch ist leerer Grund ohne Absicht, etwa eine leere Phase im Pin. Richtwert: leere Fläche nach einem Abschnitt höchstens etwa ¼ Bildschirmhöhe. Prüffrage: Trägt diese Fläche Ruhe, oder fehlt hier etwas?

## Typografie

- **S25 Höchstens zwei Familien**, gezählt nach sichtbarem Anteil, mit Kontrast in einer Achse. Fraunces, Space Grotesk und DM Sans nur mit Begründung im ARMOURY (E5). Inter, Roboto und Open Sans sind Vorgabe-Reflexe; sie brauchen eine bewusste Skala und Paarung.
- **S26 Eine Skala.** Größen aus einer Skala mit Verhältnis ab 1,25 (Anwendungen enger, SW15), Richtwert höchstens sieben Größen. Hierarchie in mindestens zwei Achsen (Größe, Gewicht, Abstand, Farbe, Lage). Die H1 ist die größte Textzeile der ersten Ansicht; ein Plakatwort (PR02) in der ersten Ansicht ist darum Teil der H1 oder kleiner als sie.
- **S27 Lesen.** Fließtext 16 bis 22 px bei 1440, ab 16 px bei 390, nichts unter 14 px. Zeilenhöhe 1,5 bis 1,6, große Zeilen 1,0 bis 1,2. Zeilenlänge 45 bis 75 Zeichen, Ziel 66 (`max-width` in `ch`).
- **S28 Laufweite.** Versalien +0,02 bis +0,08 em. Große Zeilen 0 bis −0,03 em, kaum je unter −0,04 em. Plakatwörter 0 bis −0,01 em. Prüffrage: Berühren sich Buchstaben im 2-fach-Ausschnitt?
- **S29 Deutsche Mikrotypografie.** „So“ und ‚so‘, Halbgeviertstrich für Bereiche (10–12 Uhr), schmales geschütztes Leerzeichen (z. B., 12 kg), `…`, Tabellenziffern bei Zahlen in Spalten. Gedankenstriche im Satz meiden: Punkt oder Komma. Überschriften in normaler Schreibung statt Title Case. Prüffrage: Liest es sich wie gut gesetztes Deutsch? `text-wrap: balance` für Überschriften, `pretty` für Absätze.

## Farbe

- **S30 OKLCH.** Neutraltöne getönt statt reinem `#000` und `#fff`, Verläufe in OKLCH. Prüffrage: Wirkt reines Schwarz oder Weiß hier hart, oder ist es gewollt? Die Strategie wählt der Regler `farbe`.
- **S31 Herkunft der Farbe.** Farbe kommt aus dem Gegenstand des Kunden (Werkstoff, Ort, Marke), nicht aus dem Branchenklischee. Ob Hell oder Dunkel, entscheidet ein Satz zur Nutzungsszene: wer, wo, bei welchem Licht.
- **S32 Signalfarbe** nur für die Hauptaktion (KONFLIKTE K2, entschieden 18.10.2026).
- **S33 Hell und Dunkel.** `color-scheme` ist bewusst gesetzt. Die Seite ist in beiden Systemmodi lesbar und sieht gewollt aus. Richtwert: höchstens ein Wechsel zwischen hellen und dunklen Abschnitten je Bildschirmhöhe.

## Bilder (Quellen und Video: Modul Medien)

- **S34 Pflicht (<dein-name>): scharf.** Kein verpixeltes oder niedrig auflösendes Bild oder Video. Die Quelle ist mindestens Anzeigegröße × 2. Was das nicht schafft, fliegt raus und wird nie hochskaliert. Bildschirmfotos von Websites entstehen mit `deviceScaleFactor` 2. Probe: Auflösungstabelle, 0 zu klein.
- **S35 Pflicht (<dein-name>): Bezug.** Bilder und Filme zeigen erkennbar die Leistung. Je Bild steht ein Klartext bereit: „zeigt …, für …“.
- **S36 Einbindung.** Jedes Bild hat `width` und `height`; Rasterbilder sind WebP oder AVIF, Grafik gern SVG; unter der ersten Ansicht `loading="lazy"`; das LCP-Bild trägt `fetchpriority="high"`.

## Handy

- **S37 Eigene Komposition.** 390 px ist eigens gestaltet, nicht verkleinert. Kein Querüberlauf bei 320 und 390 px, Textrand ab 16 px. Der Hauptknopf liegt im Daumenbereich (unteres Zwei-Drittel) oder in einer festen Leiste. Das Leitmotiv ist vollständig im Bild.

## Leistung

- **S38 Budget ist Grenze, kein Ziel.** Ein Wert im Budget genügt. Gemessen wird als Median aus drei Läufen ohne Cache an der Vorschau-Adresse, dazu einmal mit Cache.
- **S39 Kein Ladeschirm, kein Tor.** H1 und Knopf stehen ohne Skript und spätestens nach 1,2 s. Das LCP-Element ist H1, Poster oder ein Bild im Budget, nie ein laufendes Video. Fixiert sind höchstens Kopf und mobile Handlungsleiste; zum Kopf gilt die Vorliebe in `behavior.md`.
- **S40 Auslieferung.** Kompression (gzip oder brotli) und Cache am Server; kritisches CSS im Kopf, Bibliotheken nach `load`.

## SEO-Grundlagen

- **S41 Auffindbar.** Seitentitel 30 bis 65 Zeichen mit Kategorie, bei örtlichen Betrieben mit Ort. Eine Beschreibung je Seite, sprechende Adressen. Strukturierte Daten, wo sie passen (Ratgeber: TX09). Demos und Vorschauen tragen `noindex` und eine sperrende `robots.txt`.

## Bewegung

S42 bis S50 sind Pflicht für jede Animation (<dein-name> 18.10.2026). Sie gelten auf Websites, in Anwendungen und in der plasmind-Fenster-App, auf jeder Stufe des Reglers `bewegung`. Bei `bewegung: 0` gibt es nur Sofortwechsel.

- **S42 Easing statt linear.** Rein ease-out, raus ease-in, Ortswechsel ease-in-out. Linear nur für Fortschritt, der echter Zeit oder dem Scroll folgt, und für Schleifen (Ladezeichen, Laufband).
- **S43 Spatial Consistency.** Jedes Element hat einen Ort, an dem es lebt. Es öffnet aus seinem Auslöser oder seiner Heimatkante (`transform-origin` am Auslöser oder geteilter Übergang) und schließt dorthin zurück; Öffnen und Schließen sind Spiegelbilder. Vorbild: iOS-Lautstärke am Knopf, App-Start aus dem Icon, Kontrollzentrum von oben, Dynamic Island. Prüffrage: Sieht man allein an der Bewegung, wo das Element lebt und wie man es zurückbringt?
- **S44 Raus schneller als rein.** Der Austritt dauert etwa 70 % des Eintritts.
- **S45 Dauer nach Strecke und Größe** (Tabelle unten). Nie eine Dauer für alles.
- **S46 Kontinuität.** Wechselt ein Element Zustand oder Ort, verwandelt es sich (Vorschau wird Großbild, Karte wird Detail), statt zu verschwinden und neu zu erscheinen. Geteilte Übergänge nur für die ein bis zwei Elemente, die die Bedeutung tragen.
- **S47 Unterbrechbar und direkt.** Bewegung folgt Finger oder Zeiger, lässt sich mittendrin aus aktueller Lage und Geschwindigkeit umkehren und sperrt nie die Eingabe.
- **S48 Staffelung für Ordnung.** Gruppen dürfen um 20 bis 40 ms je Element versetzt auftreten, damit die Lesereihenfolge sichtbar wird; gedeckelt, sodass die Gruppe schnell fertig ist. Nie bei etwas, auf das der Nutzer wartet.
- **S49 Rückmeldung sofort.** Jeder Tipp, Klick oder Tastendruck zeigt binnen 100 ms eine sichtbare Antwort, auch wenn das Ergebnis länger braucht.
- **S50 Wann nicht animieren.** Häufige, absichtliche Aktionen geschehen sofort, ohne Animation:
  - Wechsel zwischen Tabs, Ansichten und Bereichen, die man ständig wechselt (etwa Agent Control Center und Graph View in plasmind);
  - Tastenkürzel und Befehlspalette, auch ihr Öffnen;
  - Kontextmenüs, Aufklapplisten und Menüs (höchstens ein sehr kurzes Ausblenden beim Schließen);
  - Start einer App oder eines Werkzeugs: kein künstliches Warten, kein Intro, das länger dauert als das Laden;
  - Tippen, Markieren, selbst gesteuertes Scrollen und Ziehen, der Zeiger selbst: nie geglättet oder verzögert (S20; Nachlauf von Schmuck in Scroll-Szenen: BE12);
  - Massenaktionen (Löschen, Abhaken, Blättern): sofort oder mit kurzem Zustandswechsel;
  - Rückgängig, Wiederholen, Fehlerkorrektur;
  - alles auf dem schnellen Weg geübter Nutzer: Was ein Experte zehnmal je Minute tut, animiert nicht.

  Je häufiger eine Aktion, desto weniger Bewegung; bei „mehrmals am Tag“ ist die Antwort null. Prüffrage: Tut der Nutzer das oft und mit Absicht, um ans Ziel zu kommen? Dann keine Animation. Im Zweifel zählen, wie oft.
- **S51 Günstige Eigenschaften.** Animiert werden `transform`, `opacity` und `clip-path`; `filter` (Schärfe) und Schatten nur auf kleinen Flächen und gegen den Leerlauf gemessen (TE12). Prüffrage: Löst die Animation Layout aus (Breite, Höhe, Abstand, Lage)? Dann anders lösen. Schmuck-Striche in SVG (`stroke-dashoffset`) sind ausgenommen. `transition: all` vermeiden, es animiert ungewollt mit.

| Weg | Dauer | Kurve (Material Design 3) |
|---|---|---|
| Rückmeldung (Druck, Zustand) | unter 100 ms | `cubic-bezier(0.2, 0, 0, 1)` |
| kleine Wege (Schalter, Tooltip) | 100 bis 200 ms | rein `cubic-bezier(0.05, 0.7, 0.1, 1)`, raus `cubic-bezier(0.3, 0, 0.8, 0.15)` |
| große Flächen, lange Wege (Blatt, Vollbild) | 250 bis 400 ms | rein und raus wie oben, Ortswechsel `cubic-bezier(0.2, 0, 0, 1)` |
| Inszenierung (Ladefolge, Einstieg), ab `bewegung: 2` | bis 1.200 ms | Modul Bewegung |
| Staffel je Element | 20 bis 40 ms | – |

Ein Satz aus Kurven und Dauern je Projekt, als CSS-Variablen im MASK: `--kurve-rein`, `--kurve-raus`, `--kurve-ort`, `--dauer-rueckmeldung`, `--dauer-klein`, `--dauer-gross`, `--dauer-inszenierung`, `--staffel`, dazu `--kurve-ueberschwingen` nur für die Ausnahmen nach BE05; Dauern nur in den Stufen von Material Design 3: 50, 100, 150, 200 ms; 250, 300, 350, 400 ms; 450, 500, 550, 600 ms; 700, 800, 900, 1.000 ms; Inszenierung bis 1.200 ms. Austrittsdauern (`--dauer-klein-raus` usw.) sind etwa 70 % der Eintrittsdauer, gerundet auf die nächste Stufe (S44). Andere Werte werden nicht erfunden.

## Formulare

- **S52 Felder.** Das Label steht sichtbar außerhalb des Felds; ein Platzhalter ersetzt es nicht (Pflicht, Barrierefreiheit). Jedes Feld mit `name`, `autocomplete`, passendem `type` und `inputmode`; Einfügen nie gesperrt; Pflichtfelder gekennzeichnet. Mehr als fünf Felder in Gruppen mit Titel, Folgefelder erst nach ihrem Auslöser. Der Senden-Knopf bleibt aktiv, bis die Anfrage startet; bei Fehlern springt der Fokus zum ersten Fehler.

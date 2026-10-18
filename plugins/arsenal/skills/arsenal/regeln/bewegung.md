# Modul Bewegung

Laden ab `bewegung: 1`. Die Regeln für jede Animation stehen im Stamm (S17 bis S20, S42 bis S51; Pflicht sind S42 bis S50). Hier steht nur, was dazukommt. Code: `rezepte/scroll.md`, `rezepte/oberflaeche.md`.

## Zweck

- **BE01 Bedienbewegung** (Knöpfe, Formulare, Zustände, jede Bewegung in Anwendungen; Menüs öffnen sofort, S50) erfüllt eine von vier Aufgaben: Orientierung, Beziehung zwischen Ansichten, Rückmeldung, Aufmerksamkeit. Prüffragen: Welche Aufgabe? Antwortet sie sofort, ohne Warten?
- **BE02 Markenbewegung** (Leitmotiv, Einstieg, Scroll-Choreografie) besteht den Markentest. Erstens: Ist sie aus dem Gegenstand gebaut (Material, Zeichen, Werkzeug, Zahl des Kunden), oder könnte sie auf jeder Seite stehen? Zweitens: Verliert die Seite ohne sie Charakter, nicht nur Schmuck? Drittens: Steht der Inhalt ohne sie (S19), und bleibt sie im Budget? Wer besteht, braucht keine weitere Begründung. „Die Seite ist auch ohne sie verständlich“ ist kein Befund.
- **BE03 Ab `bewegung: 2` bewegt sich die Seite wirklich:** eine benannte Signatur-Bewegung, bei `3` eine Choreografie mit einem Faden durch alle Abschnitte (eine Linie, eine Bahn, eine Scheibe). Eine Markenseite, die nur einblendet, ist ein Mangel. Nicht überall dieselbe Einblendung.

## Kurven und Dauern

- **BE04 Ein System je Vorhaben:** Kurven, Dauern und Variablen nach der Tabelle im Stamm; Inszenierung (`--dauer-inszenierung`, bis 1.200 ms) mit der Eintrittskurve.
- **BE05 Kein Überschwingen als Standard** (Bounce, Elastic). Ausnahme eins: eine gefeierte Stelle je Seite (ein Erfolg). Ausnahme zwei: der Aufbau eines Overlays, das nichts verschiebt; einmal beim Erscheinen, Rückweg ohne Überschwingen, keine genau zu lesende Rückmeldung. Ein Überschwing-Token für alle Fälle. Decke: Beschriftung bewegt sich unter 1 px, Stauchung unter 10 %, Fläche unter 3 %.
- **BE06 Gesten**, die mittendrin unterbrechbar sein müssen (Ziehen, Wischen), laufen mit einem Federmodell (Apple `interactiveSpring`: response 0,15, dampingFraction 0,86). Alles andere läuft mit festen Kurven.

## Erste Ansicht und Ladefolge

- **BE07 Einstiege zeigen, sie erzeugen nicht.** Bewegt wird sichtbarer Inhalt (Weg, Größe ab 0,5, Schärfe, Schatten), mit ease-out aus einem schon sichtbaren Zustand (S19). Masken und `clip-path` nur für Schmuck und für den Wortwechsel (BE19).
- **BE08 Eine Dauerbewegung.** Richtwert: In der ersten Ansicht bewegt sich ohne Eingabe höchstens ein Element neben einem Wortwechsel, das Leitmotiv. Alles andere wartet auf den Scroll.
- **BE09 Intro** (Vorspann vor der ersten Ansicht): Häufigkeit, Überspringen und reduzierte Bewegung nach der Vorliebe in `behavior.md`. Es wartet nie länger, als das Laden dauert (S50); H1 und Knopf stehen nach höchstens 1,2 s (S39).
- **BE10 Blickfänge.** Richtwert: höchstens drei benannte je Seite.
- **BE11 Höchstens zwei Techniken je Vorhaben**, etwa Video plus Scroll-Choreografie. Shader-Hintergrund plus 3D-Held plus Choreografie plus Magnetknopf wirkt wie ein Vorführband.

## Scroll

- **BE12 Scroll-Kopplung linear** (`ease: 'none'`), höchstens 1 px Weg je px Scroll, auch für Kanten unter `clip-path`. Nachlauf (`scrub` als Zahl) nur für Schmuck. Prüffrage: Hinkt etwas hinterher, das man gerade liest oder bedient? Dann ohne Nachlauf (S50). Die Pin-Länge folgt aus dem Weg, nicht umgekehrt.
- **BE13 Die Deckkraft von Inhalt hängt nie am Scroll.** Text erscheint zeitgebunden ab seinem Auslöser und endet in voller Deckkraft; der Scroll darf ihn bewegen, nicht ausblenden. Nur Schmuck darf seine Deckkraft am Scroll ändern. Prüffrage: Ist der Text in jedem Scrollzustand ganz lesbar?
- **BE14 Pins.** Richtwert höchstens 200 % Höhe. Keine Pin-Phase zeigt leeren Grund; bei größter Ausdehnung zeigt die kühne Stelle das Versprechen. Absätze im Pin decken einander, sie blenden nicht über. Der Rand eines austretenden Elements liegt auf einer ganzen Pixelreihe, damit keine Haarlinie entsteht. Probe: Standbild je Pin-Viertel (0, 25, 50, 75, 100 %) und Nahtprobe am Pin-Rand bei 1440 und 390 in mindestens 25 Scrollschritten.
- **BE15 Zeichen und Text gehen im Pin gleich.** Das bewegte Zeichen steht in jedem Viertelbild an der Station des aktiven Schritts. Text zu einem WebGL-Objekt erscheint erst, wenn das Objekt liegt. Der letzte Schritt endet mit einem Höhepunkt.
- **BE16 Kreuzungsfreiheit.** Was sich bewegt (Bahn, Linie, Form), kreuzt nie sichtbaren Text, Knöpfe oder tragende Bilder und Filme, vorwärts und rückwärts, in jeder Scrollphase. Geprüft wird die Hülle des ganzen Zeichens; eine Linie zwischen Grundlinie und x-Höhe zählt als Kreuzung. Die Freiheit entsteht aus der Ebenenordnung (Ebenenplan im MASK), die Messung ist nur der Nachweis. Probe: Kreuzungsprobe über den ganzen Scrollweg bei 1440 und 390, Ergebnis 0.
- **BE17 Scrollen bleibt nativ:** kein weiches Scrollen, kein Kapern von Richtung oder Tempo (KONFLIKTE K4, entschieden 18.10.2026). Scroll-Szenen mit Pin bleiben erlaubt.

## Wechselnde Inhalte

- **BE18 Schmuck, nie Pflichtinhalt** (E10). Selbst wechselnde Wörter und Anzeigen tragen keine Information, die sonst fehlt. Richtwert: ein selbstlaufender Wechsel je Seite; Wechsel am Scroll zählen als Choreografie. Läuft er länger als 5 s, hat er einen Pause-Knopf (S18).
- **BE19 Wortwechsel.** Drei bis sechs Wörter, alle im HTML. Takt 1,8 bis 3 s, erster Wechsel frühestens nach 4 s. Das Wort mit dem Versprechen kommt zuletzt, hält mindestens zwei Takte und steht bei reduzierter Bewegung. Das neue Wort kommt in voller Deckkraft durch die Maske, nur das gehende darf ausblenden. Das Fenster ist höchstens 100 ms leer; die Maske endet auf der Unterlänge.
- **BE20 Walze.** An jeder Stelle des Fensters steht zu jedem Zeitpunkt höchstens ein Zeichen. Gleiche Wortteile stehen an fester Kante und drehen nie. Probe: Walzenprobe mit Standbildern alle 100 ms bei 1440 und 390, 0 Mischbilder, kein Fenster länger als 100 ms leer (BE19).
- **BE21 Eine Uhr je Anzeige.** Zahl, Name und Bild derselben Anzeige wechseln auf einer Zeitachse. Zähler starten am Endwert und landen dort. Am Telefon keine halb abgeschnittenen Ziffern und kein Loch über einer Zeilenhöhe; Probe: Walzenprobe bei 390.
- **BE22 Laufband.** Takt und Verhalten unter dem Zeiger nach der Vorliebe in `behavior.md`; ein Pause-Knopf hält es an (S18). Die Kopie für die Schleife trägt `aria-hidden`.

## Messen

- **BE23 Gegen Leerlauf messen.** Bewegung wird gegen einen Leerlauf gemessen, nie als Zahl allein; ohne Bildschirm verliert Chromium 20 bis 25 % der Bilder, es zählt nur der Unterschied. Filme zum Zeigen (Projekt- und Bildschirmfilme) entstehen mit virtueller Uhr (ER06); der Messfilm im `audit` läuft in Echtzeit. Werkzeuge in SKILL.md.

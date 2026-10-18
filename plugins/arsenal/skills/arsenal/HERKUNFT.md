# Herkunft des Regelwerks (Arsenal 3)

Herkunftstabelle des Regelwerks: jede Regel von Arsenal 3 mit ihrer Quelle oder „neu“. Nicht zu verwechseln mit der Medientabelle eines Laufs (`material/MEDIEN.md`) und mit der `HERKUNFT.md` einer Galerie-Kachel. Ein „?“ hinter einer Quelle heißt: Die Zuordnung ist wahrscheinlich, aber nicht wörtlich belegt. Stand 18.10.2026.

| Kürzel | Quelle |
|---|---|
| M1–M4 | <dein-name> 16.10.2026, vier feste Regeln |
| E1–E11, Grundsatz | Entscheidungen <dein-name> 16.10. (Grundsatz: Ermessen statt Verbot) |
| N6 | Nachtrag 6, <dein-name> 18.10.: Pflicht-Animationsregeln |
| Ov | Overseer: Auftrag (Hauptteil, Nachträge 1–6) und „Vom Overseer schon entschieden“ in ENTSCHEIDUNGEN.md |
| B1–B82, WF, AD | Kalibrierung: REGELN-final, WORKFLOW-VORSCHLAG, ARSENAL-DIFF (mit Abschnitt) |
| R01–R42 | Methode (plasmind webdesign) |
| A | Arsenal 2: Datei und Abschnitt; Nummern AF, AW, AT, AL, AG, AB, AR, AC wie in REGELN-HEUTE |
| I | impeccable 4.6.0 (Nummern wie in REGELN-HEUTE) |
| V | Vercel web-interface-guidelines (Nummern wie in REGELN-HEUTE) |
| H1–H6, VV | feste Vorlieben (behavior.md), Vault-Notizen |
| PK | Recherche PREMIUM-KONVERSION (P1–P6, K1–K8, Q…) |
| KONFLIKTE K1–K4 | Geschmacksfragen, entschieden nach Vorschlag A (<dein-name> 18.10.2026) |

Art: `übernommen`, `geschärft` (Zahl oder Probe dazu), `gelockert` (Verbot → Ermessen), `zusammengeführt`, `neu`.

## regeln/stamm.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| S01 | Einfachheit, viel Weißraum | Ov, B11, A AF11 | zusammengeführt |
| S02 | Eine Idee aus der Sache | PK P1, R40, B1, B2 | zusammengeführt |
| S03 | Genau eine kühne Stelle | R42, B28, B69 | zusammengeführt |
| S04 | KI-Reflex prüfen, kein Bann | Grundsatz, R22, I8, I10, A AG4 | gelockert |
| S05 | Inhalt vor Layout | A AW1, R37, B31 | zusammengeführt |
| S06 | Nichts erfinden, Referenzen nur mit Freigabe, KI-Fotos nach Frage | R25, B31, A AW-P, R17, E11 | zusammengeführt |
| S07 | Impressum, Datenschutz erreichbar, Hinweis am Formular | A AW-P, A AW8, R34 | zusammengeführt |
| S08 | Einwilligung vor Aufruf | A AW-P, R11 | geschärft |
| S09 | Selbst hosten, keine Tracker | R31, R33, B35, A AT3, neu (<internal-project>-Formulare) | zusammengeführt |
| S10 | Sicherheits-Kopfzeilen (CSP auch als `<meta>` nach TE05), kein Inline-Skript | A stack §7 (CSP), R31, H6, neu | geschärft |
| S11 | Lizenznachweis je fremder Datei | B32, R33, A AW7 | zusammengeführt |
| S12 | WCAG 2.2 AA, Probe Textabstand | R27 (mit WCAG 1.4.12), A AL8, V1 | zusammengeführt |
| S13 | Fokus sichtbar | V2 | übernommen |
| S14 | Kontrast 4,5 : 1 | A AF7, R28, A AL4 | zusammengeführt |
| S15 | Farbe trägt nichts allein | A AF8 | übernommen |
| S16 | Tippziele mindestens 44 px | R10, Ov, PK K3 ? | geschärft |
| S17 | Reduzierte Bewegung vollständig | B23, A AB4, A AL1, A AG5, R23 | zusammengeführt |
| S18 | Pause-Knopf, kein Blitzen | B25, A AB5, V4 | zusammengeführt |
| S19 | Inhalt ohne Skript sichtbar | B24, R08, R35, A AW13 | geschärft |
| S20 | Pflicht (<dein-name>, N6): Systemzeiger bleibt, kein eigener animierter Zeiger | N6, KONFLIKTE Hinweis 1 | neu |
| S21 | Raster statt Zufall | A AF1, A AF12, B72, E7 | gelockert |
| S22 | Abstände im 4/8-px-Raster | A AF2, A AF14 | übernommen |
| S23 | Eckenradius frei, höchstens drei | E8, R22 | gelockert |
| S24 | Weißraum ja, Loch nein | B27, B28, R35, B11 | zusammengeführt |
| S25 | Höchstens zwei Schriftfamilien | A AF5, A AT1, B35, B63, R06, E5, I11 | zusammengeführt |
| S26 | Eine Größenskala, klare Hierarchie | A AF3, A AF6, I5, R02, R06, E6 | zusammengeführt |
| S27 | Lesegröße und Zeilenlänge | A AF4, R06, R39, I5 | zusammengeführt |
| S28 | Laufweite Versalien, Zeilenabstand | A AT2, B39, R06 | zusammengeführt |
| S29 | Deutsche Mikrotypografie | A AF10, V5, V16, R21, Ov | gelockert |
| S30 | OKLCH, getönte Neutraltöne | A AG1, A AF9, I3 | gelockert |
| S31 | Farbe aus dem Gegenstand | I4, R13, PK P1 ? | zusammengeführt |
| S32 | Signalfarbe nur Hauptaktion | R05, B12, KONFLIKTE K2 | zusammengeführt |
| S33 | Hell und Dunkel bewusst, ein Wechsel je Bildschirmhöhe | R29, R20, V12, H2 | zusammengeführt |
| S34 | Bilder scharf | M1, B33, B77, PK P2 | übernommen |
| S35 | Bild zeigt die Leistung | M4, B75 | übernommen |
| S36 | Bildeinbindung, Format, lazy | V7, R32 | zusammengeführt |
| S37 | Handy eigens komponiert | R10, B26, PK P6 | zusammengeführt |
| S38 | Budget ist Grenze | B40, R30, PK K7, Ov | geschärft |
| S39 | Kein Ladeschirm, kein Tor | B11, B34, B42, PK K7, H1 | zusammengeführt |
| S40 | Kompression, Cache, kritisches CSS | B82, A stack §6 ?, A performance ? | übernommen |
| S41 | Auffindbar: Titel, Beschreibung, noindex | R02, R31, neu | zusammengeführt |
| S42 | Easing statt linear | N6 | neu |
| S43 | Räumliche Folgerichtigkeit | N6 | neu |
| S44 | Raus schneller als rein | N6 | neu |
| S45 | Dauer nach Strecke | N6 | neu |
| S46 | Kontinuität bei Zustandswechsel | N6 | neu |
| S47 | Unterbrechbar und direkt | N6, V4 | neu |
| S48 | Staffelung schafft Ordnung | N6 | neu |
| S49 | Rückmeldung binnen 100 ms | N6 | neu |
| S50 | Wann nicht animieren | N6 | neu |
| S51 | Günstige Eigenschaften | A AG2, I7, V4, A non-negotiables | gelockert |
| S52 | Formularfelder (für Websites und Anwendungen) | V3, A software Regel 11, A ia-and-structure §4, PK K3, R27 | zusammengeführt |

## regeln/bewegung.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| BE01 | Bedienbewegung: vier Aufgaben | A motion-doctrine §2 (AB1), N6 | übernommen |
| BE02 | Markentest statt Bremse | Grundsatz, R08, R23, A AB1, Ov Nachtrag 5 | gelockert |
| BE03 | Ab Stufe 2 wirklich bewegen | A AR2, B20, B30 ? | zusammengeführt |
| BE04 | Ein Token-System je Vorhaben | B21, A motion-doctrine §3 (AB2), Ov | zusammengeführt |
| BE05 | Kein Überschwingen als Standard | B21, A motion-doctrine §4 (AB3), I7 | zusammengeführt |
| BE06 | Federmodell für Gesten | A motion-doctrine §4 und Checkliste | übernommen |
| BE07 | Einstiege zeigen, nicht erzeugen | B24, N6 ? | zusammengeführt |
| BE08 | Eine Dauerbewegung | B20 | gelockert |
| BE09 | Intro einmal, überspringbar | H5, B42, B11, N6, KONFLIKTE Hinweis 2 | zusammengeführt |
| BE10 | Höchstens drei Blickfänge | B21 | gelockert |
| BE11 | Höchstens zwei Techniken | B20, A AG6 | zusammengeführt |
| BE12 | Scroll-Kopplung linear, Nachlauf nur Schmuck | B29, AD 5a ?, N6 | geschärft |
| BE13 | Deckkraft nie am Scroll | B29, B24 | geschärft |
| BE14 | Pins mit Grenzen, Probe und Nahtprobe | B28, AD 5a | gelockert |
| BE15 | Zeichen und Text gleich | B67 | übernommen |
| BE16 | Kreuzungsfreiheit, auch über tragenden Medien | B64, B65, AD 5a (dort „v2 B26“), <dein-name> 16.10. (Demo 1) | zusammengeführt |
| BE17 | Scrollen bleibt nativ | N6 ?, KONFLIKTE K4 | neu |
| BE18 | Wechselndes ist nur Schmuck | E10, B13, A AB5 | zusammengeführt |
| BE19 | Wortwechsel | B13, AD 6b | geschärft |
| BE20 | Walze | B70, AD 6b (leer höchstens 100 ms) | zusammengeführt |
| BE21 | Eine Uhr je Anzeige, keine halben Ziffern mobil | B71, B41 | zusammengeführt |
| BE22 | Laufband in Pixeln | H4 | übernommen |
| BE23 | Gegen Leerlauf messen | A AL7 (performance), WF (Messfilm), neu ? | geschärft |

## regeln/praesentation.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| PR01 | Erste Ansicht: vier Teile | R01, B10, E4 | gelockert |
| PR02 | H1 sagt, für wen | R02, R06, B12, B39, E3, E6 | gelockert |
| PR03 | Zeile über H1 informiert | R02, B10, E2 | gelockert |
| PR04 | Fünf-Sekunden-Klarheit | R18, B37, R24 | übernommen |
| PR05 | Pflicht (<dein-name>, M2): Startseite ist eine Weiche | M2, B79, B78, PK K2, KONFLIKTE K3 | zusammengeführt |
| PR06 | Navigation und Bedienbarkeit | R20, A AW12, Ov, PK §6.3 ? | zusammengeführt |
| PR07 | Struktur folgt dem Inhalt | A AW11, R20 | zusammengeführt |
| PR08 | Materialmoment je Abschnitt | B27 | übernommen |
| PR09 | Leitmotiv bis zum Schluss | B68 | übernommen |
| PR10 | Pflicht (<dein-name>, M3): alle Projekte zeigen | M3, B79, PK K4 | zusammengeführt |
| PR11 | Fall mit Ergebnis | R09, R14, PK K4 | zusammengeführt |
| PR12 | Beweis mit Bezug | R03 | übernommen |
| PR13 | Vertrauen, echtes Porträt | R19, R17, E9, PK K5 | zusammengeführt |
| PR14 | Preise und Ablauf offen | PK K6, PK Q26 | neu |
| PR15 | Nichts Kopiertes, Achsen des Demo-Registers | R41, R-P3, B50, WF ?, METHODE (Gedächtnis über Läufe) | zusammengeführt |
| PR16 | Zwei Anker sichtbar | R40 | übernommen |

## regeln/medien.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| ME01 | Eigenes Material zuerst | R04, B74, PK P2 | gelockert |
| ME02 | Stock erlaubt, Passung prüfen | E11, R04, A planung/recherche-bibliotheken | gelockert |
| ME03 | Selbst Erzeugtes als Quelle | Grundsatz, Ov Nachtrag 5 | neu |
| ME04 | KI-Fotos erst nach Frage | E11, Grundsatz | gelockert |
| ME05 | Ein Iconsatz je Vorhaben | A assets, R38 | gelockert |
| ME06 | Schriften mit geprüfter Lizenz | A typography, R33, R38, B35 | zusammengeführt |
| ME07 | Medientabelle mit Kontaktbogen | B32, B75, B77, M1, R33 | zusammengeführt |
| ME08 | Ordnen nach Nähe zum Zielkunden | B74 | übernommen |
| ME09 | Gewicht und Schärfe zugleich | B77, M1, A performance ? | geschärft |
| ME10 | Naht- und Wiederholungsprobe | B76 | übernommen |
| ME11 | Material auf Hausfarben graden, Körnung mit Absicht | B33, B80 | gelockert |
| ME12 | Galerie nur frei lizenziert | Ov Nachtrag 3, B32 | übernommen |
| ME13 | Video-Klassen und Master, Größe nach S34 | B33, AD 3a, M1, B77 | geschärft |
| ME14 | Poster ist Bild 0, PSNR-Probe | AD 3a, B33 | übernommen |
| ME15 | Ladeverhalten und Autoplay | B25, AD 3a, V8 | zusammengeführt |
| ME16 | Kein Mischmodus über Film | B38 | geschärft |

## regeln/erzeugt.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| ER01 | Erwünschte Mittel, Markentest | Grundsatz, Ov Nachtrag 5, PK P1 | neu |
| ER02 | Nichts Echtes vortäuschen | B31 | übernommen |
| ER03 | Erzeugtes in doppelter Größe | M1 | übernommen |
| ER04 | 3D-Oberfläche gegen Material | B66 | übernommen |
| ER05 | Texturen mit Nahtprobe | B76 | übernommen |
| ER06 | Bild-für-Bild-Aufnahme bewegter Seiten | neu ? | neu |
| ER07 | Technikstufe je Mittel | A AR4 | geschärft |
| ER08 | Herkunft, Galerie, Bibliothek | B32, Ov Nachtrag 2 und 3 | zusammengeführt |

## regeln/text.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| TX01 | Botschaft in Reihenfolge, Wichtiges vorn | A AW2, A AC1 | übernommen |
| TX02 | Ein-Satz-, Gegenteil-, Wettbewerber-Probe | A AW3, A AW4, R40 | zusammengeführt |
| TX03 | Konkret statt Adjektive | A AW5, R21, A copywriting | zusammengeführt |
| TX04 | Laientext, Fachwort- und Flesch-Probe | B37, R24, PK K1, A AW-K | geschärft |
| TX05 | Eine menschliche Zeile, Sie | R12 | übernommen |
| TX06 | KI-Muster prüfen, nicht verbieten | R21, A AW6, I9, Grundsatz | gelockert |
| TX07 | Knöpfe nennen das Ergebnis | A AC1, A copywriting, R16, V16 | zusammengeführt |
| TX08 | Fehler- und Leerzustände | V3, V6, V16, A copywriting | zusammengeführt |
| TX09 | Ratgeber mit Google-Nebenknopf | WF (Standardbaustein Ratgeber und Blog) | neu |

## regeln/konversion.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| KO01 | Ein Ziel, ein Knopf | R16, B27, PK K3 | zusammengeführt |
| KO02 | Telefon als zweiter Weg | R15, B37, B10, PK K3 | zusammengeführt |
| KO03 | Kontakt im Fuß | PK K6 | übernommen |
| KO04 | Formulare kurz (Felder: S52) | V3, PK K3, R27 | geschärft |
| KO05 | Funnel zeigt Umfang und Dauer | B62, PK K3 | geschärft |
| KO06 | Keine Täuschung, nichts vorangehakt | A AW-P, A ia-and-structure ? | geschärft |
| KO07 | Erstklick: Aufgaben vor dem Bau, Test im Audit, 4 von 5 | WF (Prüfung zu M2: ≥ 4 von 5), B78 (5 von 5 für die <studio>-Seite, in `branchen/dienstleister.json`), PK K2, R18 | geschärft |

## regeln/technik.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| TE01 | Gerüst nach Umfang, Astro ab mehr als fünf Seiten | Ov (ENTSCHEIDUNGEN.md), A stack §9 | geschärft |
| TE02 | Werkzeugstand geprüft, Ungeprüftes benennen | A stack §1, §8 | übernommen |
| TE03 | Inseln, `client:visible` als Standard | A stack §3 | gelockert |
| TE04 | Cache: `_astro` immutable, HTML no-cache | A stack §6 | übernommen |
| TE05 | CSP-Weg vor dem Bau | A stack §7.1 | übernommen |
| TE06 | Kein rohes `<script>`, Radix-Inline-Styles | A stack §7.2, §7.3 | zusammengeführt |
| TE07 | CSP-Probe: null Inline-Skripte | A stack §7, R31 | geschärft |
| TE08 | Thema-Skript extern, unter 1 KB, wertet `?thema=` aus | H6, H2, A stack §7.2, WF | zusammengeführt |
| TE09 | Schriften WOFF2, feste Instanzen, beschnitten, vorgeladen | A performance, A AT3, R38, V8, B35 | zusammengeführt |
| TE10 | Canvas nur im Bild, Telefonfassung | A performance, A AL2, A AL3 | übernommen |
| TE11 | IntersectionObserver, Listen virtualisieren | A performance, V8 | zusammengeführt |
| TE12 | Long Tasks bei vierfacher Drosselung | A performance, A AL7 | geschärft |
| TE13 | Hover nur mit `(hover: hover)` | A performance, V15 | übernommen |
| TE14 | Telefon: touch-action, safe-area, theme-color | V10, V11, V12 | übernommen |
| TE15 | `Intl`, `translate="no"` | V13, neu ? | übernommen |
| TE16 | Artefakt: nur erlaubte CDNs | A assets, A stack (Artefakt) | zusammengeführt |
| TE17 | `.glb` als Base64 laden | A stack (Artefakt) | übernommen |

## regeln/software.md

| Kennung | Regel | Quelle | Art |
|---|---|---|---|
| SW01 | Vertraut vor eigen | I operate, A software Regel 14 | zusammengeführt |
| SW02 | Häufige Wege sofort, kein Intro | I operate, A software Regel 18, H5, N6 | zusammengeführt |
| SW03 | Zustand sichtbar, Zeitstufen beim Laden | A software Regel 1, A ia-and-structure §4 (Ladezustand), N6 (100 ms) | geschärft |
| SW04 | Jeder Schritt hat einen Ausweg | A software Regel 3 | übernommen |
| SW05 | Alle Zustände je Bedienteil | I operate, A software Regel 1 | zusammengeführt |
| SW06 | Erst inline, dann Dialog | I8, I operate | übernommen |
| SW07 | Navigation nach Zahl und Häufigkeit | A software Regel 14, A ia-and-structure §4 | übernommen |
| SW08 | Schrittweise zeigen, Vorgaben entscheiden | A software Regeln 5, 11, A ia-and-structure §5 | zusammengeführt |
| SW09 | Nichtlinear, keine Pflicht-Einführung | A software Regel 18 | übernommen |
| SW10 | Dichte nach Nutzung | A software Regel 15, A ia-and-structure §5 | übernommen |
| SW11 | Übersicht auf einer Höhe | A software Regeln 6–8 | geschärft |
| SW12 | Tabellen nach vier Aufgaben | A software Regeln 9, 10 | übernommen |
| SW13 | Datensatz: nächster Schritt, Seitenblatt | A software Record views | gelockert |
| SW14 | Einstellungen sofort wirksam (Felder: S52) | A software Regel 11, A ia-and-structure §4 | geschärft |
| SW15 | Schrift: rem-Skala 1,125–1,2 | I operate, A typography ? | geschärft |
| SW16 | Farbe zurückhaltend, Akzent funktional | I operate, A software (Anti-Patterns) | gelockert |
| SW17 | Tastatur zuerst, Kürzel dokumentiert | A software Regeln 4, 16, 17 | zusammengeführt |

## branchen/*.json

| Datei | Regeln | Quelle (Feld `quelle`) | Art |
|---|---|---|---|
| `dienstleister.json` | dienstleister-1 bis -6 | B62, B78, B61, B60, B63, E5, VV „Pakete und Preise“, M | übernommen; -5 zusammengeführt |
| `handwerk.json` | handwerk-1 bis -3 | B36, B81, B37 | übernommen |
| `schausteller.json` | schausteller-1 bis -5 | VV „Akquise Schausteller“, R26, R24, <dein-name> 13.09.2026 | -1, -2 übernommen; -3 bis -5 neu |

`schema.json` enthält keine Regeln.

## regler.md, Ablauf, Kritik

| Baustein | Inhalt | Quelle | Art |
|---|---|---|---|
| Regler 1 `auftreten` | Klang der Seite, vier Stufen | A registers (AR1) | übernommen |
| Regler 2 `bewegung` | Menge 0 bis 3, ohne Verbote | A registers (AR2), N6, Ov | gelockert |
| Regler 3 `dichte` | Inhalt je Bildschirm, drei Stufen | A registers (AR3), Ov | übernommen |
| Regler 4 `technik` | statisch, Inseln, WebGL | A registers (AR4), AD | gelockert |
| Regler 5 `tonfall` | nüchtern, direkt, selbstbewusst | A registers (AR5) | übernommen |
| Regler 6 `material` | Bildanteil gegen Typografie | Ov | neu |
| Regler 7 `farbe` | Farbstrategie bis getränkt | Ov, I (Stufennamen) | neu |
| Regler 8 `inszenierung` | Wie stark Leistung vorgeführt wird | Ov | neu |
| Regler 9 `konversionsdruck` | Wie direkt die Aufforderung | Ov, PK K3 ? | neu |
| Regler 10 `schrift` | Typo-Charakter, höchstens zwei Familien | Ov, E6, B39 | neu |
| Leitplanken | Kombinationen, bei denen gefragt wird | A registers (AR6), Analyse-Vorschlag | geschärft |
| Stufen | betrieb, kunde-hochwertig, award | Analyse-Vorschlag, B (Stufentabelle) | zusammengeführt |
| Budgets | Eine Zahl je Stufe | Ov, B40 (CLS 0,05 vor R 0,1), R32, R36 | zusammengeführt |
| Dauern (Tabelle in `regeln/stamm.md` nach S51) | Rückmeldung unter 100 ms, klein 100–200 ms, groß 250–400 ms, Inszenierung bis 1.200 ms, Staffel 20–40 ms; Stufen von Material Design 3 | N6, Ov (UI 150–400 ms; N6 geht vor), A motion-doctrine §3 (Token-Stufen) | zusammengeführt |
| Website-Arten | website, onepage, landingpage, anwendung | Ov Nachtrag 2, M2, KONFLIKTE K3 | neu |
| Lauf-Arten | demo, mockup, bau | Ov Nachtrag 2 | neu |
| Ablauf neun Schritte | Start bis Politur | WF | übernommen |
| Sechs Kritiker | G, B, K, T, M, R | A critics, WF, B50–B52, Ov (Bewegung als Kritiker) | zusammengeführt |
| Notenskala | 10 bis 1, Ziel 8 | B50, neu (Noten erst ab kunde-hochwertig) | übernommen |
| Modellregel | Opus plant, Sonnet baut | Ov Nachtrag 2, WF | zusammengeführt |
| Laufordner | `L/` mit festen Dateien, Stand-Log | WF (Einsehbarkeit) | übernommen |

## Alte Dateien

| alt | neu |
|---|---|
| `reference/_index.md` | gestrichen; Ladeplan in `SKILL.md`, `bausteine/_index.md` |
| `reference/3d.md` | `rezepte/3d.md`; `regeln/technik.md` TE10, TE17; `regeln/erzeugt.md` ER04 |
| `reference/assets.md` | `regeln/medien.md` ME02, ME04–ME06, ME12; `regeln/technik.md` TE16 |
| `reference/aus-reels.md` | `planung/aus-reels.md` |
| `reference/components.md` | `rezepte/komponenten.md` |
| `reference/copywriting.md` | `regeln/text.md` TX01–TX08 |
| `reference/design-foundations.md` | `regeln/stamm.md` S04, S14–S15, S21–S24, S26, S30–S33 |
| `reference/ia-and-structure.md` | `regeln/software.md` SW02–SW14; `regeln/praesentation.md` PR05–PR07 |
| `reference/layouts.md` | `rezepte/layouts.md`; `regeln/praesentation.md` PR07 |
| `reference/motion.md` | `rezepte/scroll.md`; `regeln/bewegung.md` BE12–BE13 |
| `reference/motion-doctrine.md` | `regeln/stamm.md` S20, S42–S51; `regeln/bewegung.md` BE01–BE06; `rezepte/scroll.md`; Dauern-Tabelle in `regeln/stamm.md` |
| `reference/performance.md` | `regler.md` (Budgets); `regeln/stamm.md` S12–S18, S36, S38–S40; `regeln/technik.md` TE09–TE13; `regeln/bewegung.md` BE23 |
| `reference/presets.md` | gestrichen |
| `reference/product-motion.md` | `rezepte/oberflaeche.md`; `regeln/bewegung.md` BE01, BE05, BE06; `regeln/software.md` SW03, SW05 |
| `reference/registers.md` | `regler.md`; Beispiele in `branchen/*.json` |
| `reference/scroll-choreography.md` | `rezepte/scroll.md`; `regeln/bewegung.md` BE14–BE17 |
| `reference/shaders.md` | `rezepte/shader.md` |
| `reference/software.md` | `regeln/software.md` SW01–SW17 |
| `reference/stack.md` | `rezepte/astro.md`; `regeln/technik.md` TE01–TE08, TE16–TE17 |
| `reference/typography.md` | `regeln/stamm.md` S25–S29; `regeln/medien.md` ME06; `regeln/technik.md` TE09 |
| `reference/website.md` | `regeln/praesentation.md` PR01–PR14; `regeln/text.md`; `regeln/konversion.md` KO01–KO07; `regeln/stamm.md` S05–S11, S19, S39; `befehle/plan.md` (Interview) |
| `commands/behavior.md` | `befehle/vorlieben.md` |
| `commands/build.md` | `befehle/bauen.md`, `befehle/bewegung.md`, `befehle/audit.md`, `befehle/politur.md` |
| `commands/critics.md` | `befehle/kritik.md`; Messteil in `befehle/audit.md` |
| `commands/db.md` | gestrichen |
| `commands/lernen.md` | `befehle/lernen.md` |
| `commands/loot.md` | `befehle/bibliothek.md` |
| `commands/plan.md` | `befehle/plan.md`, `befehle/material.md`, `befehle/entwurf.md` |
| `commands/register.md` | `befehle/plan.md` (`plan --bestand`) |
| `workflows/lernen.js` | gestrichen; Ablauf in `befehle/lernen.md` |
| `workflows/software.js` | gestrichen; Ablauf in `befehle/bauen.md`, Art `anwendung` |
| `workflows/website.js` | gestrichen; Ablauf in `SKILL.md` (neun Schritte) und `befehle/` |

## Gestrichen

| Was | Grund |
|---|---|
| `reference/presets.md` | Regler ersetzen Presets |
| `workflows/*.js` | Ablauf als Schrittfolge in `SKILL.md`/`befehle/`; keine Nutzung außerhalb gefunden |
| `commands/db.md`, Pflege von `projects.json` | entfällt |
| Befehl `interface` | ersetzt durch Website-Art `anwendung` |
| Ableitung PRODUCT.md / DESIGN.md | impeccable wird nicht mehr getrennt gebraucht |
| MOODBOARD.md | geht in SOUL und KONZEPTE auf |
| Disney-Tafel (zwölf Prinzipien) | N6 ersetzt sie |
| Lange Floskelliste (A AW6) | TX06 kurz, prüfen statt verbieten |
| Preise im Regelwerk | stehen im Vault („Pakete und Preise“) |
| Abschnitt „## Register“ brand/product | ersetzt durch Website-Art und Regler |
| Drei-Fragen-Kette für Marke | ersetzt durch Markentest BE02 |
| Bremsen aus R08, R23, R35, R36 | Grundsatz, BE02 |
| Beispiel B-11 (A registers: WebGL bei Mobil-Publikum anhalten, Handwerk-Beispiel) | Leitplanken in `regler.md`, TE10 |
| Lenis, weiches Scrollen (B22, A AB7) | KONFLIKTE K4, BE17 |
| Prüfschleife mit drei Runden | WF: eine Politur, höchstens eine Nachprüfung |
| Vermerk „Beispielbild“ bei Stock und KI (R04) | E11 |
| Radius 12–16 px (R22), Symmetriepflicht (R-P1, VV V2) | Grundsatz, E7, E8 → S21, S23 |
| Verbot von Torten- und 3D-Diagrammen (A software Regel 7) | gelockert zu Ermessen (SW11) |
| Verbot von Layout-Animation (A non-negotiables) | S51 Ermessen mit Prüffrage |
| „3D-Hero darf mobil fehlen“ (A AL2) | umgekehrt: eigene leichtere Fassung (TE10) |
| Anti-Pattern-Tabelle, Pflichtkomponenten (A software) | Kürzung (Ov) |
| Liste der Inter-Alternativen (A typography), Stock- und Video-Kataloge (A assets) | Kürzung; Recherche in `planung/` |
| Hick, Fitts, Miller, 20 Prüfpunkte (A ia-and-structure) | nur noch in `planung/recherche-software-aufbau.md` |
| Fünf Award-Haltungen als Planfrage | ersetzt durch Regler, Stufen, `branchen/` |
| Interview in drei Runden, Typ zuerst | ersetzt durch drei bis vier Fragen je Runde (`befehle/plan.md`) |
| IBM Carbon als zweites Kurven- und Dauernsystem (A motion-doctrine) | ein System: Material Design 3 (Stamm-Tabelle, BE04) |

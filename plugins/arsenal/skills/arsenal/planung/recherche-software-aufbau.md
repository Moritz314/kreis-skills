# Intelligenter Aufbau von Software-Oberflächen

Diese Datei sammelt den belegten Forschungsstand zu Informationsarchitektur, Interaktionsdesign und den Gesetzmäßigkeiten dahinter, übersetzt in prüfbare Regeln für den Skill arsenal. Jede Kernaussage ist mit einer über WebSearch oder WebFetch tatsächlich eingesehenen Quelle belegt oder ausdrücklich als ungeprüft gekennzeichnet. Recherchestand 2026-09-08.

## Inhalt

- Informationsarchitektur
- Die belegten Gesetze
- Heuristiken und Prinzipien
- Muster nach Bildschirmart
- Progressive Offenlegung und Datendichte
- Übersetzung in Regeln
- Anti-Muster
- Quellen

## Informationsarchitektur

Rosenfeld, Morville und Arango unterscheiden in ihrem Standardwerk "Information Architecture: For the Web and Beyond" (4. Auflage, O'Reilly, 2015) vier Strukturmodelle. Die Hierarchie ordnet Inhalte in sich ausschließenden Eltern-Kind-Beziehungen und eignet sich, wenn jedes Objekt klar einer übergeordneten Kategorie zuordenbar ist. Die Facettenklassifikation kombiniert mehrere unabhängige Beschreibungsdimensionen (Preis, Datum, Kategorie) und wird nötig, sobald Objekte drei oder mehr solcher Dimensionen besitzen, für die eine einzige Hierarchie nur eine Perspektive abbilden könnte. Das Matrix- beziehungsweise Datenbankmodell verzichtet auf feste Hierarchie zugunsten von Metadaten, Tags, Suche und Filterung und trägt Viele-zu-viele-Beziehungen zwischen Inhalten, die eine Hierarchie nicht abbilden kann. Die sequenzielle Struktur ordnet Inhalte in fester linearer Abfolge und ist meist kein eigenständiges Navigationsmodell, sondern das Strukturprinzip einzelner Abläufe wie Checkout oder Formular-Assistent innerhalb einer größeren Architektur.

Zur Navigationstiefe gegen Breite geht die verbreitete Faustregel "breit und flach schlägt tief und schmal" auf Larson und Czerwinski zurück ("Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval", CHI 98 Conference Proceedings, S. 25 bis 32, 1998). Zweistufige Strukturen ermöglichten dort zuverlässig schnellere Suchen als eine dreistufige Struktur mit entsprechend schmaleren Kategorien, allerdings schnitt die extremste getestete Struktur (sehr breit, sehr flach) schlechter ab als eine moderate Breite, und die Eindeutigkeit der Kategoriebezeichnungen auf der obersten Ebene erwies sich als entscheidender als die reine Zahl der Optionen. NNGroup relativiert die Faustregel in "Flat vs. Deep Website Hierarchies" (Whitenton, 2013) weiter: Es gibt keine pauschal richtige Antwort und keine feste numerische Obergrenze, flache Hierarchien eignen sich bei eindeutigen, nicht überlappenden Kategorien, tiefe Hierarchien werden nötig, sobald zu viele Kategorien für eine Ebene existieren, dann aber nur mit zusätzlichen Orientierungshilfen wie Breadcrumbs. Die Grenze zwischen gut flach und überfordernd breit hängt vom Vorwissen der Nutzer und der Unterscheidbarkeit der Kategorien ab, nicht von einer festen Zahl.

Beim Benennungssystem gilt durchgängig: Nutzer scannen nach Begriffen aus ihrer eigenen Sprache, nicht nach interner Systemterminologie, ein technisch korrektes, aber ungewohntes Label wird bei der Navigation übersehen. Zur Prüfung, welche Begriffe und Gruppierungen dem mentalen Modell der Nutzer entsprechen, nennt NNGroup zwei komplementäre Methoden: Card Sorting lässt Teilnehmende Inhalte frei gruppieren und benennen und eignet sich früh im Entwurf (Tankala/Sherwin, 2024, empfohlen 15 Teilnehmende für qualitative, 30 bis 50 für quantitative Ergebnisse), Tree Testing prüft eine bereits entworfene Struktur, indem Teilnehmende darin nach Inhalten suchen (Laubheimer, 2023).

Zu Suchen gegen Blättern zeigt Budiu ("Search Is Not Enough: Synergy Between Navigation and Search", NNGroup, 2014): Suche setzt ein klares, artikulierbares Ziel voraus, Navigation ersetzt Erinnern durch Wiedererkennen und eignet sich für exploratives, zielunscharfes Verhalten. Da site-eigene Suchfunktionen technisch oft schwächer sind als große Websuchmaschinen und Nutzer kaum wissen, welche Anfrage für eine konkrete Website funktioniert, sind beide Zugänge komplementär anzubieten, nicht gegeneinander auszuspielen.

## Die belegten Gesetze

Für jedes Gesetz gilt: was es aussagt, was die verbreitete Fehlinterpretation ist, und die konkrete Layout-Folge.

| Gesetz | Was es aussagt | Was es NICHT aussagt (Fehlinterpretation) | Layout-Folge |
|---|---|---|---|
| Hicks Gesetz (Hick 1952, Hyman 1953) | Entscheidungszeit wächst logarithmisch mit der Zahl gleichwahrscheinlicher Optionen: T = a + b·log2(n). Doppelt so viele Optionen bedeuten nicht doppelt so lange Entscheidungszeit. | Kein Beleg für "weniger Optionen ist immer besser". Gilt für tatsächlich abzuwägende Alternativen, nicht fürs Wiedererkennen bekannter, gruppierter Optionen. Kategorisierung senkt die effektive Optionenzahl pro Schritt, ist die von NNGroup empfohlene Technik, nicht das bloße Streichen von Optionen. | Lange, flache Options-Listen (Menüs, Dropdowns) in Kategorien mit Zwischenüberschriften gliedern, häufige Optionen zuerst. |
| Fitts' Gesetz (Fitts 1954) | Zeit zum Erreichen eines Ziels T = a + b·log2(2D/w), abhängig von Distanz D und Zielbreite w. Größere, näherliegende Ziele werden schneller und fehlerärmer erreicht. | Bildschirmränder als "unendliche Ziele" gilt für Maussteuerung, nicht für Touch, der Finger wird am Rand nicht wie der Cursor aufgehalten. Kein Beleg, dass jedes Ziel unabhängig vom Layout maximal groß sein soll. | Häufige und destruktive Aktionen groß und nah am Ort der vorausgehenden Interaktion platzieren (Submit-Button neben letztem Feld, nicht am Seitenanfang); Bildschirmränder nur bei Desktop-Mauszielen als Vorteil nutzen. |
| Millers Arbeit (Miller 1956, "The Magical Number Seven, Plus or Minus Two") | Beschreibt zwei separate, zufällig beide um sieben liegende Kapazitäten: absolute Urteilsbildung bei eindimensionalen Reizen und Kurzzeitgedächtnis-Spanne beim Abruf ohne Sichtkontakt (Recall). | Keine Aussage zur richtigen Zahl von Menüpunkten oder Navigationseinträgen. Miller maß Recall ohne Sichtkontakt, eine Navigation ist eine Recognition-Aufgabe mit sichtbaren Optionen, die Gedächtnisgrenze greift dort nicht. Übertragung auf "maximal 7 Menüpunkte" ist eine der verbreitetsten Fehlanwendungen der UX-Forschung. | Navigationsbreite nicht an der Zahl 7 ausrichten, sondern an Unterscheidbarkeit der Kategorien (siehe Informationsarchitektur) und an Hicks Gesetz für die Entscheidungszeit. |
| Jakobs Gesetz (Nielsen, um 2000) | Nutzer verbringen die meiste Zeit auf anderen Websites und Apps und übertragen dort gelernte Erwartungen; sie bevorzugen Oberflächen, die wie bereits bekannte funktionieren. | Kein generelles Innovationsverbot. NNGroup grenzt ab: neue Muster sind sinnvoll, wo sie einen echten, erlernbaren Vorteil bieten. | Etablierte plattformübliche Muster für Grundinteraktionen verwenden (Formularverhalten, Icon-Bedeutung, Navigationsposition), eigene Erfindungen auf Stellen mit echtem funktionalem Mehrwert konzentrieren. |
| Serienpositionseffekt (Murdock 1962) | Elemente am Anfang einer Liste (Primacy, Übertrag ins Langzeitgedächtnis) und am Ende (Recency, aktives Kurzzeitgedächtnis) werden zuverlässiger erinnert als Elemente in der Mitte. | Beschreibt freien Abruf aus dem Gedächtnis, nicht direkt das Scannen einer sichtbaren Liste. Übertragung auf UI-Listen ist plausible Praxisableitung, keine eigenständig geprüfte HCI-Gesetzmäßigkeit. | Wichtigste oder am ehesten gewählte Optionen an Anfang oder Ende von Listen und Menüs setzen, nicht in der Mitte platzieren. |
| Zeigarnik-Effekt (Zeigarnik 1927) | Unterbrochene, unvollständige Aufgaben werden besser erinnert als abgeschlossene, weil sie anhaltende kognitive Spannung erzeugen. | Kein Beleg, dass künstlich erzeugte Unvollständigkeit (unvollständige Profile als Druckmittel) ausnahmslos positiv wirkt, dafür fehlt eine eigene geprüfte Gegenuntersuchung. | Fortschrittsanzeigen und Onboarding-Checklisten mit sichtbarem, unvollständigem Zustand statt nur Erfolgsmeldungen gestalten. |
| Doherty-Schwelle (Doherty/Thadani 1982) | Nutzerproduktivität steigt mit sinkender Systemantwortzeit deutlich über den damals als ausreichend geltenden Wert von 2 Sekunden hinaus, mit einer besonders relevanten Schwelle bei rund 400 Millisekunden. | Keine allgemeine Ladezeit-Vorgabe für komplette Webseiten. Die Studie maß interaktive Terminal-Antwortzeiten, nicht vollständige Seitenladevorgänge mit Netzwerkübertragung. Ein exakter zweiter Schwellenwert unterhalb 400 ms ließ sich nicht an einer zitierfähigen Quelle verifizieren. | Reaktion auf direkte Nutzerinteraktion (Klick, Eingabe) innerhalb von rund 400 ms sichtbar bestätigen, bei längeren Wartezeiten gestufte Ladezustände einsetzen. |

## Heuristiken und Prinzipien

Jakob Nielsen entwickelte die Grundlage 1990 mit Rolf Molich ("Heuristic Evaluation of User Interfaces", CHI '90), die heute bekannte Zehnerliste stammt aus einer Faktorenanalyse von 249 dokumentierten Usability-Problemen und wurde 1994 fertiggestellt (nngroup.com/articles/ten-usability-heuristics/): Sichtbarkeit des Systemstatus, Übereinstimmung zwischen System und Realität, Nutzerkontrolle und Freiheit, Konsistenz und Standards, Fehlervermeidung, Erkennen statt Erinnern, Flexibilität und Effizienz der Nutzung, ästhetisches und minimalistisches Design, Nutzern helfen Fehler zu erkennen und zu beheben, Hilfe und Dokumentation.

Ben Shneidermans "Eight Golden Rules of Interface Design" aus "Designing the User Interface" (6. Auflage, Shneiderman et al., 2016, cs.umd.edu/users/ben/goldenrules.html): nach Konsistenz streben, universelle Nutzbarkeit anstreben, informatives Feedback anbieten, Dialoge mit klarem Abschluss gestalten, Fehler verhindern, einfache Umkehrbarkeit von Aktionen erlauben, Nutzern das Gefühl der Kontrolle geben, Kurzzeitgedächtnis-Belastung reduzieren.

Donald Normans "Gulf of Execution" und "Gulf of Evaluation" (Hutchins, Hollan, Norman 1986, popularisiert in "The Design of Everyday Things", 1988, überarbeitet 2013) beschreiben zwei Lücken: Die Handlungslücke ist die Distanz zwischen der Absicht eines Nutzers und den Möglichkeiten, sie in Handlungen zu übersetzen, sie wird geschlossen durch Bedienelemente, die unmittelbar erkennbar mit Nutzerzielen korrespondieren. Die Bewertungslücke ist die Distanz zwischen tatsächlichem Systemzustand und dem, was der Nutzer aus der Rückmeldung darüber versteht, sie wird geschlossen durch sofortiges, verständliches Feedback. In derselben überarbeiteten Auflage führt Norman die Unterscheidung zwischen Affordanz (der tatsächlichen, vom Nutzer unabhängigen Handlungsmöglichkeit eines Objekts) und Signifikant (dem wahrnehmbaren Zeichen, das diese Möglichkeit kommuniziert) ein: Ein Button ist technisch klickbar, sobald ein Klick-Handler existiert, das macht ihn aber nicht als klickbar erkennbar, erst ein sichtbares Signal wie Schatten oder Farbkontrast tut das. Flaches Design ohne solche Signifikanten macht vorhandene Affordanzen für Nutzer praktisch unsichtbar.

Die drei Systeme überschneiden sich stark: Nielsens "Erkennen statt Erinnern" und Shneidermans "Kurzzeitgedächtnis-Belastung reduzieren" sind nahezu deckungsgleich, und ein Großteil der Feedback- und Statusregeln beider Kataloge lässt sich auf Normans Bewertungslücke zurückführen, Regeln zu Kontrolle und Umkehrbarkeit auf die Handlungslücke. Diese Einordnung ist eine eigene Einschätzung auf Basis der recherchierten Originalinhalte: Norman liefert weniger eine konkurrierende Checkliste als ein erklärendes Modell darunter, Nielsen und Shneiderman sind präskriptiv und für die Evaluation gedacht. Keines der drei Systeme ist ein empirisch geprüftes Gesetz im Sinne von Fitts' oder Hicks Gesetz, es sind strukturierte Erfahrungswissen-Kataloge ohne mathematisch prüfbare Vorhersage einzelner Interaktionszeiten.

Als Norm-Gegenstück zu den drei US-geprägten Katalogen legt die internationale Norm ISO 9241-110 (aktuelle Fassung 2020, deutschsprachig als DIN EN ISO 9241-110 verbreitet) sieben Grundsätze der Dialoggestaltung fest: Aufgabenangemessenheit (ein Dialog unterstützt die Erledigung der Aufgabe, ohne durch unnötige Schritte oder Umwege abzulenken), Selbstbeschreibungsfähigkeit (für den Nutzer ist jederzeit offensichtlich, in welchem Dialog er sich befindet, welche Handlungen möglich sind und wie sie ausgeführt werden), Erwartungskonformität (der Dialog entspricht dem, was der Nutzer aus Kontext und bisheriger Erfahrung erwartet, deckt sich mit Jakobs Gesetz), Lernförderlichkeit, Steuerbarkeit (der Nutzer kann Tempo und Reihenfolge der Interaktion beeinflussen), Fehlertoleranz (das gewünschte Ergebnis wird trotz erkennbar fehlerhafter Eingabe mit minimalem Korrekturaufwand erreicht) und Individualisierbarkeit. Die Norm überschneidet sich inhaltlich stark mit Nielsen und Shneiderman, formuliert aber abstrakter und ohne Beispielkatalog, wodurch sie sich eher für Lastenhefte und Konformitätserklärungen eignet als für die tägliche Entwurfsarbeit.

## Muster nach Bildschirmart

| Bildschirmart | Belegte Pflichtbestandteile | Typische Fehler | Quelle |
|---|---|---|---|
| Dashboard | Auf einen Blick verstehbar ohne Scrollen, Visualisierung an präattentiver Verarbeitung ausrichten: Länge und 2D-Position (Balken-, Liniendiagramme) statt Fläche oder Winkel. | Kreisdiagramme (präattentiv schlecht für Vergleiche), 3D-Effekte, die Formen verzerren, Ästhetik über Klarheit gestellt. | Laubheimer, "Dashboards: Making Charts and Graphs Easier to Understand", NNGroup 2017 |
| Tabelle mit vielen Zeilen | Vier Kernaufgaben unterstützen: Datensätze finden (lesbarer Bezeichner statt ID, aufgabenorientierte Spaltenreihenfolge), vergleichen (fixierte Kopfzeile/-spalte, Zebrastreifen), einzelne Zeile ansehen/bearbeiten (Inline, Modal, Seitenpanel oder Akkordeon je nach Kontext), Aktionen anwenden (Sammelaktionen mit Checkboxen und "Alle auswählen"). | Bedeutungslose interne IDs prominent zeigen, Sammelmenüs mit schlechter Auffindbarkeit, destruktive Aktion räumlich neben bestätigender Aktion. | Laubheimer, "Data Tables: Four Major User Tasks", NNGroup 2022; Nielsen/Laubheimer, "Top 10 Application-Design Mistakes", NNGroup 2019 |
| Formular | So kurz wie möglich, Label dauerhaft sichtbar über/neben dem Feld, einspaltiges vertikales Layout, logische Feldreihenfolge, Pflicht- von optionalen Feldern klar unterscheiden, Format-Anforderungen erklären, Fehleranzeige mit mehreren Hinweisreizen bei erhaltener Eingabe. | Placeholder-Text als einziges Label (verschwindet beim Fokussieren), mehrspaltige Layouts, sichtbare Reset/Clear-Schaltflächen. | Whitenton, "Website Forms Usability: Top 10 Recommendations", NNGroup 2016 |
| Einstellungen | Anpassungsoptionen auf Funktionen mit substanziellem Nutzen beschränken, robuste Standardwerte wichtiger als Optionsbreite (bei Interface-Anpassung 83 % Aufgabenerfolg gegen 66 % bei Produktanpassung, 24 Testpersonen); Toggle-Label beschreibt den Zustand direkt und richtungsbezogen, Wirkung sofort ohne Speichern-Schritt. | Anpassungsoptionen ohne klaren Nutzervorteil, neutral formulierte Toggle-Labels, Toggles die erst nach Speichern wirken. Eine dedizierte NNGroup-Quelle zur Seitenstruktur von Settings selbst wurde nicht gefunden, das ist als Lücke zu benennen. | Nielsen, "Customization of UIs and Products", NNGroup 2009; Kendrick, "Toggle-Switch Guidelines", NNGroup 2018 |
| Onboarding | Feature-Promotion beim ersten Start vermeiden (wird meist übersprungen), visuelle Anpassung nicht ins Onboarding verlagern, Anleitungen nur für tatsächlich neuartige Interaktionsmuster. | Vorgeschaltete Tutorials außerhalb des Nutzungskontexts, die laut NNGroup keine bessere Aufgabenleistung zeigten. Diese Quellen stützen sich selbst auf punktuelle interne Beobachtung statt auf eine systematische Studie, deshalb als teilweise ungeprüft markiert. | Kendrick, "Mobile-App Onboarding", NNGroup 2020; Laubheimer, "Onboarding Tutorials vs. Contextual Help", NNGroup 2023 |
| Leerer Zustand | Systemstatus kommunizieren (Laden, Fehler, restriktiver Filter, statt Stille), Lernhinweis genau dort geben, wo er gebraucht wird, direkter Handlungspfad zur Befüllung (z.B. "Erstellen"-Schaltfläche). | Leere Fläche ganz ohne Erklärung oder Handlungsoption, widersprüchliche Statusanzeigen. | Kaplan, "3 Guidelines for Designing Empty States in Complex Applications", NNGroup 2021 |
| Fehlerzustand | Meldung direkt neben der Ursache, auffällig und barrierearm signalisiert (nicht nur Farbe), verständliche Sprache ohne Fachjargon, konstruktiver Lösungsvorschlag, Nutzereingabe erhalten, nicht verfrüht während laufender Eingabe anzeigen. | Vage Meldungen wie "Something went wrong" ohne Ursache oder Lösung, Eingaben werden beim Fehler gelöscht, ausschließlich farbliches Signal. | Neusesser/Sunwall, "Error-Message Guidelines", NNGroup 2023; Nielsen/Laubheimer 2019 |
| Ladezustand | Unter etwa 1 Sekunde keine Anzeige nötig, für einzelne Elemente Spinner, für Seitenladevorgänge zwischen etwa 2 und 10 Sekunden Skeleton Screens (deuten spätere Struktur an), über etwa 10 Sekunden Fortschrittsbalken mit konkreter Angabe. | Skeleton Screens, die nur Kopf-/Fußzeile andeuten statt der tatsächlichen Inhaltsstruktur, genereller Spinner bei vollflächigem Laden, keine Fortschrittsangabe bei langen Wartezeiten. | Tankala, "Skeleton Screens 101", NNGroup 2023, mit Bezug auf Mejtoft/Långström/Söderström 2018 |

## Progressive Offenlegung und Datendichte

Nielsen definiert Progressive Disclosure als Strategie, fortgeschrittene oder selten benötigte Funktionen auf sekundäre Bildschirme zu verschieben, während die Erstansicht nur wesentliche Optionen zeigt (NNGroup, 2006). Richtig eingesetzt verbessert das Erlernbarkeit, Effizienz und Fehlerrate zugleich.

Die zentrale, im Original wörtlich zu übernehmende Kernaussage: "designs that go beyond 2 disclosure levels typically have low usability because users often get lost when moving between the levels." Designs jenseits von zwei Offenlegungsebenen haben also typischerweise geringe Gebrauchstauglichkeit, weil Nutzer sich beim Wechsel zwischen den Ebenen verlieren. Als weitere Fehlerquelle nennt Nielsen unklare Navigation zu den sekundären Funktionen, unabhängig von einer korrekten inhaltlichen Aufteilung zwischen Erst- und Sekundäransicht.

Dass Voreinstellungen das Nutzerverhalten stark lenken, ist verhaltensökonomisch belegt: Johnson und Goldstein zeigten in "Do Defaults Save Lives?" (Science 302, 2003, S. 1338 bis 1339), dass Länder mit Opt-out-Organspende deutlich höhere Einwilligungsraten aufweisen als Länder mit Opt-in. Thaler und Sunstein ordnen das in "Nudge" (2008) konzeptionell ein: Ein Default ist selbst dann eine folgenreiche Gestaltungsentscheidung, wenn jede Option formal wählbar bleibt, weil ein erheblicher Teil der Nutzer den Weg des geringsten Widerstands geht. Davon klar abzugrenzen ist der manipulative Einsatz, den Gray et al. ("The Dark (Patterns) Side of UX Design", CHI 2018) als "Sneaking" beziehungsweise "Interface Interference" fassen und den Mathur et al. ("Dark Patterns at Scale", CSCW 2019) empirisch auf großen Shopping-Websites nachweisen; der EuGH zog im Planet49-Urteil (C-673/17, 2019-10-01) die rechtliche Grenze, dass eine vorangehakte Checkbox keine wirksame Einwilligung darstellt. Der Unterschied liegt in drei Kriterien: liegt der Default im Interesse der Nutzer oder des Anbieters, ist er als Voreinstellung erkennbar oder verschleiert, ist seine Änderung ebenso leicht wie seine Übernahme.

Für die Datendichte in Fachanwendungen lassen sich zwei belastbare Anker nennen. Carroll und Rosson beschreiben das "Paradox of the Active User" (in Carroll, Hrsg., "Interfacing Thought", MIT Press, 1987): zielorientierte Nutzer tauchen direkt in die relevante Handlung ein, statt sich systematisch mit dem Funktionsumfang vertraut zu machen, was erklärt, warum erfahrene, hochfrequente Nutzer eine dichte, direkt zugängliche Darstellung bevorzugen. Shneidermans "Visual Information Seeking Mantra" ("The Eyes Have It", IEEE Symposium on Visual Languages, 1996), "Overview first, zoom and filter, then details-on-demand", zeigt, dass hohe Dichte durch eine Übersichtsebene mit Filter- und Detailmechanismen kontrollierbar bleibt, ohne die für Experten nötige Informationsfülle zu beschneiden. Die verbreitete Faustregel, hohe Dichte passe generell zu Experten-Tools und schade generell bei Gelegenheitsnutzern und mobilen Kontexten, ist über diese beiden Anker hinaus als Praxiswissen ohne eigene quantitative Studie zu kennzeichnen.

## Übersetzung in Regeln

Prüfbare Regeln, an einem fertigen Bildschirm nachmessbar.

| # | Regel | Prüfbar an | Quelle |
|---|---|---|---|
| 1 | Systemstatus (Laden, Verarbeitung, Erfolg) ist jederzeit sichtbar, keine stillen Wartezustände über 1 Sekunde. | Existenz eines sichtbaren Status-Indikators bei jeder asynchronen Aktion. | Nielsen-Heuristik 1; Tankala 2023 |
| 2 | Navigations- und Feldbezeichnungen verwenden Nutzersprache, keine internen System- oder Datenbankbegriffe. | Card-Sorting- oder Tree-Testing-Ergebnis liegt vor oder Begriffe stammen nachweislich aus Nutzerinterviews. | Nielsen-Heuristik 2; Tankala/Sherwin 2024 |
| 3 | Jede irreversible Aktion hat einen sichtbaren Ausweg (Undo, Bestätigungsdialog). | Löschen, Zurücksetzen und vergleichbare Aktionen ohne Bestätigung oder Undo sind nicht vorhanden. | Nielsen-Heuristik 3; Shneiderman-Regel "Umkehrbarkeit" |
| 4 | Häufig genutzte Aktionen liegen nah am vorausgehenden Interaktionsort, nicht am entfernten Seitenanfang. | Abstand in Pixel/Klicks zwischen letztem Eingabefeld und Bestätigungsaktion ist minimal. | Fitts 1954 |
| 5 | Optionen-Listen ab etwa acht Einträgen sind kategorisiert, nicht als eine flache Liste dargestellt. | Zahl der Gruppen mit Zwischenüberschriften gegen Gesamtzahl der Einträge. | Hick 1952/Hyman 1953 |
| 6 | Navigationstiefe ist nicht an der Zahl 7 ausgerichtet, sondern an eindeutigen, testbaren Kategorienamen. | Tree-Test-Erfolgsquote statt einer festen Punktzahl-Obergrenze als Kriterium. | Miller 1956; Whitenton 2013 |
| 7 | Progressive Disclosure bleibt auf maximal zwei Offenlegungsebenen begrenzt. | Klickpfad von Erstansicht zu tiefstem versteckten Element hat höchstens zwei Zwischenschritte. | Nielsen 2006 |
| 8 | Formularlabels bleiben dauerhaft sichtbar, Placeholder ersetzt kein Label. | Jedes Eingabefeld hat ein Label außerhalb des Eingabetexts. | Whitenton 2016 |
| 9 | Fehlermeldungen stehen direkt neben der Ursache, benennen das Problem konkret und behalten die Nutzereingabe. | Meldungstext enthält keine generische Formulierung wie "Fehler aufgetreten", Eingabefeld ist nach Fehler nicht leer. | Neusesser/Sunwall 2023 |
| 10 | Leere Zustände zeigen Grund und direkten Handlungspfad, nie eine unerklärte leere Fläche. | Jeder Empty State enthält Text plus mindestens einen klickbaren Weg zur Befüllung. | Kaplan 2021 |
| 11 | Wichtigste Listeneinträge stehen am Anfang oder Ende, nicht in der Mitte. | Position der Standardauswahl oder Primäraktion in der Liste. | Murdock 1962 (Praxisableitung) |
| 12 | Mehrstufige Prozesse zeigen sichtbaren Fortschritt (Schritt X von Y, Prozentanzeige). | Fortschrittsindikator ist während des gesamten Prozesses sichtbar. | Zeigarnik 1927 |
| 13 | Direkte Reaktion auf Klick/Eingabe erfolgt innerhalb von etwa 400 ms sichtbar, auch wenn die eigentliche Verarbeitung länger dauert. | Zeit zwischen Interaktion und erstem sichtbaren Feedback gemessen. | Doherty/Thadani 1982 |
| 14 | Settings-Seiten zeigen sinnvolle Standardwerte, Anpassungsoptionen nur mit belegtem Nutzen. | Zahl der Optionen ohne dokumentierten Nutzerfall gegen Gesamtzahl. | Nielsen 2009 |
| 15 | Voreinstellungen liegen im Interesse der Nutzer, sind als Voreinstellung erkennbar und ebenso leicht änderbar wie übernehmbar. | Keine vorangehakte Checkbox für Zusatzverkäufe oder Datenweitergabe. | Johnson/Goldstein 2003; Thaler/Sunstein 2008; EuGH C-673/17 |
| 16 | Tabellen mit vielen Zeilen zeigen lesbare Bezeichner statt interner IDs in der ersten Spalte. | Erste Spalte enthält keinen reinen Datenbankschlüssel. | Laubheimer 2022 |
| 17 | Kopfzeile und ggf. erste Spalte bleiben beim Scrollen breiter Tabellen fixiert. | Sticky-Verhalten bei Tabellenhöhe über Viewport. | Laubheimer 2022 |
| 18 | Destruktive und bestätigende Aktionen stehen räumlich getrennt, nicht nebeneinander. | Abstand oder visuelle Trennung zwischen Löschen und Speichern. | Nielsen/Laubheimer 2019 |
| 19 | Dashboards nutzen Balken- oder Liniendiagramme für Vergleiche, keine Kreisdiagramme oder 3D-Effekte für Kennzahlen. | Diagrammtyp je Kennzahl gegen Aufgabentyp (Vergleich, Trend, Anteil). | Laubheimer 2017 |
| 20 | Onboarding verzichtet auf vorgeschaltete Tutorials außerhalb des Nutzungskontexts, Hilfe ist kontextuell abrufbar. | Existenz eines übersprungbaren, jederzeit erneut aufrufbaren Hilfe-Elements statt eines Pflicht-Tutorials. | Laubheimer 2023 |
| 21 | Skeleton Screens bilden die tatsächliche Inhaltsstruktur ab, nicht nur Kopf- und Fußzeile. | Zahl der angedeuteten Inhaltsblöcke gegen tatsächliche Seitenstruktur. | Tankala 2023 |
| 22 | Interaktive Ziele (Buttons, Icons, Formularsteuerelemente) sind mindestens 24 mal 24 CSS-Pixel groß, empfohlen 44 mal 44. | Zielgröße mit den Browser-DevTools nachmessen. | WCAG 2.5.8 Target Size Minimum, Stufe AA; WCAG 2.5.5 Target Size Enhanced, Stufe AAA |
| 23 | Jeder Bildschirm zeigt jederzeit erkennbar, in welchem Dialog sich der Nutzer befindet, welche Handlungen möglich sind und wie sie ausgeführt werden (Selbstbeschreibungsfähigkeit). | Erkennbarer Titel oder Breadcrumb vorhanden, verfügbare Aktionen sind sichtbar statt nur erratbar. | ISO 9241-110:2020 |
| 24 | Mehrstufige Vorgänge lassen, wo die Aufgabe es zulässt, Rückschritt oder Sprung zwischen Schritten zu, statt linear zu erzwingen (Steuerbarkeit). | Zurück-Navigation oder Schrittwahl innerhalb des Assistenten ist vorhanden. | ISO 9241-110:2020 |

## Anti-Muster

| Anti-Muster | Ursache | Beleg |
|---|---|---|
| Menü oder Navigation künstlich auf sieben Einträge begrenzt. | Fehlanwendung von Millers 7±2 auf eine Recognition- statt Recall-Aufgabe. | Miller 1956; Whitenton 2013 |
| Flaches Design ohne Schatten, Kontrast oder Formsignal für klickbare Elemente. | Affordanz vorhanden, aber kein Signifikant, der sie kommuniziert. | Norman 2013 |
| Kennzahl als isolierte große Zahl ohne Vergleichswert oder Zeitbezug. | Fehlende Einordnung macht die Zahl für Entscheidungen wertlos. | NNGroup-Dashboard-Prinzipien, Laubheimer 2017 |
| Für jeden Inhaltstyp dieselbe Karten-in-Karten-Struktur, unabhängig vom Inhalt. | Layout folgt einer Schablone statt dem tatsächlichen Inhalt (Tabelle, Formular, Kennzahl). | Ableitung aus Laubheimer 2022 und Whitenton 2016 |
| Reflexhafte Sidebar-Navigation bei wenigen, selten wechselnden Bereichen. | Konvention statt Ableitung aus Zahl und Wechselhäufigkeit der Bereiche. | Ableitung aus Whitenton 2013 |
| Progressive Disclosure über mehr als zwei Ebenen verschachtelt. | Nutzer verlieren beim Wechsel zwischen Ebenen die Orientierung. | Nielsen 2006 |
| Vorgeschaltetes Pflicht-Tutorial vor der ersten Nutzung. | Nutzer sind aufgabenorientiert und überspringen oder vergessen Erklärungen außerhalb des Nutzungskontexts. | Laubheimer 2023; Carroll/Rosson 1987 |
| Vage Fehlermeldung ohne Ursache oder Lösungsvorschlag. | Verstößt gegen Sichtbarkeit und Verständlichkeit als Kernkriterien guter Fehlermeldungen. | Neusesser/Sunwall 2023 |
| Vorangehakte Checkbox für Zusatzverkauf oder Datenweitergabe. | Default im Interesse des Anbieters statt der Nutzer, als Zustimmung getarnt. | Gray et al. 2018; EuGH C-673/17 |
| Leerer Bereich ganz ohne Erklärung oder Handlungsoption. | Fehlende Unterscheidung zwischen Fehler, Ladezustand und tatsächlich leerem Inhalt erzeugt Verwirrung. | Kaplan 2021 |
| Primärnavigation hinter einem Hamburger-Icon versteckt, obwohl genug Bildschirmbreite für eine sichtbare Sidebar oder Top-Navigation vorhanden ist. | Aus den Augen heißt aus dem Sinn, versteckte Navigation nimmt Nutzern den Überblick über vorhandene Bereiche. | NNGroup-Menü-Design-Prinzipien, Laubheimer 2024 |
| Mehrstufiger Prozess ohne sichtbaren Fortschritt, Nutzer wissen nicht, wie viele Schritte noch folgen. | Keine Nutzung der kognitiven Spannung unvollständiger Aufgaben zur Orientierung und Rückkehrmotivation. | Zeigarnik 1927 |
| Toggle-Beschriftung neutral formuliert ("Benachrichtigungen") statt richtungsbezogen ("Benachrichtigungen erhalten"), Zustand bleibt uneindeutig. | Nutzer können den aktuellen Zustand nicht aus dem Label allein ableiten. | Kendrick 2018 |
| Icon-only-Schaltfläche unter 24 mal 24 CSS-Pixel, ohne ausreichenden Abstand zu Nachbarelementen. | Verstößt gegen die WCAG-Zielgrößen-Kriterien, erhöht die Fehlklick-Rate besonders auf Touchscreens. | WCAG 2.5.8 |
| Erzwungener linearer Assistent ohne Rückschritt- oder Sprungmöglichkeit, obwohl die Aufgabe das erlauben würde. | Verstößt gegen die Steuerbarkeit nach ISO 9241-110 und gegen Shneidermans Prinzip der inneren Kontrolle. | ISO 9241-110:2020; Shneiderman-Regel "innere Kontrolle" |

## Quellen

### Geprüft

- Hick, W. E. (1952). "On the Rate of Gain of Information." Quarterly Journal of Experimental Psychology.
- Hyman, R. (1953). "Stimulus Information as a Determinant of Reaction Time." Journal of Experimental Psychology, 45(3), S. 188.
- Fitts, P. M. (1954). "The Information Capacity of the Human Motor System in Controlling the Amplitude of Movement." Journal of Experimental Psychology, 47(6). http://www2.psychology.uiowa.edu/faculty/mordkoff/InfoProc/pdfs/Fitts%201954.pdf
- Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information." Psychological Review. Volltext https://psychclassics.yorku.ca/Miller/
- Murdock, B. B. (1962). "The Serial Position Effect of Free Recall." Journal of Experimental Psychology, 64(5), S. 482 bis 488.
- Zeigarnik, B. (1927). "Über das Behalten von erledigten und unerledigten Handlungen." Psychologische Forschung, 9, S. 1 bis 85.
- Doherty, W. J.; Thadani, A. J. (1982). "The Economic Value of Rapid Response Time." IBM Systems Journal.
- Nielsen, J.; Molich, R. (1990). "Heuristic Evaluation of User Interfaces." CHI '90 Proceedings.
- Nielsen, J. (1994). "10 Usability Heuristics for User Interface Design." NNGroup. https://www.nngroup.com/articles/ten-usability-heuristics/
- Shneiderman, B. et al. (2016). "Designing the User Interface", 6. Auflage. https://www.cs.umd.edu/users/ben/goldenrules.html
- Norman, D. A. (1988, überarbeitet 2013). "The Design of Everyday Things." Basic Books.
- Hutchins, E.; Hollan, J.; Norman, D. (1986). Ursprung von "Gulf of Execution/Evaluation".
- Rosenfeld, L.; Morville, P.; Arango, J. (2015). "Information Architecture: For the Web and Beyond", 4. Auflage. O'Reilly.
- Larson, K.; Czerwinski, M. (1998). "Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval." CHI 98 Proceedings, S. 25 bis 32.
- Whitenton, K. (2013). "Flat vs. Deep Website Hierarchies." NNGroup. https://www.nngroup.com/articles/flat-vs-deep-hierarchy/
- Budiu, R. (2014). "Search Is Not Enough: Synergy Between Navigation and Search." NNGroup. https://www.nngroup.com/articles/search-not-enough/
- Tankala, S.; Sherwin, K. (2024). "Card Sorting: Uncover Users' Mental Models." NNGroup. https://www.nngroup.com/articles/card-sorting-definition/
- Laubheimer, P. (2023). "Tree Testing to Evaluate a Content Hierarchy." NNGroup. https://www.nngroup.com/articles/tree-testing/
- Laubheimer, P. (2022). "Data Tables: Four Major User Tasks." NNGroup. https://www.nngroup.com/articles/data-tables/
- Whitenton, K. (2016). "Website Forms Usability: Top 10 Recommendations." NNGroup. https://www.nngroup.com/articles/web-form-design/
- Nielsen, J. (2009). "Customization of UIs and Products." NNGroup. https://www.nngroup.com/articles/customization-of-uis-and-products/
- Kendrick, A. (2018). "Toggle-Switch Guidelines." NNGroup. https://www.nngroup.com/articles/toggle-switch-guidelines/
- Kendrick, A. (2020). "Mobile-App Onboarding: An Analysis of Components and Techniques." NNGroup. https://www.nngroup.com/articles/mobile-app-onboarding/
- Laubheimer, P. (2023). "Onboarding Tutorials vs. Contextual Help." NNGroup. https://www.nngroup.com/articles/onboarding-tutorials/
- Kaplan, K. (2021). "3 Guidelines for Designing Empty States in Complex Applications." NNGroup. https://www.nngroup.com/articles/empty-state-interface-design/
- Neusesser, T.; Sunwall, E. (2023). "Error-Message Guidelines." NNGroup. https://www.nngroup.com/articles/error-message-guidelines/
- Tankala, S. (2023). "Skeleton Screens 101." NNGroup, mit Bezug auf Mejtoft, Långström, Söderström (2018), European Conference on Cognitive Ergonomics. https://www.nngroup.com/articles/skeleton-screens/
- Nielsen, J.; Laubheimer, P. (2019). "Top 10 Application-Design Mistakes." NNGroup. https://www.nngroup.com/articles/top-10-application-design-mistakes/
- Laubheimer, P. (2017). "Dashboards: Making Charts and Graphs Easier to Understand." NNGroup. https://www.nngroup.com/articles/dashboards-preattentive/
- Nielsen, J. (2006). "Progressive Disclosure." NNGroup. https://www.nngroup.com/articles/progressive-disclosure/
- Johnson, E. J.; Goldstein, D. G. (2003). "Do Defaults Save Lives?" Science, 302(5649), S. 1338 bis 1339.
- Thaler, R. H.; Sunstein, C. R. (2008). "Nudge: Improving Decisions About Health, Wealth, and Happiness." Yale University Press.
- Gray, C. M. et al. (2018). "The Dark (Patterns) Side of UX Design." CHI 2018 Proceedings.
- Mathur, A. et al. (2019). "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites." Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), Artikel 81.
- Gerichtshof der Europäischen Union, Urteil vom 2019-10-01, Rechtssache C-673/17, Planet49.
- Carroll, J. M.; Rosson, M. B. (1987). "Paradox of the Active User." In Carroll (Hrsg.), "Interfacing Thought." MIT Press.
- Shneiderman, B. (1996). "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations." IEEE Symposium on Visual Languages.
- Nielsen, J. (um 2000). "Jakob's Law of Internet User Experience", bestätigt über NNGroup-Videos https://www.nngroup.com/videos/jakobs-law-internet-ux/ und https://www.nngroup.com/videos/jakobs-law-internet-user-experience/
- NNGroup-Video "How to Use the Zeigarnik Effect in UX." https://www.nngroup.com/videos/zeigarnik-effect/
- NNGroup-Video "Hick's Law: Designing Long Menu Lists." https://www.nngroup.com/videos/hicks-law-long-menus/
- NNGroup, "Fitts's Law and Its Applications in UX." https://www.nngroup.com/articles/fitts-law/
- NNGroup, "Touch Targets on Touchscreens." https://www.nngroup.com/articles/touch-target-size/
- Laubheimer, P. (2024). "Menu-Design Checklist: 17 UX Guidelines." NNGroup. https://www.nngroup.com/articles/menu-design/
- International Organization for Standardization: ISO 9241-110:2020, Ergonomie der Mensch-System-Interaktion, Teil 110: Interaktionsprinzipien (Grundsätze der Dialoggestaltung). https://www.iso.org/standard/75258.html
- World Wide Web Consortium: WCAG 2.2, Erfolgskriterium 2.5.8 Target Size (Minimum), Stufe AA, und Erfolgskriterium 2.5.5 Target Size (Enhanced), Stufe AAA. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

### Ungeprüft

- Genaue Primärquelle (konkrete Alertbox-Ausgabe) für die Erstformulierung von Jakobs Gesetz um das Jahr 2000 nicht direkt aufgefunden, nur über NNGroup-Videos und Sekundärquellen bestätigt.
- Übertragung des Serienpositionseffekts (Murdock 1962, Recall-Studie) auf das Scannen sichtbarer UI-Listen ist Praxisableitung ohne eigene HCI-Studie.
- Zweiter Millisekunden-Schwellenwert unterhalb 400 ms bei der Doherty-Schwelle, wie er in einzelnen Sekundärquellen kursiert, ließ sich nicht an einer zitierfähigen Quelle verifizieren und wurde nicht übernommen.
- Aussage, hohe Informationsdichte passe generell zu Experten-Tools und schade generell bei Gelegenheitsnutzern, über Carroll/Rosson 1987 und Shneiderman 1996 hinaus als quantitative Studie nicht gefunden.
- Dedizierte NNGroup-Quelle speziell zur Informationsarchitektur von Settings-Seiten (Seitenstruktur, nicht Anpassung oder Toggles) wurde trotz gezielter Suche nicht gefunden, als Lücke benannt statt durch eine erfundene Quelle gefüllt.
- Kernaussage zu Onboarding-Tutorials stützt sich bei NNGroup selbst auf punktuelle interne Beobachtung statt auf eine unabhängige, systematische Studie.
- Material Design 3 und Apple Human Interface Guidelines wurden gezielt recherchiert, waren über WebFetch aber nicht als Volltext zugänglich (clientseitig gerendert), deshalb nicht als geprüfte Wortlaut-Quelle verwendet.

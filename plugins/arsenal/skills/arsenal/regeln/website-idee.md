# Modul Website-Idee

Laden bei `plan` und `entwurf` jeder Website der Art `website`, `onepage` und `landingpage` für Kundenaufträge (nicht für Nachschlagen). Schärft, was S02 (Eine Idee aus der Sache) und PR15/PR16 (Nichts Kopiertes, zwei Anker) verlangen: Die Seite gehört zu genau diesem Kunden und ist vollständig, wenn sie ausgeliefert wird. Es kommt kein Agent und keine Prüfrunde hinzu; es schärft vorhandene Schritte und legt drei kurze Abschnitte in `L/MASK.md`. Skript: `werkzeuge/website_check.py`. Herkunft: Blindvergleich zweier Bauten eines Briefs (2026-11-06), eigene Formulierung.

**Lesart.** Ermessen mit Prüffrage. WI01 und WI06 sind Pflicht im Sinne von S05 (fertig heißt vollständig); sonst Abweichung mit Grund und Datum im ARMOURY.

## Reihenfolge

Auftrag, dann Abdeckung (WI01), Inhalt (echter Text und echte Zahlen, S05, S06), Welt und Idee (WI02 bis WI03), Werte aus der Idee (WI04), Bau (Schriften von der ersten Zeile an, WI05; Abschnitte unter der ersten Ansicht aus der Idee, WI07), Prüfung (`werkzeuge/website_check.py`, Modul Anti-KI, Blick), Bericht (was gebaut ist, was angenommen ist, was nicht geprüft werden konnte). Wen man während des Laufs nicht fragen kann: Die Fragen werden Zeilen unter „Annahmen“, die Wahl zwischen Richtungen werden zwei Zeilen im MASK mit den nicht gewählten Richtungen, der Bau geht weiter. Unter Zeitdruck fällt nie weg: Abdeckung, Proben, Abschnitt je Inhalt.

## Regeln

- **WI01 Auftragsabdeckung.** Vor jeder Idee den Auftrag lesen und alles auflisten, was er nennt oder erkennbar meint (was angeboten wird, was es kostet, wo und wann, wie man bestellt oder Kontakt aufnimmt, wer dahintersteht, die Rechtstexte). Im MASK unter `## Auftragsabdeckung` eine Zeile je Wunsch: `- <Wunsch> -> #<Abschnitts-Id>` oder `-> <Überschrift>`. Jede Zeile endet in einem eigenen Abschnitt mit Überschrift; Inhalt, der nur in einem Bedienteil, einem Werkzeug oder einer Fußzeile steht, hat noch keinen. Die Idee darf Abschnitte umordnen und umformen, nie einen schlucken: Ein Werkzeug, das die Preise zeigt, ersetzt den Preisabschnitt nicht. Vor der Abgabe jede Zeile abgehen: Der genannte Abschnitt existiert im gebauten Stand. Prüffrage: Hat jeder Wunsch des Auftrags einen Abschnitt mit Überschrift?
- **WI02 Die Idee ist ein Handgriff.** Die Welt (S02, PR16) gibt der Seite ihr Aussehen, die Idee gibt ihr die Aufgabe: Sie ist das, was der Besucher mit einem Stück aus der Welt dieses Kunden tut, um zur Hauptaktion zu kommen. Eine Welt ohne Handgriff ist ein Kostüm, unter der ersten Ansicht bleibt eine gewöhnliche Liste; ein Handgriff ohne gewählte Welt ist ein Zusatzgerät auf neutraler Seite. Schritte:
  - **Fundstücke zuerst.** Acht oder mehr Stücke dieses Betriebs, je eine Zeile, aus mindestens vier von sechs Schubladen: Dinge, Spuren (Formular, Etikett, Schild, Plan, Beleg, Verpackung), Maße und Zahlen, Wörter des Gewerks, Ort und Licht, Handgriffe (auch die des Kunden am Tresen: was er anfasst, ausfüllt, mitnimmt). Form: `- F4 Spur: Lieferschein mit grünem Durchschlag, Stempel schräg oben rechts (Quelle: Foto, Auftragszeile, eigener Inhalt)`. Sie kommen aus dem Material des Kunden. Was für jeden Mitbewerber gilt, ist kein Fundstück.
  - **Sieben Kandidaten**, je mit einer dritten Zeile: dem Handgriff (ankreuzen, herausziehen, abreißen, einstellen, drücken, ausfüllen) und wie daraus die Hauptaktion wird. Ein Kandidat ohne Handgriff wird vor der Auswahl ersetzt; die sieben schöpfen aus mindestens drei Schubladen.
  - **Wahl** wie `entwurf` sie beschreibt, Favorit zuerst benannt, mindestens eine Richtung, die nicht die eigene Wahl ist.
  - **Satzform** im MASK unter `## Tragende Idee`: „Der Besucher <Handgriff am Fundstück>, und die Seite <macht daraus die Hauptaktion>.“ Nicht „Die Seite ist ein <Ding>“: Das nennt ein Aussehen, der Besucher tut nichts.
  - Der Handgriff ist der schnelle Weg, nie der einzige: Dieselbe Aktion geht per Tastatur, und ohne Skript bleiben Inhalt lesbar und Kontaktweg nutzbar.

| | Kostüm (schmückt) | Handgriff (trägt) |
|---|---|---|
| Weingut | Reben als Zierlinie | der Besucher zieht ein Fach aus dem Kellerregal, sieht Jahrgang und Preis wie am Regal und bestellt daraus |
| Physiotherapie | Wellenlinien, Pastell | der Besucher geht den ersten Termin durch (Empfang, Behandlung, Training) und wählt ihn am Empfang |
| Fahrradwerkstatt | ein Zahnrad, das sich beim Scrollen dreht | der Besucher kreuzt auf dem Annahmezettel an, was klappert, sieht Dauer und Preis und bucht den Tag |

Die Beispiele zeigen die Bauweise; ein übernommenes Motiv ist eine Kopie, keine Idee (PR15).

- **WI03 Vier Proben für die Idee.** Im MASK als eine Zeile `Proben: Tausch <nein, weil>, Kulisse <ordnet was>, Erstgriff <nein>, Nutzen <ja, Handgriff>`. (1) Tausch: den nächsten Mitbewerber desselben Gewerks einsetzen; gilt der Satz weiter, ist es eine Idee des Gewerks („Es sind unsere Produkte und Preise“ zählt nicht). (2) Kulisse: das Motiv wegnehmen; bewegt sich etwas (Reihenfolge der Abschnitte, Navigation, Bedienteil der Hauptaktion)? Wenn nicht, schmückt es nur. (3) Erstgriff: Ist es die Seite, die diese Kategorie immer liefert, oder der eigene Favorit? (4) Nutzen: Führt der Besucher die Hauptaktion mit dem Handgriff selbst aus? „Spart einen Klick“ genügt nicht. Fällt eine Probe durch, wird höchstens zweimal neu gewählt, danach gilt der stärkste Kandidat und die durchgefallene Probe steht unter „Annahmen“.
- **WI04 Werte folgen aus der Idee.** Die Entscheidungen von AK25 stehen einmal, je Zeile mit zwei Einträgen mehr: `folgt aus` (das Ding der Idee, ein Fundstück `F<n>` oder die belegte Marke) und `Erstgriff` (was man ohne Nachdenken genommen hätte). Ein Wert, der seinem Erstgriff gleicht, braucht die Idee oder ein Fundstück als Grund. Zuerst das Ding der Idee fragen, die übrigen Fundstücke nur, wo es schweigt:

| Feld | Frage an das Ding der Idee |
|---|---|
| Schrift | Was steht, ist gedruckt, gestempelt oder geprägt darauf? Merkmale notieren (Breite, Strichkontrast, Ziffern, Serifen), dann unter den lieferbaren Schriften suchen, nie nach Beliebtheit |
| Grund | Woraus besteht es, in welchem Licht öffnet der Besucher die Seite? |
| Farbe | Welche Farben trägt es selbst (Material, Tinte)? Eine Farbe für die Aktion. Eine Farbe je Produkt oder Tarif quer durch den Farbkreis ist eine Ampel und fällt, außer der Betrieb zeigt genau das |
| Aufbau | Welches Format hat es (Felder, Fächer, Zeilen), welche Gestalt hat der Inhalt? |
| Erste Ansicht | Wo liegt es, was tut der Besucher zuerst damit? |
| Bild | Was zeigt es, was lässt sich im Betrieb fotografieren? Eine Behandlungsregel für alle Bilder |
| Bewegung | Was geschieht am Handgriff (herausziehen, abreißen, einrasten)? Diese eine Bewegung an der Hauptaktion |
| Form | Welche Kante hat es (gesägt, gefaltet, gestanzt)? 0 ist ein Wert wie jeder andere und braucht denselben Grund |

  Mindestens fünf der acht folgen aus der Idee oder der Marke, sonst ist die Seite eine Sammlung einzelner Griffe. Zwei Wächter: Die Bindung an Mut (Farbe im Seitenmaßstab, hell oder dunkel nach der Szene, Schriften mit Haltung; Regler und S02) bleibt; die Ableitung bestimmt, welche Farbe und welche Schrift, nie eine schwächere Bindung. Und: erst fragen, was der Kunde in der Hand hält, sieht und mitnimmt, die Werkstatt nur fragen, wo die Werkstatt das Angebot ist. Ein Wert, der der Werkstatt treu ist, aber dem Gefühl der Kundschaft widerspricht (kalt bei Essen, klinisch bei einem Geschenk), wird aus einem anderen Fundstück neu abgeleitet. Warm heißt nie Creme: die gesättigten Materialien dieser Welt nehmen.
- **WI05 Schriften reisen mit der Seite.** Jede Familie, die das Konzept nennt, ist eingebettet (WOFF2 neben der Seite per `@font-face`, bei Einzeldatei als `data:font/woff2;base64,`-Quelle; eine Datei ist nie ein Grund für eine Systemschrift). Eine Schrift, die nur ein Betriebssystem mitbringt (Bahnschrift, Segoe UI, SF Pro, Helvetica Neue, Avenir, Calibri), trägt nie den Auftritt, ebenso keine variable Achse, die der Ersatz nicht hat. Herkunft der Dateien: WOFF2 im Projekt oder auf der Platte, dann die freien Quellen in `regeln/medien.md` und `rezepte/`. Gewählt wird unter den lieferbaren Schriften; ist die passende nicht zu beschaffen, kommt die lieferbare mit den nächsten Merkmalen, gesagt unter „Annahmen“. Nach der eingebetteten Schrift setzt der Stapel mit derselben Klasse fort. Ergänzt TE09. Prüffrage: Steht jede führende Familie des Stapels als `@font-face` oder Datei bei der Seite?
- **WI06 Gegen das Hausbild.** Die Werte, die ein Regelbeispiel für eine Marke nennt (Pille an jedem Bedienteil, eckige Flächen, Vollfarbbänder, Haarlinienzeilen, Kapitel-Labels), gehören dieser Marke. Auf der Seite eines anderen Kunden sind sie das Hausbild; jeder braucht einen eigenen Grund aus der Idee dieses Kunden. Eine Zeile im MASK: `Arsenal-Reflex: <der Griff, den dieses Regelwerk hier nahelegt> -> <was stattdessen und warum>`. Eine Seite, die auf der Reflexzeile landet, wird aus der Idee neu gebaut, nicht poliert. Gewohnheitsgriffe sind nicht verboten und haben keinen vorgeschriebenen Ersatz; wer nach einem greift, beantwortet seine Frage aus Idee und Fundstücken:

| Griff | Frage |
|---|---|
| Pille an allem Anklickbaren | Welche Form hat ein Knopf, ein Schalter, ein Griff in diesem Betrieb? |
| Haarlinienliste als Muster jeder Gruppe | Was trennt dort Dinge (Fach, Fuge, Falz, Zeile)? |
| Vollfarbband je Abschnitt | Welche Abschnitte sind wirklich ein anderer Ort, und was heißt ein Grundwechsel hier? |
| Papierton mit dunkler Tinte | Welche Fläche fasst der Kunde wirklich an? |
| Zentrierter Stapel aus Zeile und Knopf | Wo beginnt das Auge auf dem Fundstück? |
| Gewerkfarbe, Gewerkmotiv, Farbe je Produkt | Was unterscheidet diesen Betrieb von seinem Nachbarn (Tauschprobe)? |
| Hauptschrift oder erste Ansicht einer früheren Arbeit | Was wäre diese Seite, wenn jene nie gebaut worden wäre? |

- **WI07 Unter der ersten Ansicht.** Das Ding der Idee setzt sich fort: Fläche, Kanten, Bedienteil und Knopfbeschriftung der Hauptaktion folgen der Ableitung; ein Abschnitt, der ohne sie eine gewöhnliche Liste wäre, wird aus ihr gebaut. **Wiedererkennungsprobe:** Bei 25 % Größe ist jedes der beiden Markendetails (AK22) an seinem Platz in der ersten Ansicht zu sehen; ohne Render werden Element und Position aus dem Quelltext benannt und gesagt, dass gelesen und nicht gesehen wurde. **Entfernungsprobe:** Ein Schmuck, dessen Wegnahme nichts bewegt und nichts vermissen lässt, bleibt draußen.
- **WI08 Abgabe: ein Abschnitt je gefordertem Inhalt, Kanal und Telefon.** Alles, was die Seite anbietet, kann die Hauptaktion aufnehmen: Jede Variante, Größe oder Option, die die Seite nennt oder bepreist, ist im Bestell-, Buchungs- oder Anfrageweg wählbar. Die Hauptaktion endet im Kanal, den der Auftrag nennt (Telefon, Messenger, Formular, Shop); ein schwächerer Ersatz, etwa ein Mail-Link, wo der Auftrag Nachricht sagt, ist eine Zeile unter „Annahmen“. Ein Betrieb mit Ort zeigt Telefonnummer oder Buchungsweg in der ersten Ansicht ohne Menü, auch am Handy.

## Abgabeprüfung

`python3 werkzeuge/website_check.py <Seite.html oder Ordner> --konzept L/MASK.md` prüft W1, W3, W5 und W6 aus dem Quelltext. Alle acht werden mit dem Befund dahinter an die Prüfliste angehängt:

- W1 Jede Zeile von `## Auftragsabdeckung` hat ihren Abschnitt (WI01).
- W2 Jede genannte Variante ist in der Hauptaktion wählbar, die Aktion endet im Kanal des Auftrags (WI08).
- W3 Kein Platzhalterwort, keine Ziffernattrappe, keine Klammerlücke in sichtbarem Text und Linkzielen (S05).
- W4 Keine erfundene Bewertung, kein erfundener Beleg (S06).
- W5 Jede führende Familie ist mit der Seite ausgeliefert (WI05).
- W6 `## Tragende Idee` enthält den Satz in Handgriff-Form und die Zeile `Proben:` mit allen vier Proben (WI02, WI03).
- W7 Wiedererkennungs- und Entfernungsprobe sind gemacht (WI07).
- W8 Die Zeile `Arsenal-Reflex:` steht, jeder benutzte Gewohnheitsgriff hat seine Antwort (WI06).

Hinweis: Das Skript prüft zusätzlich, dass ein Abschnitt `## Annahmen` vorhanden ist. Das stammt aus einer Quellregel, die erfundene Betriebsangaben zuließ und die S06 widerspricht (siehe das Protokoll der Übernahme); der Abschnitt gilt hier nur für das, was als Annahme an <dein-name> oder den Kunden geht, nie für erfundene Zahlen, Namen oder Belege.

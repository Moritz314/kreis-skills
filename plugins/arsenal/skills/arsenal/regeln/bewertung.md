# Modul Bewertung

Laden bei `audit` und `kritik` für Anwendungen und für Websites, die Bedienung enthalten (Formulare, Shop, Konfigurator). Die Skala 0 bis 4 bewertet die Bedienbarkeit nach Nielsens zehn Heuristiken; sie steht neben der Note der Kritiker (`befehle/kritik.md`, Skala 1 bis 10 für Gestaltung) und ersetzt sie nicht. Quelle: impeccable 4.6.0 `critique.md`, Abschnitt Heuristics Scoring Guide (Apache-2.0, Skill am 2026-11-20 gelöscht, Stand siehe `HERKUNFT.md`), für Arsenal umformuliert; Nielsen Norman Group, zehn Usability-Heuristiken.

**Lesart.** Ehrlich bewerten: Eine 4 heißt wirklich ausgezeichnet, nicht „gut genug“. Die meisten echten Oberflächen erreichen 20 bis 32 von 40. Jede Zahl braucht eine Beobachtung am gebauten Stand (Ort, was geschah). Ermessen mit Prüffrage; die Bewertung ist ein Befund, keine Abnahme.

## Die zehn Heuristiken (je 0 bis 4)

Anker je Heuristik: **0** = die Eigenschaft fehlt, der Nutzer rät oder sitzt fest; **1** = selten, die meisten Wege ohne; **2** = teilweise, große Lücken; **3** = gut, kleine Lücken; **4** = ausgezeichnet, nichts zu verbessern. Prüfpunkte je Heuristik:

- **BW01 Sichtbarkeit des Systemstatus.** Ladezeichen bei Asynchronem; Bestätigung von Aktionen (Speichern, Senden, Löschen); Fortschritt bei mehrstufigen Abläufen; aktueller Ort in der Navigation (Pfad, aktiver Punkt); Prüfung im Feld, nicht erst beim Senden. (Vgl. SW03.)
- **BW02 Übereinstimmung von System und Wirklichkeit.** Vertraute Begriffe ohne unerklärten Fachjargon; Reihenfolge nach Erwartung; erkennbare Icons und Bilder; Sprache der Zielgruppe; natürlicher Lesefluss. (Vgl. TX04, SW-Regeln zur Nutzersprache.)
- **BW03 Nutzerkontrolle und Freiheit.** Rückgängig und Wiederholen; Abbrechen in Formularen und Dialogen; klarer Weg zurück; Filter, Suche und Auswahl leicht zu leeren; Ausstieg aus langen Abläufen. (Vgl. SW04, SA04.)
- **BW04 Konsistenz und Standards.** Gleiche Begriffe überall; gleiche Aktion, gleiches Ergebnis; Plattformkonventionen; sichtbare Einheit (Farbe, Schrift, Abstand, Bauteile); gleiche Geste, gleiches Verhalten. (Vgl. SW05.)
- **BW05 Fehlervermeidung.** Bestätigung vor Zerstörendem; Eingabebegrenzung (Datumswähler, Auswahllisten); sinnvolle Vorgaben; eindeutige Beschriftung; Autosave und Entwurfswiederherstellung. (Vgl. SA05.)
- **BW06 Erkennen statt Erinnern.** Optionen sichtbar statt in versteckten Menüs; kontextuelle Hilfe (Tooltips, Hinweise im Feld); zuletzt Benutztes; Vervollständigung und Vorschläge; Icons mit Beschriftung, keine reine Icon-Navigation.
- **BW07 Flexibilität und Effizienz.** Kürzel für häufige Aktionen; anpassbare Elemente; Favoriten; Sammelaktionen; Expertenfunktionen, ohne das Einfache zu erschweren. (Vgl. SW17, SA03.)
- **BW08 Ästhetisches und minimalistisches Design.** Nur nötige Information je Schritt; Hierarchie lenkt die Aufmerksamkeit; Farbe und Betonung mit Zweck; kein Schmuckballast; fokussierte Aufbauten. Prüffrage (Ermessen): Wie viele Möglichkeiten muss man an einem Entscheidungspunkt zugleich überblicken? Richtwert bis 4; 5 bis 7 gruppieren oder schrittweise zeigen (SW08); ab 8 ist es überladen. Der Richtwert gilt je Entscheidungspunkt (Knopfleiste, Auswahl, Formularschritt), nicht für die Navigation: Deren Zahl regeln SW07 und PR06. (Vgl. S01.)
- **BW09 Fehler erkennen, verstehen, beheben.** Klartext statt Codes; das Problem genau benannt („Mail ohne @“, nicht „Ungültige Eingabe“); ein Weg zur Behebung; Fehler am Ursprung; das Formular wird nicht geleert. (Vgl. TX08, SA10.)
- **BW10 Hilfe und Dokumentation.** Durchsuchbare Hilfe; kontextuelle Hilfe; nach Aufgaben statt nach Funktionen geordnet; knapp und überfliegbar; erreichbar, ohne den Zusammenhang zu verlassen.

## Summe und Urteil

- **BW11 Summe.** Höchstens 40 (zehn mal 4).

| Summe | Urteil | Bedeutung |
|---|---|---|
| 36 bis 40 | ausgezeichnet | nur Feinschliff, ausliefern |
| 28 bis 35 | gut | schwache Stellen beheben, die Basis trägt |
| 20 bis 27 | brauchbar | deutliche Verbesserung nötig, bevor Nutzer zufrieden sind |
| 12 bis 19 | schwach | große Überarbeitung, die Grunderfahrung ist gestört |
| 0 bis 11 | kritisch | neu gestalten, so unbrauchbar |

- **BW12 n/a statt geschenkter Vieren.** Heuristik 7 (Flexibilität) und 10 (Hilfe) dürfen bei Werbeseiten (Landingpage, Kampagne, Portfolio) entfallen, ebenso jede, die erkennbar nicht passt: `n/a` mit einer Begründungszeile, die Summe auf das anwendbare Maximum umrechnen (4 mal Zahl der bewerteten, etwa **24/32** bei zwei `n/a`). Das Urteil dann aus dem Prozentwert: ab 90 % ausgezeichnet, ab 70 % gut, ab 50 % brauchbar, ab 30 % schwach, darunter kritisch (24/32 sind 75 %, also gut).
- **BW13 Eichung.** Eine statische Seite ohne Formular bekommt bei 5 und 9 nur dann 3 oder 4, wenn es wirklich nichts falsch zu machen gibt; sonst `n/a`. Beispiele: Ein Kontaktformular mit rotem Rahmen und ohne Text bei Fehler ist bei 9 eine 2; dasselbe mit „Mail ohne @“ am Feld und erhaltenem Text eine 4. Icon-Navigation unten ohne Beschriftung und ohne aktiven Zustand: 1 bei 6, 2 bei 1. Ein Cookie-Banner, das die Seite sperrt und neben „Annehmen“ kein „Ablehnen“ hat: 1 bei 3. Anker: Wer überall Vieren vergibt, bewertet die zwei schwächsten Punkte einen Schritt tiefer und schreibt auf, was konkret die 4 verdient hätte.

## Schwere je Befund (P0 bis P3)

- **BW14 Jeder Einzelbefund trägt eine Stufe.**

| Stufe | Name | Beschreibung | Handlung |
|---|---|---|---|
| P0 | blockiert | verhindert, die Aufgabe überhaupt zu beenden | sofort beheben |
| P1 | schwer | erhebliche Schwierigkeit oder Verwirrung | vor der Abgabe beheben |
| P2 | leicht | Ärgernis, ein Umweg besteht | im nächsten Durchgang |
| P3 | Politur | schön, wenn behoben, ohne echte Wirkung auf Nutzer | wenn Zeit bleibt |

Zweifelsfrage zwischen zwei Stufen: Würde ein Nutzer deshalb beim Support anrufen? Dann mindestens P1. Die Stufen entsprechen denen des Scanners (`werkzeuge/scan_antipatterns.py`: P0 bis P3).

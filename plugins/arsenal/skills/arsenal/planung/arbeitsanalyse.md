# Arbeitsanalyse, Durchgang und Strukturen (Art `anwendung`)

Verfahren zu `regeln/software-arbeit.md` (SA01 bis SA11). Vor dem ersten Entwurf jeder Oberfläche, an der Menschen arbeiten (Web-App, PWA, internes Werkzeug, Übersicht, Editor, Einstellungen), wird geklärt, wie die Arbeit geschieht: wer, wo, auf welchem Gerät, wie oft, in welcher Menge, wie heute, wo es am meisten kostet. Daraus folgen ein Schrittbudget je Kernaufgabe und nummerierte Aufbau-Vorgaben, die jede Variante erfüllen muss. Websites und Werbeseiten überspringen diese Datei.

Einhängen: `plan` nach den ersten Fragerunden (Hauptaktion, Zustände); Ergebnis kommt in `L/SOUL.md` bzw. als `L/ARBEIT.md`. `entwurf`/`bauen`: jede Variante erfüllt die Aufbau-Vorgaben und plant K1 innerhalb des Budgets; vor dem Code steht im `L/MASK.md` der Abschnitt „Arbeitsfluss“ (unten). `kritik`: Kritiker R führt den Durchgang aus. Vorlage: `werkzeuge/vorlagen/ARBEIT.md` (höchstens 3 KB, die ersten drei Abschnitte höchstens 1,5 KB). Prüfung: `python3 werkzeuge/arbeit_check.py <Ordner>/ARBEIT.md --json` ohne Befund.

## Arbeitsanalyse

1. **Quellen in dieser Reihenfolge:** das laufende Produkt (heutige Schritte dort zählen, nicht schätzen), ein Datenexport oder Beispieldaten, der Auftrag und die Aussagen des Kunden, das beste Werkzeug der Kategorie. Eine Zahl ohne Quelle beginnt mit `Annahme:`. Ein vorhandenes ARBEIT.md wird erweitert, nicht ersetzt.
2. **Nie warten.** Fehlt etwas, höchstens drei Fragen in einer Runde, je mit der Annahme, die sonst gilt. Ohne Antwort gelten die Annahmen, die Arbeit geht weiter; sie stehen in der Zusammenfassung von `plan`.
3. **Szene** (`## Szene`): je Rolle eine Zeile mit Person, Ort, Gerät mit Breite in px, Eingabe (Tastatur und Maus, Touch, eine freie Hand, Headset), Unterbrechungen, Licht, Stunden am Tag. Schlecht: „Büroangestellte nutzen die Übersicht“. Gut: „Die Disponentin sitzt 8 Stunden an einem 24-Zoll-Monitor (1920 px), telefoniert ständig und tippt mit beiden Händen.“
4. **Aufgaben** (`## Aufgaben`): drei bis sieben Zeilen mit Aufgabe, Rolle, Auslöser, Häufigkeit (Zahl je Tag, Woche oder Monat), Schritte heute, Dauer heute, Datenobjekt, Menge üblich und höchstens, Ergebnis. Was es heute nicht gibt, ist `neu`.
5. **Kernaufgaben** (`## Kernaufgaben heute`): höchstens drei Zeilen mit dem größten Produkt aus Häufigkeit und Dauer; K1 ist die größte. Je Kernaufgabe das heutige Vorgehen als nummerierte Handgriffe und die teuerste Stelle (meiste Zeit, meiste Fehler oder Werkzeugwechsel, mit Beleg).
6. **Daten** (`## Daten und Mengen`): je Objekt die höchstens sieben Felder, nach denen der Nutzer entscheidet (sie bilden die Listenzeile), der längste echte Wert mit Zeichenzahl, wer ihn ändert und wie oft.
7. **Budget** (`## Budget`) je Kernaufgabe. Untergrenze = Pflichteingaben + 2 (Auslöser, Abschluss). Schrittbudget = Untergrenze + 2, nie mehr als heute, nie unter der Untergrenze. Handwechsel (zwischen Tastatur und Zeiger): 0 für Tastaturrollen, sonst höchstens 2. Beispiel: drei Pflichtfelder ergeben Untergrenze 5 und Budget 7; heute sind es 9.
8. **Aufbau-Vorgaben** (`## Aufbau-Vorgaben`) aus der Tabelle unten, nummeriert A1 bis An, je mit Herkunft in Klammern: `(aus K1, 40 je Tag)`. Eine Vorgabe nennt Form, Ort oder Zahl. Schlecht: „A3 modern, klare Liste“. Gut: „A3 offene Rückrufe als Tabelle mit festem Kopf, Sofortfilter und gespeicherten Ansichten (aus Menge bis 500)“. Widersprechen sich zwei, gewinnt die der häufigeren Aufgabe.
9. **Anforderungen:** je Kernaufgabe ihr Budget mit der Abnahme „Durchgang hält das Budget“; je Ansicht die Zustände leer, lädt, Fehler, voll; je Aufbau-Vorgabe eine Zeile mit messbarer Abnahme („Liste mit 500 Zeilen scrollt ohne Ruckeln“, nicht „schnell“).
10. Prüfskript laufen lassen, jeden Befund beheben.

### Von der Arbeit zum Aufbau

| Befund im ARBEIT.md | Aufbau-Vorgabe |
|---|---|
| Aufgabe 5 mal am Tag oder öfter | von der Startansicht ohne Navigation erreichbar, eigenes Kürzel, kein Dialog im Weg |
| täglich bis wöchentlich | höchstens ein Navigationsschritt |
| seltener als wöchentlich | hinter höchstens zwei Ebenen, beschriftet statt nur Icon, bequeme Dichte |
| Menge bis 7 | alles sichtbar, keine Suche |
| Menge 8 bis 50 | Liste mit Sortierung und Sofortfilter |
| Menge 51 bis 500 | Tabelle mit festem Kopf, Filtern und gespeicherten Ansichten |
| Menge über 500 | zuerst Suche, dazu Seiten oder Virtualisierung |
| dieselbe Aktion auf drei oder mehr Einträgen hintereinander | Sammelauswahl (Kästchen, Umschalt-Bereich, alle Treffer) und Aktionsleiste mit Anzahl |
| Serienerfassung | „Speichern und weiter“, Fokus zurück ins erste Feld, letzte Werte vorbelegt |
| eine Entscheidung braucht zwei Objekte | beide zugleich sichtbar (Liste neben Detail oder Seitenblatt), kein Seitenwechsel |
| Rolle arbeitet über 2 Stunden am Tag damit | kompakte Dichte mit bequemer Variante, keine Bewegung bei häufigen Aktionen |
| Tastatur den ganzen Tag | Pfeiltasten in Listen, Enter öffnet, Escape schließt, Suche auf einer Taste |
| Touch oder eine freie Hand | Ziele ab 44 px, Hauptaktion in Daumenreichweite, nichts nur auf Hover |
| oft unterbrochen | Eingabe sichert sich selbst (Entwurf übersteht Neuladen), Zustand steht in der Adresse |
| Rolle ist beim Arbeiten am Telefon | Identität, Nummer und dauerhafte Hinweise fest im Kopf; die Anrufaktion groß und beschriftet; Notizfeld eine Taste entfernt |
| eine Entscheidung hängt an Geld oder Beträgen | Tabelle mit rechtsbündigen Tabellenziffern und Summenzeile; die abgeleitete Entscheidungszahl daneben |
| ein handlungsfordernder Status ist selten (überfällig, fehlgeschlagen) | nur dieser Status trägt Farbe, alles andere bleibt neutral |
| Szene | hell oder dunkel nach dem Licht; die Breite des Arbeitsplatzes ist eine zusätzliche Prüfbreite |

### Abschnitt „Arbeitsfluss“ im `L/MASK.md`

Jede Variante trägt ihn vor dem Code, neben den Entscheidungen von AK25: die Struktur in einem Satz mit Charakterskizze; die Schritte von K1 (und jeder weiteren Kernaufgabe) mit Tasten, die Summe gegen das Budget, die Handwechsel; je Aufbau-Vorgabe, wo sie erfüllt ist, oder der Grund im ARMOURY; zwei Stellen mit eigenem Charakter (SA11); für jeden benutzten Gewohnheitsgriff die Antwort auf seine Frage (Seitenleiste mit Kachelraster als Startansicht: welche Aufgabe beginnt hier und was braucht ihr erster Schritt? Status als Pille überall: welcher Status verlangt Handeln? Icon vor jedem Menüpunkt: welcher Punkt ist per Bild schneller zu finden als per Wort?). Ohne Antwort fällt der Griff weg.

```arbeitsfluss
navigation: <seitenleiste | kopfleiste | palette | keine>
hauptform: <tabelle | liste-detail | board | zeitleiste | formularfolge | kalender>
zeilenhoehe: <px>
bedienung: <tastatur | zeiger | touch>
kernaufgabe_schritte: <Zahl>
```

Abbruch: Gibt es weder ein laufendes Produkt noch eine Häufigkeit oder Menge mit Quelle, gilt eine Fragerunde, dann Annahmen (das Skript warnt). Geschieht keine Aufgabe mindestens wöchentlich, ist die Oberfläche kein Arbeitswerkzeug: Das wird gesagt; Budgets gelten weiter, die Dichte ist bequem.

## Durchgang (Prüfung vor der Abgabe)

Vor der Abgabe führt ein frischer Prüfer jede Kernaufgabe auf der gerenderten Oberfläche aus wie die Rolle, zählt Schritte und Wechsel und legt sie gegen das Budget. Zahlen über die Arbeit kommen nur aus dem Durchgang; kein Kritiker schätzt sie. Ein Prüfer je Variante und einer auf dem gebauten Stand, ohne das MASK der Variante und ohne die Geschichte des Bauers, auf der stärkeren Modellstufe. Schreibt `durchgang.json` nach `werkzeuge/vorlagen/durchgang.schema.json`. Prüfung: `python3 werkzeuge/arbeit_check.py <ARBEIT.md> --durchgang durchgang.json --json`, auf dem gebauten Stand zusätzlich `--alle`.

1. **Eingabe:** Adresse der Oberfläche, ARBEIT.md, ein Browserwerkzeug, das klickt, tippt und Tasten sendet. Fehlt eines, lautet das Urteil `ungeprueft`; nichts wird aus Code oder Bildern geschätzt, die Variante ist nicht freigegeben.
2. **Einrichten wie die Szene:** Arbeitsplatzbreite, Eingabe der Rolle (Tastaturrolle nur Tasten, Touchrolle nur Touch, ohne Hover), größte Menge.
3. **Umfang:** im Entwurf K1, auf dem gebauten Stand jede Kernaufgabe, vom Auslöser bis zum Ergebnis, ohne vorher den Code zu lesen. Je Handlung eine Protokollzeile: `nr`, `handlung`, `eingabe` (tastatur, zeiger, touch), `bereich` (navigation, kopf, liste, detail, dialog, formular), `rueckmeldung`; Fehlgriffe mit `fehlgriff: true`, fehlende Rückmeldung mit `warten: true`.
4. **Zählen.** Ein Schritt ist jeder Klick oder Tipp, jede Taste mit Wirkung (Kürzel, Enter, Escape, Pfeil, Tab), jede abgeschlossene Feldeingabe (zählt 1, egal wie lang), jedes nötige Scrollen. Handwechsel: Die `eingabe` wechselt von einer Zeile zur nächsten zwischen Tastatur und Zeiger. Blickwechsel: Der `bereich` wechselt. Das Skript rechnet die Summen nach. Gut („Rückruf erfassen“, Budget 7): N (Tastatur, Liste), Namen tippen (Formular), Tab, Nummer tippen, Tab, Anliegen tippen, Strg+Enter: 7 Schritte, 0 Handwechsel, 1 Blickwechsel, bestanden. Schlecht: „etwa 5 Klicks“ ohne Protokoll.
5. **Sechs Proben**, je `ergebnis` (bestanden, durchgefallen, entfaellt, ungeprueft) und `beleg`: `wiederholung` (K1 dreimal hintereinander; Fokus kehrt zurück, Vorbelegung bleibt, Schrittzahl steigt nicht); `neuladen` (mitten in der Aufgabe neu laden, dann Zurück; Zustand und Eingabe bleiben oder der Verlust wird vorher angekündigt); `falscheingabe` (Pflichtfeld leer, falsches Format, in jedem bearbeitbaren Formular samt Stammdaten; Meldung am Feld mit Ausweg, Eingabe bleibt, Fokus auf dem ersten Fehler, keine Meldung beim Tippen); `zerstoerung` (Löschen oder Überschreiben; umkehrbares bietet Rückgängig, unumkehrbares fragt mit Name und Anzahl); `zustaende` (leer, lädt, Fehler und längster Wert bei Arbeitsplatzbreite, 1440 und 440 px; kein Überlauf, gekürzter Text ganz erreichbar, jeder Zustand nennt den nächsten Schritt, Kopf und Hinweise bleiben beim Scrollen); `sammelaktion` (nur wenn eine Aufbau-Vorgabe sie verlangt; fünf Einträge wählen, einmal handeln, Anzahl stimmt).
6. **Aufbau-Vorgaben:** jede Zeile A1 bis An ist erfüllt oder wird ein Befund.
7. **Befunde:** `stufe`, `regel` (`SA<n>`/`SW<n>` oder `A<n>`, sonst `keine`), `ort`, `befund`, `korrektur`. `muss`: Kernaufgabe über Budget oder mit mehr Handwechseln als erlaubt, Sackgasse, Datenverlust, Probe `zerstoerung` durchgefallen, Aufbau-Vorgabe nicht erfüllt (eine gültige Ausnahme im ARMOURY nimmt den Befund). `soll`: falscher Handgriff an einem Standardteil, Blickwechsel in mehr als der Hälfte der Schritte, Wartepunkt, jede andere durchgefallene Probe, Tastenhinweise, die die Oberfläche überladen. `geschmack`: Geschmacksfragen. Die Korrektur nennt die Struktur, nicht die Farbe („Erfassungszeile in der Startansicht, Taste N“, nicht „größerer Knopf“).
8. **Urteil:** `freigabe` (jede Kernaufgabe besteht, kein `muss`, keine Probe durchgefallen oder ungeprüft), `verwerfen` (K1 nicht zu Ende zu bringen: die Struktur trägt die Arbeit nicht, zurück zur Variante), sonst `nacharbeit`.

Bindung: Der Prüfer ändert nichts. Ein Kürzel zählt nur, wenn die Oberfläche es zeigt (Beschriftung, Tooltip, Menü, Liste unter `?`). Der Bauer zählt vor der Übergabe nach derselben Regel und schreibt die Zahl ins MASK; sie ersetzt den Durchgang nie. Ohne ARBEIT.md (bestehendes Produkt, nur Kritik) laufen nur Schritt 3 bis 5 und 7 für die genannte Aufgabe; die gezählten Schritte werden die Spalte „Schritte heute“ eines neuen ARBEIT.md.

## Strukturen (Wissen auf Abruf)

Beim Zerlegen des besten Werkzeugs der Kategorie vor den Varianten, oder um zwischen zwei Strukturen zu wählen, die beide die Aufbau-Vorgaben erfüllen: Kernaufgabe im Werkzeug ausführen und notieren (1) die Schritte nach der Zählregel, (2) wo die nächste Aktion nach jedem Schritt liegt, (3) den Namen des Musters, das es kurz macht, (4) was man übernimmt und was nicht. Man übernimmt die Mechanik, nie das Aussehen. Zwei Maßstäbe: die Art, wie ein gutes CRM einen Datensatz bearbeiten lässt (alles zu einem Objekt auf einem Bildschirm, nächste Aktion immer am selben Ort), und die Ruhe eines gut gemachten Desktop-Fensters (ein Akzent, wenige Rahmen, der Inhalt ist das Lauteste).

| Muster | Aufbau | Passt, wenn | Bricht, wenn | Kosten |
|---|---|---|---|---|
| Datensatzansicht (drei Zonen) | fester Kopf mit Identität, wichtigstem Kontaktfeld und dauerhaften Hinweisen; links Eigenschaften (in der Zeile bearbeitbar, beim Verlassen geprüft), Mitte Verlauf (Notizen, Mails, Anrufe, Änderungen), rechts verknüpfte Objekte; feste Aktionszeile oben in der Mitte; jede Zone scrollt für sich | ein Objekt ist die Arbeitseinheit und Entscheidungen brauchen seinen Verlauf (Kunde, Auftrag, Ticket) | Objekte ohne Verlauf; Aufgaben über viele Objekte; unter etwa 1100 px faltet die rechte Zone in die Mitte | Aktivität erfassen in 2 bis 3 Schritten ohne den Datensatz zu verlassen |
| Liste mit Detail | Liste mit 30 bis 40 % Breite, die Auswahl öffnet daneben; Pfeiltasten bewegen, das Detail folgt | Abarbeiten einer Warteschlange (Eingang, Freigaben, Rückrufe), 8 bis 500 Einträge | Vergleich über viele Spalten (dann Tabelle); Detail braucht volle Breite | nächster Eintrag 1 Taste |
| Tabelle mit Seitenblatt | dichte Tabelle mit festem Kopf, Beträge rechtsbündig in Tabellenziffern mit Summenzeile, Zeilenklick öffnet ein Blatt von rechts, Tabelle behält Scroll und Filter | zuerst finden und vergleichen, dann eine Zeile ändern; ab 51 Zeilen; Rechnungen, Angebote, Buchungen | die Änderung ist die Hauptaufgabe und geschieht 40-mal am Tag (dann in der Zeile oder Erfassungszeile) | – |
| Erfassungszeile | eine Zeile mit Feldern oben oder unten an der Liste; nach dem Speichern Fokus zurück ins erste Feld, der neue Eintrag erscheint direkt darunter | Serienerfassung, kurze Datensätze (3 bis 5 Pflichtfelder), Tastaturrollen | mehr als etwa 7 Felder oder abhängige Felder | Pflichtfelder + 1 (Speichern), meist die billigste Struktur |
| Bearbeiten in der Zeile | eine Zelle wird mit Enter oder Doppelklick zum Feld, Tab zur nächsten, Escape verwirft, Speichern beim Verlassen mit Rückgängig | häufige kleine Korrekturen einzelner Werte | Werte, die gegen andere Felder geprüft werden; Touch mit kleinen Zeilen | – |
| Sammelleiste | Kästchen je Zeile, Umschalt wählt Bereich, nach der ersten Auswahl „alle Treffer wählen“, eine Leiste mit Anzahl und zwei, drei Sammelaktionen ersetzt den Tabellenkopf oder dockt unten an | dieselbe Aktion auf drei oder mehr Einträgen hintereinander | Aktionen, die je Eintrag eine Entscheidung brauchen; zerstörende Sammelaktionen bestätigen mit Name und Anzahl | – |
| Gespeicherte Ansichten | Filter, Sortierung und Spalten unter einem Namen als Reiter oder Liste über der Tabelle, in der Adresse (verlinkbar) | dieselben zwei, drei Fragen täglich („offen, meine, heute fällig“) | unter etwa 50 Einträgen, wo ein Sofortfilter schneller ist | – |
| Befehlspalette | eine Taste öffnet ein Suchfeld über der Oberfläche; Treffer mischen Ziele, Objekte und Aktionen, Jüngstes zuerst, jeder Eintrag zeigt sein Kürzel | Werkzeuge mit vielen Aktionen oder Objekten, Tastaturrollen, Experten | als einziger Weg zu einer Aktion: Gelegenheitsnutzer finden sie nie, sie ergänzt sichtbare Bedienelemente | – |
| Tafel (Spalten nach Status) | eine Spalte je Status, Karten mit drei bis vier Feldern, Ziehen ändert den Status, eine Tastaturalternative verschiebt die Karte | 5 bis 7 Status, unter etwa 30 Einträgen je Spalte, Statuswechsel ist die Kernaufgabe | mehr Einträge (Scrollen in zwei Richtungen); Entscheidung nach einem Feld, das die Karte nicht zeigt | – |
| Schrittfolge (Assistent) | eine Entscheidung je Schritt, Fortschritt sichtbar, Zurück behält die Eingabe, Zusammenfassung vor dem unumkehrbaren Schritt | seltene Aufgaben (seltener als wöchentlich) mit abhängigen Entscheidungen, Ersteinrichtung | tägliche Aufgaben: ein Assistent verdoppelt die Schritte von allem, was fünfmal am Tag geschieht | – |
| Freie Datumseingabe | Textfeld für „morgen 9“, „+3“, „Mo“ oder ein Datum, daneben die Vorschau in Worten („fällig Di 10. Nov.“); der Kalender bleibt als zweiter Weg | Wiedervorlagen und Fälligkeiten, die oft am Tag gesetzt werden, Tastaturrollen | Zeiträume und Wiederholungen (dann ein richtiger Wähler) | eine Feldeingabe statt Kalender öffnen und klicken |

**Übliche Tasten** (Abweichung kostet einen falschen Handgriff; Einzeltasten wirken nie in Eingabefeldern, SA03): `/` Suche oder Filter, `N` oder `C` neu, `E` bearbeiten, Enter öffnet oder speichert im einzeiligen Formular, Escape schließt Blatt oder Dialog und verwirft eine Zelle, Pfeil auf und ab (J, K) bewegt die Auswahl, `X` oder Leertaste wählt die Zeile, Strg/Cmd+Enter speichert und schließt (in der Serienerfassung speichert und weiter), Strg/Cmd+K Befehlspalette, Strg/Cmd+Z rückgängig, `?` Liste der Kürzel.

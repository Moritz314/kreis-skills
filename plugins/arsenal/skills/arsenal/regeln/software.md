# Modul Software

Laden für die Art `anwendung` (<internal-project>, plasmind, Verwaltungen, Werkzeuge, Einstellungen). Wer eine Anwendung öffnet, will eine Aufgabe erledigen. Bewegung: Stamm S42 bis S51; „Wann nicht animieren“ (S50) gilt hier besonders. Texte für Fehler und Leere: TX08. Code: `rezepte/oberflaeche.md`.

## Haltung

- **SW01 Vertraut vor eigen.** Wer Werkzeuge dieser Art kennt, findet sich sofort zurecht. Die Marke gibt nur Schrift, Farbe, Dichte und eine Signatur in einer Zustandsbewegung (Laden, Bestätigen); Aufbau, Navigation und Bedienelemente bleiben die vertrauten der Gattung. Gestaltet werden darf die Oberfläche (Scrollbalken, Auswahl, Fokus), nicht das Verhalten. Prüffrage: Kann jemand die Aufgabe lösen, ohne bei einem Bedienteil zu stocken?
- **SW02 Häufige Wege sofort.** Die Anwendung startet in die Aufgabe, ohne Ladefolge und ohne Intro. Bewegung zeigt Zustand (seltene Wechsel, Rückmeldung, Laden, Aufdecken), nichts sonst; häufige Wechsel geschehen sofort (S50).

## Zustand und Ausweg

- **SW03 Zustand immer sichtbar:** Laden, Arbeiten, Erfolg, Fehler. Rückmeldung binnen 100 ms (S49). Richtwerte: unter etwa 1 s kein Ladezeichen; ab etwa 2 s bis 10 s ein Skelett in der Form des kommenden Inhalts; über 10 s ein Fortschritt mit Zahl; dazwischen nach Ermessen.
- **SW04 Jeder Schritt hat einen Ausweg.** Zerstörende Aktionen lassen sich rückgängig machen oder abbrechen; keine Sackgassen.
- **SW05 Jedes Bedienteil hat alle Zustände:** Standard, Hover, Fokus, aktiv, gesperrt, lädt, Fehler. Ein Vokabular über alle Ansichten: Sieht „Speichern“ an zwei Stellen verschieden aus, ist eine falsch.
- **SW06 Erst inline, dann Dialog.** Ein Dialog ist nicht die erste Wahl. Overlays entkommen ihrem Container (`<dialog>`, Popover-API, `position: fixed`), sonst schneidet `overflow` sie ab.

## Ordnung

- **SW07 Navigation nach Zahl und Häufigkeit der Bereiche:** Seitenleiste bei vielen, oft gewechselten Bereichen (am Desktop sichtbar, nicht hinter einem Menüknopf); Kopfleiste bei wenigen, selten gewechselten; Befehlspalette bei vielen Aktionen. Die aktuelle Position ist immer markiert. Höchstens zwei Ebenen; Tieferes bekommt eine eigene Übersicht.
- **SW08 Schrittweise zeigen.** Zuerst nur das Nötige; Seltenes eine Ebene tiefer (Zahl der Ebenen: SW07). Vorgaben sind Entscheidungen: Sie dienen dem Nutzer, sind als Vorgabe erkennbar, und Ändern ist so leicht wie Behalten.
- **SW09 Nichtlinear arbeiten.** Kein erzwungener Assistent, wo die Sache keinen braucht; keine Pflicht-Einführung vor der ersten Nutzung. Geführte Hilfe nur für wirklich neue Bedienmuster.
- **SW10 Dichte nach Nutzung** (Regler `dichte`). Täglich bediente Werkzeuge sind bewusst kompakt; Labels und Tabellenköpfe treten zurück (kleiner, leichter), damit die Daten führen. Viel Inhalt bleibt beherrschbar durch Überblick zuerst, dann Filter, dann Details auf Abruf.

## Ansichten

- **SW11 Übersicht (Dashboard).** Richtwert: passt auf eine Bildschirmhöhe; was nicht passt, ist ein Bericht. Jede Kennzahl trägt einen Vergleich (Vorperiode, Ziel oder Verlauf). Die wichtigste Zahl steht zuerst und am größten, Schmuck ordnet sich unter. Gebaut für eine Rolle und ihre Entscheidungen. Diagramme nach Ermessen; Prüffrage: Lässt sich der Vergleich auf einen Blick ablesen? Balken und Linien lesen sich am schnellsten.
- **SW12 Tabellen** dienen vier Aufgaben: finden, vergleichen, einen Eintrag ansehen oder bearbeiten, mehrere zugleich bearbeiten. Die Spaltenfolge folgt diesen Aufgaben, nicht der Datenbank. Kopf (und wo nötig erste Spalte) bleibt beim Scrollen stehen; bei viel Inhalt eine kompakte und eine bequeme Dichte; Tabellenziffern.
- **SW13 Datensatz und Detail.** Der nächste Schritt steht in der ersten Ansicht, der Kopf des Datensatzes bleibt beim Scrollen stehen. Prüffrage: Sieht man jederzeit, welcher Datensatz offen ist? Die Arten von Einträgen (Notiz, Anruf, Status, Dokument) sind zugleich die Filter des Verlaufs. Ein Detail öffnet als Seitenblatt aus der Liste, nicht als neue Seite, außer es ist selbst das Ziel (Direktlink).
- **SW14 Formulare und Einstellungen.** Felder nach S52. Einstellungen wirken sofort, ohne Speichern-Knopf; ein Schalter nennt den Zustand („Benachrichtigungen erhalten“).

## Gestalt

- **SW15 Schrift.** Eine gut eingestellte Familie trägt oft alles. Feste `rem`-Skala, nicht fließend; Verhältnis 1,125 bis 1,2. Labels, Knöpfe und Daten in der Textschrift. Prüffrage: Liest man jedes Label in kleiner Größe auf einen Blick?
- **SW16 Farbe** startet bei `farbe: zurueckhaltend`. Der Akzent steht nur für Hauptaktion, Auswahl und Zustand. Eine zweite neutrale Ebene trennt Leisten und Seitenfelder vom Inhalt. Zustandsfarben (Rot, Bernstein) nur, wo sie Bedeutung tragen; inaktive Teile gedämpft. Prüffrage: Unterscheidet man aktiv und inaktiv auf einen Blick, auch ohne Farbe?

## Tastatur

- **SW17 Tastatur zuerst.** Alles ist mit Tab erreichbar und bedienbar (S12). In tastaturlastigen Werkzeugen hat jede Aktion ein Kürzel, sichtbar dokumentiert (Hinweis oder Befehlsliste), ohne Kollision mit System und Hilfstechnik, mit Gegenstück auf Mac und Windows. Experten bekommen Abkürzungen, Anfänger müssen sie nicht kennen.

## Probe (für `audit` und `kritik`, Kritiker R prüft Bedienung)

Jeder Kernablauf ohne Maus (Tab, Enter, Escape); jede Ansicht leer, mit Fehler und mit vielen Daten; Graustufenprobe (S15) auch in die Gegenrichtung: Markiert eine Farbe den Normalfall in fast allen Zeilen, ist die Zuordnung verkehrt; Kontrast und Fokus in der kompakten Dichte; Kürzel gegen System-Kürzel.

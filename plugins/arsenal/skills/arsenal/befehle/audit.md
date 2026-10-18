# audit (Schritt 7)

Misst die gebaute Fassung und liefert alle Bilder für `kritik`. Verfehltes steht als Befund, nicht als Halt.

**Aufruf:** `audit [laufordner] [lp-n]`
**Wer:** Messung, Sonnet. Werkzeugpfade in `SKILL.md`. Jede Probe mit `?thema=hell` und `?thema=dunkel`, Chromium mit festem Pfad.

## Messrezept

1. **Fotos** hell und dunkel bei 1440 und 390, oben und ganzseitig (`deviceScaleFactor` 2): `lp-n/bilder/f<k>-1440.png`, `f<k>-390.png`.
2. **Film** 12 bis 15 s über den Scrollweg (`f<k>.mp4`), Standbilder alle 1,5 s und je Pin-Viertel; 2-fach-Ausschnitte großer Flächen und großer Schrift.
3. **Inhalt ohne Skript:** Probe S19 (bei `anwendung` ohne den Teil „ohne Skript“, siehe Kopf des Stamms).
4. **Reduzierte Bewegung:** Fotos und Probe S17.
5. **Budget** nach `regler.md`: Lighthouse mobil und Desktop als Median aus drei Läufen ohne Cache, einmal mit Cache; Netzsumme der ersten Ansicht; Long Tasks bei 4-facher CPU-Drosselung gegen Leerlauf (TE12).
6. **Barrierefreiheit:** axe vollständig (mit `region` und `landmark-*`), Zahl der Knoten; Tastaturdurchlauf; Kontrast im hellsten und dunkelsten Bild einer Bewegung (S14); Tippziele (S16); Textabstand (S12).
7. **Auflösungstabelle** je Datei, Quelle gegen Anzeigemaß (S34).
8. **Bewegung:** Kreuzungsprobe über den ganzen Scrollweg bei 1440 und 390 (BE16); Nahtprobe an Pin-Rändern (BE14); Walzenprobe bei Wortwechsel und Anzeigen (BE19 bis BE21).
9. **Erstklick** (Website-Arten): fünf Aufgaben aus `befund.md`, mindestens 4 von 5 richtig (KO07).
10. **Muster:** `DO_NOT_TRACK=1 IMPECCABLE_NO_TELEMETRY=1 npx impeccable detect --json <ordner>` mit dem gebauten HTML; eine fremde Adresse erst lokal sichern, sonst „nicht gemessen“. Exit 0 frei, 2 Befunde; jeder andere Wert ist ein Fehler des Werkzeugs (ungeprüft). Befunde sind Prüffragen (S04), kein Urteil.
11. **Recht und Technik:** Impressum und Datenschutz (S07), Einwilligung (S08), Netzprotokoll mit 0 Anfragen an fremde Ursprünge außer freigegebenen (S09), Kopfzeilen und CSP (S10, TE07), `scrollWidth` gleich Fensterbreite bei 320 und 390 (S37), `content-encoding` je JS- und CSS-Datei (S40), Konsole ohne Fehler, kein Status ungleich 200.
12. **Register** (Website-Arten): Schriftpaar und helle Grundfarbe aus dem gebauten CSS gegen den Eintrag im Demo-Register (PR15).
13. Anwendung zusätzlich: Probe aus Modul `software`.

## Ergebnis

`L/lp-n/AUDIT.md`: je Prüfung Wert, Grenze, Bilddatei und „ok“, „Mangel“ oder „nicht gemessen“ mit Grund. Letzte Zeile `AUDIT FREI` oder `AUDIT <n> MÄNGEL`. Dazu `L/lp-n/bilder/`.

**„Behoben“** gilt erst mit einem Standbild genau aus dem Zeitfenster des Fehlers.

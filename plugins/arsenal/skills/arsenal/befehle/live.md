# live (Livemodus, Stufe 1)

Der Inhaber öffnet eine Website oder ein Mockup im Browser, klickt ein Element an, sagt einen Satz; du änderst den Quelltext, die Seite lädt den Teil neu. Werkzeug: `<dein-ordner>` (nur Standardbibliothek). Kein Bezug zu Lightmind.

## Starten
1. `python3 <dein-ordner> starten --ordner <Ordner der Seite> &` (Hintergrund; Port 4410 bis 4419, `--seite` setzt die Einstiegsseite).
2. Die Adressen aus der Startzeile dem Inhaber nennen. Sie binden nur an Loopback und Tailnet: `http://testbed.tailef412c.ts.net:<port>/` (vom Laptop im Tailnet) oder `http://127.0.0.1:<port>/` (auf testbed, Server-Browser). Nie 0.0.0.0, nie ein öffentlicher Zugang, nie Proxy oder Firewall ändern.
3. Inhaber: Taste L oder Knopf „Live“ unten rechts, Element anklicken, Satz tippen, „Ändern“ oder „3 Varianten“.

## Schleife
1. `livemodus.py warten --sekunden 600` gibt die nächste Anfrage als Text (Wunsch, Selektor, Textausschnitt, HTML, Datei und Zeile als ungeprüfter Hinweis). Exit 3 heißt: nichts gekommen, erneut warten oder anhalten.
2. Art `aendern`: Quelltext ändern (Datei aus dem Hinweis, sonst suchen), dann `livemodus.py fertig <id> --hinweis "was"`. Die Seite lädt Element, Stylesheets und Inline-Styles neu.
3. Art `varianten`: drei HTML-Schnipsel schreiben (je ein Element, ersetzt das gewählte; CSS im Schnipsel mit eigenem Klassenpräfix, nichts Globales), dann `livemodus.py varianten <id> v1.html v2.html v3.html`. Der Inhaber schaltet im Browser um und übernimmt oder verwirft. Übernahme setzt der Server selbst ein, wenn das Original genau einmal in der Datei steht; sonst kommt eine Anfrage „UEBERNAHME“, dann Schnipsel in den Quelltext schreiben und `fertig`. Unterschiedliche Varianten, nicht dreimal dasselbe.
4. Zurück zu 1, bis der Inhaber aufhört. Am Ende `livemodus.py stoppen`.

## Regeln
- Nur das gewählte Element und was es braucht ändern (sein CSS, seine Kinder). Nichts umbauen, nichts „nebenbei“ verbessern.
- Arsenal-Regeln gelten wie beim Bau: Marke, `design/pflichtliste.md` (D1 bis D18), Prüfung vor „fertig“ nur an der geänderten Stelle.
- Räumliche Konsistenz (D7): Die Änderung verschiebt nichts anderes; Größen und Orte der Nachbarn bleiben. Bricht ein Wunsch das, vorher in einem Satz sagen und den Inhaber fragen.
- Werte aus den vorhandenen Variablen der Seite nehmen, keine neuen Zahlen am Rand.
- Änderungen an der Quelle sind echt (kein Entwurfsordner): bei fremden Seiten vorher eine Kopie anlegen oder Git nutzen. `anwenden` legt eine Sicherung im Zustandsordner an.
- Stufe 1 kann nicht: Bildausschnitt, Regler, mehrere Anmerkungen, Handy-Rahmen, Rückgängig über mehrere Schritte, Proxy für Web-Apps. Fehlt das, sagen, nicht vortäuschen.

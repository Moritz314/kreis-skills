# Aus Reels gelernt: Nachtrag

Vier Einträge aus dem Ordner der Lightmind-Fassung (`reference/aus-reels.md`, Stand 2026-10-26), die in `planung/aus-reels.md` fehlen. Wissen auf Abruf, keine Regeln; Technik und Wirkung sind aus Reel und Kommentaren abgeleitet und nicht geprüft. Jeder Eintrag trägt das Ja von <dein-name> vom 2026-10-26.

### Scroll-Storytelling Hautpflege (Ascenta Studio)
- Muster: Die Website erzählt Problem und Lösung per Scroll: Produktszene, Tropfen-Zoom, Haut-Nahaufnahme („Dark spots“), dann „Spots fade“, zuletzt heller Produktbereich.
- Der Farbton wechselt von sattem Orange zu Hautrosa zu hellem Weiß. Die Wechsel tragen die Handlung.
- Reel-Format: Monitor und Handy laufen parallel, ein Preis-Overlay („2500$ website“) als Aufhänger.
- Technik nicht genannt; vermutlich scrollgesteuerte Bild- oder Videosequenz (Annahme).
- Quelle: https://www.instagram.com/reel/Deu0zarxG9w/ (Ascenta Studio)

### ascii-reveal (React): ASCII-Dekodier-Ladeeffekt
- Open-Source-Komponente von Quan Hoang, Demo quanhoangindex.github.io, `npm i ascii-reveal`, v0.1.
- Idee: Statt Skeleton-Loader wird der echte Inhalt Zeichen für Zeichen aus Glyphen-Rauschen „dekodiert“.
- Nutzung laut Demo: `<AsciiReveal preset="decode">` um beliebige Karten oder Galerien.
- Presets: Decode (Pixelblöcke, Strichcode, Zahlen), Dither (Punktraster), Terminal (Monospace, blaue Blöcke), Blueprint (nur in der Auswahl gezeigt).
- Steuerung: Welle von Mitte, Ecke oder Cursor, Geschwindigkeitsregler, Klick auf eine Karte spielt von dieser Stelle neu ab, „Redeploy“ spielt Laden und Geladen für die ganze Seite ab.
- Elemente: Bilder, Text, Diagramme und Knöpfe lösen sich einzeln auf; Eckklammern rahmen die Karte während des Ladens.
- Einordnung: Die Wirkung lebt von der Verzögerung; S19 (Inhalt ohne Skript, nie unsichtbar starten) und S49 (Rückmeldung binnen 100 ms) gelten zuerst.
- Quelle: https://www.instagram.com/reel/DewgLOVI_uL/ (Quan Hoang)

### 3D-Portfolio-Galerie (Three.js): Band, Raster, Kugel
- Projekt-Bildschirmfotos als Texturflächen in Three.js, die zwischen drei Anordnungen wechseln: gebogenes Band, flaches Raster, rotierende Kugel.
- Kontrast: heller Startbildschirm mit großer Typografie, dann Glitch-Übergang auf eine dunkle Kugel-Seite.
- Zeigt das Portfolio selbst als Interaktion statt als statisches Raster. Gesehen bei einem Portfolio mit 24-Stunden-Website-Angebot, Adresse nicht lesbar.
- Quelle: https://www.instagram.com/reel/DeuBoWaJvbr/ (Sean, Web3 UX Designer)

### CSS-3D-Karussell-Hero mit Loader (Avi)
- Variante 1: Karten fliegen von unten, drehen sich zum Fächer, heben sich zum Rad aus Wolken. Variante 2: Karten werden in einen kleinen schrägen Ring gegeben, die Kamera fährt hinein, der Ring öffnet sich zum 3D-Karussell.
- Gebaut mit reinem CSS 3D und React, ohne Three.js und WebGL. Loader mit Prozentzähler (0 bis 100 %) und Logo, danach Übergang in den Hero. Hintergrund: Wolkenhimmel bei Sonnenuntergang, Hero-Text darunter.
- Nachbau-Idee: Karten per `rotateY(n·Winkel) translateZ(Radius)`, Container mit `perspective`, Kamerafahrt über Radius und Z-Offset animieren.
- Quelle: https://www.instagram.com/reel/Deq3PylStBF/ (Avi, Design, Tech & AI). Code nicht öffentlich, nur gegen Kommentar.

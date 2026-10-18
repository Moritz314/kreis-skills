# Modul Selbst erzeugtes Material

Laden, sobald Material im Code oder mit Werkzeugen selbst erzeugt wird. Ausdrücklich erwünscht (<dein-name> 16.10.2026). Rezepte: `rezepte/erzeugt.md` (Film mit ffmpeg, SVG), `rezepte/shader.md`, `rezepte/3d.md`.

- **ER01 Erwünschte Mittel:** SVG-Grafik und -Animation, Motion Graphics (mit ffmpeg oder Remotion gerendert), Linienzeichnungen, Wireframes, generierte Texturen (auch KI-Texturen) in verschiedenen Ästhetiken, Canvas, WebGL-Shader, CSS-Animation, Lottie, Three.js. Prüffrage (Markentest BE02): Ist es aus dem Gegenstand des Kunden gebaut?
- **ER02 Nichts vortäuschen** (S06): Erzeugtes zeigt keine Personen, Werkstätten oder Kundenarbeiten, die echt wirken sollen. Gestaltetes Bewegtmaterial, das nichts Echtes vorgibt, braucht keinen Vermerk.
- **ER03 Auch Erzeugtes ist scharf:** gerenderte Dateien (Bild, Film, Textur) in Anzeigegröße × 2 (S34), Vektor, wo es geht. Für Echtzeit (Canvas, Shader, 3D) gilt die Pixeldichte aus dem Budget.
- **ER04 3D-Oberfläche gegen Material:** kein rechteckiges Spitzlicht, kein gleichmäßiger Kunststoffglanz; Kontaktschatten, Mikrostruktur und Licht mit Richtung. Probe: 2-fach-Ausschnitt neben einer Materialreferenz.
- **ER05 Texturen** bestehen die Naht- und Wiederholungsprobe (ME10).
- **ER06 Aufnahmen bewegter Seiten** (Projektfilme, Bildschirmfilme) entstehen mit virtueller Uhr Bild für Bild, nie in Echtzeit; die Schleifennaht wird überblendet. Werkzeug: `<dein-ordner>`.
- **ER07 Technik je Mittel:** SVG und CSS ab `technik: statisch`; Canvas und Lottie ab `inseln`; Shader und Three.js ab `webgl`. Gerenderte Filme (ffmpeg, Remotion) gehen auf jeder Stufe, denn sie sind Video.
- **ER08 Herkunft und Bibliothek:** Erzeugtes steht in `material/MEDIEN.md` mit Werkzeug und Vorlage („eigen, erzeugt“). Was gut ist und gefällt, wandert in die Galerie (Befehl `bibliothek`).

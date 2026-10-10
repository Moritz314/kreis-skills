# Aus Reels gelernt

Vom Reel-Wissensagenten (Punkt 68) eingeordnete Design-Erkenntnisse. Je Abschnitt ein Reel; Quelle steht am Ende. Bibliotheken vor Nutzung auf Lizenz und Pflege pruefen.

### Mausreaktive Framer-Komponenten (Interaktionsmuster)
- Glass Gallery Cube: drehbarer Glaswürfel mit Bildern als Galerie.
- CMS Curve Gallery: Bildraster mit gekrümmter Bewegung, an CMS gekoppelt.
- Scattered Grid Text: Text aus Gitterbuchstaben, die auf die Maus reagieren (Hero-Effekt).
- Liquid Carousel: Karussell mit flüssigem Übergang.
- 3D Globe Carousel: Bilder auf einer Kugel angeordnet.
- 3D Image Stack Scroll: gestapelte Bilder, per Scroll durchgeblättert.
- Video Gallery und Visual Carousel: Galerien mit Hover-Reaktion.
- Regel: Wenige gezielte Interaktionen steigern den polierten Eindruck einer Seite.
- Links: keine öffentlich genannt (nur per Kommentar "ASSETS").
- Quelle: https://www.instagram.com/reel/DdBi1YOo0H5 (Julia, Product Designer)

### Elastic Toggle: Mikrointeraktion fuer Switches
- Aufbau zerlegen: Knob, Fill (Track) und Laufweg (Distanz) getrennt betrachten.
- Zustandswechsel als Slide animieren, nie als harten Sprung.
- Stretch ueber die Breite des Knobs erzeugen, nicht per scaleX; so bleibt die Rundung sauber.
- Bounce mit Federphysik (Overshoot und Ausschwingen) plus leichtem Squish; dezent dosieren.
- Press-Animation beim Druecken und volle Animation erst beim Loslassen; erlaubt "Meinung aendern" waehrend des Klicks.
- Werte (Dauer, Steifigkeit, Daempfung, Stretch) als Regler exponieren und als Prompt exportieren, damit Agenten die Komponente nachbauen.
- Bibliothek zum Zeitpunkt des Reels noch nicht veroeffentlicht (Kommentar "toggle" fuer Mailingliste).
- Quelle: https://www.instagram.com/reel/DeK0AFcIRhf/ (Kabarza | Developer & Designer)

### Generative Neon-Visualisierungs-Bibliothek (Fable-Demo)
- Stil: dunkler Hintergrund, Neongrün, technische Beschriftung, Kachelraster mit je einer generativen Visualisierung.
- Motive: Hexagon-Raster, Punktefelder, Strömungslinien, Dreiecksnetz-Kugel, Blob-Formen, Radar mit rotierendem Strahl.
- Interaktiv und teils mit Ton; laut Creator per One-Shot aus einer vorbereiteten Bibliothek erzeugt.
- Ansatz: Moodboard-Daten extrahieren, per agentischem Workflow zum Design-System machen. Konkrete Schritte werden nicht gezeigt.
- Quelle: Instagram-Reel von RANDY ROBERTS, https://www.instagram.com/reel/DZcRoIEi4hB/

### sondaven.com – Scroll-Storytelling mit Motiv-Textur
- Textur aus realem Projektmerkmal ableiten (Holzlatten des Gebäudes als horizontale Linien über der ganzen Seite); Textur und Inhalt müssen zusammenpassen.
- Szenenübergang: Beim Scrollen Zoom-out; das Hintergrundbild wird zum Detail der nächsten Szene, der neue Hintergrund baut sich mit anderen Elementen neu auf.
- Animierte Masken: Objekt läuft teils hinter, teils vor Bildebenen und verschwindet hinter einem dritten Element.
- Text-Reveal: kontrastreiche Farbe füllt beim Scrollen einen kontrastarmen Text.
- Interaktive Details: Karte, Winter/Sommer-Vergleich per Ziehen.
- FAQ-Übergang mit Vögeln: in Code animiert, mit Zufallsanteil, nicht nur scrollgebunden, kein Video.
- Wichtig: Typografie, Abstände, Mikrointeraktionen und Layout einheitlich pflegen.
- Quelle: https://www.instagram.com/reel/Db4CZuahP-Q/ (Tiago Rosa); Referenz: sondaven.com

### Motion-Showreel-Stilmittel (Claude-generiert)
- Szenenfolge mit je einer Vollfarbe: Schwarz, Rot (#EE3B2E-artig), Blau, Gelb, Off-White; ein Akzent pro Szene.
- Kinetische Typo: fette Grotesk, Wort für Wort eingeblendet, Klammer-Rahmen um Schlüsselwort ("[FRAME]").
- Geometrie-Szenen: Punkt wird Kreis, Quadrat, Dreieck mit sichtbaren Transform-Handles (Editor-Look).
- Punktraster und Partikelwellen als Hintergrundbewegung; Drahtgitter für Tiefe.
- Kreisender Textring mit Disziplinbegriffen (Rhythm, Timing, Easing) um einen roten Mittelpunkt.
- Abschluss: ruhige Endkarte mit Serifen-Wortmarke und rotem Punkt.
- Quelle: Instagram Reel DeIGexJTKfe (Ononto G), https://www.instagram.com/reel/DeIGexJTKfe

### Interaktive Web-Assets: Lucide, Rive, Spline
- Lucide: Icon-Bibliothek mit über 1500 anpassbaren Icons (Strichstärke, Farbe, Größe); statt Emojis in der UI verwenden. Link: https://lucide.dev
- Rive: interaktive Vektoranimationen mit eingebauten State Machines, reagieren auf Hover und Klicks; per Code/CLI einbindbar. Link: https://rive.app
- Spline: interaktive 3D-Objekte und Szenen im Browser, reagieren auf Hover, Klick und Ziehen; direkt in die Website einbettbar. Link: https://spline.design
- Hinweis: Das Reel ist als Werbung (#ad, Manus-Partner) markiert; Manus.im (Website aus einem Prompt) ist nicht ins Arsenal übernommen.
- Quelle: Instagram-Reel DeJWc7KIUrw (Kanal Henry)
- Quelle: https://www.instagram.com/reel/DeJWc7KIUrw (Henry)

### Hairline: isometrische Linienfiguren (cursorreaktiv)
- Bibliothek mit 27 animierten isometrischen Linienzeichnungen (Caption nennt 19), die dem Mauszeiger folgen.
- Zero Dependencies, ca. 40-50 kB, nutzbar in React, Vanilla HTML oder per CDN; MIT-Lizenz, auch kommerziell nutzbar.
- Einsatz: Hero, Bento-Grid-Kacheln, Pricing-Karte; weisse Linien auf dunklem Grund, monochrom.
- Skill /hairline-create: Claude Code, Cursor oder Codex zeichnen neue Figuren aus einem Satz im selben Stil.
- Paket: npm @lucasmarkes/hairline (Name laut Bild, lesbar nur teilweise; vor Nutzung pruefen); Link und Skill nur per Kommentar-DM, daher selbst suchen.
- Quelle: Instagram-Reel speedy_devv, https://www.instagram.com/reel/DeIQfJsz2vc

### Vier schnelle Layout-Korrekturen
- Ungeordnet: Raster verwenden, um Elemente auszurichten und zu strukturieren.
- Farben harmonieren nicht: auf eine Farbe als Hauptfarbe fokussieren.
- Layout klemmt: Elementen mehr Raum zum Atmen (Weißraum) geben.
- Fokus fehlt: einen klaren Fokuspunkt bewusst setzen.
- Quelle: Instagram-Reel von Daryl Kastenholz, https://www.instagram.com/reel/DePTR2jtWDh/

### Scrollgesteuerte Storytelling-Landingpage (Referenz "Corn. Revolutionized.")
- Aufbau: Folge von Vollbild-Szenen, je eine große, kurze Headline; Scroll treibt Übergänge (Partikel, 3D, Parallax).
- Motivwechsel pro Inhaltsstation: DNA-Helix, Sternbild-Netz, Pflanztopf mit Wurzeln, Feld, Parzellenraster, Einzelkorn.
- Farbe: dunkles Grün als Grundton, warme Akzente (Orange/Gelb) für Highlights und Schlussszene.
- Rahmen: Hero-Headline am Anfang, am Ende erneut aufgegriffen; schlichter Link-Footer.
- Hinweis: Bibliothek/Technik im Reel nicht genannt (Workflow nur gegen Kommentar "HOW").
- Quelle: https://www.instagram.com/reel/DeQ5h06RyNA/ (Jerry Rogers)

### Shop-UX: Grid, Filter, Warenkorb-Overlay (Beispiel Khy)
- Raster: 12-Spalten-Grid plus Schreibmaschinen-/Monospace-Schrift wirkt redaktionell und geordnet.
- Ladezeit: Logo-Animationen von rund 6 Sekunden vermeiden; sie kosten Aufmerksamkeit.
- Shop-Grid: Bei kleinen Drop-Katalogen auf Abwechslung achten, sonst wirkt alles gleich.
- Produktbilder: Fotos am Model statt nur Freisteller (Behauptung im Reel: 20–30 % mehr Umsatz, unbelegt).
- Filter: Beschleunigen die Suche laut Reel, bei unter 25 Produkten aber eher überflüssig.
- Warenkorb: Zusatzangebote (z. B. Rückgabeschutz) nicht automatisch über den Haupt-Button hinzufügen; Opt-out-Button klar gestalten und deutlich erkennbar machen (Dark-Pattern- und Rechtsrisiko).
- Quelle: Instagram-Reel von Blaze Smith, https://www.instagram.com/reel/DeMVrhGPF0G/

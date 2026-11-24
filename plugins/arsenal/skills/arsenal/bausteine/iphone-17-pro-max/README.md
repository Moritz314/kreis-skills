# Attrappe iPhone 17 Pro Max

Maßstabsgetreue Attrappe zum Testen mobiler Websites und PWAs, hoch und quer. Pflicht vor jeder Abgabe (siehe `skills/arsenal/SKILL.md`, `skills/handy-oberflaeche/SKILL.md`).

## Aufruf
- Bild: `uv run --script attrappe.py shot <url> <out.png> [--quer] [--nur-display]`. Auf **testbed** ausführen (Standard testbed seit 2026-11-09, Anweisung des Inhabers: alles, was auf dem alten Rechner gemacht wurde, wird auf testbed gemacht; Überschreibung: anderer Host in den Befehlen). Chromium stürzte dort früher mit SIGTRAP ab, Ursache war das weiche Speicherlimit der Agenten-Shell: vorher `ulimit -v unlimited` setzen. Von einem anderen Rechner: `rsync -a . testbed:attrappe-test/ && ssh testbed 'bash -lc "ulimit -v unlimited; cd ~/attrappe-test; uv run --script attrappe.py shot URL hoch.png"'`, Bild per `scp` zurückholen. Ergebnis 1413×2958 px (hoch) bzw. 2958×1413 (quer), Faktor 3.
- WebKit statt Chromium: Playwright-WebKit auf testbed ist iOS-näher als Chromium, bleibt aber **Emulation, nicht iOS-verifiziert**. Der Shot ersetzt `env(safe-area-inset-*)` durch die `--sat/--sar/--sab/--sal`-Variablen, weil WebKit unter Linux die env()-Namen kennt und 0 liefert. (Das frühere Testlabor-Werkzeug aus Lightmind gibt es hier nicht; die Rahmen dieses Bausteins genügen.)
- Live: `attrappe.html?url=<Seite>[&quer][&z=0.8]` (iframe 440×956 bzw. 956×440, Island liegt darüber). Standard `https://kreis.systems`.
- Rahmen neu erzeugen und Proportionen prüfen: `python3 bauen.py` (Abweichung muss < 0,5 % sein; Stand: 0,004 %).
- Sicherheitszonen: Chromium kennt `env(safe-area-inset-*)` nicht. Das Skript setzt `--sat/--sar/--sab/--sal` (hoch 62/0/34/0, quer 20/62/20/62). Seiten schreiben `env(safe-area-inset-top, var(--sat, 0px))`.

## Maße (alles in pt = CSS-px, 3 px je pt, oder mm)
| Größe | Wert | Quelle |
|---|---|---|
| Gehäuse | 163,4 × 78,0 × 8,75 mm | Apple Support, iPhone 17 Pro Max Technische Daten: https://support.apple.com/en-us/125091 |
| Display | 6,9", 1320 × 2868 px, 460 ppi | Apple Tech Specs (gleiche Seite); useyourloaf https://useyourloaf.com/blog/iphone-17-screen-sizes/ |
| Display in pt | 440 × 956, Faktor 3 | useyourloaf (Simulator-Werte) |
| Display in mm | 72,89 × 158,36 | abgeleitet: px / 460 × 25,4 |
| 1 pt | 0,1657 mm | abgeleitet |
| Rand Gehäuse–Display | 2,56 mm | abgeleitet: (78 − 72,89) / 2 |
| Display-Eckenradius | 62 pt = 10,27 mm | kylebshr/ScreenCorners (Tabelle: iPhone 16 Pro … 17 Pro Max = 62,0); Apple veröffentlicht den Wert nicht |
| Gehäuse-Eckenradius | 12,83 mm | abgeleitet: Display-Radius + Rand (Apple veröffentlicht den Wert nicht) |
| Dynamic Island | 125 × 37 pt, 11 pt vom oberen Displayrand, Radius 18,5 pt (Kapsel) | Gemeinschaftswerte (Figma-Bezel-Kits von developer.apple.com/design/resources); für 17 Pro Max nicht bei Apple veröffentlicht; Annahme: gleich wie 16 Pro Max |
| Statusleiste | 54 pt | useyourloaf |
| Safe Area hoch | oben 62, unten 34, links/rechts 0 | useyourloaf, HIG Layout: https://developer.apple.com/design/human-interface-guidelines/layout |
| Safe Area quer | oben 20, unten 20, links/rechts 62 | useyourloaf (neu seit iOS 26: oben 20) |

Für die Pflichtprüfung gilt diese Attrappe (Ecke 62 nach ScreenCorners, quer 62/20/20/62 nach useyourloaf, beide mit Quelle).

## Dateien
`frame-hoch.svg`, `frame-quer.svg` (1 Einheit = 0,01 mm, Display ausgestanzt, Island oben drauf), `attrappe.html`, `attrappe.py`, `bauen.py`.

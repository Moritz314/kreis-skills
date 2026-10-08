# Bildquellen

Stand 2026-10-03. Alle Bilder der Elementeschau sind selbst erzeugt. Es wurden keine Fotos und keine Bilder von Dritten verwendet, kein Pixabay-Abruf, keine Zugangsdaten. Es gelten keine fremden Lizenzen.

Ablage: dieser Ordner. Je Bild vier Dateien: `-dark` und `-light` als SVG und als PNG. Die PNG sind gegenueber dem Original (2560 px) auf 1600 px Breite verkleinert (B7: 1600 x 400, alle anderen 1600 x 900); die SVG sind unveraendert.
Die Dateinamen tragen die Themen englisch: `B1-dark.svg`, `B1-light.svg`, `B1-dark.png`, `B1-light.png`.

Verfahren für alle: SVG von Hand als Text erzeugt (Skript mit festen Zufallswerten, Blobkurven als geschlossene Catmull-Rom-Kurven, Farben aus dem Tokenblock der Bausteine in beiden Themen). PNG: die SVG-Datei in Chromium über Playwright geöffnet und bei 2560 Pixel Breite als Bildschirmfoto gespeichert.

| Kennung | Datei | Herkunft | Verfahren |
|---|---|---|---|
| B1 | `B1-dark/light.svg/.png` | selbst erzeugt | Feld aus 14 Zellkonturen; Logo W12 (gestapelt) unverändert aus dem plasmind-Logo W12 (gestapelt, dunkel bzw. hell) eingebettet |
| B2 | `B2-*` | selbst erzeugt | 34 Zellen mit Augen, Fäden zu den zwei nächsten Nachbarn als Kurven, Signalpunkte auf den Fäden |
| B3 | `B3-*` | selbst erzeugt | Wachstumsringe: drei Mittelpunkte mit je 22 ineinanderliegenden Zellkonturen, nach außen schwächer |
| B4 | `B4-*` | selbst erzeugt | Wabenraster aus kleinen Zellen, für Fußzeilen und Flächen |
| B5 | `B5-*` | selbst erzeugt | Glänzender Blob mit Augen, Verläufe (Radial) für Licht, Randlicht, Glanzlicht und Schatten, kein 3D-Programm |
| B6 | `B6-*` | selbst erzeugt | Umkehrfläche: dieselbe Szene zweimal, die zweite mit vertauschten Farben, beschnitten mit drei Blobformen |
| B7 | `B7-*` | selbst erzeugt | Teilungsstreifen: fünf Phasen einer Zelle, die sich über einen schmaler werdenden Hals teilt |
| B8 | `B8-*` | selbst erzeugt | Verschmelzende Zellen mit SVG-Filter (Weichzeichnen und Schwellwert), zweite Lage für die Innenkontur |

Das Logo in B1 ist die Marke selbst (W12), keine Neuzeichnung.
Die Skripte zum Erzeugen liegen nicht in diesem Ordner; Aenderungen werden am SVG direkt gemacht und die PNG neu gerendert.

## Lizenz

Eigenes Werk von <studio>, frei zur eigenen Verwendung. Herkunft: plasmind Elementeschau 2026-10-03. Keine Bilder Dritter, keine Zugangsdaten.

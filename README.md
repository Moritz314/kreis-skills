# kreis-skills

Design- und Frontend-Skills für Claude, als Claude-Code-Marktplatz und als ZIP für claude.ai.

| Skill | Was es tut | Lizenz |
|---|---|---|
| `arsenal` | Technische Bausteine für anspruchsvolle Oberflächen: Shader, 3D, Scroll-Choreografie, kuratierte freie Bibliotheken, fertige animierte Komponenten (`bausteine/`), Befehle `plan`, `build`, `critics` u. a. | MIT (eigenes Werk) |
| `impeccable` | Design-Skill für Frontends: gestalten, kritisieren, prüfen, polieren, animieren, härten. Von Paul Bakaus. | Apache-2.0 |
| `web-design-guidelines` | Prüft UI-Code gegen die Web Interface Guidelines. Von Vercel. | MIT |

## Installation in Claude Code

```
/plugin marketplace add Moritz314/kreis-skills
/plugin install arsenal@kreis-skills
/plugin install impeccable@kreis-skills
/plugin install web-design-guidelines@kreis-skills
```

## Installation in claude.ai

1. Die ZIP aus `dist/` herunterladen (`arsenal.zip`, `impeccable.zip`, `web-design-guidelines.zip`).
2. Einstellungen › Fähigkeiten (Skills) › Skill hochladen und die ZIP wählen.
3. Skill einschalten.

Hinweis: Skripte, Dateizugriff und Workflows (z. B. `arsenal build`) brauchen Claude Code. In claude.ai wirken vor allem die Referenzen und Regeln.

## Beispiel

> Nutze arsenal und impeccable und bau mir eine Landingpage für eine Fahrradwerkstatt.

## Lizenzen

- Eigenes Werk (`arsenal`, inklusive `bausteine/` und deren Bilder): MIT, siehe `LICENSE`.
- `impeccable`: Apache-2.0, Quelle https://github.com/pbakaus/impeccable, mit `LICENSE` und `NOTICE.md` im Skill-Ordner. Enthält die Bibliothek modern-screenshot (MIT).
- `web-design-guidelines`: MIT, Quelle Vercel (https://github.com/vercel-labs/agent-skills), Hinweis in `NOTICE.md`.
- Die in `arsenal/reference/components.md` genannten UI-Bibliotheken werden **nicht mitgeliefert**, sondern nur beschrieben und verlinkt. Ihre Lizenzen (teils MIT, teils AGPL oder unklar) sind dort je Eintrag vermerkt und vor der Nutzung selbst zu prüfen.
- Die Schrift Martian Mono ist nicht eingebettet (OFL); bei Bedarf selbst einbinden.

## Pflege

`sync.sh` kopiert die Skills aus dem privaten Quellordner, bereinigt sie, bricht bei verbliebenen sensiblen Resten ab und baut `plugins/`, `dist/` und `.claude-plugin/marketplace.json` neu. Nicht von Hand in `plugins/` oder `dist/` ändern.

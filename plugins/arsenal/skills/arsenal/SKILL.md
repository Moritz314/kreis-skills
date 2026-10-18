---
name: arsenal
description: Der Webdesign-Skill von <studio>, für Websites, Onepages, Landingpages und Web-Anwendungen von der Planung bis zur Politur. Ein Regelwerk aus Stamm, Modulen, zehn Reglern, drei Stufen und Branchen; dazu Befehle für Plan, Material, Entwurf, Bau, Bewegung, Audit, Kritik, Politur, Bibliothek, Lernen und Vorlieben, Code-Rezepte (Shader, 3D, Scroll, Astro) und Bausteine. Nutzen bei jeder Gestaltung, jedem Bau und jeder Prüfung einer Weboberfläche, auch für Mockups, Demos und einzelne Fragen zu Gestaltung, Bewegung oder Technik. Ersetzt impeccable und web-design-guidelines.
version: 3.0.0
user-invocable: true
argument-hint: "plan|material|entwurf|bauen|bewegung|audit|kritik|politur|bibliothek|lernen|vorlieben [argumente]"
---

# Arsenal

Ein Regelwerk für alles Webdesign bei <studio>: Websites, Mockups, Demos und Anwendungen. Ohne Befehl und ohne Frage zeigt Arsenal die Befehlstabelle.

## Ablauf (neun Schritte)

```
1 Start ─ 2 Befund ─ 3 SOUL ─ 4 Material ─ 5 Entwurf (3 erste Ansichten) ─ Wahl ─ 6 Bau + Bewegung ─ 7 Audit ─ 8 Kritik ─ 9 Politur ─ Vorlage
                                                                                                         └── höchstens eine Nachprüfung (7 und 8) ──┘
```

Gilt für jeden Lauf (`demo`, `mockup`, `bau`). Jeder Schritt hinterlässt eine Datei im Laufordner `L/` und eine Zeile in `L/stand.log` (`Zeit | fertig | Beleg | nächster Schritt`). Liegt eine Note nach der ersten Kritik unter 6 (auf `betrieb`: ein Mangel an der Grundentscheidung), geht es zurück zu Schritt 5.

## Befehle

| Befehl | Schritt | Datei |
|---|---|---|
| `plan` (`--bestand` für bestehende Projekte) | 1 bis 3 | `befehle/plan.md` |
| `material` | 4 | `befehle/material.md` |
| `entwurf` | 5 | `befehle/entwurf.md` |
| `bauen` | 6 | `befehle/bauen.md` |
| `bewegung` | 6 | `befehle/bewegung.md` |
| `audit` | 7 | `befehle/audit.md` |
| `kritik` (`--datei` für Einzelnes und fremde Seiten) | 8 | `befehle/kritik.md` |
| `politur` | 9 | `befehle/politur.md` |
| `bibliothek` | Muster, Bausteine, Medien | `befehle/bibliothek.md` |
| `lernen` | neue Regeln | `befehle/lernen.md` |
| `vorlieben` | stehende Vorlieben | `befehle/vorlieben.md` |

Alte Namen: `build` = `bauen`, `hero` = `entwurf`, `critics` = `kritik`, `loot` = `bibliothek`, `behavior` = `vorlieben`, `register` = `plan --bestand`.

## Ladeplan (kein Agent liest alles)

| Wann | Datei |
|---|---|
| immer | diese Datei, `regeln/stamm.md`, `regler.md`, `behavior.md` (Zustandsordner), `branchen/<branche>.json` (nicht bei `anwendung`) |
| `entwurf`, `bauen` | dazu `library/galerie/_index.md` und `bausteine/_index.md` |
| Art `website`, `onepage`, `landingpage` | `regeln/praesentation.md`, `regeln/text.md`, `regeln/konversion.md` |
| Art `anwendung` | `regeln/software.md`, `regeln/text.md` |
| nach Reglern und Material | `regeln/bewegung.md`, `regeln/medien.md`, `regeln/erzeugt.md`, `regeln/technik.md` (Bedingungen in `regler.md`; Technik immer bei `bauen` und `audit`), dazu die Liste `module` der Branche |
| je Befehl | nur `befehle/<befehl>.md` |
| je gewählter Technik | `rezepte/<technik>.md` |
| Kritiker | Stamm, `regler.md` und die Module ihrer Rolle |

Ohne Befehl und ohne ARMOURY (Nachschlagen) gelten keine Tore: Antwort aus Stamm und passendem Modul.

**Rezepte** (Code, nur bei gewählter Technik): `shader.md` (WebGL-Hintergründe), `3d.md` (Three.js, React Three Fiber), `scroll.md` (Scroll-Szenen, Pins, Text), `oberflaeche.md` (Bewegung in Anwendungen), `layouts.md` (Aufbau jenseits des Kachelrasters), `astro.md` (Gerüst, Inseln, Auslieferung), `komponenten.md` (freie Bibliotheken), `erzeugt.md` (Film mit ffmpeg, SVG).

## Vorrang bei Widerspruch

1. **Pflicht** (Recht, Datenschutz, Sicherheit, Barrierefreiheit, Lizenz, feste Regeln von <dein-name>): gilt immer.
2. **Ausnahme im ARMOURY** mit Datum und Grund.
3. **Vorlieben** (`behavior.md`).
4. **Stamm**, dann **Modul**, dann **Branche**. Widerspricht ein Modul dem Stamm, ist das ein Fehler im Regelwerk: melden.
5. **Rezepte** zeigen Wege; widerspricht ein Rezept einer Regel, gilt die Regel.

Herkunft jeder Regel: `HERKUNFT.md`.

## Modelle

| Aufgabe | Modell |
|---|---|
| Leitung, Plan, SOUL, Gestaltung (Konzepte, Vorgaben und Korrekturliste in Entwurf und Politur, Prüfung), Kritiker G und B | Opus, Aufwand xhigh |
| Umsetzen von schwerer Bewegung, Shader, 3D | Opus |
| Umsetzen (Bau, erste Ansichten im Entwurf, Änderungen der Politur), Material, Audit, Kritiker K, T, M und R | Sonnet |
| kleine Änderungen | Haiku |

## Pfade

**Zustandsordner** (Vorlieben, Bibliothek mit Galerie und Mustern; nicht im Skill-Ordner):

| System | Pfad |
|---|---|
| Windows | `<dein-ordner>` |

Inhalt: `behavior.md`, `library/galerie/<slug>/` (Bausteine und Medien, Index `library/galerie/_index.md`, Arten in `library/galerie/_ordnung.json`), `library/muster/<slug>.md` (Muster, Index `library/muster/_index.md`). Mitgelieferte Vorlagen im Skill: `bausteine/_index.md`.

**Formate** für Branchen und Kacheln: `<dein-ordner>` (maschinenlesbar: `branchen/schema.json`); Kachel-Vorgaben: `<dein-ordner>`.

**Entscheidungen:** `<dein-ordner>` (E1 bis E11, K1 bis K4) und `…/arsenal-3/KONFLIKTE.md` (Fragen und Gründe zu K1 bis K4). In den Regeln meinen E1 bis E11 und „KONFLIKTE K1“ bis „K4“ diese Dateien; gleich benannte Kennungen in `bausteine/` (E, H, F, B, K) sind Bausteine.

**Projektdateien** im Laufordner: `SOUL.md` (wer und warum), `MASK.md` (wie es aussieht), `ARMOURY.md` (womit gebaut wird: Block aus `regler.md`). Getrennte Aufgaben, kein Inhalt doppelt.

**Prüfwerkzeuge** (`K` = `<dein-ordner>`):

| Werkzeug | Pfad |
|---|---|
| Auflösungstabelle | `<dein-ordner>` (`messen.mjs`, `auswerten.py`) |
| Kreuzungsprobe | `K/demo-3/selbstprobe-r2/werkzeug/kreuzung.mjs` |
| Walzenprobe | `<dein-ordner>` |
| Erstklick | `K/demo-2/messung-r3b/werkzeug/erstklick.mjs` |
| Lighthouse und axe | `<dein-ordner>` |
| Messfilm und Standbilder (`audit`, Echtzeit) | `<dein-ordner>` |
| Film mit virtueller Uhr (Projekt- und Bildschirmfilme, ER06) | `<dein-ordner>` |
| Muster | `npx impeccable detect` (Telemetrie aus, siehe `befehle/audit.md`) |

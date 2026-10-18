# Rezept: Freie Bibliotheken für Bausteine

Wo es Aufbau, Zustände und Ablauf für einen Baustein zum Nachsehen gibt, mit Lizenz, Stand und Einbau. Regeln: Lizenz S11, Gestalt aus dem MASK (PR15), Inline-Styles TE06. Ab `technik: inseln` (alles hier ist React).

## Lizenz und Stand

Jeder Eintrag ist am Datum in „Geprüft“ gelesen, nicht laufend. Ein älteres Datum heißt „galt damals“. Vor dem Einsatz die LICENSE-Datei der eingebauten Fassung lesen, nicht einen Blogbeitrag (S11). Das Ergebnis steht im ARMOURY unter Bausteine.

Nachgeprüft am 09.09.2026 gegen npm und GitHub (genutzt in `3d.md` und `shader.md`):

| Paket | Fassung | Lizenz |
|---|---|---|
| `@react-three/fiber` | `rezepte/3d.md` | MIT |
| `@react-three/drei` | `rezepte/3d.md` | MIT |
| `@shadergradient/react` | – | MIT |
| `@paper-design/shaders` | – | Apache-2.0 |
| `@splinetool/react-spline` | – | MIT |
| `@heroui/react` | – | uneinheitlich, siehe HeroUI |

Übernommene Effekte (Aceternity, Magic UI, Originkit) vor dem Einbau gegen S17, S19 und BE07 prüfen: Startwerte und Fassung für reduzierte Bewegung stehen oft anders im Code.

## Bibliotheken

### shadcn/ui
- **Geprüft:** 08.09.2026. **Lizenz:** MIT, frei.
- Zugängliche Bausteine als Quelltext im eigenen Projekt, kein Paket in `node_modules`. Dazu fertige Blöcke und Diagramme.
- **Einbau:** CLI kopiert den Quelltext ins Projekt (auch mit `pnpm dlx` oder `bunx --bun`).
  ```bash
  npx shadcn@latest init
  npx shadcn@latest add <component>
  ```
- **Wofür:** Unterbau für einen eigenen Baustein. Die meisten Bibliotheken unten bauen darauf auf oder passen dazu.

### Radix UI Primitives
- **Geprüft:** 08.09.2026. **Lizenz:** MIT, frei.
- Ungestaltete React-Grundbausteine nach WAI-ARIA (Dialog, Popover, Dropdown Menu, Tabs, Accordion, Slider) mit Tastatur und Bildschirmleser.
- **Einbau:** je Baustein ein Paket oder das Sammelpaket `radix-ui` (nur Genutztes wird gebündelt).
  ```bash
  npm i @radix-ui/react-dialog
  ```
- **Wofür:** Zugänglichkeit und Zustandslogik ohne Gestalt. Falle: setzt Inline-Styles, bei strengem `style-src` siehe TE06.

### Aceternity UI
- **Geprüft:** 08.09.2026. **Lizenz:** Grundbestand MIT, frei nutzbar. „All-Access Pass“ 249 $ einmalig für Premium-Blöcke und Seitenvorlagen.
- Über 200 bewegte Bausteine (Hero, Bento, Parallax, Glanzkarten, Text-Reveal) mit Tailwind und Framer Motion, passend zu shadcn.
- **Einbau:** Code je Baustein von der Seite kopieren; ein MCP-Server ist angeboten.
- **Wofür:** nachsehen, wie ein Effekt in React und Framer Motion aufgebaut ist, dann neu bauen.

### Magic UI
- **Geprüft:** 08.09.2026. **Lizenz:** Bibliothek frei und quelloffen. Magic UI Pro (pro.magicui.design, 199 $ einmalig) verkauft nur Vorlagen und Blöcke.
- Über 150 bewegte Bausteine (Laufbänder, Partikel- und Kugelhintergründe, Strahlen, Bento) mit React, TypeScript, Tailwind und Motion. Begleiter zu shadcn/ui.
- **Einbau:** kopieren oder über das shadcn-Register, Befehl je Baustein auf der Seite.
- **Wofür:** einzelne Hintergrund- und Umgebungseffekte, nicht ganze Seiten.

### coss ui (früher Origin UI)
- **Geprüft:** 09.09.2026. **Lizenz:** **AGPL v3.** Kostenlos, aber nicht frei von Pflichten.
- **Falle:** Origin UI wurde umbenannt und neu lizenziert. originui.com zeigt jetzt „coss ui“, das Repo `origin-space/originui` leitet auf `cosscom/coss`. AGPL ist eine Netzwerk-Copyleft-Lizenz: Übernommener Code kann das Kundenprojekt zur Offenlegung seines Quelltexts verpflichten. Kein Code in ein Kundenprojekt ohne ausdrückliche Lizenzentscheidung von <dein-name>. Jede Notiz mit „Origin UI, MIT“ ist falsch und wird am Fundort korrigiert.
- Große Sammlung nach shadcn-Art (Eingaben, Tabellen, Kalender, Auswahl, Navigation). Nicht zu verwechseln mit Originkit.
- **Wofür:** dichte Formular-, Tabellen- und Einstellungsmuster nur ansehen. Für Code im Kundenprojekt shadcn/ui oder Radix (beide MIT).

### Originkit
- **Geprüft:** 08.09.2026. **Lizenz:** kostenlos. Ansehen ohne Konto, Quelltext nur mit kostenlosem API-Schlüssel.
- Über 250 Bausteine mit eingebauter Bewegung, ausgeliefert je Stack (React, Next.js, Vite, Framer) und Stil (Tailwind, CSS, CSS Modules).
- **Einbau:** geholten Quelltext kopieren, in Framer nutzen oder per MCP-Server.
- **Wofür:** Maßstab für Handwerk an bewegten Bausteinen. Ablauf und Kurven einer Interaktion ansehen, dann neu bauen.

### 21st.dev
- **Geprüft:** 08.09.2026. **Lizenz:** je Baustein verschieden, Eintrag prüfen. Ansehen frei; kostenloses Konto 2 Kopien am Tag; Bezahlkonto unbegrenzt mit Premium-Vorlagen.
- Offenes Register von Bausteinen, Vorlagen und Themen aus der Gemeinschaft, laufend ergänzt.
- **Einbau:** KI-Prompt kopieren (Cursor, Claude Code, v0) oder per shadcn-CLI (Register-Format).
- **Wofür:** sehen, was gerade gebaut wird. Als dauerhafte Abhängigkeit unsicher.

### HeroUI (früher NextUI)
- **Geprüft:** 09.09.2026. **Lizenz:** **ungeklärt.** npm meldete `@heroui/react` als MIT, das GitHub-Repo trug Apache-2.0 mit zwei verschiedenen LICENSE-Dateien. Kostenlos in beiden Fällen; die Lizenzen unterscheiden sich bei Patentrecht und Namensnennung. LICENSE der eingebauten Fassung lesen und ins ARMOURY schreiben.
- Vollständige React-Bibliothek (Knöpfe, Dialoge, Tabellen, Datumswahl, Formulare) auf React Aria und Tailwind CSS v4.
- **Einbau:** `@heroui/styles` im globalen CSS nach Tailwind importieren. `heroui-cli` legt Starter für Next.js, Vite und React Router an.
  ```bash
  npm i @heroui/react @heroui/styles
  ```
- **Wofür:** vollständiger, zugänglicher Satz, wenn es schnell gehen muss. Eigene Gestalt ist stark und wird ganz ersetzt (PR15).

## Nur Anschauung, kein Code

Für Aufbau und Tempo ganzer Seiten. Keine dieser Seiten liefert Code.

- **Awwwards**: Preisträger nach Kategorie und Technik (WebGL, React, Figma). Ansehen frei; Marktplatz und Kurse kosten.
- **Mobbin**: echte Produktoberflächen als Bildschirmfotos (iOS, Android, Web; über 500.000 Ansichten, über 1.000 Apps). Frei nur die 4 neuesten Apps, 3 Sammlungen, kein Download.
- **Land-book**: über 5.000 Landingpages, nach Stil, Branche und Farbe. Ansehen frei; Pro für unbegrenzte Boards und Telefonansicht.
- **Recent Design** (früher Godly, godly.website leitet dorthin): kühne, experimentelle Seiten. Ansehen frei.
- **Siteinspire**: kuratierte fertige Seiten nach Stil und Branche, ruhiger als Awwwards. Ansehen frei; nur der Newsletter kostet.

## Quellen

- https://ui.shadcn.com/
- https://www.radix-ui.com/primitives
- https://ui.aceternity.com/
- https://magicui.design/
- https://originui.com/ (coss ui, Repo `cosscom/coss`)
- https://www.originkit.dev/
- https://21st.dev/
- https://www.heroui.com/
- https://www.awwwards.com/, https://mobbin.com/, https://land-book.com/, https://recent.design/, https://www.siteinspire.com/

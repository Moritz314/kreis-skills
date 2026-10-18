# Rezept: Astro, Tailwind und Inseln

Gerüst, Inseln, fremde Komponenten und Auslieferung an nginx. Regeln: TE01 bis TE09, S10, S36, S40, Budgets in `regler.md`. Ab `technik: statisch`. Versionen nur in TE02.

## Start

Fassungen von Astro, Tailwind und Node: TE02.

```bash
npm create astro@latest mein-projekt
cd mein-projekt
# Tailwind 4 via the Vite plugin; @astrojs/tailwind is deprecated
npm install tailwindcss @tailwindcss/vite
# only if islands are needed: installs @astrojs/react, react, react-dom, types,
# registers react() and sets jsx in tsconfig.json
npx astro add react
```

`astro.config.mjs`:

```js
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import react from "@astrojs/react";

export default defineConfig({
  vite: { plugins: [tailwindcss()] },
  integrations: [react()], // omit at technik: statisch
});
```

`src/styles/global.css` einmal im Grundlayout einbinden, Inhalt `@import "tailwindcss";`.

Bauen, lokal prüfen, ausliefern:

```bash
npx astro build
npx astro preview   # local check of dist/
tar -czf - -C dist . | ssh myserver "tar -xzf - -C /var/www/mein-projekt"
```

## Aufbau

Pflicht sind nur `src/` und `package.json`. In `src/` ist nur `src/pages` reserviert: jede Datei dort ist eine Route. Der Rest ist Konvention.

```
src/
  pages/                 # reserved: one route per file
  layouts/               # base layout(s); import global.css, <ClientRouter />
  components/            # .astro components; islands live here too
    ui/                  # shadcn lands here as source, not a package
  content/               # markdown/MDX/JSON, read by content.config.ts
  content.config.ts
  styles/global.css      # @import "tailwindcss"; @theme; :root tokens
public/                  # unprocessed static files
astro.config.mjs
```

Sammlungen stehen in `src/content.config.ts` (nicht mehr `src/content/config.ts`, seit Astro 5):

```ts
import { defineCollection } from "astro:content";
import { glob, file } from "astro/loaders";
import { z } from "astro/zod"; // since Astro 6, not from astro:content

const artikel = defineCollection({
  loader: glob({ base: "./src/content/artikel", pattern: "**/*.md" }),
  schema: z.object({ titel: z.string(), datum: z.date() }),
});

export const collections = { artikel };
```

`glob()` liest einen Ordner (Markdown, MDX, Markdoc, JSON, YAML, TOML), `file()` eine Datei mit mehreren Einträgen nach `id`. Ausgabe ist statisch (`output: 'static'` oder weglassen), `astro build` schreibt alles nach `dist/`.

## Inseln

Ohne `client:`-Direktive kommt kein JavaScript an. Eine Komponente wird erst an der Stelle ihrer Nutzung zur Insel. Welche Direktive wann: TE03.

| Direktive | Löst aus | Fall |
|---|---|---|
| `client:load` | sofort beim Laden | oben und sofort bedienbar |
| `client:idle` | `requestIdleCallback` (optional `timeout`) | bald gebraucht, nicht dringend |
| `client:visible` | Element kommt ins Bild (IntersectionObserver, optional `rootMargin`) | Standard |
| `client:media` | Media Query passt, z. B. `client:media="(max-width: 50em)"` | hängt an der Breite, etwa Menü nur mobil |
| `client:only` | ohne Server-Rendern, Framework als Text, z. B. `client:only="react"` | braucht `window` oder eine reine Browser-API; ohne Platzhalter, also Risiko für Layoutsprung |

Ein Framework lädt nur, wo es genutzt wird, einmal je Seite. Mehrere Frameworks gehen auf einer Seite, aber nur über getrennte `.astro`-Dateien. Astro empfiehlt viele kleine Inseln statt einer großen; eine feste Grenze nennt die Doku nicht (ungeprüft über diese Empfehlung hinaus).

Stufen in Astro:

- `technik: statisch`: keine Inseln, keine Framework-Integration. Kleines Skript nur als eigene Datei (TE06).
- `technik: inseln`: Inseln nach TE03.
- `technik: webgl`: Shader und 3D immer als Insel mit `client:visible` oder `client:idle`, mit Standbild und Telefonfassung nach TE10. Code: `rezepte/shader.md`, `rezepte/3d.md`.

## Tailwind

Tailwind 4 braucht keine `tailwind.config.js`, es wird über `@import` und `@theme` im CSS eingestellt. Eine alte JS-Datei lässt sich mit `@config "../../tailwind.config.js";` einbinden. Token sind CSS-Variablen:

```css
/* generates a utility too, e.g. bg-marke-500 */
@theme { --color-marke-500: #...; }

/* plain custom property, no utility */
:root { --marke-hover-opacity: 0.85; }

/* a theme var referencing another var needs `inline`,
   otherwise it resolves at definition site, not at use site */
@theme inline { --font-sans: var(--font-inter); }

/* two widths as tokens: content width and reading width in ch (S27) */
@theme { --width-content: /* project value */; --width-read: /* in ch */; }
```

Fallen aus v3: `shadow`, `rounded`, `blur` sind eine Stufe verschoben (`shadow-sm` heißt jetzt `shadow-xs`, altes `shadow` heißt `shadow-sm`). `ring` ist jetzt 1 px statt 3 px (alt: `ring-3`). Mindestbrowser: Safari 16.4, Chrome 111, Firefox 128. Ältere Browser verlangen Tailwind 3.4.

## Fremde Komponenten

shadcn/ui hat eine offizielle Astro-Anleitung (geprüft 08.09.2026). Tailwind und React müssen vorher eingerichtet sein. Lizenz MIT.

```bash
pnpm dlx shadcn@latest init -t astro
pnpm dlx shadcn@latest add button
```

Die Teile landen als Quelltext in `src/components/ui/`. Import aus `.astro` mit `import { Button } from "@/components/ui/button"`; dafür braucht `tsconfig.json` den Alias `@/*`. Ohne `client:`-Direktive rendert ein shadcn-Teil nur Markup ohne Bedienung. Das ist das Inselmodell, kein Fehler.

coss ui (früher Origin UI) folgt denselben Konventionen und landet am selben Ort. Lizenz: **AGPL v3** (gelesen 09.09.2026: `originui.com` zeigt coss ui, `origin-space/originui` leitet auf `cosscom/coss`). Nicht ohne Lizenzentscheid in ein Kundenprojekt übernehmen. Auswahl der Bibliothek: `rezepte/komponenten.md`.

## Auslieferung an nginx

`astro build` legt CSS und JS gebündelt und mit Hash unter `dist/_astro/` ab (Pfad über `build.assets`, Standard `'_astro'`; `build.assetsPrefix` für ein CDN). Bilder aus `astro:assets` ebenso, z. B. `/_astro/mein-bild.<hash>.webp`. Versionsendungen von Hand (`style.v2.css`) entfallen.

Cache nach TE04. Astro gibt kein nginx-Rezept; Vorlage ist die Kopfzeile des Node-Adapters. Ein `add_header` in einem `location`-Block hebt alle `add_header` der Server-Ebene auf. Darum holt jeder Block die Kopfzeilen aus S10 per `include` neu:

```nginx
# /etc/nginx/snippets/security-headers.conf (S10, TE05)
add_header Strict-Transport-Security "max-age=31536000" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "frame-ancestors 'self'" always;  # meta route; header route: full CSP here

# server block
location /_astro/ {
  include snippets/security-headers.conf;
  add_header Cache-Control "public, max-age=31536000, immutable";
}
location / {
  include snippets/security-headers.conf;
  add_header Cache-Control "no-cache";   # HTML; the longer prefix /_astro/ wins
}
```

`publish.sh` behält sein Muster (Ausschlussliste, Sicherung am Server vor der Übertragung, `tar` über `ssh` ohne `--delete`, HTTPS-Prüfung danach). Vier Änderungen:

- Quelle ist `dist/` nach `astro build`, nicht der Projektordner.
- Die Git-Sauberkeitsprüfung läuft gegen den Projektordner; `dist/` gehört nicht ins Repo.
- Die Prüfung auf CSS/JS ohne Versionsendung entfällt (Hash).
- Prüfungen auf `canonical`, `<title>` und keine Google Fonts laufen gegen die gebauten Dateien in `dist/`.

## CSP

`astro build` warnt bei kaputter CSP nicht. Der Fehler zeigt sich erst in der Browserkonsole. Weg wählen nach TE05, Skripte nach TE06.

```js
// astro.config.mjs, without <ClientRouter />
export default defineConfig({
  security: { csp: true },               // since Astro 6.0, SHA-256 hashes in <meta>
  build: { inlineStylesheets: "never" },
});
```

Mit `<ClientRouter />` kein `security.csp`, CSP als nginx-Kopfzeile (TE05), `inlineStylesheets: "never"` bleibt. `security.csp` deckt `<ClientRouter />` und Shiki nicht ab; Shiki setzt immer Inline-Styles und braucht `'unsafe-inline'` in `style-src`.

Fallen:

- Astro schreibt kleine handgeschriebene `<script>` aus `.astro` direkt ins HTML. Die Schwelle ist nicht dokumentiert, wohl Vites `assetsInlineLimit` (ungeprüft). Jedes Inline-Skript gilt als unsicher. Lösung: Insel oder eigene `.js`/`.ts`-Datei per `<script src="...">`. Inseln selbst laden immer als externe Module aus `dist/_astro/`.
- Radix (Unterbau von shadcn) setzt über `react-remove-scroll` zur Laufzeit `<style>`-Elemente (Dialog, Sheet, ScrollArea). Mit `'unsafe-inline'` in `style-src` geht das; ein `style-src` nur mit Hash oder Nonce verlangt den Verzicht auf diese Teile.

Prüfen (TE07):

```bash
# which CSP route is active
curl -s https://example.com/ | grep -o '<meta http-equiv="[Cc]ontent-[Ss]ecurity-[Pp]olicy"[^>]*>'  # meta route
curl -sI https://example.com/ | grep -i 'content-security-policy'                                   # header route
# inline scripts in the build, expect 0 hits
rg -P '<script(?![^>]*\bsrc=)(?![^>]*application/ld\+json)[^>]*>' dist --glob '*.html'
```

Danach im Browser mit offener Konsole jede Insel auslösen, jedes shadcn-Teil mit Scroll-Sperre öffnen und bei `<ClientRouter />` die Seite wechseln. Ziel: kein `Refused to execute`, kein `Refused to apply style`.

## Bilder und Schriften

Bilder bevorzugt über `astro:assets`; ein `<img>` erfüllt S36 mit `width`, `height`, Format und `loading`:

```astro
---
import { Image, Picture } from "astro:assets";
import foto from "../assets/werkstatt.jpg";
---
<Image src={foto} alt="…" layout="constrained" width={1200} height={800} priority />
<Picture src={foto} alt="…" layout="full-width" />
```

`<Image />` kennt `width`/`height`, `widths`, `densities`, `sizes`, `format` (Standard `webp`), `quality` (`low`/`mid`/`high`/`max`), `layout` (`constrained`/`full-width`/`fixed`/`none`), `priority` (Standard `false`), `fit` (Standard `cover`). Mit `layout` erzeugt Astro `srcset`, `sizes`, `loading`, `decoding` und feste Maße gegen Layoutsprung. `<Picture />` liefert mehrere Formate mit Rückfall (Standard `formats: ['webp']`). `priority` nur für das LCP-Bild.

Schriften über die Fonts API von Astro (`astro:assets`; Quellen: lokale Dateien, Google, Fontsource, Bunny, Fontshare). Sie lädt die Schrift herunter, hält sie lokal und liefert sie selbst aus, mit Preload. Die Doku führt sie nicht mehr als experimentell; seit wann, ist ungeprüft (experimentell ab Astro 5.7, April 2025). Eigenes `@font-face` unter `public/fonts/` geht weiter, ist aber nicht mehr der empfohlene Weg. Schriftformat und Budget: TE09.

Core Web Vitals messen gegen `regler.md`. Eine feste Zahl für Astro-Seiten gibt es nicht, der Wert ist je Seite.

## Quellen

- Offizielle Doku von Astro, Tailwind und shadcn/ui sowie GitHub-Releases (geprüft 08.09.2026)
- originui.com, github.com/cosscom/coss (Lizenz, gelesen 09.09.2026)
- Offene Issues bei Radix UI zu Inline-Styles über `react-remove-scroll`
- web.dev (Core Web Vitals)

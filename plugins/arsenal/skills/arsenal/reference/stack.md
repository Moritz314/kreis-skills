# Stack: Astro, Tailwind, Islands

The default stack for a new project in this skill: Astro as the scaffold,
Tailwind CSS for styling, islands for interactivity, static output shipped to
the project's own nginx server. This choice is not re-argued here. This file
is the sole reference a model needs to set up, build and ship a project
without looking anything up. Version numbers carry the date they were
checked against official docs; anything not confirmed against an official
source is marked "unverified" and treated as a guess, not a fact. Source:
official Astro/Tailwind/shadcn docs and GitHub releases, checked live
2026-09-08.

Read [registers.md](registers.md) first, especially the `technik` dial, and
[performance.md](performance.md) for the budget that still applies. Library
choice beyond shadcn/Origin UI lives in [components.md](components.md), not
here.

## 1. Startup commands

Checked sequence, empty folder to a shipped first page. Current major
versions, checked 2026-09-08: **Astro 7.3.2**, **Tailwind CSS 4.3.3**. Astro
6+ requires Node >= 22.12.

```bash
npm create astro@latest mein-projekt
cd mein-projekt
# Tailwind 4 via the Vite plugin: recommended for Astro, @astrojs/tailwind is deprecated
npm install tailwindcss @tailwindcss/vite
```

`astro.config.mjs`: Tailwind plugin, plus a framework integration only if
islands are actually needed.

```js
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import react from "@astrojs/react";

export default defineConfig({
  vite: { plugins: [tailwindcss()] },
  integrations: [react()],
});
```

```bash
# installs @astrojs/react + react + react-dom + types, registers react()
# above, sets jsx in tsconfig.json
npx astro add react
```

`src/styles/global.css`, imported once in the base layout: `@import
"tailwindcss";`. No `tailwind.config.js` needed (section 4). Optionally
prepare shadcn/ui (needs Tailwind and React already set up, section 5):

```bash
pnpm dlx shadcn@latest init -t astro
pnpm dlx shadcn@latest add button
```

Build, check locally, ship (section 6 has the full `publish.sh` picture):

```bash
npx astro build
npx astro preview   # local check of the dist/ output
tar -czf - -C dist . | ssh myserver "tar -xzf - -C /var/www/mein-projekt"
```

## 2. Project structure

Only `src/` and `package.json` are required. `public/`, `astro.config.mjs`,
`tsconfig.json` are recommended, not enforced. Inside `src/`, only
**`src/pages`** is reserved by Astro, every file there becomes a route.
`src/components`, `src/layouts`, `src/styles` are convention, freely
renamable.

```
src/
  pages/                 # reserved: one route per file
  layouts/               # base layout(s); import global.css, <ClientRouter />
  components/             # .astro components; framework islands live here too
    ui/                    # shadcn/Origin UI land here as source, not a package
  content/                # markdown/MDX/JSON etc, read by content.config.ts
  content.config.ts
  styles/global.css       # @import "tailwindcss"; @theme block; :root tokens
public/                  # unprocessed static files
astro.config.mjs
```

Tokens live in `src/styles/global.css` (section 4). Islands are ordinary
files under `src/components/`, nothing marks them as islands beyond the
`client:` directive at their usage site.

Content Collections are defined in **`src/content.config.ts`** (not
`src/content/config.ts`, gone since the Content Layer API in Astro 5):

```ts
import { defineCollection, z } from "astro:content";
import { glob, file } from "astro/loaders";

const artikel = defineCollection({
  loader: glob({ base: "./src/content/artikel", pattern: "**/*.md" }),
  schema: z.object({ titel: z.string(), datum: z.date() }),
});

export const collections = { artikel };
```

`glob()` reads a directory (markdown/MDX/Markdoc/JSON/YAML/TOML), `file()`
reads one file with several entries distinguished by `id`. Since Astro 6,
`z` comes from `astro/zod`, not `astro:content`. Output is static by default
(`output: 'static'`, or omit it); `astro build` writes a fully static tree
to `dist/`.

## 3. Using islands correctly

Astro ships every page as plain HTML and CSS and strips all client-side
JavaScript unless a component is explicitly marked as an island. Five
directives control hydration timing. Each has one deciding question, not
just a trigger:

| Directive | Fires | Use when |
|---|---|---|
| `client:load` | immediately on page load | Above the fold **and** needs to be interactive the instant the page appears. |
| `client:idle` | on `requestIdleCallback` (optional `timeout`) | Needs to work soon, but not before everything more urgent is handled. |
| `client:visible` | element enters the viewport (`IntersectionObserver`, optional `rootMargin`) | Below the fold, or not needed until the visitor scrolls to it. Default choice for most islands. |
| `client:media` | a CSS media query matches, e.g. `client:media="(max-width: 50em)"` | Necessity depends on viewport size, not scroll position, e.g. a mobile-only nav toggle. |
| `client:only` | skips server rendering, framework required as a string, e.g. `client:only="react"` | SSR would be wrong or impossible (depends on `window` or a browser-only API). Costs a layout-shift risk since there is no server-rendered placeholder, use only when SSR genuinely does not work. |

No directive means no JavaScript ever: a React Three Fiber canvas imported
without a `client:` directive stays static markup, the React runtime never
ships. A framework loads only where used, deduplicated across islands on one
page. Multiple frameworks can coexist and even mix on one page, but only
across separate `.astro` files composing them, never inside a single one.

Astro's own guidance, no numeric threshold: prefer many small,
individually-triggered islands over one large island hydrating a whole page
as an app, that defeats the point of islands. No documented rule of thumb
for when a large island is justified (unverified beyond this general
guidance), treat it case by case.

### The `technik` dial in Astro terms

- **`statisch`**: no islands at all. Skip framework integrations entirely.
  All motion is CSS. Any interactivity is minimal, unhydrated JavaScript,
  written with section 7's CSP rule in mind.
- **`inseln`**: islands for the parts that need them. `client:visible` is
  the default; `client:load` only for an element both above the fold and
  immediately interactive.
- **`webgl`**: the above plus shader and 3D layers, always as islands, never
  on the critical path (`client:visible`/`client:idle`, essentially never
  `client:load` for a heavy scene), always with the static fallback and
  mobile budget from [performance.md](performance.md).

## 4. Tailwind

Tailwind 4 in Astro uses the Vite plugin, not the deprecated
`@astrojs/tailwind` integration; install and config are the three blocks
already shown in section 1 (`@tailwindcss/vite` in `astro.config.mjs`,
`@import "tailwindcss";` in `global.css`). No `tailwind.config.js` is
required, Tailwind 4 configures CSS-first via `@import` and `@theme`. An
existing JS config can still be pulled in with
`@config "../../tailwind.config.js";`. A PostCSS path exists for setups
without native Vite; for Astro the docs name the Vite plugin as preferred.

**Rule: design tokens are CSS variables, not Tailwind config**, so a
project's own color strategy never fights Tailwind's:

```css
/* generates a utility too, e.g. bg-marke-500 */
@theme { --color-marke-500: #...; }

/* plain custom property, no utility generated */
:root { --marke-hover-opacity: 0.85; }

/* a theme var referencing another var needs `inline`, otherwise the
   reference resolves at definition site, not at use site */
@theme inline { --font-sans: var(--font-inter); }
```

Actual token values (palette, type scale) belong to
[design-foundations.md](design-foundations.md), not here. On a fresh
Tailwind 4 project the v3-to-v4 breaking changes mostly do not apply, but
two matter if reusing old muscle memory: `shadow`/`rounded`/`blur` shifted
one step (`shadow-sm` is now `shadow-xs`, old `shadow` is now `shadow-sm`),
and `ring` default width dropped from 3px to 1px (old width is `ring-3`).
Minimum browsers: Safari 16.4+, Chrome 111+, Firefox 128+; an older-browser
requirement means Tailwind 3.4 instead.

## 5. Foreign components

**shadcn/ui** has an official Astro guide (checked directly 2026-09-08),
needs Tailwind and the React integration already set up:

```bash
pnpm dlx shadcn@latest init -t astro
pnpm dlx shadcn@latest add button
```

Components land as source under `src/components/ui/`, imported from
`.astro` files (`import { Button } from "@/components/ui/button"`, needs the
`@/*` alias in `tsconfig.json`). shadcn/ui itself is MIT.

**coss ui (formerly Origin UI)** follows the same shadcn conventions (CLI or
copy-paste), same landing spot. The earlier "MIT" claim here was secondhand
and is now wrong: as read on 2026-09-09, `originui.com` serves "coss ui", the
repo `origin-space/originui` redirects to `cosscom/coss`, and the license is
**AGPL v3**, a copyleft network license. Do not drop its source into a client
project without an explicit licensing decision, see the warning in
[components.md](components.md). Library selection between shadcn, coss ui and
the rest lives in [components.md](components.md); this section covers only how
they land in Astro.

**The boundary in both cases**: the CLI drops in source code, an ordinary
framework component, not a black box. It stays static markup until it
carries a `client:` directive like any other island (section 3). A shadcn
component dropped into `.astro` without a directive renders markup and none
of its interactivity, the islands model applying uniformly, not a bug.

## 6. Shipping to nginx

`astro build` writes `dist/`. CSS and JS land bundled and **hashed by
default** under `dist/_astro/` (path via `build.assets`, default `'_astro'`;
`build.assetsPrefix` adds a CDN prefix). Images through `astro:assets` hash
the same way, e.g. `/_astro/mein-bild.<hash>.webp`. This replaces the manual
cache-busting `publish.sh` did with filenames like `style.v2.css`, for CSS,
JS and images it is now automatic.

`publish.sh` keeps its <internal-project> pattern unchanged (exclusion list,
server-side backup before transfer, `tar` over `ssh` without `--delete`,
HTTPS check after transfer), with four adjustments: the transfer source
becomes `dist/` after a preceding `astro build`, not the project folder; the
git-clean check stays against the project folder, not `dist/`, which is
build output and does not belong in the repo; the old "CSS/JS without a
version suffix" self-check can be dropped, Astro's hashing makes it moot;
the `canonical` link, `<title>`, and no-Google-Fonts checks stay meaningful
but now run against the built files in `dist/`.

Cache headers: Astro's deploy docs give no nginx recipe, the template is the
Node adapter's `Cache-Control: public, max-age=31536000, immutable` for
everything under `_astro/`. Applied to nginx: a long immutable cache for
`/_astro/*` (hashed filenames break the cache automatically on change),
short or no cache for HTML, same as <internal-project>'s `no-cache` on HTML.

## 7. The CSP trap

This is the section that matters most. A project that ships broken CSP
passes `astro build` without a single warning, the break is only visible in
the browser console at delivery time.

### 7.1 `security.csp` does not cover everything

Since **Astro 6.0**, `security.csp` (`boolean | object`, default `false`)
hashes (default SHA-256) the inline scripts and styles a page actually uses
and writes them into a per-page `<meta http-equiv="content-security-policy">`,
no `unsafe-inline` needed. On server-rendered pages Astro sets the header
instead. Two explicit exclusions: **`<ClientRouter />` (View Transitions) is
not supported**, and **Shiki is not supported** (keeps using inline styles
regardless of this setting).

**Countermeasure**: decide per project, up front, whether `<ClientRouter />`
is actually needed.
- No `<ClientRouter />` (typical `technik: statisch`/`inseln` without page
  transitions): `security.csp: true` plus `build.inlineStylesheets: 'never'`.
  Every page carries its own hash-based CSP in `<meta>`, nginx sets no
  `Content-Security-Policy` header.
- `<ClientRouter />` in use (typical `technik: webgl` with scroll
  choreography): fall back to the <internal-project> pattern, CSP as an nginx header
  (`script-src 'self'`, `style-src 'self' 'unsafe-inline'`), no
  `security.csp`, still set `build.inlineStylesheets: 'never'` to keep
  component styles out of the inline risk; Shiki stays the one remaining
  inline-style source covered by `'unsafe-inline'`.

**Acceptance check**: confirm which mechanism is actually active on the
built page.

```bash
curl -s https://example.com/ | grep -o '<meta http-equiv="[Cc]ontent-[Ss]ecurity-[Pp]olicy"[^>]*>'  # meta-tag route
curl -sI https://example.com/ | grep -i 'content-security-policy'  # header route
```

Then load the page in a real browser with devtools open, check the console
for `Refused to execute`/`Refused to apply style` after triggering every
interactive island, and after page navigation if `<ClientRouter />` is used.

### 7.2 Astro auto-inlines small hand-written `<script>` tags

Astro inlines small `<script>` tags written directly in `.astro` files into
the HTML by default. The exact size threshold is undocumented on the
checked page, likely tied to Vite's `assetsInlineLimit` **(unverified)**,
so treat any inline `<script>` as unsafe rather than trusting a size cutoff.
Island hydration itself is unaffected, always external hashed module scripts
from `dist/_astro/`, already covered by `script-src 'self'`. The risk is
specifically a hand-written `<script>` sitting inline in `.astro` markup.

**Countermeasure**: never write a raw `<script>` block inside `.astro`
markup on a project shipping strict `script-src 'self'`. Put the logic in an
island, or in a `.js`/`.ts` file imported via `<script src="...">`.

**Acceptance check**: after `astro build`, search the built HTML for a
`<script>` tag without `src`; any hit will violate a strict `script-src`.

```bash
rg -P '<script(?![^>]*\bsrc=)[^>]*>' dist --glob '*.html'
```

No match means no surviving inline scripts. Any match needs to move to an
island or an external file before shipping.

### 7.3 Radix UI (shadcn's substrate) injects inline styles at runtime

Multiple open Radix issues confirm that Radix primitives (via
`react-remove-scroll`, e.g. Dialog, ScrollArea) inject inline `<style>`
elements at runtime, breaking a strict `style-src` without `unsafe-inline`,
a nonce, or a hash. No equivalent problem is documented for `script-src
'self'`, the known cases are all styles.

**Countermeasure**: a project using shadcn's scroll-locking primitives
(Dialog, Sheet, ScrollArea, similar) cannot run a strict `style-src` without
`unsafe-inline` unless those primitives are avoided. Current practice at
<internal-project> and <deine-domain> already keeps `'unsafe-inline'` in `style-src`,
that stays compatible; only a project attempting a hash/nonce-only
`style-src` needs to drop those primitives or accept the violation.

**Acceptance check**: in a real browser with devtools open, open every
shadcn component that can scroll-lock and watch the console for a
`style-src` violation the moment it opens.

## 8. Performance

Budgets from [performance.md](performance.md) apply in full, especially the
reduced-motion and mobile/low-power fallback for any shader or 3D island.

Images go through `astro:assets`, `<Image />` and `<Picture />`, never a raw
`<img>`. `<Image />` takes `width`/`height`, `widths`, `densities`, `sizes`,
`format` (default `webp`), `quality` (`low`/`mid`/`high`/`max`), `layout`
(`constrained`/`full-width`/`fixed`/`none`), `priority` (default `false`),
`fit` (default `cover`); using `layout` auto-generates `srcset`, `sizes`,
`alt`, `loading`, `decoding` and fixed dimensions against layout shift.
`<Picture />` emits several formats at once (default `formats: ['webp']`)
with a fallback for older browsers.

Fonts are self-hosted through Astro's Fonts API (`astro:assets`, providers
include local filesystem, Google, Fontsource, Bunny, Fontshare): downloads,
caches locally, serves self-hosted with preload links. Current docs no
longer mark it experimental; the exact point it stopped being experimental
is **unverified** beyond "started experimental in Astro 5.7, April 2025".
Plain manual `@font-face` under `public/fonts/` still works but is no longer
the recommended path.

Core Web Vitals thresholds (web.dev, 75th percentile of real users): **LCP**
good at <= 2.5s, **INP** good at <= 200ms, **CLS** good at <= 0.1. A mostly
static Astro page with a few deliberately-loaded islands and hashed,
long-cached assets sits in this range by default when images and fonts are
handled as above; the exact number is always page-specific, no blanket
Astro figure for this is documented.

## 9. When Astro is the wrong tool

Astro describes itself as "the web framework for building content-driven
websites": blogs, marketing sites, online shops. For state-heavy,
application-like UI, logged-in admin dashboards, inboxes, social feeds, task
managers, its own docs point to other frameworks as the ones that excel
there, while Astro can lose performance delivering that kind of surface. A
product built around a lot of persistent client-side state is better served
by a conventional SPA framework from the start, not by stretching islands to
cover it.

## Claude-Artefakt als Vorschau (2026-09-26)

Artefakte liefern `.glb` nicht aus (erlaubt sind u. a. .html .css .js .json .txt .webp .svg .woff2 .mp4). 3D-Modell als Base64-Text (`*.b64.txt`) daneben legen und im Loader per `fetch().text()`, `atob` und `GLTFLoader.parse` laden. three.js-Addons (GLTFLoader, meshopt) gibt es nicht auf cdnjs, im Artefakt über `cdn.jsdelivr.net/npm/three@<version>/` per Importmap laden, das ist dort erlaubt. Das Artefakt-Gerüst setzt selbst `<html>`, `<head>`, `<body>`: für die Veröffentlichung eine Fassung ohne diese Tags erzeugen, die Quelle bleibt vollständig.

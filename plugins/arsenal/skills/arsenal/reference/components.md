# Component libraries and inspiration sources

This file is a map of where to look for concrete implementation patterns —
markup structure, animation choreography, state handling — when you need one
for an ambitious effect. It is not a design system to import wholesale, and
none of these entries is a shortcut to a finished UI.

**Hard rule:** anything pulled from here gets re-themed into the project's
actual OKLCH color strategy, spacing rhythm, and copy before it counts as
done. Swap the palette, swap the type scale, swap the placeholder copy, adjust
the motion timing to the project's own rhythm. A component lifted unchanged —
same colors, same spacing, same lorem-ipsum-adjacent copy — reads as
templated and fails impeccable's slop test even if the code is technically
sound. Use these as reference to learn the *approach*, not as inventory to
paste in.

Licenses, pricing, and install commands below are **verified per entry on the
date noted** in that entry's `Checked:` line, not continuously. A date older
than a few weeks means "was true then", nothing more. Re-check from the
project's own LICENSE file (not from a blog post, not from a summary page)
before relying on any license or pricing claim, because free tiers, pro-tier
splits and even project ownership change.

Re-verified on 2026-09-09 against npm and GitHub, and referenced from the
technique files: `@react-three/fiber` 9.7.0 MIT, `@react-three/drei` 10.7.8
MIT, `@shadergradient/react` MIT, `@paper-design/shaders` Apache-2.0,
`@splinetool/react-spline` MIT. `@heroui/react` came back inconsistent, see
the HeroUI entry below.

## Component libraries

### shadcn/ui
- **Checked:** 2026-09-08.
- **URL:** https://ui.shadcn.com/
- **What it is:** Composable, accessible components distributed as source
  code you own, not a package you import from `node_modules`. Includes
  components, prebuilt blocks, and charts.
- **License/cost:** MIT, fully free.
- **Install:** `npx shadcn@latest init`, then `npx shadcn@latest add <component>`
  (also works with `pnpm dlx` / `bunx --bun`). The CLI copies component source
  directly into your project.
- **Go here for:** the base layer when building a component from scratch —
  accessible structure and sane defaults you then restyle completely. This is
  the substrate most of the other libraries below build on or are compatible
  with.

### Radix UI Primitives
- **Checked:** 2026-09-08.
- **URL:** https://www.radix-ui.com/primitives
- **What it is:** Unstyled, WAI-ARIA-compliant React primitives (Dialog,
  Popover, Dropdown Menu, Tabs, Accordion, Slider, etc.) with full keyboard
  navigation and screen-reader support baked in. 130M+ monthly downloads.
- **License/cost:** MIT, fully free.
- **Install:** `npm i @radix-ui/react-dialog` (per-primitive packages), or the
  consolidated `radix-ui` package importing only what you use (tree-shakeable).
- **Go here for:** the accessibility and interaction-state logic underneath
  shadcn's styling — go straight to Radix when you need the unstyled
  primitive with zero visual opinion to build a fully custom look on top of.

### Aceternity UI
- **Checked:** 2026-09-08.
- **URL:** https://ui.aceternity.com/
- **What it is:** 200+ animated, effect-heavy React components (hero
  sections, bento grids, parallax blocks, glare/glow cards, text-reveal
  effects) built with Tailwind CSS and Framer Motion, shadcn-compatible.
- **License/cost:** Free tier (core components, MIT) is genuinely usable
  standalone; a paid "All-Access Pass" ($249 one-time) unlocks premium blocks
  and full page templates.
- **Install:** copy-paste from the site (each component ships its own code
  block); an MCP server is also offered for AI-agent-driven insertion.
- **Go here for:** studying how a specific animated effect (parallax, glow,
  reveal-on-scroll) is structured in React + Framer Motion before building
  your own re-themed version — not for dropping a hero section in unchanged.

### Magic UI
- **Checked:** 2026-09-08.
- **URL:** https://magicui.design/
- **What it is:** 150+ free, open-source animated components and effects
  (marquees, particle/orb backgrounds, animated beams, bento grids) built
  with React, TypeScript, Tailwind, and Motion. Positioned as a companion to
  shadcn/ui. 22k+ GitHub stars.
- **License/cost:** Free and open source for the component library itself.
  A separate paid product, Magic UI Pro (pro.magicui.design, $199 one-time),
  sells finished page templates and blocks — the components themselves stay free.
- **Install:** copy-paste, or via the shadcn-compatible CLI registry format
  shown per-component on the site.
- **Go here for:** background/ambient motion effects (particle fields,
  animated gradients, beams) to study and re-theme — strong on isolated
  effects, not full page composition.

### coss ui (formerly Origin UI)
- **Checked:** 2026-09-09.
- **URL:** https://originui.com/ now serves "coss ui"; the GitHub repo
  `origin-space/originui` redirects to `cosscom/coss`.
- **Warning, read before use:** the library that arsenal earlier listed as
  "Origin UI, MIT" no longer exists under that name or that license. The
  project was renamed and relicensed: the current repo carries **AGPL v3**,
  not MIT. AGPL is a copyleft network license: pulling its component source
  into a client project can oblige that project to publish its own source.
  Do not copy code from here into a client build without an explicit
  licensing decision by the user. Any older note, prompt or ARMOURY entry that
  still says "Origin UI, MIT" is wrong and gets corrected where it is found.
- **What it is:** A large shadcn-convention component collection, copy-paste
  UI building blocks (inputs, tables, calendars, pickers, nav patterns) built
  with Tailwind and React. Distinct from the animated "Originkit" site below
  despite the similar name, and now also distinct from its own old name.
- **License/cost:** AGPL v3 as read on 2026-09-09. Free of charge, not free
  of obligations.
- **Install:** copy-paste from the site, following shadcn conventions, only
  after the licensing decision above.
- **Go here for:** studying dense, unglamorous UI patterns (form controls,
  data tables, settings panels) as a reference for how the interaction is
  structured. For code that ships in a client project, prefer shadcn/ui or
  Radix, both MIT, and treat this entry as inspiration only.

### Originkit
- **Checked:** 2026-09-08.
- **URL:** https://www.originkit.dev/
- **What it is:** A free animated-component library (250+ components) with
  motion built into every component. Components are fetched per your stack
  (React, Next.js, Vite, Framer) and styling target (Tailwind, CSS, CSS
  Modules), browsable via search/category with no key required.
- **License/cost:** Free; browsing needs no account, but fetching a
  component's actual source code requires a free API key.
- **Install:** copy fetched source directly, use inside Framer, or connect an
  MCP server so an AI agent can browse and place components.
- **Go here for:** this is the site the project treats as an aspirational
  quality bar for motion-heavy component craft — go here to study
  choreography and easing on a specific interaction, then rebuild it in the
  project's own visual language rather than fetching-and-pasting.

### 21st.dev
- **Checked:** 2026-09-08.
- **URL:** https://21st.dev/
- **What it is:** A community-built, crowdsourced registry/marketplace of UI
  components, templates, and themes ("living library" model rather than a
  fixed release).
- **License/cost:** Browsing is free; free accounts get 2 component copies
  per day; a paid membership unlocks unlimited copies and premium templates.
  Licensing is per-component (published in shadcn registry format) — check
  the individual entry.
- **Install:** copy an AI-ready prompt that pipes a component into
  Cursor/Claude Code/v0/etc., or install via the shadcn CLI since components
  are published in shadcn registry format.
- **Go here for:** browsing a wide, current cross-section of what design
  engineers are actually shipping right now — good for spotting a specific
  interaction pattern in the wild, less reliable as a stable long-term
  dependency source given the daily-copy-limited free tier.

### HeroUI (formerly NextUI)
- **Checked:** 2026-09-09.
- **URL:** https://www.heroui.com/
- **What it is:** A full React component library (buttons, modals, tables,
  date pickers, full form kit) built on React Aria and Tailwind CSS v4 —
  positioned as an alternative to MUI/Chakra/shadcn for shipping complete
  app UI rather than assembling primitives.
- **License/cost:** **unclear, resolve before use.** On 2026-09-09 npm
  reported `@heroui/react` as MIT while the GitHub repository carried
  Apache-2.0 and shipped two different LICENSE files. Free of charge either
  way, but the two licenses differ on patent grant and attribution, so read
  the LICENSE file of the exact version being installed and record the answer
  in the project's ARMOURY.md before shipping it.
- **Install:** `npm i @heroui/react @heroui/styles`, then import
  `@heroui/styles` after Tailwind in your global CSS; a dedicated
  `heroui-cli` scaffolds Next.js/Vite/React Router starters pre-wired.
- **Go here for:** a batteries-included alternative when a project needs a
  complete, accessible component set fast and will do heavy re-theming
  anyway (HeroUI's own visual identity is strong, so don't ship it as-is).

## Layout/visual inspiration only, not component code

These are for studying composition, motion pacing, and structural layout
decisions at the whole-page level — never for lifting code, since none of
them ship implementation.

- **Awwwards** — https://www.awwwards.com/ — award-winning site showcase,
  organized by category and technology (WebGL, React, Figma); best for
  seeing what "technically extraordinary" currently looks like at the
  top end. Free to browse; paid marketplace/courses are separate add-ons.
- **Mobbin** — https://mobbin.com/ — real product UI captured as screenshots
  across iOS/Android/web (500k+ screens, 1000+ apps); best for how a shipped
  product actually solved a flow, not a concept mockup. Free tier is narrow
  (latest 4 apps, 3 collections, no downloads) — full archive needs a paid plan.
- **Land-book** — https://land-book.com/ — curated landing-page gallery
  (5,000+ examples), filterable by style/industry/color; best for
  above-the-fold composition and landing-page structure ideas. Free browsing;
  Pro tier adds unlimited boards and mobile previews.
- **Recent Design** (formerly Godly; godly.website now redirects here) —
  https://recent.design/ — showcase of bold, experimental site design; best
  for unconventional layout and interaction ideas rather than conventional
  SaaS patterns. Free to browse.
- **Siteinspire** — https://www.siteinspire.com/ — long-running curated
  gallery of finished sites by style and industry; best as a second, calmer
  source alongside Awwwards when you want fewer stunt sites and more
  consistently well-executed ones. Free to browse; only the newsletter is paid.

# Icon, stock, and AI image sources

Where to get icons, stock photography, stock video, and AI-generated images for
a project, with license terms and how to pull each one in. Read
[components.md](components.md) for UI component sources and
[typography.md](typography.md) for fonts, both live in separate files.

**Hard rule:** license and cost claims below were checked live in September
2026 (see [recherche-bibliotheken.md](../planung/recherche-bibliotheken.md)
for the full trail with sources). Re-check before relying on a claim in a
client-facing or commercial context, free tiers and licensing terms change.
Never invent a license or price that isn't verified here or in that file.

## Icons

Pick one icon set per project and stay with it. Mixing stroke weights and
corner radii across sets is an instant tell of an assembled-not-designed
interface.

### Lucide
- **URL:** https://lucide.dev/ (license https://lucide.dev/license, packages
  https://lucide.dev/packages, code https://github.com/lucide-icons/lucide)
- **What it is:** Fork of Feather Icons, consistent thin-stroke line style,
  roughly 1600 to 1800 icons. Reached v1.0 in 2026 (v1.41.0 released
  2026-09-04).
- **License/cost:** ISC, fully free.
- **Install:** framework packages (`lucide-react`, `lucide-vue-next`,
  `lucide-svelte`, `lucide-solid` with context providers in v1,
  `lucide-angular`). In a published Artifact, load it from jsDelivr, not
  cdnjs, see the CDN section below.
- **Go here for:** the default icon set for any Tailwind/shadcn project.
  shadcn/ui ships Lucide as its own default, so this is the safest first
  choice whenever the stack is shadcn-adjacent and no other reason points
  elsewhere.

### Phosphor Icons
- **URL:** https://phosphoricons.com/
- **What it is:** Around 1200 base icons, each in six weights (Thin, Light,
  Regular, Bold, Fill, Duotone), over 7200 variants total. Packages for
  React, Vue, Svelte, Flutter, Elm, and Web Components.
- **License/cost:** MIT, fully free.
- **Install:** framework packages, e.g. `@phosphor-icons/react`.
- **Go here for:** a project that needs weight or style variety within one
  icon family, e.g. a Fill weight for active nav states and Regular
  elsewhere, without switching icon sets.

### Tabler Icons
- **URL:** https://tabler.io/icons (packages
  https://tabler.io/icons/packages, code
  https://github.com/tabler/tabler-icons, Figma plugin
  https://www.figma.com/community/plugin/1169807996149376642/tabler-icons)
- **What it is:** The largest of the four sets, 6100 to 6184 icons. Packages
  for React, Vue, Angular, Svelte, SolidJS, React Native.
- **License/cost:** MIT, fully free.
- **Go here for:** wide, unusual coverage, business or dashboard-specific
  symbols that Lucide, Phosphor, or Heroicons simply don't have. Go here
  second, after confirming the icon you need isn't already in whichever set
  the project has standardized on.

### Heroicons
- **URL:** https://heroicons.com/ (code
  https://github.com/tailwindlabs/heroicons)
- **What it is:** About 300 hand-drawn icons in Outline and Solid, plus a
  Mini variant, roughly 1288 icons combined. Built by the Tailwind team.
  First-party packages exist only for React and Vue.
- **License/cost:** MIT, fully free.
- **Go here for:** a small, curated set that is visually tuned to Tailwind
  defaults specifically, when the project wants exactly that look and
  doesn't need thousands of icons. Skip if the stack isn't React or Vue and
  no community port fits, the first-party coverage is narrow.

## Stock photos

### Unsplash
- **URL:** https://unsplash.com/ (license https://unsplash.com/license, API
  terms https://unsplash.com/api-terms, attribution guideline
  https://help.unsplash.com/en/articles/2511315-guideline-attribution)
- **What it is:** The largest curated free photo library.
- **License/cost:** Free, commercial and non-commercial use. Normal download
  needs no attribution. API use requires attribution of Unsplash and the
  photographer with a link back to their profile, formatted with
  `utm_source`/`utm_medium=referral`, or the API key gets revoked. Forbidden:
  reselling unaltered images as stock, mass-collecting to build a competing
  photo service. Unsplash+ (paid) additionally excludes AI training use in
  its terms, the free tier doesn't address that.
- **Install:** free API key, demo mode has a low rate limit, production
  access on request raises it.
- **Go here for:** the widest selection when authorship attribution in the
  UI or footer is acceptable.

### Pexels
- **URL:** https://www.pexels.com/ (license
  https://www.pexels.com/license/, API
  https://www.pexels.com/api/documentation/)
- **What it is:** Free stock photo library, commercial and private use, no
  attribution required.
- **License/cost:** Free. Forbidden: standalone resale or distribution
  (posters, wallpaper, merchandise without substantial creative rework),
  selling on other stock platforms.
- **Install:** free API key, default limit 200 requests/hour and 20,000/month,
  raise on request at no cost
  (https://help.pexels.com/hc/en-us/articles/900005851863).
- **Go here for:** the no-attribution default for photos, same API family as
  Pexels Video below, which keeps the project on one client and one rule set
  for both media types.

### Pixabay
- **URL:** https://pixabay.com/ (content license
  https://pixabay.com/service/license-summary/, API
  https://pixabay.com/service/about/api/)
- **What it is:** Free photo, illustration, and video library. Current
  Content License (since 2023-04-17) is CC0-like: irrevocable, worldwide,
  royalty-free, commercial and private use, no attribution needed. AI
  training use is explicitly permitted, with an opt-out for uploaders, which
  is the opposite stance from Unsplash+.
- **License/cost:** Free, API access essentially unlimited, no attribution
  required for API use.
- **Install:** already available in this system as an MCP server
  (`mcp__claude_ai_Pixabay__search_images`, `search_videos`,
  `download_image`), usable in arsenal directly with no extra setup.
- **Go here for:** the fastest path when the MCP connector is already live
  and a quick, no-attribution image or video is needed without standing up a
  separate API key.

## Stock video

### Pexels Video (primary source)
- **URL:** https://www.pexels.com/license/ (same license as Pexels photos)
- **What it is:** Commercially free stock video, no attribution, no
  watermark, direct download up to 4K, large and growing catalog.
- **License/cost:** Free, same terms as Pexels photos.
- **Install:** same Pexels API as photos.
- **Go here for:** the default stock video source. Chosen as primary over
  Mixkit and Coverr because its license has stayed stable and
  attribution-free for years with no per-clip exceptions, unlike Mixkit's
  mixed license classes, and because sharing one API and one rule set with
  Pexels photos keeps the arsenal media workflow to a single client. Good
  for web hero video loops, no watermark, no account required to download.

### Coverr (secondary source)
- **URL:** https://coverr.co/ (license https://coverr.co/license, terms
  https://coverr.co/terms)
- **What it is:** A more cinematically curated free video library.
- **License/cost:** Free, irrevocable, non-exclusive, worldwide license to
  download, modify, and use commercially, no attribution, no watermark.
  Forbidden: resale or redistribution as a standalone product, use on a
  competing stock or website-builder service, and explicitly, AI training or
  dataset use.
- **Go here for:** stylistically consistent, more cinematic loop backgrounds
  when Pexels Video doesn't have the right mood. Never feed Coverr footage
  into an AI training or dataset pipeline, that use is explicitly forbidden
  by its license, unlike Pexels.

**Not recommended:** Mixkit mixes a commercial-free license with some
clips restricted to private/educational use only, marked per clip, check
before every download. Videvo no longer exists as an independent service in
2026, folded into Freepik/Magnific, often behind an account or subscription,
not a reliable free source anymore.

## AI image

### Leonardo AI
- **What it is:** Image and video generation, model training, and an editor,
  reachable in this system through an MCP server (`mcp__leonardo__*`
  tools).
- **Status:** the MCP connector is currently disconnected. Reconnect it
  before the first use in a project, don't assume it's live.
- **License/cost:** Free tier gives 150 fast tokens/day plus a
  non-accumulating 150-token bank, free results are public and IP stays with
  Leonardo. Paid: Essential 12 USD/month (8500 tokens), Premium 30 USD/month
  (25000 tokens), Ultimate 60 USD/month (60000 tokens), annual billing saves
  up to 20 percent.
- **Install:** MCP tools are already wired in, no API key goes into any
  project file. If a raw API key is ever needed outside the MCP path, it
  stays in an environment variable or the system's credential store, never
  written into a skill file, commit, or artifact, only a placeholder like
  `<LEONARDO_API_KEY>` if a reference is ever needed in code.
- **Go here for:** the project's AI image generation, given it's already
  wired into this system and has a usable free tier, which Midjourney lacks.

**Alternatives, not wired into this system:** Midjourney has no free tier
(10 to 120 USD/month) but is often the most aesthetically convincing.
Ideogram has a usable free tier and cheap paid plans (7 to 48 USD/month),
strong at rendering text inside an image. Flux (Black Forest Labs) splits in
two: Flux.1 schnell is free under Apache 2.0, Flux.1 dev is free only for
non-commercial use, API pricing 0.003 to 0.05 USD per image, strongest at
photorealism.

**AI image vs. stock photo:** choose AI for a specific, non-existent subject
(exact brand colors, an invented creature, an impossible scenario) or when no
matching stock photo exists. Choose stock or a real photo whenever
authenticity and credibility matter, real people, real places, testimonials,
documentary intent, because AI images show artifacts on close inspection
(hands, embedded text, symmetry errors) and being recognized as AI-generated
costs trust. Legally, a purely AI-generated image is not copyrightable in
most jurisdictions including the US, commercial usage rights come from the
vendor's contract terms, not from copyright. The more practically relevant
risk than training-data questions is an identifiable real person without
consent, or an unintentionally reproduced brand or character in the output.

## Loading these in published Artifacts: CDN allowlist gotchas

Artifacts only allow external scripts from four hosts: `cdnjs.cloudflare.com`,
`cdn.jsdelivr.net/npm/`, `cdn.tailwindcss.com`, and `code.jquery.com`.
Everything else silently fails to load, with no visible error. Two specific
traps here have caused repeated failures and are worth stating explicitly:

- **Lucide is not on cdnjs** (404, verified). It lives on jsDelivr instead.
  Verified working path (HTTP 200, checked 2026-09):
  `https://cdn.jsdelivr.net/npm/lucide@1.43.0/dist/umd/lucide.min.js`. Pin
  the exact version, don't rely on a floating tag.
- **three.js on cdnjs has no UMD build from 0.185.1 onward**, only ESM,
  which fails in a plain `<script>` tag. Use the r128 UMD build instead,
  verified working (HTTP 200, checked 2026-09):
  `https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js`. This
  is an older revision on purpose, it's the last one with a working UMD file
  on cdnjs.

Both of these belong in [3d.md](3d.md)'s and any icon-loading pattern's
script tags whenever the target is a published Artifact rather than a normal
web build with a bundler, where the npm package works normally instead.

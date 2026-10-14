# Typography and typesetting

Font choice, pairing, scale, and setting. See [assets.md](assets.md) for
icons, stock, and AI image sources, this file covers type only. License
claims below come from
[recherche-bibliotheken.md](../planung/recherche-bibliotheken.md) section 6,
checked live in September 2026, don't extend the list without a checked
source.

## What makes a typographic choice read as generic

Inter, Roboto, and Open Sans are the default font of nearly every tool and
therefore of nearly every LLM-generated design, because they're the
pretrained shortcut. A page set entirely in one of these, at one weight, with
browser-default line-height and no deliberate scale, reads as templated even
if every other design decision is sound. The fix isn't "never use Inter", a
genuinely good product can use it well, the fix is a deliberate scale,
deliberate pairing, and deliberate spacing on top of whatever typeface is
chosen, plus considering one of the alternatives below when the brief calls
for more character.

## Pairing

Two typefaces, rarely three. A working pairing needs contrast in at least one
axis (serif/sans, geometric/humanist, wide/narrow) and restraint in the
others, two competing display faces on one page fight each other.

- **Grotesk headline + humanist sans body:** e.g. Space Grotesk or Schibsted
  Grotesk for headlines, DM Sans for body. Technical, contemporary, safe for
  SaaS and product UI.
- **Serif display + grotesk UI:** e.g. Fraunces for hero headlines, a grotesk
  (Schibsted Grotesk, DM Sans) for body and interface chrome. Warm,
  editorial, works for brand-forward marketing pages that want to avoid
  looking like a dev tool.
- **Buchtext serif for long-form + sans for UI chrome:** e.g. Crimson Pro or
  EB Garamond for article body copy, a grotesk for nav, labels, and buttons
  around it. For content-heavy, longform-reading pages, blogs, documentation,
  editorial.
- **Mono accent inside a sans system:** JetBrains Mono for code, technical
  labels, timestamps, or numeric data, layered into a grotesk or humanist
  system rather than replacing it. Signals precision, common in dev tools and
  data-dense dashboards, see [software.md](software.md) for the UI patterns
  this pairs with.
- **High-contrast display serif for oversized headlines only:** e.g. Tan
  Pearl (check the license at the specific foundry/source before use, see
  below), paired with a plain grotesk for everything else. For fashion,
  beauty, luxury positioning where the headline itself needs to carry drama.

Never pair two typefaces from the same genre at similar weight, e.g. two
different grotesks as headline and body, the difference reads as a mistake
rather than a choice.

## Type scale

Pick a ratio and stick to it rather than eyeballing sizes per component. A
modular scale (1.25 major third, 1.333 perfect fourth, or 1.5 for a bolder
jump) gives every heading level a size relationship that reads as intentional
instead of arbitrary.

- Body text: 16 to 18px baseline for marketing/editorial reading, 13 to 14px
  is defensible in dense software UI where scannability at volume beats
  comfort per [performance.md](performance.md)'s density guidance for
  professional tools (see also `software.md`'s dashboard density rules).
- Line-height: 1.5 to 1.6 for body paragraphs, tighter (1.1 to 1.25) for
  large display headlines where loose leading reads as accidental gaps.
- Don't skip scale levels arbitrarily inside one page, if H2 is 1.5rem and H3
  is 1.4rem, the hierarchy barely registers, use the ratio consistently or
  collapse levels you don't need.

## Letter spacing (tracking)

- Small caps and all-caps labels (nav items, eyebrow text, buttons) need
  positive tracking, roughly 0.02em to 0.08em, uppercase letterforms read as
  cramped at default spacing.
- Large display headlines, especially in a geometric or grotesk face, often
  read better with slightly negative tracking (-0.01em to -0.03em) at large
  sizes, tightening the visual gaps that widen as size increases.
- Body text at normal size: leave tracking at default. Adding letter-spacing
  to body paragraphs measurably hurts reading speed, reserve it for short
  strings only.

## Line length (measure)

Target 45 to 75 characters per line for body copy, 66 is the commonly cited
sweet spot. Below 45 the eye jumps lines too often, above 75 it loses the
start of the next line on the return sweep. In practice this means capping
body text columns with `max-width` in `ch` units (e.g. `max-width: 65ch`)
rather than letting a paragraph stretch to the full width of a wide container
or viewport.

## Variable fonts and load weight

- Prefer a variable font file over loading four or five static weight files
  separately, one variable file (e.g. `Inter-Variable.woff2`) covers the
  whole weight axis and often the whole family in one network request.
- Subset to the character set actually used (Latin only, unless the project
  needs Cyrillic/Greek/extended glyphs) to cut file size.
- Set `font-display: swap` (or `optional` for a non-critical accent face) so
  text renders in a fallback font immediately rather than staying invisible
  during load, then swaps once the webfont arrives.
- Self-host rather than pulling from Google's CDN when avoiding a third-party
  request matters (privacy, one less DNS lookup, resilience if the CDN is
  slow), all the OFL-licensed sources below permit this.
- Preload the primary body/heading font file (`<link rel="preload" as="font"
  type="font/woff2" crossorigin>`) so it doesn't wait behind other render-
  blocking requests, but don't preload every weight, that defeats the point.

## Free sources with license

- **Google Fonts** (https://fonts.google.com/): almost entirely SIL Open
  Font License, some Apache 2.0. Unrestricted commercial use, self-hosting
  allowed, no attribution required. Largest catalog, but its most-used faces
  (Inter, Roboto, Open Sans) are exactly the overused defaults this file
  argues against reaching for by default.
- **Fontshare** (https://www.fontshare.com/licenses/itf-ffl): ITF Free Font
  License. Commercial use explicitly permitted for client work, sold
  products, marketing, web, and apps. The only restriction is against
  reselling the font files themselves or redistributing them on another font
  platform. Around 100 families from Indian Type Foundry, free with no usage
  cap.
- **Velvetyne Type Foundry** (https://velvetyne.fr/about/faq): libre/open
  source, mostly OFL-like licenses with a copyleft character. Use,
  modification, and redistribution are allowed for private and commercial
  work, but designer and foundry attribution is required, and derivative
  works must redistribute under the same license. This copyleft clause is
  what distinguishes Velvetyne from plain OFL, check it per typeface before
  shipping a modified version.
- **Open Foundry** (https://open-foundry.com/about): a curation layer only,
  no hosting of its own, links out to Google Fonts, GitHub, and other
  sources. Most listed faces use OFL, but license must be verified per font
  individually since Open Foundry doesn't set the terms itself.

## Eight license-safe alternatives to Inter and Roboto

1. **Space Grotesk** (Google Fonts, OFL). Geometric, technically edged,
   character without being loud. Use for headlines, tech/startup branding.
2. **Schibsted Grotesk** (Google Fonts, OFL). More personality than Inter,
   originally built for media use. Use for headlines and UI.
3. **DM Sans** (Google Fonts, OFL). Softer curves, contemporary. Use for
   body copy, product UI.
4. **Fraunces** (Google Fonts, OFL). Warm editorial serif with an optical
   size axis. Use for display and editorial headlines.
5. **Tan Pearl** (available via Fontshare or other foundry sources, check the
   license at whichever specific source before use). High-contrast display
   serif. Use for large display headlines, fashion, beauty, luxury.
6. **Crimson Pro** (Google Fonts, OFL). Variable text serif, nine cuts. Use
   for body copy, longform reading.
7. **EB Garamond** (Google Fonts, OFL). Classic book serif with open forms,
   pairs well with modern groteskes. Use for editorial body copy.
8. **JetBrains Mono** (Google Fonts and Fontshare, OFL). Technical mono with
   character instead of a stock monospace. Use for code and technical UI
   accents.

For a genuinely distinctive display face beyond this list, search Velvetyne
directly, but check that specific typeface's attribution and copyleft terms
before committing it to a commercial project, they're stricter than plain
OFL and vary per family.

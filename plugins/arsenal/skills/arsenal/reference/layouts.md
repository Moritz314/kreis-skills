# Structural layout patterns

Concrete, named alternatives to the grid-of-equal-cards default, with real CSS. Reach for one of these when the *content itself* has a shape the default flattens: one hero item among several minor ones, a reading hierarchy with a clear lead story, two comparable things that want to be seen side by side, a stream of items with no natural end. If the content is genuinely homogeneous — a list of N similar products, N similar team members — a simple stack or an honest equal grid is correct and reaching for bento/asymmetric/marquee anyway is decoration, not structure. Picking a pattern is a content-modeling decision made before any CSS gets written.

## Asymmetric / broken grid

**What/why:** Named "broken grid" layout in editorial and portfolio design — elements deliberately overlap grid lines, offset from a uniform column rhythm, so the composition reads as designed tension rather than a spreadsheet. Fits a hero or case-study intro where one image and one text block need to feel hand-placed, not a repeating list.

```css
.broken-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  column-gap: clamp(1rem, 3vw, 2.5rem);
}

.broken-grid__image {
  grid-column: 1 / 8;
  grid-row: 1 / 3;
}

.broken-grid__text {
  grid-column: 6 / 13;
  grid-row: 2 / 4;
  /* overlaps the image's bottom two rows — the offset IS the layout */
  align-self: end;
  background: var(--surface);
  padding: clamp(1.5rem, 4vw, 3rem);
}

.broken-grid__eyebrow {
  grid-column: 1 / 5;
  grid-row: 1;
  align-self: start;
  /* a third element pinned off-axis from both, not centered on either */
}
```

**Avoid the slop version:** the tell is overlap with nothing at stake — a floating label offset by 8px for the sake of it. A real broken grid has exactly one deliberate collision point (image bleeds under text, or text bleeds over image edge) and every other element sits on the clean grid. Offsetting everything is just messy, not asymmetric.

## Bento grid

**What/why:** Named "bento grid" (bento-box compartments), popularized by Apple's product pages. Fits a feature showcase with one hero feature and several secondary ones — genuine size variation mapped to genuine importance, not a card grid relabeled with rounded corners.

```css
.bento {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  grid-auto-rows: 180px;
  gap: 1rem;
  grid-auto-flow: dense;
}

.bento__item {
  border-radius: 24px;
  overflow: hidden;
  position: relative;
}

.bento__item--hero   { grid-column: span 2; grid-row: span 2; }
.bento__item--wide   { grid-column: span 2; grid-row: span 1; }
.bento__item--tall   { grid-column: span 1; grid-row: span 2; }
/* everything else defaults to span 1 / span 1 */
```

Use `minmax(0, 1fr)` not bare `1fr` — a long unbroken string (URL, code, a number) in a narrow tile otherwise blows the track out. `grid-auto-flow: dense` backfills gaps but reorders DOM-to-visual position, which breaks keyboard/reader focus order — only use it when tab order genuinely doesn't matter, or set explicit `grid-column`/`grid-row` on every tile instead and skip `dense`.

**Avoid the slop version:** bento is itself a cliché now when every tile is identical-icon + heading + one line of body text at the same visual weight, just resized. What makes it read as bespoke: the hero tile carries a real screenshot, chart, or live data — not a repeated line icon — and tile size differences track a real importance ranking someone could defend, not a random Tetris pattern for visual interest.

## Editorial / magazine layout

**What/why:** Fits long-form content with a real reading hierarchy — a lead story, a pull quote, sidebar commentary, an image the text wraps around. Named after print magazine layout; the CSS tools are unequal grid columns, `column-span` for breakouts, and `shape-outside` for true text wrap (not a floated box with a hard rectangular edge).

```css
.article {
  display: grid;
  grid-template-columns: 1fr min(65ch, 100%) 1fr;
  column-gap: 1.5rem;
}

.article > * { grid-column: 2; }

/* pull quote breaks out of the text column into the margin */
.pull-quote {
  grid-column: 1 / 4;
  font-size: clamp(1.5rem, 4vw, 2.25rem);
  font-style: italic;
  line-height: 1.2;
  padding-block: 1rem;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

/* image with running text wrapped around its actual silhouette */
.article__figure--inline {
  float: left;
  width: min(40%, 320px);
  margin: 0 1.5rem 1rem 0;
  shape-outside: polygon(0 0, 100% 0, 100% 80%, 60% 100%, 0 100%);
  clip-path: polygon(0 0, 100% 0, 100% 80%, 60% 100%, 0 100%);
}
```

For a two-column news-style grid with span-based featured panels instead of a single article column:

```css
.magazine {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  grid-auto-flow: dense;
  gap: 1.5rem;
}

.magazine__featured { grid-column: span 2; grid-row: span 2; }
```

**Avoid the slop version:** the tell is a pull quote that just repeats a sentence already visible two lines above it, purely for visual texture. A real pull quote is an editorial choice — the single most quotable sentence, pulled forward as a scannable anchor for someone skimming, and the body copy actually varies in column width/weight instead of being one uniform gray block with a quote stamped on top.

## Split-screen layout

**What/why:** Two full-height panes, each carrying equal narrative weight — a comparison (before/after, two products, two audiences) or a hero with image on one side, message on the other. Fits exactly two things that want simultaneous attention, not three or four.

```css
.split-screen {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100dvh;
}

.split-screen__pane {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: clamp(2rem, 6vw, 6rem);
}

@media (max-width: 48rem) {
  .split-screen { grid-template-columns: 1fr; }
}
```

For a diagonal divider instead of a hard vertical line:

```css
.split-screen--diagonal .split-screen__pane:first-child {
  clip-path: polygon(0 0, 100% 0, 88% 100%, 0 100%);
  margin-right: -8vw; /* pull the second pane under the cut edge */
}
```

**Avoid the slop version:** a diagonal cut with no relationship to the content — same generic angle on every project — reads as a template. It earns its place when the two panes are genuinely comparable (not one hero image + one generic CTA pane), and the split ratio reflects actual content weight instead of a rote 50/50.

## Marquee (content, not just logos)

**What/why:** A horizontally scrolling strip for a genuinely long list of same-type items with no natural "page" — testimonials, press mentions, a product carousel someone browses passively. CSS-only, no JS marquee library. The technique: duplicate the content once, animate `translateX` by exactly -50%, so the loop seam is invisible.

```html
<div class="marquee">
  <div class="marquee__track">
    <div class="marquee__group">
      <!-- real content items -->
    </div>
    <div class="marquee__group" aria-hidden="true">
      <!-- exact duplicate, hidden from AT -->
    </div>
  </div>
</div>
```

```css
.marquee {
  overflow: hidden;
  mask-image: linear-gradient(90deg, transparent, black 5%, black 95%, transparent);
}

.marquee__track {
  display: flex;
  width: max-content;
  animation: marquee 30s linear infinite;
}

.marquee__group {
  display: flex;
  gap: 2rem;
  flex-shrink: 0;
}

@keyframes marquee {
  to { transform: translateX(-50%); }
}

.marquee:hover .marquee__track {
  animation-play-state: paused;
}

@media (prefers-reduced-motion: reduce) {
  .marquee__track { animation: none; }
}
```

The two `.marquee__group` children must be *identical* width for the -50% loop to seam cleanly — that's why the duplicate is `aria-hidden`, not a second real content set (screen readers must not announce the list twice). Full motion budget (mobile CPU cost, pause-on-hover as a requirement not a nicety) is in [performance.md](performance.md); the note here is the minimum to not ship a stuttering or duplicate-announced marquee.

**Avoid the slop version:** a marquee of testimonial cards that are all the same card component at the same size scrolling at a lifeless constant speed is the generic version. What makes it feel intentional: varying card width to actual quote length (not a fixed-width card truncating text), and a speed slow enough to actually read one item before it exits — a marquee people can't read is decoration, not content.

## Full-bleed alternating sections

**What/why:** A long page (landing page, product story) where sections alternate between a full-viewport-width band (image, color field, video) and a constrained-width text column, and left/right emphasis alternates section to section instead of every section pinning content to the same side. Fits scrollytelling / product-story pages more than dashboards.

```css
.content-column {
  width: min(65ch, 100% - 2rem);
  margin-inline: auto;
}

.full-bleed {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.story-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  min-height: 80vh;
}

/* alternate media/text sides without touching markup order */
.story-section:nth-of-type(even) {
  direction: rtl;
}
.story-section:nth-of-type(even) > * {
  direction: ltr; /* undo the flip for the content itself */
}
```

The `calc(50% - 50vw)` full-bleed trick escapes a centered max-width parent without needing `overflow-x` hacks or a separate top-level wrapper per section — it works as long as the parent has no horizontal scrollbar of its own (a stray wide child elsewhere on the page will break it, so pair it with `overflow-x: clip` on `body` as a guard).

**Avoid the slop version:** alternating purely for alternation's sake — image-left/text-right, then image-right/text-left, repeated mechanically down a page with no other variation — reads as a template scroll. It lands when section height, media treatment (some full-bleed photo, some a tight product shot, some a data visualization) and copy length actually differ section to section, so alternation is one axis of variety among several, not the only one.

## CSS Grid subgrid

**What/why:** Nested grid items inherit the parent grid's row/column track sizing, so children at different DOM depths align to the same lines — the classic case is a row of cards whose image/title/body/button need to line up horizontally across cards even though each card's internal content has different heights. Without subgrid this needs JS height-matching or fragile fixed heights.

```css
.card-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto auto 1fr auto; /* eyebrow / title / body / cta */
  gap: 1.5rem;
}

.card {
  display: grid;
  grid-row: span 4;
  grid-template-rows: subgrid;
  gap: inherit;
}

.card__title { grid-row: 2; }
.card__body  { grid-row: 3; }
.card__cta   { grid-row: 4; align-self: end; }
```

Every card's title now sits on the same line regardless of how long the eyebrow text above it ran, and every CTA sits flush at the bottom regardless of body copy length — the row, not each card, owns the rhythm.

**Support:** `subgrid` reached Baseline Widely Available in March 2026 (Chrome/Edge 117+, Firefox, Safari 16+) — safe to ship without a fallback or feature query in a current-baseline project. If the project must support an unusually old browser fleet, the fallback is the pre-subgrid pattern: fixed `min-height` per row role, or a JS height-matcher — not a silently broken layout.

**Avoid the slop version:** reaching for subgrid to align things that didn't need alignment (three unrelated widgets forced onto one invisible grid) adds complexity with no visible payoff. It earns its place specifically for repeated, structurally-identical children — a card row, a comparison table, a pricing grid — where cross-item alignment is the actual design requirement.

## Live lookup

- [every-layout.dev](https://every-layout.dev/) — Heydon Pickering & Andy Bell's algorithmic layout primitives (Stack, Cluster, Cover, Switcher, Reel); the compositional building blocks most of the above patterns are assembled from.
- [1linelayouts.com](https://1linelayouts.com/) — Una Kravets' modern one-line CSS Grid/Flexbox techniques (deconstructed pancake, RAM pattern, clamp-based sizing) with live CodePen demos.
- [superdesign.dev/styles/bento-grid](https://superdesign.dev/styles/bento-grid) — bento grid recipe with production examples pulled from Apple, Raycast, Amie and GitHub Copilot, plus explicit guidance on when *not* to use bento.
- [css-tricks.com — responsive grid magazine layout](https://css-tricks.com/responsive-grid-magazine-layout-in-just-20-lines-of-css/) — minimal `auto-fit`/`minmax()` + `grid-auto-flow: dense` technique for magazine-style featured panels.
- [awwwards.com/websites/grid](https://www.awwwards.com/websites/grid/) — award-nominated sites tagged for grid-driven layout; browse for structural inspiration, not for code.

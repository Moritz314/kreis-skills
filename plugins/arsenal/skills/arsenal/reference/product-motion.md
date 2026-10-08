# Product-surface motion

Motion for product and utility surfaces: controls that morph, bars that expand and collapse, shells that slide in, status color that carries meaning, and the two effects (goo filter, overshoot) that are usually wrong and occasionally right. This is the file [software.md](software.md) points to for the *how*.

Boundaries, so nothing here gets re-litigated per section:

- **Curves and durations come from [motion-doctrine.md](motion-doctrine.md)**, which holds the sourced token sets. Every number below is an example. Map it to the project token set before use.
- **[motion.md](motion.md) is the brand-register file** (scroll choreography, text splitting, magnetic cursors, view transitions). Most of what lives there is explicitly ruled out for product surfaces. Do not read its ruling as "no motion here", read it as "the techniques in that file are not the ones you want here". The ones you want are in this file.
- **The reduced-motion and contrast rules from [performance.md](performance.md) apply to every pattern below**, without exception and without restating them per section.
- Every pattern here obeys the layout rule: **overlay, never displace.** Nothing in this file animates a layout property.

Each section is written as Rule, Why, When not, Measurement point, Pattern.

---

## 1. Morphing a small control: dot to pill

**Rule.** A compact control that grows into a labelled pill on hover, focus or activation is built from two stacked layers. A background layer is revealed by animating `clip-path: inset(... round 999px)`, and the label sits in its own separate layer that is never inside a filtered or clipped subtree. The open width is measured from the real rendered label after `document.fonts.ready` and written to a custom property. The grown state overlays its neighbours; the collapsed footprint is what the layout reserves.

The reference for the interaction is the Apple traffic-light button group: three small dots that gain their glyphs and their pill shape on hover without anything else on the window chrome moving.

**Why.** Three reasons, in order of how often they are ignored:

1. **`scaleX` on a capsule is not an option.** A capsule has round ends. Scaling it horizontally turns those circular ends into ellipses, and the whole shape reads as a stretched sticker. `clip-path` with a `round 999px` corner term keeps the radius constant in device pixels while the revealed area changes, which is what the eye expects from a shape that is growing rather than being stretched. The same argument rules out `scaleX` on any rounded rectangle whose radius is a meaningful part of its identity.
2. **Animating `width` is a layout animation.** It reflows and repaints every frame and it moves the neighbours. Revealing a fixed-size element instead keeps geometry constant.
3. **The label must not be scaled, clipped or filtered.** Text inside a transformed or filtered subtree loses subpixel rendering and reads as blurred at exactly the moment the user is trying to read it. Keeping the label in its own layer, animated only with `opacity`, is the whole reason the layer split exists.
4. **The revealed area is paint work, not compositor work.** `clip-path` with a rounded corner term repaints the clipped region on the CPU every frame it changes (measured 41 to 45 paint events per pill, 0 for a plain `inset()` without `round`, see [performance.md](performance.md)'s budget table). Keep the painted area small, a single control rather than a full-width band, and cap how many pills can be mid-morph at once; measure against an idle run per section 7.

**Precedence on duration tier.** [motion-doctrine.md](motion-doctrine.md) section 3 assigns hover feedback to the fast tier (Carbon fast-01/fast-02, Material short1 to short3, 70 to 150 ms). The pill morph above is not hover feedback, it is the one-time build-up of an overlay per section 6's exception: nothing is being confirmed or reported, a control is changing its own shape. Where the two appear to conflict, this distinction governs: hover feedback (a color or elevation change signalling "you are over this") stays on the fast tier without exception; an overlay build-up triggered by hover (this pill, the bars in section 2) may use the moderate tier (Carbon moderate-01/02, Material medium, roughly 150 to 280 ms), because it is judged as a build-up, not as feedback. Do not extend this exception to a plain hover color or shadow change, that stays fast.

**When not.** When the element genuinely changes its place in the layout (a card growing into a detail view, a list item expanding in flow), a clip reveal is a lie: everything below it should move, and the honest technique is FLIP. Measure the first and last geometry, apply the inverse transform, then play it out with `transform` only. Also do not use this pattern when the collapsed state carries no meaning of its own; a control that is unreadable until hovered is a discoverability problem that motion cannot fix, and it fails on touch, where there is no hover at all.

**Neighbours make way, they are not covered.** When more than one instance sits in a row (a strip of dot-to-pill controls), the growing pill's neighbours make way by translating aside with `transform`, by the pill's extra width, or receive `inert` if a neighbour would otherwise end up fully under the grown pill and lose its hit area entirely. The grown layer itself accepts pointer events (`pointer-events: auto`), it never passes clicks through to whatever it is drawn over: whatever control was reachable under the pointer before the morph stays reachable after it.

**Touch fallback.** There is no hover on touch, so the collapsed dot cannot rely on it. Render the collapsed state as a filled circle 28 to 32px across with a small symbol, not a bare dot, so the control reads as tappable rather than decorative. The tap target is 44 by 44px minimum (a transparent padding box around the visible circle, not the circle itself grown), per WCAG 2.5.8 the target itself and any other target within 24px of it must not overlap. The label that a hover reveal shows sighted mouse users reaches a touch or screen-reader user as `aria-label` on the control instead, it is never only conveyed by the opened pill. Where the morph sits next to a title or heading (not just another dot), the title keeps at least half the header's width even at the control's fully grown state, the grown pill overlays free space and its own neighbours per the paragraph above, it does not eat into the title's reserved share.

**Pointer-events timing.** The grown layer's `pointer-events: auto` (set in the paragraph above) only takes effect once the opening transition actually finishes; transfer it in the `transitionend` handler, not synchronously on open, so a fast pointer pass mid-animation cannot click through a shape that only visually, not yet geometrically, covers the target. Closing on touch happens on a `pointerdown` outside the grown control, matching the bar pattern in section 2, not on a second tap of the control itself, which would read as an accidental re-open.

**Measurement point.** `elementFromPoint()` at a fixed point along the pill's path returns the same logical control before, during and after the morph, confirming nothing under the grown shield became unreachable. Layout shift contribution is 0 (a neighbour's move is a `transform`, not a reflow). No main-thread task over 16 ms during the morph, measured against an idle run per section 7. The collapsed touch target measures at least 44 by 44px in devtools' box model, and the control's accessible name (via `aria-label` or the visible label once open) is non-empty at every state.

**Pattern.**

```html
<span class="ctl" data-open="false">
  <span class="ctl__ground" aria-hidden="true"></span>
  <span class="ctl__label">Publish</span>
</span>
```

```css
.ctl {
  position: relative;
  display: inline-block;
  inline-size: var(--ctl-dot, 1.5rem);   /* the footprint the layout reserves */
  block-size: var(--ctl-dot, 1.5rem);
}
.ctl__ground {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: var(--ctl-open, 1.5rem);  /* set from JS after fonts are ready */
  background: var(--role-confirm-surface);
  border-radius: 999px;
  clip-path: inset(0 calc(var(--ctl-open) - var(--ctl-dot)) 0 0 round 999px);
  transition: clip-path var(--dur-moderate) var(--ease-standard);
}
.ctl[data-open="true"] .ctl__ground { clip-path: inset(0 0 0 0 round 999px); }

.ctl__label {                            /* own layer: no filter, no clip, no scale */
  position: relative;
  opacity: 0;
  transition: opacity var(--dur-fast) linear;
}
.ctl[data-open="true"] .ctl__label { opacity: 1; }
```

```js
// The open width is a measurement, never a guess: a webfont swap changes it.
await document.fonts.ready
const label = ctl.querySelector('.ctl__label')
const w = Math.ceil(label.getBoundingClientRect().width) + PAD_INLINE * 2
ctl.style.setProperty('--ctl-open', `${w}px`)
// Re-measure on a locale change or a dynamic label change, not on every resize.
```

```js
// Neighbours make way instead of being covered; the grown layer stays interactive.
function makeWay(ctl, open) {
  const shift = open ? w - dotWidth : 0
  ctl.querySelectorAll('.ctl-neighbour').forEach((n) => { n.style.transform = `translateX(${shift}px)` })
  ctl.querySelector('.ctl__ground').style.pointerEvents = 'auto'
}
```

---

## 2. Expanding and collapsing bars

**Rule.** A minimized filter bar, command bar or send bar keeps its slot at a fixed height. The visible ground grows as an overlay, driven by `clip-path: inset()` alone on the ground layer, which carries the border radius; the content inside appears with `opacity` alone and never scales. Do not add a `scaleY` (or any) transform to that same ground layer: `clip-path` is evaluated in the element's untransformed local coordinates and a transform then scales the already-clipped result, so a `scaleY(bar-min / bar-max)` on top of a clip already sized to `bar-min` leaves the closed state at `bar-min² / bar-max` tall, not `bar-min`, and it also squashes the radius into an ellipse exactly as ruled out for `scaleX` in section 1. If a surface genuinely wants a squeeze effect on top of the reveal, put that transform on a separate, radius-less inner layer, never on the layer that also carries `border-radius` and `clip-path`. Opening runs on a 120 ms hover-intent delay that a `pointerout` before it fires cancels; a click or `Tab`-focus opens immediately, with no delay. `pointerover` only starts the intent timer for `pointerType` `mouse` or `pen`, touch never opens a bar by hover, since there is no hover on touch: a tap (`pointerup` with `pointerType: 'touch'`) opens it directly. Closing runs on a 400 ms delay that any new `pointerover` cancels. Focus inside the bar, or a non-empty input, blocks closing entirely. `Tab` into the bar opens it, `Escape` closes it and returns focus to a named target, never to an assumed opener that may not exist, touch opens on tap. If the input holds unsent draft text when the bar is minimized, the minimized layer shows a visible sign of it (a dot, a truncated first line), not just a refusal to close.

**Why.** A bar that changes the height of its slot pushes the content below it every time the pointer passes, which is the most common cause of a surface feeling twitchy. Fixing the slot height and letting the ground overlay downward (or upward) removes the reflow entirely. The open delay exists for the same reason as the close delay: a bar that opens the instant the pointer arrives fires on every diagonal mouse path that merely crosses it on the way elsewhere; 120 ms is short enough that a deliberate hover still feels immediate and long enough to filter a pass-through. The `pointerType` check exists because `pointerover` fires for touch too, right before the click; without the check, a tap would open the bar via the hover path and then immediately re-trigger it via the tap path. The close delay exists because a bar that closes the instant the pointer leaves flickers on every diagonal mouse path across it; 400 ms is long enough to cover a normal overshoot and short enough that a deliberate exit still feels immediate. The focus and input locks exist because closing a bar out from under a keyboard user, or discarding half-typed text, is a data-loss bug wearing an animation costume. The named Escape target exists because a bar opened by hover or by `Tab` reaching it in DOM order has no click opener to return focus to; assuming one and calling `.focus()` on it throws on `undefined`, which is exactly the bug this rule closes.

**When not.** Do not use this when the expanded content is tall enough to cover the thing the user is working on: past roughly a third of the viewport height, an overlay bar becomes a modal in disguise and should be built as the side sheet in section 3, with the focus contract that comes with it. Do not use hover as the only opener on a touch-primary surface. And do not stack it with a second hover-opened overlay in the same corner, since the two close timers will fight.

**Measurement point.** With the bar cycling open and closed, the `y` coordinate of the first element below the bar never changes. Cumulative layout shift stays 0. In the closed state, `bar__ground.getBoundingClientRect().height` equals `bar-min` exactly, not `bar-min² / bar-max`, confirming no transform is stacked on top of the clip. A pointer sweep that crosses the bar and leaves within 120 ms never produces a `data-open` change (the intent timer never fired). The close timer is cancelled on every `pointerover`, verified by opening the bar, sweeping the pointer out and back within 400 ms, and confirming it never begins to close. On `Escape`, focus lands on a named target (the element that opened the bar, or, if it was opened by hover or `Tab` reaching it, the next focusable element after the bar), never a thrown error from calling `.focus()` on `undefined`.

**Pattern.**

```css
.bar { position: relative; block-size: var(--bar-min); }  /* slot never changes */
.bar__ground {
  position: absolute; inset-inline: 0; inset-block-start: 0;
  block-size: var(--bar-max);          /* full height, overlays what is below */
  background: var(--surface-raised);
  border-radius: var(--radius-m);
  clip-path: inset(0 0 calc(var(--bar-max) - var(--bar-min)) 0 round var(--radius-m));
  transition: clip-path var(--dur-moderate) var(--ease-standard);
}
.bar[data-open="true"] .bar__ground {
  clip-path: inset(0 round var(--radius-m));
}
.bar__content { position: relative; opacity: 0; transition: opacity var(--dur-fast) linear; }
.bar[data-open="true"] .bar__content { opacity: 1; }
```

```js
const OPEN_DELAY = 120
const CLOSE_DELAY = 400
let openTimer = null
let closeTimer = null
let lastOpener = null   // set by a click/tap or Tab focus; stays null when opened by hover

const open  = (trigger = null) => { clearTimeout(closeTimer); if (trigger) lastOpener = trigger; bar.dataset.open = 'true' }
const close = () => { if (isLocked()) return; bar.dataset.open = 'false'; lastOpener = null }
const isLocked = () => bar.contains(document.activeElement) || input.value.trim() !== ''

bar.addEventListener('pointerover', (e) => {
  if (e.pointerType !== 'mouse' && e.pointerType !== 'pen') return   // touch never hover-opens
  clearTimeout(closeTimer)
  openTimer = setTimeout(() => open(), OPEN_DELAY)
})
bar.addEventListener('pointerout', () => clearTimeout(openTimer))   // leaving before intent fires cancels it
bar.addEventListener('pointerleave', () => {
  clearTimeout(closeTimer)
  closeTimer = setTimeout(close, CLOSE_DELAY)
})
ground.addEventListener('pointerup', (e) => {
  if (e.pointerType === 'touch') open(ground)      // tap opens immediately, no hover path exists on touch
})
bar.addEventListener('focusin', (e) => open(e.target))   // Tab in opens immediately, no intent delay
bar.addEventListener('focusout', () => {                 // leaving by keyboard closes
  if (!bar.contains(document.relatedTarget)) close()
})
bar.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape') return
  bar.dataset.open = 'false'
  ;(lastOpener ?? bar.nextElementSibling)?.focus()   // named target, never .focus() on an assumed opener
})
```

---

## 3. Three shell patterns: side sheet, master-detail, rail

**Rule.** A product shell that shows secondary content next to primary content is one of exactly three named patterns. Name it before building it, because the focus contract differs per pattern and cannot be retrofitted.

| Pattern | What it is | Focus contract |
|---|---|---|
| **Side sheet** | A panel that slides in over the surface, primary content stays visible behind it | Two variants, name which one before building: **modal** (`aria-modal="true"`, `role="dialog"`, the rest of the page gets `inert`, focus is genuinely trapped in the sheet) for a sheet that blocks the primary task; **non-modal** (no `aria-modal`, no `inert`, no trap, `Tab` can leave the sheet into the surface behind it, which stays operable) for a sheet the user consults while still working in the surface. A markup that traps focus without `aria-modal` fails ARIA, a trap the accessibility tree never announced as modal. In both variants: `Escape` closes, a click on the surface outside closes the modal variant, and on close focus returns to the element that opened it. |
| **Master-detail** | A persistent list beside a detail pane; selecting a list item swaps the detail content | No trap, both panes are reachable by `Tab` in DOM order. Selecting a new item swaps the detail content **without closing anything**, and moves focus to the detail heading (`tabindex="-1"`, then `focus()`), not back to the top of the page. `Escape` in the detail returns focus to the selected list item. |
| **Rail** | A narrow persistent strip of icon-level navigation or tools at the edge, optionally expanding to labels | No trap, never steals focus. Expanding to labels is the section 1 morph, applied per item. `Escape` collapses an expanded rail without moving focus. |

**Overlay, never displace, in all three.** The sheet draws above the surface with `transform: translateX()`, it does not squeeze the main column. The detail pane in a master-detail shell has a fixed track width per breakpoint, so swapping content never resizes the list. The rail reserves its collapsed width in the layout and its expanded state overlays.

**Why.** Squeezing the main column means animating its width, which is a layout animation: reflow and repaint every frame, text re-wrapping mid-motion, and every measurement the page took becoming stale. It is also the pattern most likely to move the exact thing the user was reading. Overlaying costs one composited transform and moves nothing. The focus contracts differ because the patterns differ in kind: a sheet is modal in intent even when it is not modal in markup, a master-detail is two peer regions, a rail is chrome.

**When not.** Do not use a side sheet where the user must compare the sheet content against the surface behind it; that is a master-detail. Do not use master-detail below 720px; there is no room for two tracks, and the honest mobile form is a full-screen detail view with a back affordance. Do not add a rail purely to have somewhere to put icons.

**Width steps.** Below **720px**: one column, sheets go full width, master-detail collapses to list-then-detail navigation, the rail becomes a bottom bar or a menu. **720px to 1024px**: side sheet as an overlay at a fixed width, master-detail only if the detail pane is genuinely narrow, rail collapsed to icons. **1024px and up**: all three at full form, rail may expand to labels. These two numbers are the only breakpoints this file names; a project may add more, but not fewer.

**Measurement point.** With the pattern open, `document.activeElement` matches the contract in the table above at every step: after open, after a `Tab` cycle, after `Escape`, and after an outside click. For the modal variant, a full `Tab` cycle never lands outside the sheet, because the rest of the page is `inert`. For the non-modal variant, `Tab` from the sheet's last focusable element lands on the next focusable element in the surface behind it, in DOM order, not back at the top of the page. The main column's `getBoundingClientRect().width` is unchanged between the closed and open state. No layout property appears in any transition on the shell.

```js
// Side sheet, the parts that are actually a contract.
let opener = null

function openSheet(trigger, { modal = true } = {}) {
  opener = trigger
  sheet.hidden = false
  if (modal) {
    sheet.setAttribute('aria-modal', 'true')
    sheet.setAttribute('role', 'dialog')
    for (const el of document.querySelectorAll('body > :not(#sheet-root)')) el.inert = true
  }
  sheet.querySelector('[autofocus], button, [href], input, select, textarea')?.focus()
}
function closeSheet() {
  const wasModal = sheet.getAttribute('aria-modal') === 'true'
  sheet.hidden = true
  sheet.removeAttribute('aria-modal')
  if (wasModal) for (const el of document.querySelectorAll('[inert]')) el.inert = false
  opener?.focus()                     // return, never drop focus to <body>
}
sheet.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeSheet() })
scrim?.addEventListener('pointerdown', closeSheet)   // only the modal variant renders a scrim to click
```

---

## 4. Meaning-bearing color: three to five roles

**Rule.** A product surface with real status needs a small, named set of semantic color roles, not one accent. Three to five roles, no more:

| Role | Carries |
|---|---|
| Input and confirmation | the primary action, a confirmed value, a saved state |
| Options | selectable alternatives, filters, choices not yet taken |
| Notices | warnings and things that need attention but are not failures |
| Cancel and close | destructive, dismissive and undoing actions |
| Automation | anything the system did on its own, without the user asking |
| Neutral gray | the past: completed, expired, archived, no longer actionable |

Each role gets exactly **three steps**, defined in OKLCH so the lightness axis is perceptually even:

- **Surface**: a low-chroma fill for backgrounds of chips, rows and banners.
- **Line**: a mid-chroma value for borders, dividers and icon strokes on that surface.
- **Solid**: the full-strength value for a filled button, a dot, a bar.

**Hard thresholds.** Text on a role surface reaches **4.5:1** against that surface, checked per role and per theme, not assumed from the neutral palette. And no role may be the only carrier of its meaning: every status also says a word or shows a shape, per [design-foundations.md](design-foundations.md)'s no-meaning-by-color-alone rule (WCAG 1.4.1). The grayscale test is the check: convert the screen to grayscale and confirm every distinction still reads.

**Why.** A surface that shows state needs the viewer to sort it at a glance, and hue is the fastest sorting channel available. Three steps per role rather than a full ramp keeps the set memorable and keeps a component from inventing an intermediate value; the argument is the same token-discipline argument motion-doctrine.md makes for durations. OKLCH matters here specifically because these roles get compared against each other: in sRGB hex, two colors with the same nominal lightness read as visibly different weights, and a status row looks arbitrarily emphasized.

**The yellow exception.** Yellow does not survive the three-step treatment unchanged. A yellow dark enough to carry white text reads as brown or olive, not as yellow, so the meaning is lost exactly when it is made accessible. Give the notice role a separate dot and chip tone: a bright, high-chroma yellow with **dark text on it**, rather than a darkened yellow with light text. This is the only role in the set that inverts its text polarity, and that is a deliberate, documented exception rather than an oversight.

**Boundary against [presets.md](presets.md).** presets.md's "one restrained accent reserved for links and CTAs only" is a **marketing-surface** rule, and it is correct there: a reading page has no status to encode and every extra hue costs it calm. It does not govern a product surface that must distinguish confirmation from cancellation from automation. When a project runs both (a marketing site and an app behind it), they run two palettes: one accent out front, the role set inside. Say so in MASK.md rather than letting one leak into the other.

**When not.** Do not build the role set on a surface that has no status: a content page, a form with one action, a documentation site. Five roles on a surface with nothing to distinguish is noise pretending to be a system.

**Measurement point.** Every role surface and its text pass 4.5:1 in both themes, measured, not eyeballed. The grayscale screenshot still distinguishes every status. No component uses a color value outside the role set.

```css
:root {
  /* Confirmation role, three steps. Hues and chroma are examples. */
  --role-confirm-surface: oklch(0.96 0.03 150);
  --role-confirm-line:    oklch(0.72 0.11 150);
  --role-confirm-solid:   oklch(0.55 0.16 150);
  /* Notice role: the yellow exception, dark text on a bright chip. */
  --role-notice-solid:    oklch(0.86 0.17 95);
  --role-notice-on-solid: oklch(0.25 0.03 95);
}
```

---

## 5. The SVG goo filter

**Rule.** The gooey/metaball effect is a `feGaussianBlur` followed by an `feColorMatrix` that re-hardens the alpha edge. Use it only on the shape layer, and only where two or more moving shapes actually meet. **Text must never be inside the filtered subtree**: the same blur that fuses the shapes destroys the glyphs. Put the label in a sibling layer above the filtered group, exactly as in section 1.

**Why it sometimes earns its place.** When two round shapes approach each other, the goo filter makes them bulge and merge like drops of liquid rather than sliding over one another. That merge is a genuine perceptual cue: it tells the eye the two things are becoming one thing. On a control that splits into options, or a set of dots that collapses into a bar, it makes the relationship legible in a way a cross-fade does not.

**Cost, stated plainly.** An SVG filter is not composited. The filtered subtree is re-rasterized on the CPU every frame it changes, which is the most expensive category in [performance.md](performance.md)'s budget table. It scales with the filtered area, so a full-width goo layer is a different proposition from a 48px one. Budget it as an animated SVG filter, not as a CSS effect.

**When not.** No goo when the filtered area is large, when the surface is dense or high-frequency, when the shapes never actually touch (there is nothing to merge and the cost buys a slight blur), or when the project's `bewegung` dial is 0 or 1. Under `prefers-reduced-motion: reduce`, drop the filter entirely and cross-fade between the start and end shapes; the merge is decoration, not information. Re-check contrast with the filter on, because the alpha re-hardening changes edge color against the background.

```html
<svg width="0" height="0" aria-hidden="true">
  <filter id="goo">
    <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur"/>
    <feColorMatrix in="blur" type="matrix"
      values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="goo"/>
    <feBlend in="SourceGraphic" in2="goo"/>
  </filter>
</svg>
```

```css
.goo-shapes { filter: url(#goo); }        /* shapes only */
.goo-label  { position: relative; }        /* sibling, never a child */
@media (prefers-reduced-motion: reduce) { .goo-shapes { filter: none; } }
```

---

## 6. Overshoot: where it survives

**Rule.** Overshoot is excluded by default on a product surface, per [motion-doctrine.md](motion-doctrine.md) section 4. It survives in exactly one place: the **one-time build-up of an overlay that displaces nothing**, with a calm return path that has no overshoot at all.

All of these must hold at once:

- The moving element is drawn above the layout, so no neighbour moves because of it.
- The motion happens on appearance, once, not on every state change.
- The way back is a plain decelerating curve. Overshoot on both directions reads as a wobble.
- The element is not carrying feedback that has to be read precisely.

**Excluded, without exception.** State changes (toggles, checkboxes, selection), form and validation feedback, error and success messaging, loading and progress, navigation, and anything that repeats often. An overshoot set as a design-system default contradicts both Carbon and Material 3, which is the argument motion-doctrine.md section 4 already makes; this section only names the narrow case where it does not apply.

**Why the exception holds.** A direction reversal carries extra visual information that costs reading time. On a repeated microinteraction that cost is paid over and over for nothing. On a single appearance of an overlay that nothing else is competing with, it is paid once and buys a sense of physical arrival.

**One token, not one instance.** Per [motion-doctrine.md](motion-doctrine.md) section 4, the exception binds to the overlay-build-up *pattern*, not to a single spot in the project: a pill, a bar and a dot group may all use it, and a control that overshoots on every hover is still "once per appearance", not "once ever". What has to stay singular is the curve itself, one overshoot token, reused everywhere the pattern applies. A repeated, deliberate customer-signature moment (something that overshoots on every hover by design) is this exception at scale and carries its own measurable ceiling: label offset under 1px, squash under 10 percent, moving area under 3 percent of the viewport, per occurrence.

**Measurement point.** Every overshoot transition in the project uses the same token (one curve, `cubic-bezier` or `linear()`, defined once), on an element that is `position: absolute` or `fixed`, and its reverse transition uses a non-overshooting curve. Grep the stylesheet: a second, *different* overshoot curve is a finding; a second or third element referencing the same token is not. For a repeated customer-signature use of the token, additionally check the three ceilings above per occurrence.

```css
.overlay { transition: transform var(--dur-moderate) var(--ease-standard); }  /* leaving: calm */
.overlay[data-entering="true"] {
  animation: arrive var(--dur-moderate) cubic-bezier(0.34, 1.4, 0.64, 1) both;
}
@keyframes arrive { from { transform: scale(0.96) } to { transform: none } }

/* Spring-equivalent without a JS spring model: a linear() easing curve sampled
   from a critically-light spring, for a browser that supports it (Chrome/Edge 113+,
   Firefox 112+, Safari 16.4+; provide the cubic-bezier version above as the fallback,
   linear() is additive progressive enhancement, never the only definition). */
.overlay[data-entering="true"].spring-token {
  animation: arrive var(--dur-moderate) linear(
    0, 0.42 10.4%, 0.83 22.1%, 1.05 32.6%, 1.14 40.5%,
    1.08 52.1%, 1.02 63.4%, 0.99 76.7%, 1 100%
  ) both;
}
```

---

## 7. Measuring CSS-only motion

**Rule.** For motion built purely in CSS, the budget is: **no main-thread task longer than 16 ms while the animation runs**, and the number only counts when it is reported next to an idle control run of the same page.

**Why the control run is mandatory.** A headless renderer drops frames on its own. On an idle page, **20 to 25 percent of `requestAnimationFrame` intervals exceeded 16.7 ms** in Puppeteer, Playwright or CI Chrome, because no display refresh is driving the loop. That range is a single measurement, not a constant: measured once on 2026-09-09 on the Windows workstation during the <internal-project> customer-file mockup (headless Chromium via Playwright); re-measure per machine before relying on it. A raw frame count or a raw dropped-frame percentage from such an environment therefore proves nothing about the animation, in either direction: it will condemn a clean animation and it will absolve a bad one. Only the delta between the animated run and the idle run is evidence.

**When not.** This rule is about CSS and main-thread work. It does not cover WebGL or canvas, where the relevant budget is GPU time and the checks in [performance.md](performance.md) apply instead.

**Measurement point.** Two long-task recordings, idle and animated, on the same machine in the same session, reported together. A single number without its control run is treated as an unmeasured claim by the build's performance gate. This rule is duplicated in [performance.md](performance.md) so the gate can find it without loading this file.

```js
const tasks = []
new PerformanceObserver((l) => tasks.push(...l.getEntries().map((e) => e.duration)))
  .observe({ entryTypes: ['longtask'] })
// Report for both runs: tasks.filter((d) => d > 16).length and Math.max(...tasks)
```

---

## 8. Reduced motion for micro-interactions

**Rule.** `prefers-reduced-motion: reduce` is not one global block placed over every transition, see [motion-doctrine.md](motion-doctrine.md) section 5 for why the blanket selector is a named failure mode. Each pattern in this file defines its own complete reduced state instead: the dot-to-pill morph (section 1), the expanding bar (section 2) and the side sheet (section 3) each ship a `[data-open]` end state that applies instantly, with no intermediate frame. An opacity fade under 120 ms may still run (the label fading in on the pill, the bar content fading in), because a short fade carries no vestibular risk; `clip-path` travel, `transform` travel and any overshoot curve are removed, the element simply appears or disappears at its final geometry. The preference is read with `matchMedia('(prefers-reduced-motion: reduce)')` and a `change` listener, never a one-time `.matches` read at load, because the OS setting can change while the page stays open. Any Web Animations API animation already in flight when the preference flips is cancelled (`animation.cancel()`) and the element is set to its end state in the same handler, not left to finish the motion it was already playing.

**Why.** A user who turns reduced motion on mid-session, or opens the page with it already on, gets the same complete design either way. motion-doctrine.md section 5 already rules out stripping every transition wholesale, because that also kills focus rings and the opacity feedback that carries no vestibular risk; the failure this section fixes is narrower than that blanket-selector mistake. Even a correctly scoped `prefers-reduced-motion` CSS rule written once at load time misses a mid-session toggle, and a `clip-path` or `transform` animation driven by the Web Animations API, not a CSS transition, ignores a CSS `@media` override entirely, so JS has to check the preference and act on it directly.

**When not.** Do not build one reduced-motion handler shared indiscriminately across every pattern in this file; the pill, the bar and the sheet have different end states and different in-flight animations to cancel, a shared handler either does too little (misses one pattern's running WAAPI animation) or too much (an `animation: none !important` that also mutes the label's legitimate opacity fade). Do not skip the `change` listener because most visits are short: the setting is commonly flipped from an OS control panel the user opens specifically because a page just bothered them.

**Measurement point.** After toggling the OS setting while a pattern is mid-animation, `document.getAnimations()` on the affected element returns none still running, confirming any in-flight WAAPI animation was cancelled, and the element's computed geometry matches its final, non-reduced-motion end state within one frame. Toggling the setting back off does not require a reload: the `change` listener re-applies the current pattern state under the new preference immediately.

**Pattern.**

```js
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)')

function applyMotionPreference(reduced) {
  document.querySelectorAll('.ctl, .bar, .sheet').forEach((el) => {
    el.getAnimations().forEach((a) => a.cancel())    // drop any in-flight WAAPI animation
    el.classList.toggle('motion-reduced', reduced)   // CSS end-state below: no travel, no overshoot
  })
}

applyMotionPreference(reduceMotion.matches)                                      // read once at load...
reduceMotion.addEventListener('change', (e) => applyMotionPreference(e.matches)) // ...and again on every toggle
```

```css
.motion-reduced.ctl .ctl__ground { transition: none; }          /* clip-path jumps straight to its end state */
.motion-reduced.ctl .ctl__label { transition-duration: 80ms; }  /* an opacity fade under 120ms may stay */
.motion-reduced.bar .bar__ground { transition: none; }
.motion-reduced .overlay[data-entering="true"] { animation: none; transform: none; }  /* no overshoot, no travel */
```

---

## Checklist

- [ ] No pattern on the surface animates a layout property. Every morph, bar and shell overlays.
- [ ] Every label sits outside every clipped, scaled or filtered subtree.
- [ ] Any measured width comes from a measurement taken after `document.fonts.ready`.
- [ ] Every expanding bar keeps its slot height fixed, cancels its close timer on `pointerover`, and refuses to close while focused or while its input holds text.
- [ ] Each shell is named as side sheet, master-detail or rail, and meets that row's focus contract, verified by keyboard.
- [ ] Color roles number between three and five, each with surface, line and solid, text on surface at 4.5:1, and every status carries a word or a shape as well.
- [ ] The notice role uses the bright chip with dark text, not a darkened yellow.
- [ ] A goo filter, if present, contains no text, covers a small area, and is dropped under reduced motion.
- [ ] At most one overshoot token exists in the project (reused across every overlay-build-up occurrence, including a repeated customer-signature moment), each occurrence has a calm return, and a repeated occurrence stays under the label-offset/squash/area ceiling in section 6.
- [ ] Every motion budget claim is reported with its idle control run.
- [ ] `prefers-reduced-motion` is read with a `change` listener, not only at load, and cancels any in-flight WAAPI animation on toggle (section 8).

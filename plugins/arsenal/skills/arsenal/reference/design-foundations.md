# Design foundations: grid, type, color, perception

Rules translated from academic design theory into checks a model can apply
while designing and re-verify against a finished design. Source and full
citation list: [../planung/recherche-gestaltung.md](../planung/recherche-gestaltung.md).
Every rule below carries its source in parens. Items the source flagged as
unproven are marked "unproven" and are background, never a binding check.

Register dials (`auftreten`, `bewegung`, `dichte`, `technik`, `tonfall`) are
defined in [registers.md](registers.md). Where a rule's target number shifts
with a dial position, that is stated inline. No new dial or stop is invented
here.

## 1. Grid and composition

- Pick a fixed column grid (commonly 8 to 16 columns) before placing any
  block. Every text and image block starts and ends on a column line, not a
  freehand offset. (Müller-Brockmann 1981)
- Pick one baseline unit (4px or 8px). Every vertical spacing value, line
  spacing, paragraph gap, section gap, is an integer multiple of it. At
  `dichte: verdichtet` use the smaller unit (4px) and tight multiples; at
  `dichte: luftig` use the larger unit (8px) or more with generous multiples;
  `ausgewogen` sits between. (Bringhurst 1992, baseline grid concept)
- The modular grid combines the column axis and the baseline axis into
  rectangles or squares that image and card sizes also snap to, not only
  text.
- Whitespace is a designed element with weight, not leftover space. It
  separates groups and must be spent deliberately, more of it at `luftig`,
  less at `verdichtet`, never simply "whatever is left over." (Müller-
  Brockmann grid tradition, active/passive area)
- Optical alignment overrides geometric alignment for hanging punctuation
  (quotes, bullets, round letterforms) and for icons centered next to text:
  push them slightly past the mathematical edge, because the geometric
  center or edge reads as offset to the eye. (Butterick, practicaltypography.com)
- A grid break is a decision, not an accident, only when both hold: it
  carries meaning that would be missing without it, and the same deviation
  recurs consistently elsewhere in the layout rather than once. Anything
  that fails either test goes back on the grid. (Müller-Brockmann 1981)

## 2. Typography

Font pairing, the type scale's chosen ratios and sizes, letter spacing, line
length in characters, and variable-font loading are already specified in
[typography.md](typography.md). Do not re-derive them here. **On any
conflict between this section and typography.md, typography.md governs**,
it is the more specific and already-adopted reference; this section only
adds what typography.md does not cover.

What's added here:

- The type scale's underlying math: `size(n) = base × ratio^n`. Any font
  size present in a design must resolve to this formula for some integer
  `n` and the project's chosen ratio, not a freehand in-between value.
  Named ratios map to musical intervals: minor third 1.2, major third 1.25,
  perfect fifth 1.5, golden ratio 1.618. typography.md's recommended ratios
  (1.25, 1.333, 1.5) are specific picks within this family, use those, this
  is the formula to verify them against. (Bringhurst 1992)
- Line-height: typography.md's 1.5 to 1.6 for body paragraphs is the number
  to build to. Note only as background, and marked **unproven**: the
  academic literature cites a 120 to 145 percent comfort zone (Butterick),
  which is a practice-wide convention, not a figure from a single
  controlled study. Do not loosen typography.md's numbers to chase this
  range.
- Hierarchy without relying on bold alone: each hierarchy level must differ
  from its neighbor in at least two of {size, weight, spacing, color,
  position}. A design that separates levels only by bold versus not-bold
  has used one axis out of five and reads as flat past two levels. (Lupton
  2004; Bringhurst 1992)
- German microtypography (applies whenever body copy is German):
  - Quotation marks: „so" for the primary pair, ‚so' for a nested quote.
    Never the straight or English-slanted form.
  - En dash (glyph: –) for parenthetical asides, ranges, and what German
    calls the Gedankenstrich. Plain hyphen (-) only inside compound words.
  - A narrow non-breaking space before abbreviations ("z. B.") and between
    a number and its unit ("12 kg"), and no space around the hyphen in a
    compound (Divis).
  - (Forssman/de Jong, Detailtypografie)
- Font pairing itself, the rule that two similar typefaces read as a
  mistake rather than a decision, is already stated in typography.md, don't
  duplicate it, just enforce it.

## 3. Color

- Build palettes and gradients in OKLCH (or CIELAB), never in HSL. HSL's
  lightness axis is not perceptually uniform, a ten-point lightness step
  looks larger on dark tones than on light ones, and two hues at identical
  HSL lightness can look unequally bright. OKLCH is native CSS since
  December 2021 (CSS Color Module Level 4/5) and works at any `technik`
  register stage, including `statisch`, since it needs no JavaScript.
  (Ottosson 2020)
- Contrast ratio is the binding, checkable threshold: WCAG 2.2, SC 1.4.3.
  Body text needs 4.5:1 against its background, large text (18pt or larger,
  or 14pt bold) needs 3:1. Values are not rounded, 4.499:1 fails.
- **WCAG contrast is necessary but not sufficient.** The formula ignores
  font weight and stroke width entirely, a hairline weight and a bold
  weight at identical color values score identically despite unequal real
  legibility. Treat a pair that clears the threshold only barely (under
  roughly 5:1 for body) at a light or thin weight as still unresolved, and
  either bump the weight or widen the color gap. APCA is the sharper
  perceptual alternative but is not yet a ratified standard, it's a
  candidate in the W3C Silver process for a future WCAG 3. Use it as an
  informative secondary check when available, never as a substitute for
  the WCAG 1.4.3 number, which stays the one that must pass. (WCAG 2.2 SC
  1.4.3; APCA, git.apcacontrast.com)
- Contrast must survive motion: a shader background, gradient animation, or
  any `bewegung`-budget effect must never drop text below the WCAG
  threshold at any point in its cycle, check the darkest and brightest
  frame, not the average. (see [performance.md](performance.md))
- Color harmony is a vocabulary, not a formula to max out: Itten's seven
  contrasts (contrast of hue, light-dark, warm-cool, complementary,
  simultaneous, saturation, extension) are choices, one dominates by
  decision. Running several at full strength simultaneously cancels them
  out rather than compounding them. (Itten 1961)
- No meaning may depend on color alone. A second channel, shape, text,
  icon, or pattern, must carry the same distinction (status, active versus
  inactive, error versus success). Check by converting the design to
  grayscale and confirming every distinction still reads. (WCAG 2.1 SC
  1.4.1)
- Red-versus-green as the sole status channel fails roughly 8 percent of
  men and 0.4 percent of women of European descent (higher in some other
  populations), this is a measurable failure rate, not a theoretical edge
  case. (Birch 2012)
- The "semantic versus decorative color" label itself comes from design-
  system practice, not an academic source, treat the label as informal.
  The binding rule behind it is WCAG 1.4.1 above, cite that, not the label.

## 4. Perception

- Gestalt grouping, applied as build rules: proximity (elements meant to be
  read as one group sit closer to each other than to neighboring groups),
  similarity (identical visual treatment implies identical category, never
  reuse one treatment for two unrelated things), closure (a shape may be
  left implied only where the missing part doesn't cost clarity), Prägnanz
  (when a layout admits two equally plausible readings, simplify it until
  only one remains). (Wertheimer 1923)
- Visual hierarchy, the squint test: blur the design or shrink it to
  thumbnail size. The single most important element (headline, primary
  action) must still read as the largest, brightest, or highest-contrast
  shape on the page. If nothing stands out at that scale, hierarchy hasn't
  been built, no amount of "looks organized" language substitutes for this
  check. (MIT 6.831, User Interface Design and Implementation)
- Signal-to-noise / cognitive load: every element that carries no intrinsic
  function (required by the task) and no germane function (helps build
  understanding) adds only extraneous load and must be removed or
  visually receded, regardless of how decorative it was meant to look.
  `dichte: verdichtet` tolerates more elements per screen than `luftig`,
  but every one of them still has to clear this test, density is not an
  exemption from justifying an element's presence. (Sweller 1988; Sweller,
  van Merriënboer, Paas 1998)

## 5. The checklist

The point of this file: every row below is something to measure on a
finished design, not just judge by eye.

1. **Grid conformance.** Overlay the column grid, confirm every text and
   image block edge lands on a column line.
2. **Baseline multiple.** Divide every vertical spacing value by the base
   unit (4px or 8px per `dichte`), the remainder must be 0.
3. **Type scale conformance.** For every font size present, solve
   `size = base × ratio^n` for an integer `n` using the project's chosen
   ratio (typography.md), reject any size that doesn't resolve. Exception
   for `dichte: verdichtet`: a dense professional surface (a data table,
   an activity stream with many small status labels) may run up to six
   steps at a shallower ratio, minimum 1.1, instead of the project's main
   scale; the exception is the shallow, many-step ladder itself, not a
   license to add arbitrary in-between sizes to the main scale.
4. **Line length.** Count characters per line in the narrowest and widest
   text column, target 45 to 75, aim near 66. `luftig` sits toward 66 to
   75, `verdichtet` toward 45 to 55 or drops to a smaller type size instead
   of a narrower column. (typography.md; Dyson/Haselgrove 2001)
5. **Font family count.** Count distinct type families used, must be ≤ 2,
   and confirm they differ in category or x-height per typography.md's
   pairing rule.
6. **Hierarchy axis count.** For each hierarchy level, list which of
   {size, weight, spacing, color, position} differ from the adjacent
   level, must be ≥ 2.
7. **Contrast ratio.** Run a contrast calculator on every text/background
   pair actually used, confirm 4.5:1 (body) or 3:1 (large text), unrounded.
   Flag any pair that clears the number only at a hairline weight.
8. **Color-alone check.** Convert the design to grayscale, confirm every
   meaning distinction (status, state, category) is still legible from a
   second channel. Check the reverse failure too: count which color each
   status uses, if one color marks most rows (roughly a third or more)
   while the rest split several ways, the assignment is backwards, the
   frequent, unremarkable case should be the neutral one and color should
   mark what's actually different. A minimized or icon-only state (a
   collapsed control, a status dot with no visible label) still needs a
   word: a short label or symbol legible at that size, or an `aria-label`
   carrying the same word for anyone who can't see the color or the icon.
9. **Color space check.** Inspect palette and gradient definitions in the
   code itself, confirm OKLCH or CIELAB, not HSL.
10. **German microtypography scan** (German copy only). Search body text
    for straight quotes, a hyphen used where an en dash belongs, and
    missing narrow space before abbreviations or between number and unit.
11. **Signal-to-noise pass.** List every element on the screen, name its
    intrinsic or germane function. Anything without one gets removed or
    demoted in size, contrast, and color.
12. **Proximity measurement.** Measure the gap within a content group and
    the gap to the nearest unrelated group, the within-group gap must be
    smaller.
13. **Grid-break consistency.** List every off-grid element, confirm each
    either recurs at least twice in the same deviation or gets reverted to
    the grid.
14. **Squint test.** Blur or shrink a screenshot of the finished design,
    confirm the single most important element still reads as dominant.

## 6. Anti-patterns

What a machine builds without this file, and why:

- **Arbitrary font sizes** (14, 15, 17, 19px side by side) happen when each
  size is picked by eye instead of from `base × ratio^n`. Without a scale,
  no size can be justified against another.
- **Centered body paragraphs** ignore that the eye needs a fixed left edge
  to find the next line. Fine for a headline or a one-liner, wrong for
  anything longer, every line-wrap forces a fresh search for the start.
- **HSL-interpolated gradients** produce a muddy, unevenly bright midtone
  because HSL has no perceptually uniform lightness axis. A blue-to-yellow
  HSL gradient visibly dips through gray in the middle; OKLCH doesn't.
- **Red-versus-green as the only status signal** fails roughly 8 percent
  of men outright. The cause is routing one meaning pair through a single
  color channel instead of adding shape, text, or an icon.
- **Uniform text everywhere** (same size, same weight, same spacing) has
  no hierarchy axis in play and fails the squint test outright, there is
  no dominant shape to find.
- **Arbitrary spacing** (10, 13, 22, 18px in the same design) happens when
  each gap is picked individually instead of derived from a baseline unit.
  Small inconsistencies compound into a visibly unsteady vertical rhythm.
- **Contrast that barely clears WCAG at a hairline weight** passes the
  formal check and still reads poorly, because 1.4.3 doesn't score stroke
  width. This is a known gap in the standard itself, not only a design
  mistake.
- **Elements neither on a grid nor deliberately off it** result when
  position is decided per element instead of from a shared grid. The
  result can't be read as systematic or as a decision, because those two
  states are indistinguishable until the deviation repeats.
- **Wrong quotation marks and a hyphen standing in for an en dash** happen
  because most models default to English punctuation conventions unless
  the German microtypography rules above are explicitly enforced.

Full citation list, primary sources, and the two items marked unproven in
the underlying research: [../planung/recherche-gestaltung.md](../planung/recherche-gestaltung.md).
For structure and information architecture, motion budgets, scroll
choreography, and the technical stack, see
[ia-and-structure.md](ia-and-structure.md), [motion-doctrine.md](motion-doctrine.md),
[scroll-choreography.md](scroll-choreography.md), and [stack.md](stack.md).

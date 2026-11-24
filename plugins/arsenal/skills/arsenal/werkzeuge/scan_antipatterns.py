#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Static anti-pattern scanner for Arsenal: finds design and accessibility tells in HTML/CSS/JSX/TSX/Vue/Svelte.

It replaces the automatic detector of the original template. Only what can be read from source is checked;
rules that need a rendered page are listed by `--list` (kind "browser") and are a hand check in
befehle/audit.md und befehle/kritik.md (use the skills `browser` / `browser-workspace` for screenshots).

Usage:  scan_antipatterns.py PATH [PATH...] [--json] [--min P0|P1|P2|P3] [--list] [--all] [--abgabe]
Exit:   0 no findings, 1 findings of P0/P1, 3 only P2/P3 (after --min filter).

Source of the rules: skills/design/pflichtliste.md (D1-D18 hard rules, Q1-Q15 questions of judgment). Hints name the number.
Bundles (Q13): AI look comes from the combination of features, not from one element. A single feature is a P3 hint, two
features of one bundle give the P2 finding "bundle", two bundles give the P1 finding "bundle-multi". Bundles are judged
per file; with --abgabe all given files count as one submission (index.html plus style.css).
Exceptions: a comment `design-ok: Qn reason` (also `D4 reason` for side-tab) anywhere in a file excuses the findings of the
rules that belong to that question in that file; they are counted as "begründet", not as findings. D5, D7, D8, D10, D11 have no
such exception (only a deviation from the brief or the brand, written in the block "Designprüfung", D1).

Severity: P0 blocks a task, P1 major (WCAG AA / release blocker), P2 minor, P3 polish / review prompt.
The template has no P-levels; they are assigned here from its category (slop/quality/advisory) and from audit.md.

RULES (id | severity | what | source file of the template, or "arsenal" = own rule from design-regeln.md / audit.md)
  side-tab                    P2 colored border-left/right >=2px on a block (D4 question)    antipatterns.json
  border-accent-on-rounded    P2 thick accent border plus border-radius (D4 question)         antipatterns.json
  overused-font               P3 Inter/Roboto/Fraunces/Geist/Plus Jakarta/Space Grotesk       antipatterns.json
  gradient-text               P1 background-clip:text with a gradient                         antipatterns.json
  ai-color-palette            P2 violet/purple gradient; neon cyan text on dark               antipatterns.json
  cream-palette               P3 warm cream/beige page background                             antipatterns.json
  nested-cards                P2 card element inside a card element                           antipatterns.json
  identical-card-grid         P3 3+ sibling cards with the same inner structure               design-regeln.md s5
  bounce-easing               P2 bounce/elastic easing (overshooting cubic-bezier, names)     antipatterns.json
  layout-animation            P2 transition/keyframes on width/height/top/left/margin/padding  motion.md
  transition-all              P3 `transition: all`                                            arsenal
  pulsing-dot                 P3 small round element with a pulse animation                   antipatterns.json
  blinking-cursor             P3 decorative blinking cursor/caret animation                   antipatterns.json
  shape-assembled-illustration P3 large inline SVG built from many primitive shapes           antipatterns.json
  organic-clip-path           P3 clip-path polygon with many vertices or path()               antipatterns.json
  buried-raster               P3 url() image under a near-opaque gradient wash                antipatterns.json
  hard-offset-shadow          P3 unblurred shadow offset >=4px (review prompt)                antipatterns.json
  dark-glow                   P3 zero-offset colored halo shadow / colored blur on dark       antipatterns.json
  radial-halo                 P3 chromatic radial-gradient glow to transparent                antipatterns.json
  gpt-thin-border-wide-shadow P3 hairline border plus wide diffuse shadow                     antipatterns.json
  repeating-stripes-gradient  P3 repeating-linear-gradient stripes as surface                 antipatterns.json
  codex-grid-background       P3 hairline-gradient grid background with fixed cell            antipatterns.json
  glassmorphism               P3 backdrop-filter blur as decoration (Q2)                      design-regeln.md s5
  marquee                     P2 <marquee>, marquee class, endless translate loop             antipatterns.json
  italic-serif-display        P3 italic serif on h1/hero                                      antipatterns.json
  kicker-above-heading        P3 eyebrow/kicker/overline label class (Q3)                     antipatterns.json
  hero-eyebrow-chip           P3 uppercase tracked pill/chip above hero heading               antipatterns.json
  numbered-section-labels     P3 3+ tiny "01/02/03" labels                                    antipatterns.json
  em-dash-overuse             P3 >=8 em-dashes at high density in copy                        antipatterns.json
  marketing-buzzword          P3 generic SaaS phrases                                         antipatterns.json
  aphoristic-cadence          P3 3+ "Not X. Y." / "X. No Y." copy turns                       antipatterns.json
  theater-slop-phrase         P3 "... theater" as dismissal                                   antipatterns.json
  oversized-h1                P3 h1 font-size max >= 120px                                    antipatterns.json
  extreme-negative-tracking   P2 letter-spacing below -0.04em                                 antipatterns.json / design-regeln.md s8
  wide-tracking               P3 letter-spacing above 0.05em on body text                     antipatterns.json
  all-caps-body               P2 text-transform:uppercase on body text elements               antipatterns.json
  justified-text              P3 text-align:justify without hyphens:auto                      antipatterns.json
  tight-leading               P2 line-height below 1.3 on body text                           antipatterns.json
  line-length                 P3 measure wider than 80ch/ ~ 900px on text                      antipatterns.json
  tiny-text                   P2 font-size below 11px (P3 for 11px)                                         antipatterns.json
  undersized-ui-text          P2 font-size below 11px on links/buttons/labels/table cells     antipatterns.json
  low-contrast                P1 text/background pair below WCAG AA (4.5:1, large 3:1)        antipatterns.json
  gray-on-color               P2 gray text on a saturated background                          antipatterns.json
  pure-black-white            P3 #000 / #fff / black / white as color                         design-regeln.md
  broken-image                P1 <img> with empty or placeholder src                          antipatterns.json
  img-no-alt                  P1 <img> without alt                                            audit.md
  skipped-heading             P2 heading levels skip (h1 then h3)                             antipatterns.json
  heading-structure           P2 no h1 or several h1                                          audit.md
  html-lang-missing           P2 <html> without lang                                          audit.md
  viewport-meta               P1 viewport missing, or user-scalable=no / maximum-scale<5      audit.md
  outline-none                P1 outline:none/0 without a focus replacement                   audit.md
  focus-styles-missing        P1 interactive elements, own CSS, no :focus/:focus-visible      audit.md
  reduced-motion-missing      P1 animation/transition, no prefers-reduced-motion              audit.md / motion.md
  positive-tabindex           P2 tabindex greater than 0                                      audit.md
  clickable-div               P2 onclick on div/span without role and keyboard                audit.md
  input-no-label              P2 form field without label / aria-label                        audit.md
  linear-easing               P3 `linear` timing on a movement (D5)                           pflichtliste.md
  scale-no-origin             P3 scale-in of a popover/menu/modal without transform-origin (D7)  pflichtliste.md
  no-tabular-nums             P3 comparing/changing numbers, tabular-nums nowhere (D8)        pflichtliste.md
  emoji-in-text               P2 emoji in visible text, attributes, SVG text, CSS content (D10)  pflichtliste.md
  simple-gradient             P2 gradient of two or three stops as a surface (D11)            pflichtliste.md
  cramped-padding             P3 card/panel/dialog with padding under 10px                    arsenal
  radial-spotlight-glow       P3 radial-gradient spotlight/glow at a position fading out       arsenal
  bundle-feature              P3 one feature of a look bundle (Q13)                           pflichtliste.md Q13
  bundle                      P2 two features of one bundle together (Q13)                    pflichtliste.md Q13
  bundle-multi                P1 two bundles in one submission (Q13)                          pflichtliste.md Q13
  design-ok-no-reason         P3 `design-ok:` comment without question number or reason       pflichtliste.md
  paste-blocked               P2 onpaste/@paste handler that cancels the paste                  S52
  field-attrs-missing         P3 text-like field without name, or identity field without autocomplete  S52
  autofocus                   P3 autofocus attribute (desktop only, one primary field)          S52
  no-intl-format              P3 hand-built date/currency string instead of Intl                TE15
  img-no-lazy                 P3 4th and later <img> of a page without loading attribute       S36
  hero-img-lazy               P2 <img loading=lazy> inside a hero element (LCP image)          S36
  video-autoplay-attrs        P2 <video autoplay> without muted or without playsinline         ME15
  gif-image                   P3 <img src=*.gif>: animated GIF belongs in compressed video     ME15
  will-change-static          P3 will-change on * / html / body or on 4+ always-on selectors   TE11
  color-scheme-missing        P3 full page without color-scheme (no linked stylesheet)         S33
  theme-color-missing         P3 full page without <meta name=theme-color>                     TE14
  viewport-fit-missing        P2 env(safe-area-inset-*) used, viewport meta lacks viewport-fit TE14
  anchor-under-fixed-bar      P2 #anchor links, fixed/sticky bar, no scroll-margin/-padding    TE14
  font-display-missing        P2 @font-face without font-display                               TE09
  icon-no-aria-hidden         P3 small inline <svg> without aria-hidden, title or aria-label   S12
  onclick-navigation          P2 onclick/@click that navigates (location, router) on non-<a>   S12 / SW18

BROWSER-ONLY (not checked here, hand check in audit.md / critique.md):
  flat-type-hierarchy, monotonous-spacing, script-error, content-hidden-at-rest, edge-flush-cards,
  text-occlusion, first-viewport-column-overflow, body-text-viewport-edge, heading-rhythm, straggler,
  unbalanced-heading, text-overflow, repeated-container-text, clipped-overflow-container, icon-tile-stack,
  design-system-font, design-system-color, design-system-radius, design-system-font-size (need a design file).
"""
from __future__ import annotations

import argparse
import colorsys
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".jsx", ".tsx", ".vue", ".svelte", ".js", ".ts", ".svg"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".cache"}
SEV_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}

# rule id -> (severity, kind, hint). kind "static" or "browser".
RULES: dict[str, tuple[str, str, str]] = {
    "side-tab": ("P2", "static", "D4: colored side border on a card/alert; keep it only with a function a half-sentence names (design-ok: D4 reason)."),
    "border-accent-on-rounded": ("P2", "static", "D4: thick accent border clashes with the radius: drop one, or name the function."),
    "overused-font": ("P3", "static", "Inter/Roboto/Fraunces/Geist/Jakarta/Space Grotesk converge on the same look: choose a distinctive face."),
    "gradient-text": ("P1", "static", "Gradient text is decoration: use a solid color, emphasis by weight or size."),
    "ai-color-palette": ("P2", "static", "Violet/cyan-neon is the generated-UI palette: pick colors from the brand world."),
    "cream-palette": ("P3", "static", "Warm cream page background as reflex: choose it from a deliberate palette."),
    "nested-cards": ("P2", "static", "Card inside a card: flatten, use spacing, type and dividers."),
    "identical-card-grid": ("P3", "static", "Same-structure card row as page scaffold: vary size, weight or layout."),
    "bounce-easing": ("P2", "static", "Use exponential ease-out (quart/quint/expo), not bounce or overshoot."),
    "layout-animation": ("P2", "static", "Animate transform/opacity, not layout properties."),
    "transition-all": ("P3", "static", "Name the properties instead of `all`."),
    "pulsing-dot": ("P3", "static", "Pulse only for genuinely live data; use a static labeled indicator."),
    "blinking-cursor": ("P3", "static", "Decorative cursor simulates typing where no input exists."),
    "shape-assembled-illustration": ("P3", "static", "Pile of primitives reads as clip art: real illustration or none."),
    "organic-clip-path": ("P3", "static", "Many-vertex clip-path fakes an organic edge: use a real alpha matte."),
    "buried-raster": ("P3", "static", "Image under a near-opaque wash never shows: lower the wash or drop the image."),
    "hard-offset-shadow": ("P3", "static", "Q1: hard offset shadow only where the style carries it."),
    "dark-glow": ("P3", "static", "Q1: glow only on active or focused elements; otherwise neutral elevation."),
    "radial-halo": ("P3", "static", "Q1: chromatic radial wash as glow: same tell as glow shadows."),
    "gpt-thin-border-wide-shadow": ("P3", "static", "Declare elevation once: border or shadow, not both."),
    "repeating-stripes-gradient": ("P3", "static", "Gradient stripes as surface are a generated signature: plain or deliberate texture."),
    "codex-grid-background": ("P3", "static", "Hairline grid background only on canvas/map/blueprint surfaces."),
    "glassmorphism": ("P3", "static", "Q2: blur only where it makes a layer over content readable."),
    "marquee": ("P2", "static", "Auto-scrolling content hides half its content: let readers move on their own."),
    "italic-serif-display": ("P3", "static", "Italic serif hero headline is the AI-startup default."),
    "kicker-above-heading": ("P3", "static", "Q3: kicker above the heading only when the line carries information."),
    "hero-eyebrow-chip": ("P3", "static", "Q3: uppercase tracked chip above the hero headline: only with information in it."),
    "numbered-section-labels": ("P3", "static", "Numbered chapter labels are scaffolding unless the order carries information."),
    "em-dash-overuse": ("P3", "static", "Em-dash saturation is an AI cadence tell: vary punctuation."),
    "marketing-buzzword": ("P3", "static", "Generic SaaS phrase: name the specific verb and noun."),
    "aphoristic-cadence": ("P3", "static", "'Not X. Y.' turns repeated across sections read as AI cadence."),
    "theater-slop-phrase": ("P3", "static", "Say plainly what the thing does or does not do."),
    "oversized-h1": ("P3", "static", "Q7: headline from 120px needs a reason; a full sentence at display size eats the viewport."),
    "extreme-negative-tracking": ("P2", "static", "Tracking below -0.04em crushes letter shapes."),
    "wide-tracking": ("P3", "static", "Wide tracking on body text slows reading: only short uppercase labels."),
    "all-caps-body": ("P2", "static", "Uppercase body copy removes word shapes."),
    "justified-text": ("P3", "static", "Justified without hyphens makes rivers: left-align or hyphens:auto."),
    "tight-leading": ("P2", "static", "Body line-height under 1.3: use 1.5 to 1.7."),
    "line-length": ("P3", "static", "Measure over ~80 characters: cap with max-width in ch."),
    "tiny-text": ("P2", "static", "Text under 12px: use 14px or more for body, 16px ideal."),
    "undersized-ui-text": ("P2", "static", "Interactive/content UI text under 11px."),
    "low-contrast": ("P1", "static", "Below WCAG AA (4.5:1 text, 3:1 large text)."),
    "gray-on-color": ("P2", "static", "Gray on a colored ground looks washed: use a dark shade of the ground or near-white."),
    "pure-black-white": ("P3", "static", "Pure #000/#fff: tint toward the brand hue."),
    "broken-image": ("P1", "static", "Empty or placeholder src ships a broken-image box."),
    "img-no-alt": ("P1", "static", "Add alt text (alt=\"\" for decoration)."),
    "skipped-heading": ("P2", "static", "Heading levels must not skip."),
    "heading-structure": ("P2", "static", "One h1 per page."),
    "html-lang-missing": ("P2", "static", "Set lang on <html>."),
    "viewport-meta": ("P1", "static", "Viewport meta missing or blocks zoom."),
    "outline-none": ("P1", "static", "Removing the outline needs a visible :focus-visible replacement."),
    "focus-styles-missing": ("P1", "static", "Add visible :focus-visible styles for interactive elements."),
    "reduced-motion-missing": ("P1", "static", "Handle prefers-reduced-motion for animation."),
    "positive-tabindex": ("P2", "static", "tabindex > 0 breaks the natural focus order."),
    "clickable-div": ("P2", "static", "Use <button>, or add role, tabindex and key handling."),
    "input-no-label": ("P2", "static", "Give every field a <label> or aria-label."),
    "linear-easing": ("P3", "static", "D5: use ease-out for appearing, ease-in for leaving, ease-in-out for A to B; linear only for progress and endless rotation."),
    "scale-no-origin": ("P3", "static", "D7: what appears grows from its trigger: set transform-origin at the button, anchor or click point."),
    "no-tabular-nums": ("P3", "static", "D8: numbers that are compared or change need font-variant-numeric: tabular-nums (amounts right-aligned)."),
    "emoji-in-text": ("P2", "static", "D10: no emojis; use a symbol from an SVG icon set (exception only for user content)."),
    "simple-gradient": ("P2", "static", "D11: no gradient of two or three stops as surface, button, text or card; allowed: light, depth, data, photo darkening, lines, masks, brand gradients."),
    "cramped-padding": ("P3", "static", "Container padding under 10px: give content room (spacing ladder 12, 16, 24)."),
    "radial-spotlight-glow": ("P3", "static", "Q1: radial spotlight/glow as background is the generated hero look: only with a reason from the content."),
    "bundle-feature": ("P3", "static", "Q13: one feature of a look bundle; fine alone, a problem together with a second."),
    "bundle": ("P2", "static", "Q13: two features of one look bundle meet: who chose each, and for what? Remove one or give the reason."),
    "bundle-multi": ("P1", "static", "Q13: two look bundles in one submission: this reads as a template; change the look or state the order that asked for it."),
    "design-ok-no-reason": ("P3", "static", "`design-ok:` needs a question number (Q1-Q15, or D4) and a half-sentence reason."),
    "paste-blocked": ("P2", "static", "S52: never block paste (password managers, accessibility): remove the preventDefault."),
    "field-attrs-missing": ("P3", "static", "S52: every field gets name; identity fields (email, tel, password, url) get autocomplete."),
    "autofocus": ("P3", "static", "S52: autofocus only on desktop and on one primary field; never on touch."),
    "no-intl-format": ("P3", "static", "TE15: format dates and amounts with Intl.DateTimeFormat / Intl.NumberFormat, not by hand."),
    "img-no-lazy": ("P3", "static", "S36: images below the first view get loading=\"lazy\" (the LCP image gets fetchpriority=\"high\")."),
    "hero-img-lazy": ("P2", "static", "S36: the hero image is the LCP element: no loading=lazy, set fetchpriority=\"high\"."),
    "video-autoplay-attrs": ("P2", "static", "ME15: autoplay needs muted and playsinline (and a poster); otherwise browsers block it."),
    "gif-image": ("P3", "static", "ME15: an animated GIF is large; use compressed video (muted, loop, playsinline) with a still."),
    "will-change-static": ("P3", "static", "TE11: will-change is a short hint for a known expensive animation, not a permanent style."),
    "color-scheme-missing": ("P3", "static", "S33: set color-scheme on :root so scrollbars and form controls follow the theme."),
    "theme-color-missing": ("P3", "static", "TE14: add <meta name=\"theme-color\"> matching the page ground (light and dark)."),
    "viewport-fit-missing": ("P2", "static", "TE14: env(safe-area-inset-*) needs viewport-fit=cover in the viewport meta."),
    "anchor-under-fixed-bar": ("P2", "static", "TE14: set scroll-margin-top (or scroll-padding-top) so the fixed bar does not cover anchor targets."),
    "font-display-missing": ("P2", "static", "TE09: @font-face without font-display blocks text; use swap or optional."),
    "icon-no-aria-hidden": ("P3", "static", "S12: decorative icon gets aria-hidden=\"true\"; a meaningful one gets a title or aria-label."),
    "onclick-navigation": ("P2", "static", "S12/SW18: navigation is a real <a href> (Ctrl-click, middle click, shareable URL)."),
}
BROWSER_ONLY = [
    "flat-type-hierarchy", "monotonous-spacing", "script-error", "content-hidden-at-rest", "edge-flush-cards",
    "text-occlusion", "first-viewport-column-overflow", "body-text-viewport-edge", "heading-rhythm", "straggler",
    "unbalanced-heading", "text-overflow", "repeated-container-text", "clipped-overflow-container",
    "icon-tile-stack", "design-system-font", "design-system-color", "design-system-radius",
    "design-system-font-size",
]

NAMED = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "gray": (128, 128, 128),
         "grey": (128, 128, 128), "silver": (192, 192, 192), "blue": (0, 0, 255), "green": (0, 128, 0),
         "yellow": (255, 255, 0), "cyan": (0, 255, 255), "purple": (128, 0, 128), "lightgray": (211, 211, 211),
         "lightgrey": (211, 211, 211), "darkgray": (169, 169, 169), "orange": (255, 165, 0)}
COLOR_RE = re.compile(r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")
BUZZ = re.compile(r"\b(streamline[sd]?|empower(?:s|ing)?|supercharge[sd]?|world-class|enterprise-grade|next-generation|"
                  r"cutting-edge|game-chang(?:er|ing)|revolutioni[sz]e[sd]?|seamless(?:ly)?|unlock the power|"
                  r"state-of-the-art|best-in-class|leverage[sd]?|elevate your|take your .{1,20} to the next level)\b", re.I)
OVERUSED = ("inter", "roboto", "fraunces", "geist", "plus jakarta sans", "space grotesk")
BUZZ_DE = re.compile(r"\b(nahtlos\w*|ma(?:ß|ss)geschneidert\w*|ganzheitlich\w*|revolution(?:är|ar)\w*|next-level|game-?changer|"
                     r"auf (?:das|die) n(?:ä|ae)chste (?:level|stufe)|synergie\w*|innovative l(?:ö|oe)sung\w*)", re.I)
SERIFS = ("georgia", "playfair", "fraunces", "newsreader", "garamond", "cormorant", "lora", "merriweather", "dm serif",
          "instrument serif", "recoleta", "source serif", "libre baskerville", "crimson", "spectral", "canela", "tiempos",
          "times", "bodoni", "didot", "baskerville", "gt sectra", "cooper", "young serif")

# Emoji: Emoji_Presentation characters, pictograph blocks, flags, and any symbol followed by the emoji selector U+FE0F.
EMOJI_RE = re.compile(
    "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001F64F\U0001F680-\U0001F6FF\U0001F7E0-\U0001F7EB\U0001F90C-\U0001F9FF"
    "\U0001FA70-\U0001FAFF\U0001F004\U0001F0CF\U0001F18E\U0001F191-\U0001F19A\U0001F201\U0001F21A\U0001F22F"
    "\U0001F232-\U0001F236\U0001F238-\U0001F23A\U0001F250\U0001F251"
    "\u231A\u231B\u23E9-\u23EC\u23F0\u23F3\u25FD\u25FE\u2614\u2615\u2648-\u2653\u267F\u2693\u26A1\u26AA\u26AB"
    "\u26BD\u26BE\u26C4\u26C5\u26CE\u26D4\u26EA\u26F2\u26F3\u26F5\u26FA\u26FD\u2705\u270A\u270B\u2728\u274C"
    "\u274E\u2753-\u2755\u2757\u2795-\u2797\u27B0\u27BF\u2B1B\u2B1C\u2B50\u2B55]"
    "|[\u00A9\u00AE\u203C\u2049\u2122\u2139\u2194-\u21AA\u231A-\u23FF\u24C2\u25AA-\u25FE\u2600-\u27BF\u2934\u2935"
    "\u2B05-\u2B55\u3030\u303D\u3297\u3299\U0001F000-\U0001FAFF]\uFE0F|[#*0-9]\uFE0F?\u20E3")

# bundles of Q13 in pflichtliste.md: id -> name. A bundle is a set of features that together make a template look.
BUNDLES = {
    "creme": "Creme-Look", "neon": "Neon-Dunkel", "zeitung": "Zeitungs-Look", "kasten": "Kasten-Look",
    "saas": "SaaS-Hero", "karte": "Kartenvorlage", "text": "Textmuster",
}
# existing rules that are themselves one feature of a bundle: rule -> (bundle, feature label)
RULE_FEATURE = {
    "cream-palette": ("creme", "Creme-Grund"), "italic-serif-display": ("zeitung", "kursive Serif"),
    "dark-glow": ("neon", "Leuchtschatten"), "radial-halo": ("neon", "Leuchtschatten"),
    "radial-spotlight-glow": ("neon", "Leuchtschatten"), "hard-offset-shadow": ("kasten", "harter Schatten"),
    "hero-eyebrow-chip": ("saas", "Etikett über Überschrift"), "kicker-above-heading": ("saas", "Etikett über Überschrift"),
    "identical-card-grid": ("karte", "gleiche Karten"), "gpt-thin-border-wide-shadow": ("karte", "Haarrand mit Breitschatten"),
    "marketing-buzzword": ("text", "Marketingwörter"), "aphoristic-cadence": ("text", "nicht X, sondern Y"),
    "em-dash-overuse": ("text", "Gedankenstriche"),
}
# rule -> questions whose `design-ok:` comment excuses it (D5, D7, D8, D10, D11 are not here: no exception)
RULE_Q = {
    "side-tab": ("D4",), "border-accent-on-rounded": ("D4",), "glassmorphism": ("Q2",),
    "kicker-above-heading": ("Q3",), "hero-eyebrow-chip": ("Q3",),
    "hard-offset-shadow": ("Q1",), "dark-glow": ("Q1",), "radial-halo": ("Q1",), "radial-spotlight-glow": ("Q1",),
    "oversized-h1": ("Q7",), "em-dash-overuse": ("Q10",), "marketing-buzzword": ("Q10",), "aphoristic-cadence": ("Q10",),
    "theater-slop-phrase": ("Q10",), "bundle-feature": ("Q13",), "bundle": ("Q13",), "bundle-multi": ("Q13",),
}
for _r in RULE_FEATURE:
    RULE_Q[_r] = tuple(dict.fromkeys(RULE_Q.get(_r, ()) + ("Q13",)))
WEAK_FEATURES = {"Fast-Schwarz"}  # common on its own (any dark UI): counts for a bundle, but no single hint
DESIGN_OK_RE = re.compile(r"design-ok:?[ \t]*([^\n]*)", re.I)


class Finding(dict):
    """One hit: file, line, rule, severity, hint (plus optional detail)."""


def line_of(text: str, offset: int) -> int:
    """1-based line number of a character offset."""
    return text.count("\n", 0, offset) + 1


def parse_color(s: str, vars_: dict[str, str] | None = None):
    """Return (r,g,b,a) 0-255 / 0-1 for a literal color string, or None when not computable."""
    s = s.strip().lower()
    m = re.match(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^)]*))?\)", s)
    if m:
        v = (vars_ or {}).get(m.group(1)) or m.group(2)
        return parse_color(v, vars_) if v else None
    if s in NAMED:
        r, g, b = NAMED[s]
        return (r, g, b, 1.0)
    if s.startswith("#"):
        h = s[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) not in (6, 8) or not re.fullmatch(r"[0-9a-f]+", h):
            return None
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)
    m = re.match(r"(rgba?|hsla?)\(([^)]*)\)", s)
    if not m:
        return None
    nums = re.findall(r"-?\d*\.?\d+%?", m.group(2))
    if len(nums) < 3:
        return None

    def num(t, scale=1.0):
        return float(t[:-1]) / 100 * scale if t.endswith("%") else float(t)
    a = num(nums[3], 1.0) if len(nums) > 3 else 1.0
    if m.group(1).startswith("rgb"):
        return (num(nums[0], 255), num(nums[1], 255), num(nums[2], 255), a)
    h, sat, lig = float(nums[0].rstrip("%")) / 360 % 1, num(nums[1], 1.0), num(nums[2], 1.0)
    sat = sat / 100 if sat > 1 else sat
    lig = lig / 100 if lig > 1 else lig
    r, g, b = colorsys.hls_to_rgb(h, lig, sat)
    return (r * 255, g * 255, b * 255, a)


def luminance(c) -> float:
    """WCAG relative luminance."""
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def contrast(a, b) -> float:
    """WCAG contrast ratio of two opaque colors."""
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hsv(c):
    """(hue deg, saturation, value) of an rgb tuple."""
    h, s, v = colorsys.rgb_to_hsv(c[0] / 255, c[1] / 255, c[2] / 255)
    return h * 360, s, v


def is_gray(c, tol=14) -> bool:
    return max(c[:3]) - min(c[:3]) <= tol


def size_px(value: str):
    """Largest font size in px found in a value (px/rem/em, clamp ok); None when unit is relative to the viewport."""
    vals = []
    for n, u in re.findall(r"(-?\d*\.?\d+)(px|rem|em)\b", value):
        vals.append(float(n) * (1 if u == "px" else 16))
    return max(vals) if vals else None


def gradient_calls(v: str):
    """[(kind, args)] of every linear/radial/conic gradient function in a value, parentheses balanced."""
    out = []
    for m in re.finditer(r"(repeating-)?(linear|radial|conic)-gradient\(", v):
        i, depth = m.end(), 1
        while i < len(v) and depth:
            depth += {"(": 1, ")": -1}.get(v[i], 0)
            i += 1
        out.append((("repeating-" if m.group(1) else "") + m.group(2), v[m.end():i - 1]))
    return out


def split_top(args: str) -> list[str]:
    """Split on commas outside parentheses."""
    parts, depth, cur = [], 0, ""
    for ch in args:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def gradient_stops(args: str) -> list[str]:
    """The color-stop items of a gradient argument list (the direction/shape item dropped)."""
    items = split_top(args)
    if items and re.match(r"(to\s|in\s|from\s|at\s|circle|ellipse|closest|farthest|[-\d.]+(deg|turn|rad|grad)\b)|.*\sat\s", items[0].lower()):
        items = items[1:]
    return items


def stop_color(stop: str, vars_=None):
    """Color (r,g,b,a) of one gradient stop, transparent = alpha 0, None when not computable."""
    st = stop.lower()
    m = re.search(r"var\([^)]*\)", st)
    if m:
        return parse_color(m.group(0), vars_)
    m = COLOR_RE.search(stop)
    if m:
        return parse_color(m.group(0), vars_)
    if "transparent" in st:
        return (0, 0, 0, 0.0)
    for tok in st.split():
        if tok in NAMED:
            return parse_color(tok)
    return None


def hue_gap(a: float, b: float) -> float:
    d = abs(a - b) % 360
    return min(d, 360 - d)


def flat_gradient(cols) -> str:
    """Why a two/three-stop opaque gradient is a simple gradient ("" when it is depth or too unclear)."""
    chroma = [c for c in cols if hsv(c)[1] >= 0.25 and hsv(c)[2] >= 0.15]
    neutral = [c for c in cols if c not in chroma]
    if len(chroma) >= 2:
        gap = max(hue_gap(hsv(a)[0], hsv(b)[0]) for a in chroma for b in chroma)
        if gap >= 30:
            return f"hue shift {gap:.0f} degrees"
    if chroma and neutral and any(hsv(c)[1] >= 0.45 for c in chroma) and any(contrast(c, n) >= 2.5 for c in chroma for n in neutral):
        return "color to neutral"
    return ""


class Block:
    """One CSS rule: selector, declarations [(prop, value, line)], the enclosing at-rule text."""

    def __init__(self, selector: str, line: int, at: str = ""):
        self.selector, self.line, self.at, self.decls = selector.strip(), line, at, []

    def get(self, prop: str):
        for p, v, ln in self.decls:
            if p == prop:
                return v, ln
        return None


def strip_comments(text: str) -> str:
    """Blank out comments but keep offsets so line numbers stay right."""
    return re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)


def parse_css(text: str, base_line: int = 1) -> tuple[list[Block], dict[str, str]]:
    """Scan CSS with nesting; returns blocks (innermost rules, at-rule chain kept) and custom properties."""
    text = strip_comments(text)
    blocks: list[Block] = []
    vars_: dict[str, str] = {}
    stack: list[tuple[str, Block | None]] = []
    start = 0
    for i, ch in enumerate(text):
        if ch == "{":
            head = text[start:i].strip()
            at = " ".join(h for h, _ in stack if h.startswith("@"))
            blk = None if head.startswith("@") else Block(head, base_line + text.count("\n", 0, i), at)
            if blk:
                blocks.append(blk)
            stack.append((head, blk))
            start = i + 1
        elif ch == "}":
            body = text[start:i]
            if stack and stack[-1][1] is not None:
                blk = stack[-1][1]
                off = start
                for part in body.split(";"):
                    if ":" in part and part.strip():
                        p, v = part.split(":", 1)
                        p, v = p.strip().lower(), v.strip().rstrip(";")
                        ln = base_line + text.count("\n", 0, off + len(part) - len(part.lstrip()))
                        blk.decls.append((p, re.sub(r"\s*!important", "", v), ln))
                        if p.startswith("--"):
                            vars_[p] = v
                    off += len(part) + 1
            if stack:
                stack.pop()
            start = i + 1
        elif ch == ";" and not stack:
            start = i + 1
    return blocks, vars_


def jsx_blocks(text: str) -> list[Block]:
    """Turn JSX/TS style objects (style={{ borderLeft: '4px solid red' }}) into pseudo blocks."""
    out = []
    for m in re.finditer(r"style=\{\{(.*?)\}\}", text, re.S):
        blk = Block("[style]", line_of(text, m.start()))
        for k, v in re.findall(r"(\w+)\s*:\s*(['\"`][^'\"`]*['\"`]|-?[\d.]+)", m.group(1)):
            prop = re.sub(r"([A-Z])", lambda x: "-" + x.group(1).lower(), k)
            val = v.strip("'\"`") + ("px" if re.fullmatch(r"-?[\d.]+", v) and prop in ("font-size",) else "")
            blk.decls.append((prop, val, blk.line))
        out.append(blk)
    return out


class Node:
    """Element of the parsed markup tree."""

    def __init__(self, tag, attrs, line, parent):
        self.tag, self.attrs, self.line, self.parent, self.children = tag, dict(attrs), line, parent, []
        self.classes = (self.attrs.get("class") or self.attrs.get("classname") or "").split()
        self.text = ""


VOID = {"img", "br", "hr", "input", "meta", "link", "source", "area", "base", "col", "embed", "track", "wbr"}


class Markup(HTMLParser):
    """Builds a light element tree and collects visible text plus <style> blocks and <img>/<svg> facts."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], 1, None)
        self.cur = self.root
        self.nodes: list[Node] = []
        self.styles: list[tuple[str, int]] = []
        self.texts: list[tuple[str, int]] = []
        self.scripts: list[tuple[str, int]] = []
        self._in = None
        self._buf = ""
        self._buf_line = 1

    def handle_starttag(self, tag, attrs):
        n = Node(tag, [(k.lower(), v or "") for k, v in attrs], self.getpos()[0], self.cur)
        self.cur.children.append(n)
        self.nodes.append(n)
        if tag in ("style", "script"):
            self._in, self._buf, self._buf_line = tag, "", self.getpos()[0]
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        n = Node(tag, [(k.lower(), v or "") for k, v in attrs], self.getpos()[0], self.cur)
        self.cur.children.append(n)
        self.nodes.append(n)

    def handle_endtag(self, tag):
        if self._in == tag:
            if tag == "style":
                self.styles.append((self._buf, self._buf_line))
            else:
                self.scripts.append((self._buf, self._buf_line))
            self._in = None
        c = self.cur
        while c is not self.root and c.tag != tag:
            c = c.parent
        if c is not self.root:
            self.cur = c.parent

    def handle_data(self, data):
        if self._in:
            self._buf += data
        elif data.strip():
            self.cur.text += " " + data.strip()
            self.texts.append((data, self.getpos()[0]))


def walk(n: Node):
    """Depth-first iteration over a tree node and its descendants."""
    yield n
    for c in n.children:
        yield from walk(c)


def is_card(n: Node) -> bool:
    """Class name contains 'card', or Tailwind-style rounded + shadow/border + padding."""
    cl = " ".join(n.classes).lower()
    if re.search(r"(^|[\s_-])card($|[\s_-])|\bcard", cl) and "discard" not in cl:
        return True
    return bool(re.search(r"\brounded", cl) and re.search(r"\b(shadow|border)\b", cl) and re.search(r"\bp-\d", cl))


def signature(n: Node) -> tuple:
    """Tag skeleton of an element's subtree, used to spot identical cards."""
    return tuple(c.tag for c in walk(n))[1:]


class Scan:
    """Scan of one file; collects findings."""

    def __init__(self, path: Path, text: str, project_flags: dict):
        self.path, self.text, self.flags = path, text, project_flags
        self.out: list[Finding] = []
        self.ext = path.suffix.lower()
        self.feats: dict[str, dict[str, dict]] = {}   # bundle -> feature -> {"line", "own_rule"}
        self.excuses: dict[str, tuple[str, int]] = {}  # question -> (reason, line) from `design-ok:` comments
        self.acc: dict[str, list] = {}                 # counters for features that need several hits

    def feat(self, bundle: str, name: str, line: int, own_rule: bool = False):
        """Register one feature of a look bundle (Q13); the first line and a rule flag are kept."""
        f = self.feats.setdefault(bundle, {}).setdefault(name, {"line": line, "own_rule": own_rule})
        f["line"] = min(f["line"], line)
        f["own_rule"] = f["own_rule"] or own_rule

    def add(self, rule: str, line: int, detail: str = "", sev: str | None = None):
        sev, _, hint = (sev or RULES[rule][0]), None, RULES[rule][2]
        if rule in RULE_FEATURE:
            self.feat(*RULE_FEATURE[rule], line, own_rule=True)
        key = (rule, line)
        if any((f["rule"], f["line"]) == key for f in self.out):
            return
        self.out.append(Finding(file=str(self.path), line=line, rule=rule, severity=sev,
                                hint=(detail + " - " if detail else "") + hint))

    # ---- CSS rules -------------------------------------------------------------------------------------------
    def css_rules(self, blocks: list[Block], vars_: dict[str, str]):
        """Run all declaration-level rules over parsed blocks."""
        self.vars = vars_
        self.kf_scale: set[str] = set()      # keyframes that scale something up from < 1
        self.origin_tokens: set[str] = set()  # class/id tokens of selectors that set transform-origin
        for b in blocks:
            m = re.search(r"@(?:-webkit-)?keyframes\s+([\w-]+)", b.at, re.I)
            if m and any(p == "transform" and self.scale_below_one(v) for p, v, _ in b.decls):
                self.kf_scale.add(m.group(1))
            if any(p == "transform-origin" for p, _, _ in b.decls):
                self.origin_tokens.update(re.findall(r"[.#][\w-]+", b.selector.lower()))
        for b in blocks:
            self.one_block(b, vars_)

    @staticmethod
    def scale_below_one(v: str) -> bool:
        m = re.search(r"scale(?:3d|x|y)?\(\s*(-?\d*\.?\d+)", v.lower())
        return bool(m) and 0 <= float(m.group(1)) < 1

    def one_block(self, b: Block, vars_: dict[str, str]):
        sel = b.selector.lower()
        for p, v, ln in list(b.decls):  # expand the `font` shorthand into size and line-height
            m = re.match(r"(?:[\w.-]+\s+)*?(\d*\.?\d+(?:px|rem|em))(?:\s*/\s*(\d*\.?\d+(?:px|rem|em)?))?(?:\s|$)", v) if p == "font" else None
            if m:
                b.decls.append(("font-size", m.group(1), ln))
                if m.group(2):
                    b.decls.append(("line-height", m.group(2), ln))
        d = {p: (v, ln) for p, v, ln in b.decls}
        in_kf = "@keyframes" in b.at.lower() or "@-webkit-keyframes" in b.at.lower()
        is_text_sel = bool(re.search(r"(^|[\s,>+~])(p|li|body|article|blockquote|dd|td)\b|prose|body-text|\.copy|\.lead|\.desc|\.text\b", sel))
        is_head = bool(re.search(r"\bh[1-6]\b|title|heading|display|headline|hero|logo|\.num|stat|metric|price|badge|btn|button", sel))
        is_ui = bool(re.search(r"(^|[\s,>+~])(a|button|label|th|td|nav|input|select|summary)\b|btn|button|nav|label|meta|caption|\btab|badge|chip|timecode|link", sel))

        for prop, val, ln in b.decls:
            v = val.lower()
            # side-tab / border-accent-on-rounded
            m = re.fullmatch(r"border-(left|right|inline-start|inline-end)(?:-width)?", prop)
            if m and not in_kf:
                width = size_px(v)
                colored = prop.endswith("-width") or not re.search(r"\b(none|transparent|0)\b", v)
                if width and width >= 2 and colored and "blockquote" not in sel and "::before" not in sel and "::after" not in sel:
                    self.add("side-tab", ln, f"{prop}: {val}")
                    rad = d.get("border-radius")
                    if rad and (size_px(rad[0]) or 0) >= 4:
                        self.add("border-accent-on-rounded", ln, f"radius {rad[0]}")
            # overused font
            if prop == "font-family":
                first = re.split(r",", v)[0].strip().strip("'\"")
                if first in OVERUSED:
                    self.add("overused-font", ln, first)
            # gradients
            if prop in ("background", "background-image") or "gradient" in v:
                if re.search(r"(linear|radial|conic)-gradient", v):
                    self.gradient_rules(b, d, prop, val, ln, vars_)
                if "repeating-linear-gradient" in v or "repeating-radial-gradient" in v:
                    self.add("repeating-stripes-gradient", ln)
            if prop in ("background-clip", "-webkit-background-clip") and "text" in v:
                bg = " ".join(x[0] for k, x in d.items() if k in ("background", "background-image")).lower()
                if "gradient" in bg:
                    self.add("gradient-text", ln)
            # bounce / elastic easing
            if prop in ("transition", "transition-timing-function", "animation", "animation-timing-function", "--ease", "--easing") or "ease" in prop:
                for cb in re.findall(r"cubic-bezier\(([^)]*)\)", v):
                    nums = [float(x) for x in re.findall(r"-?\d*\.?\d+", cb)]
                    if len(nums) == 4 and (nums[1] > 1.05 or nums[3] > 1.05 or nums[1] < -0.05 or nums[3] < -0.05):
                        self.add("bounce-easing", ln, f"cubic-bezier({cb.strip()})")
                if re.search(r"bounce|elastic|spring\(", v) and "animate-" not in v:
                    self.add("bounce-easing", ln, v[:40])
                if "linear(" in v and re.search(r"linear\([^)]{80,}\)", v):
                    self.add("bounce-easing", ln, "linear() easing curve; check it does not overshoot")
            # layout animation
            if prop in ("transition", "transition-property"):
                if re.search(r"(^|[\s,])(width|height|top|left|right|bottom|margin[\w-]*|padding[\w-]*|max-height|min-height)\b", v):
                    self.add("layout-animation", ln, v[:50])
                if re.search(r"(^|[\s:])all\b", v) and prop == "transition" or v.strip() == "all":
                    self.add("transition-all", ln)
            if in_kf and prop in ("width", "height", "top", "left", "right", "bottom", "margin", "padding") and not b.selector.startswith("["):
                self.add("layout-animation", ln, f"keyframe sets {prop}")
            # glass
            if prop in ("backdrop-filter", "-webkit-backdrop-filter") and "blur" in v:
                self.add("glassmorphism", ln, v[:40])
            # shadows
            if prop in ("box-shadow", "text-shadow", "filter", "drop-shadow"):
                self.shadow_rules(b, d, prop, val, ln, vars_)
            # clip-path
            if prop == "clip-path":
                m2 = re.search(r"polygon\(([^)]*)\)", v)
                if (m2 and m2.group(1).count(",") >= 7) or "path(" in v:
                    self.add("organic-clip-path", ln, v[:50])
            # typography
            if prop == "letter-spacing":
                em = re.match(r"(-?\d*\.?\d+)(em|px|rem)", v)
                if em:
                    n = float(em.group(1))
                    emv = n if em.group(2) == "em" else n / 16 if em.group(2) == "rem" else None
                    if emv is not None and emv < -0.04:
                        self.add("extreme-negative-tracking", ln, f"{val}")
                    if emv is not None and emv > 0.05 and is_text_sel and not is_head:
                        self.add("wide-tracking", ln, f"{val} on {b.selector[:30]}")
            if prop == "text-transform" and "uppercase" in v and is_text_sel and not is_head and not is_ui:
                self.add("all-caps-body", ln, b.selector[:40])
            if prop == "text-align" and "justify" in v and "hyphens" not in " ".join(k for k in d if k == "hyphens"):
                self.add("justified-text", ln)
            if prop == "line-height" and is_text_sel and not is_head:
                n = re.fullmatch(r"(\d*\.?\d+)", v.strip())
                if n and float(n.group(1)) < 1.3:
                    self.add("tight-leading", ln, f"line-height {val}")
            if prop in ("max-width", "width") and is_text_sel:
                mm = re.fullmatch(r"(\d*\.?\d+)(ch|px|em|rem)", v.strip())
                if mm and prop == "max-width":
                    n = float(mm.group(1))
                    if (mm.group(2) == "ch" and n > 80) or (mm.group(2) == "px" and n > 900) or (mm.group(2) in ("em", "rem") and n > 56):
                        self.add("line-length", ln, f"{prop}: {val}")
            if prop == "font-size" and not in_kf:
                px = size_px(v)
                if px is not None:
                    if px < 11 and is_ui:
                        self.add("undersized-ui-text", ln, f"{val} on {b.selector[:30]}")
                    elif px < 12 and not (re.search(r"::?(before|after)|sup|sub|\.icon", sel)):
                        self.add("tiny-text", ln, f"{val} on {b.selector[:30]}", sev="P2" if px < 11 else "P3")
                    if re.search(r"(^|[\s,>+~])h1\b", sel) and px >= 120:
                        self.add("oversized-h1", ln, val)
            # pure black / white
            if prop in ("color", "background", "background-color", "border-color", "fill", "stroke"):
                if re.fullmatch(r"(#000|#000000|#fff|#ffffff|black|white|rgb\(0,\s*0,\s*0\)|rgb\(255,\s*255,\s*255\))", v.strip()):
                    self.add("pure-black-white", ln, f"{prop}: {val}")
            # outline none
            if prop in ("outline", "outline-style") and re.fullmatch(r"(none|0|0px|0 none)", v.strip()):
                self.out_none(b, ln)
        # italic serif h1
        fs, ff = d.get("font-style"), d.get("font-family")
        if fs and "italic" in fs[0].lower() and ff and re.search(r"serif|georgia|playfair|fraunces|recoleta|newsreader|garamond|times", ff[0].lower()) \
                and not re.search(r"sans-serif", ff[0].lower().split(",")[-1]) and re.search(r"h1|hero|display|headline", sel):
            self.add("italic-serif-display", fs[1], b.selector[:40])
        # marquee / pulse / cursor via animation
        anim = " ".join(x[0] for k, x in d.items() if k in ("animation", "animation-name")).lower()
        if anim:
            aln = (d.get("animation") or d.get("animation-name"))[1]
            if "marquee" in sel or "marquee" in anim or (re.search(r"infinite", anim) and re.search(r"scroll|ticker|slide", anim)):
                self.add("marquee", aln, anim[:40])
            if re.search(r"pulse|ping|beat", anim) and re.search(r"dot|status|indicator|live|badge|\.ping", sel):
                self.add("pulsing-dot", aln, b.selector[:40])
            if re.search(r"blink|caret|cursor", anim) or ("cursor" in sel and "infinite" in anim):
                self.add("blinking-cursor", aln, b.selector[:40])
        # kicker / eyebrow
        if re.search(r"eyebrow|kicker|overline|pretitle", sel):
            self.add("kicker-above-heading", b.line, b.selector[:40])
        # thin border + wide shadow
        bd, sh = d.get("border"), d.get("box-shadow")
        if bd and sh and re.match(r"\s*1px", bd[0]) and not re.search(r"\b(none|transparent)\b", bd[0]):
            nums = [float(x) for x in re.findall(r"(?<![\w#.])(\d+(?:\.\d+)?)(?:px)?(?=\s|,|$)", re.sub(COLOR_RE, "", sh[0]))]
            if len(nums) >= 3 and nums[2] >= 24:
                self.add("gpt-thin-border-wide-shadow", sh[1], f"blur {nums[2]:g}px")
        # contrast and gray on color
        self.contrast_rules(b, d, vars_)
        self.pflicht_rules(b, d, vars_, in_kf)

    # ---- D5, D7, D10 and the features of the look bundles (CSS side) ------------------------------------------
    def pflicht_rules(self, b: Block, d: dict, vars_: dict, in_kf: bool):
        sel = b.selector.lower()
        acc = self.acc
        heading_sel = bool(re.search(r"\bh[1-4]\b|display|hero|headline|title|heading|blockquote|\.lead|\bquote|\bem\b", sel))
        box_sel = bool(re.search(r"card|panel|tile|\bbox\b|modal|dialog|popover|callout|alert|toast|sheet|btn|button", sel))
        root_sel = bool(re.search(r"(^|[\s,])(html|body|:root|main|#app|\.app|#root)(\s|,|$|\{)", sel + " "))
        pop = bool(re.search(r"popover|dropdown|drop-down|menu|modal|tooltip|popup|dialog|toast|flyout|sheet|lightbox|overlay|"
                             r"\.open\b|\.is-open|\.show\b|\.visible|\.shown|\[open\]|\[data-state=.?open", sel))
        for prop, val, ln in b.decls:
            v = val.lower()
            # D5: linear timing on a movement
            if prop in ("transition", "transition-timing-function", "animation", "animation-timing-function"):
                parts = [x for x in split_top(v) if not re.match(r"\s*(visibility|pointer-events|display)\b", x)
                         and not re.search(r"(^|\s)0m?s\s+linear", x)]
                lin = [x for x in parts if re.search(r"(?<![\w-])linear(?![\w(-])", x)]
                if lin and "infinite" not in v \
                        and not re.search(r"progress|\bbar\b|meter|spinner|loader|loading|rotat|fill|ring|marquee|ticker|countdown|timer|wave|shimmer|"
                                          r"skeleton|spin|scroll|pulse|blink|typing|caret|cursor|gauge|track", sel + " " + v):
                    self.add("linear-easing", ln, lin[0][:50])
            # D7: scale-in without transform-origin
            if not in_kf and pop and "transform-origin" not in d and (
                    (prop == "transform" and self.scale_below_one(val)) or (prop == "scale" and self.scale_below_one("scale(" + v + ")"))
                    or (prop in ("animation", "animation-name") and any(k in v for k in self.kf_scale))):
                if not (set(re.findall(r"[.#][\w-]+", sel)) & self.origin_tokens):
                    self.add("scale-no-origin", ln, f"{prop}: {val[:40]}")
            # D10: emoji in CSS content
            if prop == "content" and EMOJI_RE.search(val):
                self.add("emoji-in-text", ln, f"content: {val[:20]}")
            # cramped padding on containers
            last = [re.split(r"[\s>+~]+", part.strip())[-1] for part in sel.split(",") if part.strip()]
            if prop == "padding" and not in_kf and any(
                    re.search(r"card|panel|tile|modal|dialog|popover|callout|alert|toast|\bbox\b|sheet", x)
                    and not re.search(r"btn|button|chip|badge|pill|tag|icon|input|nav|toolbar|dot|avatar|cell|tab|^th$|^td$|row|item", x) for x in last):
                nums = [float(n) * (1 if u == "px" else 16) for n, u in re.findall(r"(-?\d*\.?\d+)(px|rem|em)\b", v)]
                nz = [n for n in nums if n > 0]
                if nz and max(nz) < 10 and "var(" not in v:
                    self.add("cramped-padding", ln, f"padding: {val}")
            # --- features of bundles ---
            for c in COLOR_RE.findall(val):
                col = parse_color(c, vars_)
                if not col or col[3] < 0.5:
                    continue
                h, sat, vv = hsv(col)
                if 8 <= h <= 24 and 0.45 <= sat <= 0.80 and 0.55 <= vv <= 0.92 and (prop.startswith("--") or prop in (
                        "color", "background", "background-color", "background-image", "border", "border-color", "fill", "stroke", "accent-color")):
                    acc.setdefault("terra", []).append((ln, prop.startswith("--")))
                if sat >= 0.70 and vv >= 0.85 and (70 <= h <= 200 or 270 <= h <= 330) and (prop.startswith("--") or prop in (
                        "color", "background", "background-color", "background-image", "border", "border-color", "fill", "stroke", "box-shadow", "text-shadow")):
                    acc.setdefault("neon", []).append(ln)
            if prop in ("background", "background-color") or (prop.startswith("--") and re.search(r"^--(bg|background|base|canvas|page)", prop)):
                m = re.match(r"\s*(#[0-9a-f]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)|var\([^)]*\))", v)
                col = parse_color(m.group(1), vars_) if m else None
                if col and col[3] >= 0.95 and luminance(col) < 0.012 and (root_sel or prop.startswith("--")):
                    self.feat("neon", "Fast-Schwarz", ln)
                if col and col[3] >= 0.95 and luminance(col) > 0.7 and 25 <= hsv(col)[0] <= 55 and 0.04 <= hsv(col)[1] <= 0.25 \
                        and (root_sel or prop.startswith("--")):
                    self.feat("creme", "Creme-Grund", ln)
            if prop in ("border-top", "border-bottom", "border-block-start", "border-block-end") and re.match(r"\s*(1|0?\.5)px\b", v) \
                    and not re.search(r"\b(none|transparent)\b", v):
                acc.setdefault("hair", []).append(ln)
            if prop == "text-transform" and "uppercase" in v:
                ls = d.get("letter-spacing")
                fs = d.get("font-size")
                lsv = re.match(r"(-?\d*\.?\d+)(em|px|rem)", ls[0].lower()) if ls else None
                lse = (float(lsv.group(1)) if lsv.group(2) == "em" else float(lsv.group(1)) / 16) if lsv else 0
                fpx = size_px(fs[0].lower()) if fs else None
                if lse >= 0.06 and fpx is not None and fpx <= 13.5:
                    acc.setdefault("caps", []).append(ln)
            if prop == "font-weight" and re.fullmatch(r"(800|900|black|extrabold|heavy)", v.strip()) and (heading_sel or box_sel):
                acc.setdefault("heavy", []).append(ln)
            if prop in ("border", "border-width") and box_sel and not in_kf:
                m = re.match(r"\s*(\d*\.?\d+)px\b", v)
                if m and float(m.group(1)) >= 3 and not re.search(r"\b(none|transparent)\b", v):
                    acc.setdefault("thick", []).append(ln)
            if prop == "border-radius" and not in_kf:
                m = re.fullmatch(r"\s*(\d*\.?\d+)(px|rem)\s*|\s*var\(\s*(--[\w-]+)[^)]*\)\s*", v)
                if m:
                    px = float(m.group(1)) * (1 if m.group(2) == "px" else 16) if m.group(1) else (
                        size_px(vars_.get(m.group(3), "")) or 0)
                    if 8 <= px <= 64:
                        acc.setdefault("radius", []).append((ln, round(px, 1)))
            if prop == "font-family" or (prop.startswith("--") and re.search(r"serif|display|heading|title", prop)):
                first = re.split(r",", v)[0].strip().strip("'\"")
                last = v.split(",")[-1].strip().strip("'\"")
                serif = any(first.startswith(x) for x in SERIFS) or (last == "serif" and first not in ("inter", "roboto", "geist"))
                if serif and (heading_sel or root_sel or prop.startswith("--")):
                    self.feat("creme", "Serif", ln)
                    if "italic" in (d.get("font-style") or ("", 0))[0].lower() and heading_sel:
                        self.feat("zeitung", "kursive Serif", ln)
            if prop == "text-align" and "center" in v and re.search(r"\bh1\b|hero|headline|display", sel):
                acc.setdefault("center", []).append(ln)
            if prop == "font-size" and re.search(r"(^|[\s,>+~])h1\b|hero.*(title|headline|h1)|display|headline", sel) and not in_kf:
                px = size_px(v)
                if px and px >= 56:
                    acc.setdefault("giant", []).append(ln)

    def finish_css(self):
        """Counters of the CSS side that turn into bundle features (thresholds calibrated on 20 mockups, p13-bericht)."""
        acc = self.acc
        terra = acc.get("terra", [])
        if any(var for _, var in terra) or len(terra) >= 2:
            self.feat("creme", "Terrakotta", terra[0][0])
        if len(acc.get("neon", [])) >= 2:
            self.feat("neon", "Neon", acc["neon"][0])
        if len(acc.get("hair", [])) >= 4:
            self.feat("zeitung", "Haarlinien", acc["hair"][0])
        if len(acc.get("caps", [])) >= 2:
            self.feat("zeitung", "Versalien-Etiketten", acc["caps"][0])
        if len(acc.get("heavy", [])) >= 2:
            self.feat("kasten", "schwere Schrift", acc["heavy"][0])
        if len(acc.get("thick", [])) >= 2:
            self.feat("kasten", "dicke Rahmen", acc["thick"][0])
        rad = acc.get("radius", [])
        if len(rad) >= 5 and len({r for _, r in rad}) == 1:
            self.feat("karte", "ein Radius überall", rad[0][0])
        if acc.get("giant") and acc.get("center"):
            self.feat("saas", "zentrierte Riesenzeile", acc["giant"][0])

    def out_none(self, b: Block, ln: int):
        """outline:none is fine when the same selector or the file sets a focus style; flag otherwise."""
        sel = b.selector.lower()
        if ":focus-visible" in sel or ":focus" in sel and self.flags.get("focus_visible_text"):
            return
        if self.flags.get("focus_visible_text"):
            return
        self.add("outline-none", ln, b.selector[:40])

    def gradient_rules(self, b, d, prop, val, ln, vars_):
        v = val.lower()
        cols = [parse_color(c, vars_) for c in COLOR_RE.findall(val)]
        cols = [c for c in cols if c]
        violet = [c for c in cols if (lambda h: 255 <= h[0] <= 310 and h[1] > 0.35 and h[2] > 0.3)(hsv(c))]
        if "linear-gradient" in v and violet and "url(" not in v.split("linear-gradient")[0][-1:]:
            self.add("ai-color-palette", ln, "violet gradient")
        if "radial-gradient" in v and cols and "transparent" in v or ("radial-gradient" in v and any(c[3] < 0.05 for c in cols)):
            chroma = [c for c in cols if c[3] > 0.1 and hsv(c)[1] > 0.4 and hsv(c)[2] > 0.4]
            if chroma and re.search(r"(^|[\s,(])(\d+px|circle|ellipse|at |closest|farthest)", v):
                self.add("radial-halo", ln, v[:50])
        if "url(" in v and "gradient" in v:
            alphas = [c[3] for c in cols]
            if alphas and min(alphas) >= 0.85 and v.index("gradient") < v.index("url("):
                self.add("buried-raster", ln)
        lin = len(re.findall(r"linear-gradient", v))
        if lin >= 2 and re.search(r"\b1px\b", v) and "background-size" in {k for k in d}:
            self.add("codex-grid-background", ln)
        if "radial-gradient" in v and re.search(r"\bat\b", v) and ("transparent" in v or any(c[3] < 0.05 for c in cols)) \
                and not any(f["rule"] == "radial-halo" and f["line"] == ln for f in self.out):
            for kind, args in gradient_calls(v):
                st = [stop_color(x, vars_) for x in gradient_stops(args)]
                if kind == "radial" and re.search(r"\bat\b", args.split(",")[0]) and any(c and c[3] < 0.05 for c in st):
                    self.add("radial-spotlight-glow", ln, v[:50])
                    break
        self.simple_gradient(b, prop, val, ln, vars_)

    def simple_gradient(self, b, prop, val, ln, vars_):
        """D11: a gradient of two or three opaque stops as a surface, unless it shows light, depth, data or a photo."""
        sel = b.selector.lower()
        if not (prop.startswith("background") or prop in ("border-image", "border-image-source")):
            return
        if re.search(r"heat|legend|scale|gauge|spectrum|chart|ramp|swatch|picker|skeleton|shimmer|progress|\bbar\b|meter|scrim|vignette", sel):
            return
        if "url(" in val.lower() or "mask" in prop:
            return
        for kind, args in gradient_calls(val):
            if kind.startswith("repeating"):
                continue
            stops = gradient_stops(args)
            if len(stops) not in (2, 3):
                continue
            cols = [stop_color(x, vars_) for x in stops]
            if any(c is None or c[3] < 0.95 for c in cols):
                continue
            why = flat_gradient(cols)
            if why:
                self.add("simple-gradient", ln, f"{len(stops)} stops, {why}")
                break

    def shadow_rules(self, b, d, prop, val, ln, vars_):
        if prop == "filter" and "drop-shadow" not in val.lower():
            return
        dark = False
        bgv = (d.get("background-color") or d.get("background") or ("", 0))[0]
        bc = parse_color(bgv.split()[0], vars_) if bgv else None
        if bc:
            dark = luminance(bc) < 0.1
        for part in re.split(r",\s*(?![^()]*\))", val):
            col = None
            for c in COLOR_RE.findall(part):
                col = parse_color(c, vars_)
            nums = [float(x) for x in re.findall(r"(?<![\w#.])(-?\d*\.?\d+)(?:px)?(?=\s|$)", re.sub(COLOR_RE, "", part))]
            if len(nums) < 2:
                continue
            x, y = nums[0], nums[1]
            blur = nums[2] if len(nums) > 2 else 0
            chromatic = col is not None and not is_gray(col) and hsv(col)[1] > 0.4
            if "inset" in part:
                continue
            if chromatic and ((x == 0 and y == 0 and blur >= 6) or (dark and blur >= 8)):
                self.add("dark-glow", ln, part.strip()[:50])
            elif blur == 0 and (abs(x) >= 4 or abs(y) >= 4) and prop == "box-shadow":
                self.add("hard-offset-shadow", ln, part.strip()[:50])

    def contrast_rules(self, b, d, vars_):
        fg_raw = d.get("color")
        bg_raw = d.get("background-color") or d.get("background")
        if not fg_raw or not bg_raw or "gradient" in bg_raw[0] or "url(" in bg_raw[0]:
            return  # gradients and images are not computable
        fg = parse_color(fg_raw[0], vars_)
        bgs = COLOR_RE.findall(bg_raw[0]) or [w for w in bg_raw[0].split() if w in NAMED]
        bg = parse_color(bgs[0], vars_) if bgs else parse_color(bg_raw[0].split()[0], vars_)
        if not fg or not bg or fg[3] < 1 or bg[3] < 1:
            return
        ratio = contrast(fg, bg)
        size = size_px((d.get("font-size") or ("", 0))[0]) or 16
        bold = re.search(r"\b(bold|[6-9]00)\b", (d.get("font-weight") or ("", 0))[0])
        large = size >= 24 or (size >= 18.66 and bold)
        need = 3.0 if large else 4.5
        if ratio < need:
            self.add("low-contrast", fg_raw[1], f"{ratio:.2f}:1 ({fg_raw[0]} on {bgs[0] if bgs else bg_raw[0]})")
        elif is_gray(fg) and hsv(bg)[1] > 0.45 and 40 < sum(fg[:3]) / 3 < 215:
            self.add("gray-on-color", fg_raw[1], f"{fg_raw[0]} on {bg_raw[0]}")
        if hsv(fg)[1] > 0.6 and 170 <= hsv(fg)[0] <= 200 and luminance(bg) < 0.05 and luminance(fg) > 0.4:
            self.add("ai-color-palette", fg_raw[1], "neon cyan text on dark")
        if luminance(bg) > 0.7 and 25 <= hsv(bg)[0] <= 55 and 0.04 <= hsv(bg)[1] <= 0.25 and re.search(r"(^|[\s,])(html|body|:root|main)\b", b.selector.lower()):
            self.add("cream-palette", bg_raw[1], bg_raw[0])

    # ---- markup rules ------------------------------------------------------------------------------------------
    def markup(self, mk: Markup):
        nodes = mk.nodes
        by_tag = {}
        for n in nodes:
            by_tag.setdefault(n.tag, []).append(n)
        html = by_tag.get("html")
        if html and "lang" not in html[0].attrs:
            self.add("html-lang-missing", html[0].line)
        if html:
            vp = [n for n in by_tag.get("meta", []) if n.attrs.get("name", "").lower() == "viewport"]
            if not vp:
                self.add("viewport-meta", html[0].line, "no viewport meta")
            for n in vp:
                c = n.attrs.get("content", "").lower()
                mx = re.search(r"maximum-scale\s*=\s*([\d.]+)", c)
                if "user-scalable=no" in c.replace(" ", "") or "user-scalable=0" in c.replace(" ", "") or (mx and float(mx.group(1)) < 5):
                    self.add("viewport-meta", n.line, c)
        heads = [n for n in nodes if re.fullmatch(r"h[1-6]", n.tag)]
        prev = 0
        for h in heads:
            lv = int(h.tag[1])
            if prev and lv > prev + 1:
                self.add("skipped-heading", h.line, f"h{prev} then h{lv}")
            prev = lv
        h1 = [h for h in heads if h.tag == "h1"]
        if html and heads and len(h1) != 1:
            self.add("heading-structure", (h1[1] if len(h1) > 1 else html[0]).line, f"{len(h1)} h1")
        for n in by_tag.get("img", []):
            src = n.attrs.get("src")
            if "alt" not in n.attrs and not n.attrs.get("role") == "presentation":
                self.add("img-no-alt", n.line)
            if src is not None and re.fullmatch(r"\s*|#|about:blank|data:,?|https?://(via\.placeholder\.com|placehold\.co|picsum)[^\s]*|placeholder[\w./-]*", src.strip(), re.I):
                self.add("broken-image", n.line, f"src={src[:30]!r}")
            elif "src" not in n.attrs and not any(k.startswith(("data-src", ":src", "v-bind", "srcset")) for k in n.attrs):
                self.add("broken-image", n.line, "no src")
        for n in nodes:
            ti = n.attrs.get("tabindex", "")
            if re.fullmatch(r"[1-9]\d*", ti.strip()):
                self.add("positive-tabindex", n.line, f"tabindex={ti}")
            if n.tag in ("div", "span") and any(k in n.attrs for k in ("onclick", "@click", "v-on:click")) \
                    and not n.attrs.get("role") and "tabindex" not in n.attrs:
                self.add("clickable-div", n.line, f"<{n.tag}>")
            if n.tag == "marquee":
                self.add("marquee", n.line, "<marquee>")
            if n.tag in ("input", "select", "textarea") and n.attrs.get("type", "text").lower() not in ("hidden", "submit", "button", "reset", "image"):
                labelled = any(k in n.attrs for k in ("aria-label", "aria-labelledby", "title"))
                anc = n.parent
                while anc and not labelled:
                    if anc.tag == "label":
                        labelled = True
                    anc = anc.parent
                fid = n.attrs.get("id")
                if fid and any(l.attrs.get("for") == fid for l in by_tag.get("label", [])):
                    labelled = True
                if not labelled:
                    self.add("input-no-label", n.line, f"<{n.tag}>")
        # nested cards and identical grids
        for n in nodes:
            if is_card(n):
                anc = n.parent
                while anc and anc.tag != "#root":
                    if is_card(anc):
                        self.add("nested-cards", n.line, f"<{n.tag}> in <{anc.tag}> line {anc.line}")
                        break
                    anc = anc.parent
            cards = [c for c in n.children if is_card(c)]
            if len(cards) >= 3 and len({signature(c) for c in cards}) == 1 and len(signature(cards[0])) >= 2:
                self.add("identical-card-grid", cards[0].line, f"{len(cards)} cards")
        # classes: kicker / eyebrow / chips / pulse / marquee / tailwind
        for n in nodes:
            cl = " ".join(n.classes).lower()
            if re.search(r"\b(eyebrow|kicker|overline|pretitle)\b", cl):
                nxt = self.next_heading(n)
                self.add("kicker-above-heading", n.line, f"class={cl[:30]}")
                if nxt and nxt.tag == "h1":
                    self.add("hero-eyebrow-chip", n.line)
            self.tailwind(n, cl)
        # text rules
        copy = " ".join(t for t, _ in mk.texts)
        self.copy_rules(mk, copy)
        self.pflicht_markup(mk, nodes, by_tag)
        # svg illustration
        for n in by_tag.get("svg", []):
            prims = [c for c in walk(n) if c.tag in ("circle", "rect", "ellipse", "polygon", "line", "polyline")]
            vb = re.findall(r"[\d.]+", n.attrs.get("viewbox", ""))
            big = (len(vb) == 4 and float(vb[2]) >= 300) or (re.match(r"\d+", n.attrs.get("width", "")) and int(re.match(r"\d+", n.attrs["width"]).group()) >= 300)
            if len(prims) >= 14 and big:
                self.add("shape-assembled-illustration", n.line, f"{len(prims)} primitives")

    def pflicht_markup(self, mk: Markup, nodes: list[Node], by_tag: dict):
        """D8, D10, D11 (SVG gradients) and the markup features of the look bundles."""
        # D10: emoji in visible text, attributes, script strings
        for t, ln in mk.texts:
            m = EMOJI_RE.search(t)
            if m:
                self.add("emoji-in-text", ln, f"{m.group(0)!r} in text")
        for n in nodes:
            for k in ("alt", "title", "aria-label", "placeholder", "value", "label"):
                m = EMOJI_RE.search(n.attrs.get(k, ""))
                if m:
                    self.add("emoji-in-text", n.line, f"{m.group(0)!r} in {k}")
        for body, ln0 in mk.scripts:
            for i, row in enumerate(body.split("\n")):
                if "console." in row or row.lstrip().startswith("//"):
                    continue
                m = EMOJI_RE.search(row)
                if m:
                    self.add("emoji-in-text", ln0 + i, f"{m.group(0)!r} in script string")
        # D8: numbers that are compared or change, tabular-nums nowhere
        if not re.search(r"tabular-nums|tnum|font-variant-numeric", self.text):
            num = re.compile(r"[+\-\u2212]?\s*[\u20ac$\u00a3]?\s*\d[\d .,:'\u2019]*\s*(?:%|\u20ac|\$|\u00a3|[A-Za-z]{1,4}\.?)?")
            cls = re.compile(r"(^|[-_])(price|amount|total|counter|timer|clock|kpi|metric|betrag|preis|summe)([-_]|$)|stat-?(value|num|number)", re.I)
            hits = [n for n in nodes if (n.tag in ("td", "th") and num.fullmatch(n.text.strip() or "x"))
                    or (any(cls.search(c) for c in n.classes) and re.search(r"\d", n.text))]
            if len(hits) >= 2:
                self.add("no-tabular-nums", hits[0].line, f"{len(hits)} numeric cells/elements")
        # D11: SVG gradient of two or three opaque stops
        for g in by_tag.get("lineargradient", []) + by_tag.get("radialgradient", []):
            stops = [c for c in g.children if c.tag == "stop"]
            if len(stops) not in (2, 3):
                continue
            cols = []
            for st in stops:
                col = st.attrs.get("stop-color") or (re.search(r"stop-color:\s*([^;]+)", st.attrs.get("style", "")) or [None, ""])[1]
                op = st.attrs.get("stop-opacity") or (re.search(r"stop-opacity:\s*([^;]+)", st.attrs.get("style", "")) or [None, "1"])[1]
                try:
                    opv = float(op)
                except ValueError:
                    opv = 1.0
                c = stop_color(col or "", None) if col else None
                cols.append(None if (c is None or opv < 0.95) else c)
            if all(cols):
                why = flat_gradient(cols)
                if why:
                    self.add("simple-gradient", g.line, f"svg {len(stops)} stops, {why}")
        # bundle features in markup: two buttons beside the heading, band of key figures, same reveal
        btn = re.compile(r"(^|[-_])(btn|button|cta)([-_]|$)", re.I)
        for n in nodes:
            kids = [c for c in n.children]
            if len(kids) == 2 and all(c.tag == "button" or (c.tag in ("a", "button") and any(btn.search(x) for x in c.classes)) for c in kids):
                anc, depth = n.parent, 0
                while anc and anc.tag != "#root" and depth < 4:
                    if any(x.tag == "h1" for x in walk(anc)):
                        self.feat("saas", "zwei Knöpfe", n.line)
                        break
                    anc, depth = anc.parent, depth + 1
            stat = [c for c in kids if any(re.search(r"(^|[-_])(stat|stats|metric|kpi|counter|figure)([-_]|$)", x, re.I) for x in c.classes)]
            if len(stat) >= 3 and all(re.search(r"\d", " ".join(x.text for x in walk(c))) for c in stat):
                self.feat("saas", "Kennzahlenband", n.line)
        rev = [n for n in nodes if any(re.search(r"(^|[-_])(reveal|fade-?up|fade-?in|animate-in|aos|appear|slide-up)([-_]|$)", x, re.I) for x in n.classes)
               or any(k in n.attrs for k in ("data-aos", "data-reveal", "data-animate"))]
        if len(rev) >= 4:
            self.feat("karte", "gleiche Einblendung", rev[0].line)

    @staticmethod
    def next_heading(n: Node):
        """The next sibling element when it is a heading."""
        if not n.parent:
            return None
        sib = n.parent.children
        i = sib.index(n)
        return sib[i + 1] if i + 1 < len(sib) and re.fullmatch(r"h[1-6]", sib[i + 1].tag) else None

    def tailwind(self, n: Node, cl: str):
        """Utility-class forms of the CSS rules."""
        if re.search(r"\bborder-[lr]-(2|4|8)\b|\bborder-(s|e)-(2|4|8)\b", cl) and not re.search(r"border-[lr]-(transparent|none)", cl):
            self.add("side-tab", n.line, "tailwind border-l/r-N")
            if "rounded" in cl:
                self.add("border-accent-on-rounded", n.line)
        if "bg-clip-text" in cl and re.search(r"bg-gradient|from-", cl):
            self.add("gradient-text", n.line, "tailwind bg-clip-text")
        if re.search(r"\banimate-bounce\b", cl):
            self.add("bounce-easing", n.line, "animate-bounce")
        if "animate-pulse" in cl or "animate-ping" in cl:
            if re.search(r"\b(w|h)-[1-3]\b", cl) and "rounded-full" in cl:
                self.add("pulsing-dot", n.line)
        if re.search(r"\bbackdrop-blur", cl):
            self.add("glassmorphism", n.line, "tailwind backdrop-blur")
        if re.search(r"\btext-\[(\d+(?:\.\d+)?)px\]", cl):
            px = float(re.search(r"\btext-\[(\d+(?:\.\d+)?)px\]", cl).group(1))
            if px < 12:
                self.add("tiny-text", n.line, f"{px:g}px")
        if re.search(r"\b(text|bg)-(black|white)\b", cl):
            self.add("pure-black-white", n.line, "tailwind black/white")
        if re.search(r"\btransition-all\b", cl):
            self.add("transition-all", n.line)
        m = re.search(r"\bbg-(?:gradient|linear)-to-\w+\b", cl)
        if m and "bg-clip-text" not in cl:
            ends = re.findall(r"(?<![:\w-])(from|via|to)-([a-z]+)(?:-\d+)?(/\d+)?(?=\s|$)", cl)
            if 2 <= len(ends) <= 3 and not any(o or c == "transparent" for _, c, o in ends):
                neutral = {"white", "black", "gray", "slate", "zinc", "neutral", "stone"}
                fam = {"neutral" if c in neutral else c for _, c, _ in ends}
                if len(fam) >= 2:
                    self.add("simple-gradient", n.line, "tailwind " + " ".join(f"{k}-{c}" for k, c, _ in ends))
        if re.search(r"\b(from|via|to)-(purple|violet|fuchsia|indigo)-\d", cl) and "gradient" in cl:
            self.add("ai-color-palette", n.line, "tailwind violet gradient")
        if re.search(r"\boutline-none\b|\bfocus:outline-none\b", cl) and not re.search(r"focus(-visible)?:(ring|outline|border|shadow)", cl):
            self.add("outline-none", n.line, "tailwind outline-none")

    def copy_rules(self, mk: Markup, copy: str):
        em = copy.count("—") + copy.count(" – ") + copy.count(" -- ")
        if em >= 8 and len(copy) / max(em, 1) <= 500:
            self.add("em-dash-overuse", mk.texts[0][1] if mk.texts else 1, f"{em} dashes in {len(copy)} chars")
        elif em >= 6 and len(copy) / max(em, 1) <= 700:
            self.feat("text", "Gedankenstriche", mk.texts[0][1] if mk.texts else 1)
        for t, ln in mk.texts:
            m = BUZZ.search(t) or BUZZ_DE.search(t)
            if m:
                self.add("marketing-buzzword", ln, m.group(0))
            if re.search(r"\b\w+ theat(?:er|re)\b", t, re.I) and re.search(r"security|compliance|innovation|productivity|process|agile|\bis\b|\bjust\b|\bpure\b", t, re.I):
                self.add("theater-slop-phrase", ln, re.search(r"\b\w+ theat(?:er|re)\b", t, re.I).group(0))
        hits = re.findall(r"\bNot an? [^.!?]{2,40}[.,] (?:It'?s |But )?(?:an? |the )?[^.!?]{2,40}[.!]|\b[A-Z][^.!?]{3,40}\. (?:No|Just) [^.!?]{2,30}\.", copy)
        de = re.findall(r"\bnicht\s+(?!nur\b)[^.!?;:]{2,50}?,?\s+sondern\b", copy, re.I)
        if len(hits) + len(de) >= 3:
            self.add("aphoristic-cadence", 1, f"{len(hits) + len(de)} turns, e.g. {(hits + de)[0][:40]!r}")
        elif len(de) >= 2:
            self.feat("text", "nicht X, sondern Y", 1)
        nums = [(t, ln) for t, ln in mk.texts if re.fullmatch(r"\s*0?\d{1,2}\s*[./]?\s*", t) and t.strip().startswith("0")]
        if len(nums) >= 3:
            self.add("numbered-section-labels", nums[0][1], f"{len(nums)} labels")

    # ---- file level --------------------------------------------------------------------------------------------
    def run(self):
        text = self.text
        markup_file = self.ext in (".html", ".htm", ".vue", ".svelte", ".jsx", ".tsx", ".svg")
        blocks: list[Block] = []
        vars_: dict[str, str] = {}
        mk = None
        if self.ext == ".css":
            blocks, vars_ = parse_css(text)
        elif markup_file:
            mk = Markup()
            try:
                mk.feed(text)
            except Exception:  # malformed markup: keep what parsed so far
                pass
            for css, ln in mk.styles:
                bl, vs = parse_css(css, ln)
                blocks += bl
                vars_.update(vs)
            # inline style attributes
            for n in mk.nodes:
                st = n.attrs.get("style")
                if st:
                    bl, _ = parse_css("[style]{" + st + "}", n.line)
                    blocks += bl
            if self.ext in (".jsx", ".tsx"):
                blocks += jsx_blocks(text)
        else:
            blocks += jsx_blocks(text)
        all_css = "\n".join(f"{b.selector}{{{';'.join(p + ':' + v for p, v, _ in b.decls)}}}" for b in blocks)
        self.flags["focus_visible_text"] = bool(re.search(r":focus(-visible|-within)?\b", all_css + text if self.ext == ".css" else all_css))
        self.css_rules(blocks, vars_)
        self.read_design_ok()
        if mk:
            self.markup(mk)
            self.file_level(mk, blocks)
            self.extra_markup(mk, blocks)
        elif self.ext == ".css":
            self.flags.setdefault("css_files", []).append(self)
        self.extra_text(mk)
        self.will_change(blocks)
        self.finish_css()
        self.flags["reduced_any"] = self.flags.get("reduced_any") or ("prefers-reduced-motion" in text)
        self.flags["focus_any"] = self.flags.get("focus_any") or self.flags["focus_visible_text"]
        return self.out

    # ---- rules from the review of 2026-11-20 (Vercel guide, old design skill); each fires only on a clear signal ---------------
    NAV_JS = re.compile(r"\b(?:window\.)?location(?:\.href|\.assign|\.replace)?\s*=[^=]|location\.(?:assign|replace)\(|"
                        r"window\.open\(|\brouter\.(?:push|replace)\(|\bnavigate\(|\bnavigateTo\(", re.I)
    FIELD_TYPES = ("text", "email", "tel", "url", "password", "number", "search", "date")
    ID_TYPES = ("email", "tel", "url", "password")

    def extra_markup(self, mk: Markup, blocks: list[Block]):
        nodes = mk.nodes
        css_text = "\n".join(c for c, _ in mk.styles)
        linked = any(n.tag == "link" and "stylesheet" in n.attrs.get("rel", "") for n in nodes) or "@import" in self.text
        html = [n for n in nodes if n.tag == "html"]
        for n in nodes:
            spread = any(k.startswith(("{", "...", "v-bind")) for k in n.attrs)
            for k in ("onpaste", "@paste", "v-on:paste"):
                if k in n.attrs and re.search(r"preventDefault|return\s+false", n.attrs[k]):
                    self.add("paste-blocked", n.line, f"<{n.tag}>")
            if any(k.startswith(("@paste.", "v-on:paste.")) and "prevent" in k for k in n.attrs):
                self.add("paste-blocked", n.line, f"<{n.tag}>")
            if "autofocus" in n.attrs:
                self.add("autofocus", n.line, f"<{n.tag}>")
            if n.tag in ("input", "textarea", "select") and not spread:
                t = n.attrs.get("type", "text").lower() if n.tag == "input" else n.tag
                if n.tag == "input" and t not in self.FIELD_TYPES:
                    pass
                elif t == "search" or n.attrs.get("role") == "searchbox":
                    pass
                elif "name" not in n.attrs:
                    self.add("field-attrs-missing", n.line, f"<{n.tag}> without name")
                elif t in self.ID_TYPES and "autocomplete" not in n.attrs:
                    self.add("field-attrs-missing", n.line, f"<{n.tag} type={t}> without autocomplete")
            if n.tag != "a":
                for k in ("onclick", "@click", "v-on:click"):
                    if k in n.attrs and self.NAV_JS.search(n.attrs[k]):
                        self.add("onclick-navigation", n.line, f"<{n.tag}>")
            if n.tag == "video" and "autoplay" in n.attrs and not ("muted" in n.attrs and "playsinline" in n.attrs):
                self.add("video-autoplay-attrs", n.line, "autoplay without muted/playsinline")
            if n.tag == "img" and re.search(r"\.gif(?:[?#]|$)", n.attrs.get("src", ""), re.I):
                self.add("gif-image", n.line, n.attrs["src"][:40])
            if n.tag == "svg" and "aria-hidden" not in n.attrs and not any(k in n.attrs for k in ("aria-label", "aria-labelledby", "title")) \
                    and n.attrs.get("role") not in ("img", "graphics-symbol", "presentation", "none") \
                    and not any(c.tag == "title" for c in n.children):
                vb = re.findall(r"[\d.]+", n.attrs.get("viewbox", ""))
                w = re.match(r"\d+(?:\.\d+)?", n.attrs.get("width", ""))
                size = float(w.group()) if w else (float(vb[2]) if len(vb) == 4 else None)
                if size is not None and size <= 48:
                    self.add("icon-no-aria-hidden", n.line, f"{size:g}px svg")
        imgs = [n for n in nodes if n.tag == "img"]
        for i, n in enumerate(imgs):
            lazy = n.attrs.get("loading", "").lower() == "lazy"
            anc, in_hero = n.parent, False
            while anc and anc.tag != "#root":
                if re.search(r"\bhero\b", " ".join(anc.classes).lower() + " " + anc.attrs.get("id", "").lower()):
                    in_hero = True
                anc = anc.parent
            if in_hero and lazy:
                self.add("hero-img-lazy", n.line)
            elif i >= 3 and "loading" not in n.attrs and "fetchpriority" not in n.attrs and not in_hero:
                self.add("img-no-lazy", n.line, f"image no. {i + 1}")
        if html:
            metas = [n for n in nodes if n.tag == "meta"]
            if not any(m.attrs.get("name", "").lower() == "theme-color" for m in metas):
                self.add("theme-color-missing", html[0].line)
            if not linked and not re.search(r"color-scheme\s*:", css_text) \
                    and not any(m.attrs.get("name", "").lower() == "color-scheme" for m in metas):
                self.add("color-scheme-missing", html[0].line)
            vps = [m for m in metas if m.attrs.get("name", "").lower() == "viewport"]
            if vps and "env(safe-area-inset" in css_text and not any("viewport-fit" in v.attrs.get("content", "").lower() for v in vps):
                self.add("viewport-fit-missing", vps[0].line)
            ids = {n.attrs.get("id") for n in nodes if n.attrs.get("id")}
            links = [n for n in nodes if n.tag == "a" and re.fullmatch(r"#[\w-]+", n.attrs.get("href", "")) and n.attrs["href"][1:] in ids]
            bar = [b for b in blocks if re.search(r"header|nav|topbar|navbar", b.selector.lower())
                   and any(p == "position" and v.strip().lower() in ("fixed", "sticky") for p, v, _ in b.decls)]
            if links and bar and not linked and not re.search(r"scroll-(margin|padding)", css_text):
                self.add("anchor-under-fixed-bar", links[0].line, f"{len(links)} anchor links, bar line {bar[0].line}")

    def extra_text(self, mk):
        """Text-level rules: @font-face without font-display, hand-built formats in scripts."""
        text = self.text
        if self.ext in (".css", ".html", ".htm", ".vue", ".svelte"):
            clean = strip_comments(text)
            for m in re.finditer(r"@font-face\s*\{([^}]*)\}", clean, re.I):
                if "font-display" not in m.group(1).lower():
                    self.add("font-display-missing", line_of(text, m.start()))
        if self.ext in (".jsx", ".tsx", ".vue", ".svelte"):  # JSX handlers hold `=>`, which the HTML parser cannot read
            for m in re.finditer(r"\bon[Pp]aste=\{[^}]*preventDefault", text):
                self.add("paste-blocked", line_of(text, m.start()), "onPaste")
            for m in re.finditer(r"<(?!(?:a|Link|NavLink)\b)([A-Za-z][\w.]*)\b[^<]*?\bonClick=\{([^}]*(?:\{[^}]*\}[^}]*)?)\}", text):
                if self.NAV_JS.search(m.group(2)):
                    self.add("onclick-navigation", line_of(text, m.start()), f"<{m.group(1)}>")
        code = []
        if self.ext in (".js", ".mjs", ".ts", ".jsx", ".tsx", ".vue", ".svelte"):
            code.append((text, 1))
        if mk:
            code += [(c, ln) for c, ln in mk.scripts if c.strip()]
        fmt = re.compile(r"getMonth\(\)\s*\+\s*1|toFixed\(\d\)\s*\)?\s*\+\s*['\"` ]*[€$£]|['\"][€$£] ?['\"]\s*\+[^;\n]{0,40}toFixed\(")
        for c, base in code:
            m = fmt.search(c)
            if m:
                self.add("no-intl-format", base + c.count("\n", 0, m.start()), m.group(0)[:30])

    def will_change(self, blocks: list[Block]):
        """will-change as a permanent style: on * / html / body, or on four or more selectors without a state."""
        state = re.compile(r":hover|:focus|:active|\.is-|\.active|\.animat|\[data-|\.open|\.show|:checked")
        hits = [b for b in blocks if any(p == "will-change" and v.strip().lower() not in ("auto", "initial", "unset") for p, v, _ in b.decls)
                and not state.search(b.selector.lower())]
        broad = [b for b in hits if b.selector.strip() in ("*", "html", "body", ":root")]
        if broad or len(hits) >= 4:
            first = (broad or hits)[0]
            self.add("will-change-static", first.line, first.selector[:30])

    def read_design_ok(self):
        """`design-ok: Qn reason` in any comment: the question's findings in this file become justified exceptions."""
        for m in DESIGN_OK_RE.finditer(self.text):
            ln = line_of(self.text, m.start())
            body = re.sub(r"(\*/|-->|\}\}|\*\}).*$", "", m.group(1)).strip()
            q = re.match(r"(Q(?:1[0-5]|[1-9])|D4)\b[\s:,\-]*(.*)$", body, re.I)
            reason = q.group(2).strip(" -:.") if q else ""
            if not q or len(reason) < 8:
                self.add("design-ok-no-reason", ln, body[:40])
            else:
                self.excuses.setdefault(q.group(1).upper(), (reason, ln))

    def file_level(self, mk: Markup, blocks: list[Block]):
        """Rules that need the whole file: focus styles, reduced motion."""
        linked = any(n.tag == "link" and "stylesheet" in n.attrs.get("rel", "") for n in mk.nodes) or "@import" in self.text
        animates = [ln for b in blocks for p, v, ln in b.decls
                    if (p in ("animation", "animation-name") and not re.match(r"\s*none", v)) or
                    (p == "transition" and not re.match(r"\s*none", v) and not re.match(r"\s*0s?\b", v))]
        kf = [b for b in blocks if "@keyframes" in b.at]
        animates = animates or [b.line for b in kf[:1]]
        reduced = "prefers-reduced-motion" in self.text
        if animates and not reduced and not (linked and self.flags.get("reduced_any")):
            self.add("reduced-motion-missing", animates[0], f"{len(animates)} animation/transition declarations")
        interactive = [n for n in mk.nodes if n.tag in ("a", "button", "input", "select", "textarea", "summary")]
        has_css = bool(blocks)
        if interactive and has_css and not self.flags["focus_visible_text"] and not linked:
            self.add("focus-styles-missing", interactive[0].line, f"{len(interactive)} interactive elements")


def postprocess(scans: list["Scan"], abgabe: bool):
    """Bundles (Q13) and `design-ok` exceptions over the scans. Returns (findings, excused findings).
    Per file by default; with abgabe all scans are one submission."""
    groups = [scans] if abgabe else [[sc] for sc in scans]
    found: list[Finding] = []
    excused: list[Finding] = []
    for g in groups:
        feats: dict[str, dict[str, dict]] = {}
        excuses: dict[str, tuple[str, int, str]] = {}
        for sc in g:
            for bid, fs in sc.feats.items():
                for name, info in fs.items():
                    cur = feats.setdefault(bid, {}).setdefault(name, {**info, "file": str(sc.path)})
                    if info["line"] < cur["line"] and cur["file"] == str(sc.path):
                        cur["line"] = info["line"]
            for q, (reason, ln) in sc.excuses.items():
                excuses.setdefault(q, (reason, ln, str(sc.path)))
        raw = [x for sc in g for x in sc.out]
        hit = {bid: fs for bid, fs in feats.items() if len(fs) >= 2}
        for bid, fs in hit.items():
            first = min(fs.values(), key=lambda i: i["line"])
            names = ", ".join(f"{n} (line {i['line']})" for n, i in sorted(fs.items(), key=lambda kv: kv[1]["line"]))
            raw.append(Finding(file=first["file"], line=first["line"], rule="bundle", severity=RULES["bundle"][0],
                               hint=f"Bundle {BUNDLES[bid]}: {names} - " + RULES["bundle"][2]))
        if len(hit) >= 2:
            first = min((min(fs.values(), key=lambda i: i["line"]) for fs in hit.values()), key=lambda i: i["line"])
            raw.append(Finding(file=first["file"], line=first["line"], rule="bundle-multi", severity=RULES["bundle-multi"][0],
                               hint="Bundles " + " + ".join(BUNDLES[b] for b in hit) + " - " + RULES["bundle-multi"][2]))
        for bid, fs in feats.items():
            if len(fs) == 1:
                (name, info), = fs.items()
                if not info["own_rule"] and name not in WEAK_FEATURES:
                    raw.append(Finding(file=info["file"], line=info["line"], rule="bundle-feature", severity="P3",
                                       hint=f"Bundle {BUNDLES[bid]}: {name} - " + RULES["bundle-feature"][2]))
        for x in raw:
            qs = [q for q in RULE_Q.get(x["rule"], ()) if q in excuses]
            if qs:
                reason, ln, fl = excuses[qs[0]]
                excused.append(Finding(**x, excuse=qs[0], reason=reason))
            else:
                found.append(x)
    return found, excused


def collect(paths: list[str]) -> list[Path]:
    """Expand arguments into files, skipping vendored and build folders."""
    out: list[Path] = []
    for p in paths:
        pp = Path(p)
        if pp.is_file():
            out.append(pp)
        elif pp.is_dir():
            for f in sorted(pp.rglob("*")):
                if f.is_file() and f.suffix.lower() in EXTS and not (set(f.relative_to(pp).parts[:-1]) & SKIP_DIRS):
                    out.append(f)
        else:
            print(f"scan_antipatterns: not found: {p}", file=sys.stderr)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Static anti-pattern scan (see file header for the rule list).")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--min", default="P3", choices=list(SEV_ORDER), help="lowest severity to report")
    ap.add_argument("--list", action="store_true", help="print all rules (static and browser-only) and exit")
    ap.add_argument("--all", action="store_true", help="do not cap repeated hits per rule and file at 5")
    ap.add_argument("--abgabe", action="store_true", help="judge bundles (Q13) over all given files as one submission, not per file")
    a = ap.parse_args(argv)
    if a.list:
        for rid, (sev, kind, hint) in RULES.items():
            print(f"{rid:30} {sev}  static   {hint}")
        for rid in BROWSER_ONLY:
            print(f"{rid:30} --  browser  hand check in audit.md / critique.md")
        return 0
    if not a.paths:
        ap.error("give a file or folder")
    files = collect(a.paths)
    flags: dict = {}
    scans: list[Scan] = []
    for f in files:
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"scan_antipatterns: {f}: {e}", file=sys.stderr)
            continue
        sc = Scan(f, txt, flags)
        sc.run()
        scans.append(sc)
    found, excused = postprocess(scans, a.abgabe)
    found = [x for x in found if SEV_ORDER[x["severity"]] <= SEV_ORDER[a.min]]
    excused = [x for x in excused if SEV_ORDER[x["severity"]] <= SEV_ORDER[a.min]]
    found.sort(key=lambda x: (x["file"], x["line"], SEV_ORDER[x["severity"]]))
    shown, hidden = [], {}
    if a.all or a.json:
        shown = found
    else:
        seen: dict = {}
        for x in found:
            k = (x["file"], x["rule"])
            seen[k] = seen.get(k, 0) + 1
            if seen[k] <= 5:
                shown.append(x)
            else:
                hidden[k] = hidden.get(k, 0) + 1
    if a.json:
        print(json.dumps({"files": len(files), "findings": shown, "excused": excused,
                          "counts": {s: sum(1 for x in found if x["severity"] == s) for s in SEV_ORDER},
                          "excused_count": len(excused)}, indent=2, ensure_ascii=False))
    else:
        for x in shown:
            print(f"{x['file']}:{x['line']}\t{x['rule']}\t{x['severity']}\t{x['hint']}")
        for (fl, r), n in hidden.items():
            print(f"{fl}\t{r}\t..\t(+{n} more, use --all)")
        by_q: dict = {}
        for x in excused:
            by_q.setdefault((x["file"], x["excuse"], x["reason"]), []).append(x)
        for (fl, q, why), xs in by_q.items():
            print(f"{fl}\tdesign-ok\tbegruendet\t{q} x{len(xs)} ({', '.join(sorted({x['rule'] for x in xs}))}): {why}")
        counts = {s: sum(1 for x in found if x["severity"] == s) for s in SEV_ORDER}
        print(f"-- {len(files)} files, {len(found)} findings: " + ", ".join(f"{s} {n}" for s, n in counts.items())
              + f", justified {len(excused)}", file=sys.stderr)
    if any(x["severity"] in ("P0", "P1") for x in found):
        return 1
    return 3 if found else 0


if __name__ == "__main__":
    sys.exit(main())

# Advanced Scroll-Driven & Choreographed Motion

This file covers layered, precisely-timed motion: scroll-triggered sequences and pinning, text-split reveals, magnetic/cursor-follow interactions, smooth-scroll setup, SVG path animation, and native view transitions. It answers "how is this built", not "what number goes in".

**The authority for curves, durations and the no-bounce/no-elastic law is [motion-doctrine.md](motion-doctrine.md)**, which holds the sourced token sets and the reasoning behind them. Every duration and easing in the snippets below is an illustrative value carried over from its upstream demo; before any of it ships, replace it with the matching token from motion-doctrine.md and from the project's MASK.md. Where the two disagree, motion-doctrine.md wins.

For motion on product surfaces (panel morphs, expanding bars, side sheets, status color, overshoot exceptions) see [product-motion.md](product-motion.md); the techniques in this file are brand-register techniques and mostly do not belong there.

**When NOT to use this.** These techniques register as *brand* moments (impeccable's brand-vs-product split): a marketing site hero, a case-study scroll story, a product-launch page. Do not add scroll-pinning, cursor-magnetism, or SVG morphs to a dense data table, an admin dashboard, a settings screen, or any high-frequency-use product surface — the motion competes with the task instead of serving it. In product UI, use at most one of these techniques, once, at a moment that matters (e.g. a single magnetic primary CTA), never as house style throughout.

---

## 1. GSAP + ScrollTrigger

**What/why.** The industry-standard timeline engine for scroll-synced sequences: pin a section, scrub a timeline against scroll position, choreograph multi-element sequences with exact overlap control (`"-=0.3"` style offsets).

**License — verified 2026-09.** As of April 29, 2025, Webflow (which now employs the GSAP/GreenSock team) made **the entire GSAP toolset free for everyone, including every plugin formerly gated behind "Club GreenSock"** — ScrollTrigger, ScrollSmoother, SplitText, MorphSVG, DrawSVG, Draggable, Flip, Physics2D, and more. Confirmed directly on gsap.com/pricing: *"GSAP is now 100% free for all users, thanks to Webflow's support."* No paid tier remains. Important nuance found in independent coverage: GSAP is **free-to-use, not open-source** — you may not decompile/repackage the source or build a competing product from it, but ordinary commercial use (client sites, SaaS products) is unrestricted at no cost. If you have older notes calling ScrollTrigger/SplitText "paid" or "Club GreenSock-only," that information is outdated as of April 2025.

**Install.**
```bash
npm install gsap
```
```js
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);
```

> Values are examples; map to the project token set from motion-doctrine.md before use.

**Minimal working example — pinned section with scrubbed timeline:**
```js
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".chapter-2",
    start: "top top",
    end: "+=150%",   // pin for 1.5x the viewport height of scroll
    scrub: 1,         // smooth-lag the scrub by 1s, don't hard-tie to scroll
    pin: true,
  },
});
tl.to(".chapter-2 .headline", { yPercent: -20, opacity: 0.4 })
  .to(".chapter-2 .diagram", { scale: 1.15, rotate: 3 }, "<")   // "<" = start with previous
  .to(".chapter-2 .caption", { opacity: 1, y: 0 }, "-=0.3");     // overlap the prior tween
```

**Avoid the template look.** Default demos scrub everything at the same rate — real sites vary scrub values per layer (background scrubs slower/`scrub: 2`, foreground text faster/`scrub: 0.5`) so depth reads as parallax, not a slideshow. Tie pin duration to actual content length, not a round `100%`. Never pin more than one section per screen's worth of scroll.

---

## 2. Lenis — smooth scroll

**What/why.** Normalizes native scroll into an eased, interruptible scroll that syncs cleanly with ScrollTrigger, WebGL scenes, and parallax — without hijacking scroll physics or breaking accessibility (keeps native scrollbar, keyboard, and wheel events working).

**License — verified 2026-09.** MIT, by **darkroom.engineering** (the team, formerly branded "Studio Freight" — same authors). Actively maintained (1000+ commits, open issues/PRs being triaged). **Package name changed**: the old `@studio-freight/lenis` is deprecated — current package is simply `lenis`. Docs/demo site also moved: `lenis.darkroom.engineering` now redirects to **lenis.dev**.

**Install.**
```bash
npm install lenis
```

> Values are examples; map to the project token set from motion-doctrine.md before use.

**Minimal working example (vanilla, paired with GSAP ScrollTrigger):**
```js
import Lenis from "lenis";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

const lenis = new Lenis({ duration: 1.1, smoothWheel: true });

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```

**Avoid the template look.** Stock demos use one global `duration` and call it done. Tune `duration` per project feel (0.8–1.4s is the usable range; below ~0.6 feels un-smoothed, above ~1.6 feels laggy/broken). Always test with a real trackpad and a mouse wheel, not just a demo GIF — over-smoothed scroll on a trackpad reads as janky, not premium. Respect `prefers-reduced-motion`: disable Lenis entirely (`lenis.destroy()` or don't instantiate) when it's set.

---

## 3. Motion (formerly Framer Motion)

**What/why.** Declarative animation for React (and a lighter vanilla-JS core) with scroll-linked values, layout animation, and spring physics — the most ergonomic option when you need React state-driven motion rather than hand-built timelines.

**License — verified 2026-09.** MIT, fully open source. **Rebrand**: the library and npm package were renamed from `framer-motion` to **`motion`** after becoming an independent project from Framer in 2025 (docs now live at motion.dev, not framer.com). The old `framer-motion` package still resolves and works but receives no further active development — new code should import from `motion/react` (React) or `motion` (vanilla).

**Install.**
```bash
npm install motion
```

> Values are examples; map to the project token set from motion-doctrine.md before use.

**Minimal working example — scroll-linked progress value (React):**
```jsx
import { motion, useScroll, useSpring } from "motion/react";

function ScrollProgress() {
  const { scrollYProgress } = useScroll();
  const smoothed = useSpring(scrollYProgress, { stiffness: 120, damping: 20 });

  return (
    <motion.div
      style={{
        scaleX: smoothed,
        transformOrigin: "0% 50%",
        position: "fixed", top: 0, left: 0, right: 0, height: 3,
      }}
    />
  );
}
```

**Avoid the template look.** Every Framer Motion tutorial fades+slides a `<div>` with `initial`/`animate` and lorem ipsum — don't ship that unmodified. Bind scroll progress to something specific to the content (a reading-progress bar tied to article length, a horizontal rail that maps 1:1 to a numbered step sequence), and stagger children with content-aware delay (`transition: { delayChildren: i * 0.04 }`) rather than a uniform stagger constant copied from docs.

---

## 4. Text-splitting / reveal — GSAP SplitText

**What/why.** Splits text into chars/words/lines as individually animatable DOM nodes for line-by-line or char-by-char reveals — the mechanism behind most "text rises into view" hero treatments.

**License — verified 2026-09.** SplitText is one of the plugins that moved from Club-GreenSock-only to **fully free** in the April 2025 Webflow change (see GSAP section above) — no separate purchase needed, same free-to-use (not open-source) terms as core GSAP.

**Install.** Ships in the same `gsap` package as of the 2025 free release:
```js
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
gsap.registerPlugin(SplitText);
```

> Values are examples; map to the project token set from motion-doctrine.md before use.

**Minimal working example (current v3.13+ API, auto re-split on resize/font-load via `onSplit`):**
```js
SplitText.create(".hero-headline", {
  type: "lines, words",
  mask: "lines",       // clips each line so it reveals from a hard edge, not a soft crop
  autoSplit: true,      // re-splits automatically on resize / webfont load
  onSplit(self) {
    return gsap.from(self.words, {
      yPercent: 110,
      duration: 0.8,
      stagger: 0.03,
      ease: "expo.out",
    });
  },
});
```

**Open alternative (no dependency):** CSS `::first-line`/manual `<span>`-wrapping per word plus `IntersectionObserver` + `animate()` (Web Animations API) — viable when you only need word-level, one-shot reveal and want zero JS dependency weight.

**Avoid the template look.** Char-by-char stagger on every headline is the single most recognizable "agency template" tell — reserve char-splitting for one hero moment per page at most; use line-level or word-level splitting (cheaper, subtler) everywhere else. Always split real, final copy — never lorem ipsum — because line-break points change the reveal rhythm.

---

## 5. Magnetic button / cursor-follow (hand-rolled, no library needed)

**What/why.** A button (or icon) that subtly pulls toward the cursor within a radius, and springs back on leave. Pure vanilla JS + CSS transform — a dedicated library is unnecessary overhead for this pattern.

**License.** N/A — no dependency.

> Values are examples; map to the project token set from motion-doctrine.md before use.

**Minimal working example:**
```html
<button class="magnetic"><span>Get started</span></button>
```
```css
.magnetic {
  transition: transform 0.15s ease-out;
  will-change: transform;
}
.magnetic span { display: inline-block; transition: transform 0.15s ease-out; }
```
```js
document.querySelectorAll(".magnetic").forEach((el) => {
  const strength = 0.35;      // fraction of offset the button itself moves
  const strengthInner = 0.6;  // inner span moves more, for a layered pull

  el.addEventListener("pointermove", (e) => {
    const r = el.getBoundingClientRect();
    const x = e.clientX - (r.left + r.width / 2);
    const y = e.clientY - (r.top + r.height / 2);
    el.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
    el.querySelector("span").style.transform =
      `translate(${x * strengthInner}px, ${y * strengthInner}px)`;
  });

  el.addEventListener("pointerleave", () => {
    el.style.transform = "translate(0, 0)";
    el.querySelector("span").style.transform = "translate(0, 0)";
  });
});
```

**Avoid the template look.** The generic version moves the whole button uniformly — layering two transforms (outer shell at lower strength, inner label/icon at higher strength) is what makes it read as considered rather than copy-pasted from a Codrops demo. Cap the pull radius (only attach the listener region to roughly 1.5× the button's own bounding box, not the whole viewport) so it doesn't feel like the button is chasing the mouse from across the screen. Never apply this to more than a small number of primary actions per screen — a page where every button is magnetic reads as broken, not premium. Respect `prefers-reduced-motion` by skipping the listener entirely.

---

## 6. View Transitions API (native, no dependency)

**What/why.** Browser-native cross-fade/morph between DOM states (SPA) or between full page loads (MPA) — captures before/after screenshots and interpolates automatically, including shared-element morphs via `view-transition-name`. Genuinely free: zero bytes of JS shipped for the mechanism itself.

**License.** N/A — web platform API.

**Browser support — verified 2026-09 (caniuse).** Global support **~91.75%**. Same-document (SPA) transitions: Chrome/Edge 111+, Safari 18+. Cross-document (MPA) transitions: Chrome/Edge 126+, Safari 18.2+. Firefox shipped support at version 144 (was behind a flag in 143) — treat Firefox cross-document support as very recent; verify against the current caniuse figure before relying on it in production, and always feature-detect.

> Values are examples; map to the project token set from motion-doctrine.md before use.

**Minimal working example — SPA same-document transition:**
```js
function navigateTo(newState) {
  if (!document.startViewTransition) {
    applyState(newState);   // no-op fallback: instant change, no error
    return;
  }
  document.startViewTransition(() => applyState(newState));
}
```
```css
/* shared-element morph: tag the element present in both before/after states */
.product-thumb { view-transition-name: product-hero; }

::view-transition-old(product-hero),
::view-transition-new(product-hero) {
  animation-duration: 0.4s;
}
```

**Avoid the template look.** The default cross-fade (no custom `::view-transition-*` rules) is instantly recognizable as unstyled default — always author at least the duration/easing for the transition pseudo-elements, and use `view-transition-name` deliberately on the one or two elements that should visibly morph (a thumbnail becoming a hero image), not blanket-applied to every element on the page. Always ship the `if (!document.startViewTransition)` fallback — this is still a progressive enhancement, not a baseline.

---

## Live lookup

- https://gsap.com/showcase/ — GSAP's own curated showcase of production sites, filterable by plugin used (ScrollTrigger, SplitText, MorphSVG, etc.)
- https://gsap.com/docs/v3/Plugins/SplitText/ — current SplitText API reference (v3.13+ `onSplit`/`autoSplit` syntax)
- https://lenis.dev/ — Lenis docs, live demo, and framework adapters (canonical URL as of 2026; darkroom.engineering domain now redirects here)
- https://motion.dev/examples — 400+ categorized Motion snippets (React/JS/Vue) across scroll, cursor, text, and 3D patterns
- https://tympanus.net/codrops/ — Codrops: long-running demo/tutorial site for exactly this category (scroll choreography, SVG morphs, text reveals), each post ships real working source
- https://developer.chrome.com/docs/web-platform/view-transitions — Chrome team's View Transitions API guide with same-document and cross-document code examples

# Performance & accessibility budget

Applies to every technique in [shaders.md](shaders.md), [3d.md](3d.md), [motion.md](motion.md), [product-motion.md](product-motion.md) and [scroll-choreography.md](scroll-choreography.md). Read this before shipping any of them: an effect that isn't budgeted is a regression, not a feature.

## The four checks, every time

1. **`prefers-reduced-motion` fallback.** Anyone with the OS setting on gets the static end-state, not a broken half-animation. Never skip this for "just one effect": it compounds across a page.

   **Not with the blanket selector.** The widely copied `*, *::before, *::after { transition-duration: 0.01ms !important }` reset is named as a failure mode by [motion-doctrine.md](motion-doctrine.md) section 5 and its checklist in section 6: it also kills focus rings, error feedback and plain fades that carried no vestibular risk, and it leaves the user with a design that is not reduced but broken. Scope the override to the motion that actually causes the problem, which is large positional change, parallax, zoom and autoplay:

   ```css
   /* Opt in per class, not globally. Large movement becomes a fade, feedback stays. */
   @media (prefers-reduced-motion: reduce) {
     .reveal-on-scroll,
     .parallax-layer,
     .marquee,
     .hero-zoom {
       animation: none;
       transition: opacity 120ms ease;
       transform: none;
     }
     html { scroll-behavior: auto; }
   }
   ```

   Focus rings, error and validation states, hover feedback and small state-change transitions stay animated: they are feedback, not decoration. The rule is "replace large motion with a fade", not "switch motion off", per motion-doctrine.md section 5.

   For JS-driven effects (GSAP, R3F, custom canvas loops), check the media query in JS and branch; don't just rely on the CSS override, since a canvas RAF loop or WebGL scene ignores CSS entirely:

   ```js
   const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
   if (prefersReducedMotion) {
     // render static frame, skip the animation loop / don't mount the Canvas at all
   }
   ```

2. **Mobile / low-power fallback.** WebGL shaders and 3D scenes are GPU cost centers. Budget:
   - Cap `devicePixelRatio`: never render a shader/3D canvas at full retina DPR. `Math.min(window.devicePixelRatio, 2)`, often even capped at 1.5 for full-viewport shader backgrounds.
   - Below a viewport-width breakpoint (typically 768px) or on a detected low-end device, swap the shader/3D layer for a static image or CSS gradient. A 3D hero that's the whole point of a desktop landing page can legitimately just not exist on mobile.
   - Never block first paint or interaction on a WebGL context or a 3D asset load. Mount the canvas after the critical content is visible, or behind a lightweight placeholder.

3. **Lazy mount, always clean up.** Shader/3D canvases must not run when off-screen or unmounted.
   - Use an `IntersectionObserver` (or your framework's viewport hook) to pause the render loop when the element scrolls out of view, resume when it scrolls back in.
   - React Three Fiber: unmounting the `<Canvas>` disposes its GL context automatically; don't keep it mounted `display: none` "for performance," that keeps the context and RAF loop alive.
   - Raw WebGL/Three.js outside React: explicitly call `renderer.dispose()`, cancel the `requestAnimationFrame` handle, and remove event listeners in a cleanup path. A leaked WebGL context is one of the few browser errors that can crash the whole tab after enough page navigations.

4. **Contrast and focus survive the effect.** A shader background or particle field must never drop text contrast below WCAG AA (4.5:1 body text) at any point in its animation cycle: check the darkest/brightest frame, not just the average. Interactive elements layered over 3D/shader content still need a visible focus ring; `outline: none` without a replacement is not acceptable because the background looks cool.

## Quick budget table

| Technique | First-paint cost | Ongoing cost | Typical fallback |
|---|---|---|---|
| CSS-only shader-adjacent (static gradients, static filters) | ~0 | Low (GPU-composited) | None needed |
| Animated `clip-path` (rounded corners) / animated SVG filter | ~0 | Paint work, not compositor work: repaints the clipped region every frame it changes (measured 41 to 45 paint events per pill, 0 for a plain `inset()` without `round`) | Keep the painted area small, cap how many can be mid-animation at once, cross-fade or instant state on reduced-motion; measure against an idle run |
| Fragment shader / WebGL background | Shader compile + GL context | Medium to high, scales with resolution | Static gradient/image below breakpoint or on reduced-motion |
| Three.js / R3F scene | Asset + scene graph load | High, scales with poly count and lights | Poster-frame image; mount only in viewport |
| GSAP ScrollTrigger sequences | Low | Low (transform/opacity only) | Instant end-state on reduced-motion |
| Particle systems (canvas2d or WebGL) | Low to medium | Scales with particle count | Cap count on mobile, disable below breakpoint |

## Sanity check before calling it done

- Throttle CPU 4x and network to Fast 3G in devtools: does the page still feel intentional, or does the effect visibly stutter/pop in?
- Toggle `prefers-reduced-motion` in devtools and reload: is the result still a complete, non-broken design?
- Run Lighthouse (mobile): a showpiece effect that tanks the performance score into the red has failed the brief, not succeeded at ambition.

## Measuring CSS-only motion: always against an idle run

For motion that is pure CSS (a `clip-path` reveal, an expanding bar, a filter animation) the budget is: **no main-thread task longer than 16 ms while the animation runs**, measured with a long-task observer or the devtools performance panel, and compared against a control recording of the same page doing nothing.

The control run is not optional. A headless renderer (Puppeteer, Playwright, CI Chrome) drops frames on its own: 20 to 25 percent of `requestAnimationFrame` intervals exceeded 16.7 ms even on an idle page, because there is no display refresh driving the loop. That range is a single measurement, not a constant: measured once on 2026-09-09 on the Windows workstation during the <internal-project> customer-file mockup (headless Chromium via Playwright); re-measure per machine before relying on it. A raw frame count or a raw "dropped frames" number from such an environment therefore says nothing about the animation. Only the delta between the animated run and the idle run is evidence.

```js
// Long-task probe, run once idle and once while the animation plays, then compare.
const tasks = []
new PerformanceObserver((list) => tasks.push(...list.getEntries().map((e) => e.duration)))
  .observe({ entryTypes: ['longtask'] })
// after the run: tasks.filter((d) => d > 16).length, and the max
```

Report both numbers (idle and animated) whenever a motion budget is claimed to pass. A single number without its control run is not a measurement, and the performance gate treats it as an unmeasured claim.

## Measuring with Playwright: a repeatable recipe

- Run under the project's own Playwright install, `NODE_PATH` pointed at the project's own `node_modules`. A globally installed Playwright resolves a different browser build and produces numbers that don't match what CI will see.
- Reading `document.styleSheets[i].cssRules` on a cross-origin stylesheet (Google Fonts and similar) throws `SecurityError` under CORS. Wrap that read in `try/catch` and skip the sheet rather than letting it abort the whole probe.
- **Forced reflow as a search pattern.** Grep the animated code path for a layout read (`offsetWidth`, `offsetHeight`, `scrollWidth`, `getBoundingClientRect`, `getComputedStyle`) placed after a style or class write in the same frame. That read-after-write order is what forces a synchronous layout mid-animation; it is the single most common cause of a `transform`/`opacity`-only animation still costing a layout pass.
- Record, for the idle run and the animated run: layout count (target 0 during a `transform`/`opacity`/`clip-path`-only animation), paint time, and the count of `requestAnimationFrame` intervals over 16.7 ms. Report the delta between the two runs, per the mandatory control run above, never either number alone.

## Scroll and resize handlers

A `scroll` or `resize` listener that reads or writes a layout property (see the forced-reflow pattern above) on every event is a budget failure regardless of how cheap a single call looks in isolation, because both events can fire many times inside a single frame. Gate visibility-driven work behind `IntersectionObserver` instead of a `scroll` listener wherever the question is "is this on screen", and throttle or `requestAnimationFrame`-batch anything that genuinely needs the live scroll or resize value.

## Accessibility checks beyond reduced motion

- **Keyboard.** Anything that reveals content on `:hover` also reveals it on `:focus-within` or `:focus`, verified with the mouse disconnected, `Tab` only.
- **Touch.** Anything gated behind `:hover` has a tap or focus equivalent, see [product-motion.md](product-motion.md) section 2 for the pattern, verified under `(hover: none)` and `(pointer: coarse)` emulation, not assumed from desktop testing.
- **Contrast under motion.** The darkest and brightest frame of any color, opacity or shader animation still clears 4.5:1 for body text, checked per [design-foundations.md](design-foundations.md) section 3, not only the resting frame.

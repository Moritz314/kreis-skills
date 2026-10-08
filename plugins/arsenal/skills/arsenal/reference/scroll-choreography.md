# Scroll Choreography

This file answers how to build scroll-driven motion once [motion-doctrine.md](motion-doctrine.md) has already established that the effect belongs and [registers.md](registers.md) confirms the `bewegung` budget covers it. It is the technique layer. [motion.md](motion.md) already documents GSAP + ScrollTrigger's basic pin/scrub API, license, Lenis, Motion, SplitText, magnetic buttons and the View Transitions API with working code, none of that is repeated here. This file covers the decisions and patterns motion.md does not: native CSS vs GSAP, the Firefox gap, dissection/explosion builds, multi-section timeline choreography, and background interaction. The performance budget in [performance.md](performance.md) applies unchanged, including its existing WebGL/3D entries.

## 1. The tool decision: native CSS scroll animations vs GSAP ScrollTrigger

"CSS Scroll-driven Animations" (`animation-timeline`, `scroll()`, `view()`, plus `scroll-timeline`, `view-timeline`, `timeline-scope`, `animation-range`) is a W3C CSS Working Group Working Draft, not yet finalized. Browser status, checked 2026-09: Chrome and Edge support it fully and unflagged since version 115 (July 2023); Safari since 26.0 (September 2025), including `animation-range`. Firefox lags: caniuse lists support from Firefox 158, while current stable in early September 2026 is 155/156: native scroll-driven animation is **not yet in Firefox stable** at the time of this research. MDN accordingly marks `animation-timeline` "Limited availability, not Baseline."

**What native gives you for zero JavaScript:** a CSS property whose progress is linearly coupled to a container's scroll position (`scroll()`) or to an element's viewport visibility (`view()`), running on the compositor thread with no main-thread blocking.

**What native cannot do, compared to a JS library:** no JS hooks or callbacks at specific scroll positions, no Web Animations API control mid-animation, no delayed "lag" scrub with smoothing, no multi-step pinning choreography across sections with named time marks, no native pattern for horizontal scroll sections, and only limited devtools debugging.

**Decision criterion.** Use native CSS for a single element whose progress is linear against scroll or visibility: a progress bar, a fade-in on appear, a simple single-element parallax. It is the right choice once Chrome, Edge and Safari cover the target audience and a Firefox fallback is planned (section 2). Reach for GSAP ScrollTrigger (documented with its pin/scrub example and its confirmed free license in [motion.md §1](motion.md)) as soon as the effect needs pinning across multiple sections, named timeline labels, or damped/lagged scrubbing, none of which the native spec offers today.

## 2. The Firefox fallback path

Because native scroll-driven animation is not yet in Firefox stable, treat it as progressive enhancement, not a baseline every visitor gets. Feature-detect with `@supports`, and design the fallback state to be a reasonable static or CSS-transition end-state, not a blank or half-built one.

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
}

@supports (animation-timeline: view()) {
  .reveal {
    animation: reveal-in linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 30%;
  }
  @keyframes reveal-in {
    to { opacity: 1; transform: translateY(0); }
  }
}

/* Firefox and any browser without support: fall back to a plain
   IntersectionObserver-triggered CSS transition, or simply show
   the element in its resting state without motion. */
@supports not (animation-timeline: view()) {
  .reveal {
    opacity: 1;
    transform: none;
  }
}
```

The `@supports not (...)` branch matters as much as the enhancement itself: a Firefox visitor should see the finished layout immediately, never a permanently-`opacity: 0` element because the triggering feature never fired.

## 3. Dissection animations (explosion diagrams)

| Build | Effort | File size / performance | Right for |
|---|---|---|---|
| CSS transform chains | Low to medium: one layer (a div) per part, moved apart with `transform`, driven natively via `animation-timeline`/`scroll()` or via GSAP ScrollTrigger with `scrub`. No 3D or illustration skill needed | Very small, only the part graphics themselves; GSAP core plus ScrollTrigger adds a few dozen KB. Runs on the compositor thread, minimal GPU load | Flat or 2D-style product depictions, icons, schematic diagrams with few layers |
| SVG groups | Medium: needs a vector illustration where each part is its own cleanly anchored `<g>` group (transform attributes inherit to child elements per MDN); the actual scroll-driving is then simple | Very small, vector, scales losslessly | Icons, diagrams, infographics, illustrative rather than photorealistic product depictions |
| Real 3D model with separated parts | High: 3D modeling, split into named nodes, camera and lighting setup, a WebGL rendering pipeline (Three.js, React Three Fiber or Babylon.js, glTF). Three.js's `GLTFLoader` returns a `THREE.Group` as `gltf.scene` whose child meshes animate individually | Highly variable; no reliable figure found for simple product models specifically. What is documented: character models at roughly 30,000 triangles with a 2K texture run 5 to 15 MB uncompressed, with Draco/Meshopt compression and KTX2 textures reaching 10 to 70 percent reduction. Requires an active WebGL context and GPU | Genuine 3D products, engineering/machine storytelling, high-end brand work |
| Image sequence | High in production: typically 60 to 150 pre-rendered frames from a 3D render farm or photo studio; the implementation itself is simple (frame index from scroll progress, `drawImage` on canvas, usually paired with GSAP scrub and pinning) | Can grow large with many high-resolution frames; needs WebP/AVIF, sprite sheets and lazy-loading of individual frames | Photorealistic product presentation, the familiar Apple product-page pattern |

**Recommendation from the research.** For schematic or illustrative decomposition, CSS chains or SVG groups are almost always the right call: small, performant, buildable without specialist tooling. A real 3D model earns its cost only when free camera movement or rotation is itself part of the message, not just the decomposition; if it is only the decomposition that matters, a pre-rendered image sequence delivers the same photorealistic result with far less runtime risk, paid for with a heavier one-time production step instead.

## 4. Pinning, scrubbing, timelines across multiple sections

[motion.md §1](motion.md) already shows the base ScrollTrigger API: `pin: true` fixes an element via `position: fixed` for the duration of its trigger phase, with an auto-generated pin-spacer holding its place in the document flow; `scrub` couples animation progress to scrollbar position instead of time (`scrub: true` for 1:1, a number like `scrub: 1` adding a second of lag that smooths jerky scrolling). What that example does not show is choreography spanning **multiple sections** with named stages.

```js
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".story",
    start: "top top",
    end: "+=300%",
    scrub: 1,
    pin: true,
  },
});

tl.addLabel("intro")
  .to(".story .part-a", { xPercent: -40 })
  .addLabel("reveal")
  .to(".story .part-b", { xPercent: 40 }, "reveal")
  .to(".story .caption-2", { opacity: 1 }, "reveal+=0.2")
  .addLabel("outro")
  .to(".story .part-a, .story .part-b", { opacity: 0 }, "outro");
```

Named labels (`addLabel`) let a multi-stage sequence be addressed by stage name rather than by absolute time, and each stage's share of scroll distance is proportional to its share of the timeline's total duration: lengthening one label's segment means adding more tweened time between labels, not touching the ScrollTrigger's own `start`/`end`.

**Pitfalls specific to multi-section choreography**, beyond what motion.md already flags (vary scrub speed per layer, tie pin duration to real content length, never pin more than one section per screen's worth of scroll):

- The auto-generated pin-spacer changes document height; measure and test scroll distance after adding content, not before, since inserting new tweens mid-timeline silently changes how much real scroll each label needs.
- Nesting a pinned section inside another pinned section (or inside a smooth-scroll wrapper like Lenis, see motion.md §2) is a common source of layout thrashing; test the two together, not in isolation.
- A timeline with many labels but a single `scrub` value flattens all stages to the same felt speed; stagger `scrub` per tracked property, not just per section, if some parts of the sequence should read as slower or heavier than others.

## 5. Background interaction

Pointer-coupled reaction, cursor-driven distortion, particle systems and WebGL backgrounds with input coupling all rest on the same documented building blocks: the Pointer Events API for cursor tracking, `<canvas>` or WebGL for particles and shaders, and shader uniforms that pass cursor position into a fragment shader to drive local distortion (the pattern is documented at trade-article level, e.g. Codrops on bulge distortion, not in a formal spec).

**Defensible:** locally scoped, cursor-coupled micro effects on individual elements such as buttons or cards, since they are typically only active during interaction and cost little outside it.

**Costly:** a fullscreen WebGL shader background running continuously. Every screen pixel is recomputed every frame (a high pixel fill-rate cost), usually inside a `requestAnimationFrame` loop, which measurably raises GPU load and battery drain on mobile.

**Mandatory fallbacks.** MDN documents that `requestAnimationFrame` automatically pauses in background tabs and hidden iframes; extend the same idea deliberately with the Intersection Observer API so a decorative loop also pauses once its element scrolls out of the viewport:

```js
const canvas = document.querySelector(".shader-bg");
let rafId = null;

const io = new IntersectionObserver(([entry]) => {
  if (entry.isIntersecting) {
    rafId = requestAnimationFrame(renderLoop);
  } else if (rafId) {
    cancelAnimationFrame(rafId);
    rafId = null;
  }
}, { threshold: 0 });

io.observe(canvas);
```

Decorative WebGL effects should also respect `prefers-reduced-motion` (per [motion-doctrine.md §5](motion-doctrine.md)); the checked research found this stated for UI animation generally but not with a literal WebGL-specific citation, so treat it as a sound extension of the general rule rather than a separately sourced one. See [performance.md](performance.md) for the DPR caps, lazy-mount rules and contrast checks that apply to every fullscreen shader or 3D layer regardless of whether it responds to the pointer.

## 6. Binding to the `bewegung` and `technik` registers

Consistent with [registers.md](registers.md); this section adds no new stop values, only what each stop means for scroll techniques specifically.

- **`bewegung: 0` or `1`.** No scroll-driven choreography of any kind, native or GSAP. Stop `1` allows functional page transitions but explicitly excludes scroll-triggered reveals.
- **`bewegung: 2`.** At most one accented scroll moment per page: a single native reveal, or one short dissection sequence. Continuous ambient motion and parallax across a long page stay forbidden at this stop, so a multi-section pinned story does not fit here.
- **`bewegung: 3`.** Full choreography is in scope: multi-section pinning, dissection, ambient background motion, all still bound by [motion-doctrine.md](motion-doctrine.md)'s purpose test and by the performance budget.
- **`technik: statisch`.** Ships no scroll-driven JavaScript. A single native CSS scroll animation (section 1) is technically CSS-only and therefore compatible with this stop, provided the Firefox gap (section 2) degrades to a static, non-broken fallback rather than a missing feature. Multi-section GSAP choreography needs scripted timeline control and does not fit `statisch`.
- **`technik: inseln`.** Required for GSAP ScrollTrigger sequences, Lenis, and any pointer-coupled canvas effect; ship as an island, not on the critical path.
- **`technik: webgl`.** Required for any fullscreen shader or 3D dissection build; always paired with the static fallback and lazy-mount discipline from [performance.md](performance.md).
- **Guard rail, restated precisely for this file:** [registers.md](registers.md) already flags `bewegung: 3` with `technik: statisch` as a contradiction, because that combination assumes full choreography while forbidding the scripted timeline control it needs. The one exception this file adds no new allowance for: a single native scroll animation at `statisch` is not "full choreography" and does not satisfy `bewegung: 3` on its own: real stop-3 work needs at least `technik: inseln`.

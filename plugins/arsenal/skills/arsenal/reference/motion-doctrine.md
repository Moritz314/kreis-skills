# Motion Doctrine

This file answers whether motion belongs on a page at all, and if it does, which motion and how long. It is the judgment layer, not the build layer. For scroll-driven sequences, text-split reveals, magnetic buttons, view transitions and smooth-scroll setup, see [motion.md](motion.md); for how to build scroll choreography specifically (native CSS vs GSAP, dissection animations, background interaction), see [scroll-choreography.md](scroll-choreography.md). The performance budget in [performance.md](performance.md) applies unchanged to everything below.

All claims trace to a checked research pass (2026-09-08). Citations below are inline and brief; consult the research file for full source URLs. A point marked unverified carries no rule weight and must not be treated as settled.

## 1. The twelve principles, honestly sorted

Frank Thomas and Ollie Johnston set out twelve principles of animation for hand-drawn Disney characters on a cinema screen (*The Illusion of Life*, Disney Editions, 1981): Squash and Stretch, Anticipation, Staging, Straight Ahead Action and Pose to Pose, Follow Through and Overlapping Action, Slow In and Slow Out, Arcs, Secondary Action, Timing, Exaggeration, Solid Drawing, Appeal. They were built for drawn characters, not for surfaces that acknowledge user input, and they do not transfer evenly.

Val Head, the standard reference for interface animation (*Designing Interface Animation*, Rosenfeld Media, 2016), warns against adopting all twelve unexamined: "Not all of the 12 principles apply equally to work on the web or to modern tools." Her own useful set, verbatim: "A solid understanding of Timing, Follow-through, Appeal, Anticipation and Squash and Stretch will be useful in web design." She names "concepts like Staging and Solid Drawing" as largely irrelevant (valhead.com, 18.01.2016).

**Corrected ranking, not the intuitive one.** Squash and Stretch sits on the useful side, against the common assumption that a body-deformation principle has no place in a flat interface. Head's reasoning is not about literal squashing: "Squash and Stretch shows how manipulating the shape of an object can suggest traits about the material it's made of." It earns its place through what it communicates about material, not through cartoon exaggeration. Staging and Solid Drawing fail for the opposite reason: both assume a camera, a stage and a drawn volume, and a flat, compositor-rendered surface has no equivalent to any of the three.

| Principle | Status | Why |
|---|---|---|
| Timing | Useful | Head's named set |
| Follow-through | Useful | Head's named set |
| Appeal | Useful | Head's named set |
| Anticipation | Useful | Head's named set |
| Squash and Stretch | Useful | Communicates material properties, not literal deformation |
| Staging | Irrelevant | Assumes a camera and a stage; no equivalent in a flat UI |
| Solid Drawing | Irrelevant | Assumes a drawn volume; no equivalent in a flat UI |
| Slow In and Slow Out | Not individually rated, but effectively load-bearing | Restated independently by both Carbon and Material as the basis of all easing curves (section 3) |
| Arcs | Ungraded, loosely grouped | No explicit source rating found. Related to Follow Through where Head names it: curved rather than linear motion paths |
| Secondary Action | Ungraded, loosely grouped | No explicit source rating found. Related to Follow Through: a supporting motion that reinforces the primary one |
| Straight Ahead vs Pose to Pose | Ungraded | No explicit source rating found in the checked literature; a production technique with no clear UI analogue either way |
| Exaggeration | Avoid by default | Contradicts Apple's and Carbon's brevity principle (section 3); reserve for deliberately playful success moments, not standard transitions |

The four ungraded rows are an explicit gap, not a quiet demotion: no source in the checked research rates them individually for interface work. Treat any claim that ranks them definitively as unsourced.

**What the useful five mean in interface practice**, staying inside what sections 2 to 4 already establish rather than adding new claims:

- **Timing** is the duration side of the token system in section 3: how long a change takes, and whether that duration matches how significant the change is.
- **Follow-through** covers a motion that continues or settles slightly after the triggering event, the same idea Slow In and Slow Out formalizes as an easing curve (section 3), and the idea Arcs and Secondary Action extend when a source names them.
- **Appeal** is not decoration; it is the same purpose test from section 2 answered well; an animation that clears the three-question chain and still feels considered has appeal, one that clears the chain but feels mechanical does not yet.
- **Anticipation** is a small, brief pre-motion cue before a larger state change, useful only where it serves orientation or feedback (section 2), not as a flourish before an already-obvious action.
- **Squash and Stretch** is the material cue from section 1 itself: a button that compresses slightly on press is suggesting give, not performing a cartoon squash, and stays inside the small-token durations from section 3.

## 2. Purpose before decoration

Material Design names four functions of motion directly: it "informs users by highlighting relationships between elements, action availability, and action outcomes," "helps orient users by showing how elements in a transition are related," "provides timely feedback and indicates the status of user or system actions," and "focuses attention on what's important, without creating unnecessary distraction" (m2.material.io). That covers the four functions this doctrine asks every animation to justify: orientation across a state change, spatial relationship between views, feedback on input, attention direction. IBM Carbon frames it functionally too, separating fast, task-oriented "productive" motion from "expressive" motion reserved for "occasional, important moments."

The counter-check is sharper than the function list itself. Apple's Human Interface Guidelines: "Don't add motion for the sake of adding motion. Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable." Val Head turns this into a test: "All UI animations need to have a defined purpose tied to a design outcome," and warns that delight-only motion backfires: "An animation that you add solely to increase delight usually does exactly the opposite from the user's perspective." Her second requirement is about responsiveness, not expression: an animation must "always feel responsive to a user's input, even if the animation is currently animating": it must never block.

**The three-question chain**, for every animation in a design before it ships:

1. Does it serve one of the four functions (orientation, spatial relationship, feedback, attention)?
2. Would the interface be measurably harder to understand without it, or was it added because an empty moment felt unfinished?
3. Does it respond immediately to input, without forcing a wait?

Any "no" identifies a decorative animation, not a functional one, and decorative animation needs a different justification than "it looks unfinished without it."

**Applying the chain to two contrasting cases.** A save button that briefly morphs into a checkmark and settles passes all three questions: it serves feedback, the user would otherwise have to guess whether the save succeeded, and it does not block further input. A hero section where every heading letter drifts up from below on page load typically fails the second question: the same information is available instantly without the drift, and the drift was added because a static heading felt plain, not because the page was harder to read without it. The same technique (a character-by-character reveal) can pass the chain once, on one hero, in a `bewegung: 2` or `3` project where it is the one accented moment named in section 7, and fail it everywhere else on the same page.

## 3. Motion tokens: durations and curves as a system

No component picks its own millisecond value or invents a bezier curve. It refers to a named token from a small, fixed set. Three systems document this differently, and they do not agree with each other, so pick one system per project and stay inside it rather than blending numbers across systems.

| System | Shortest duration | Typical standard transitions | Longest documented duration | Bounce/elastic in the system |
|---|---|---|---|---|
| Material Design 3 | 50 ms (short1) | 200 to 400 ms (short4 to medium) | 1000 ms (extra-long4) | Not in the easing set |
| Apple HIG | Not specified | Not specified, only "brief" required | Not specified | Not in the fixed curve system; possible as a spring overshoot parameter |
| IBM Carbon | 70 ms (fast-01) | 150 to 240 ms (moderate-01/02) | 700 ms (slow-02) | Explicitly excluded |

**Material Design 3** (m3.material.io): duration tokens in four tiers of four substeps each: short1 to short4 (50, 100, 150, 200 ms), medium1 to medium4 (250, 300, 350, 400 ms), long1 to long4 (450, 500, 550, 600 ms), extra-long1 to extra-long4 (700, 800, 900, 1000 ms). Easing tokens: Standard `cubic-bezier(0.2, 0, 0, 1)`, Standard Decelerate `cubic-bezier(0, 0, 0, 1)`, Standard Accelerate `cubic-bezier(0.3, 0, 1, 1)`, Emphasized Decelerate `cubic-bezier(0.05, 0.7, 0.1, 1)`, Emphasized Accelerate `cubic-bezier(0.3, 0, 0.8, 0.15)`. The base "Emphasized" curve itself is a multi-segment spline with no single official bezier number; `cubic-bezier(0.2, 0, 0, 1)` is a common web approximation, not an official value.

**IBM Carbon** (carbondesignsystem.com, and the `motion.json` design tokens in the carbon repo): six duration tokens, staggered by element and distance size: fast-01 (70 ms), fast-02 (110 ms), moderate-01 (150 ms), moderate-02 (240 ms), slow-01 (400 ms), slow-02 (700 ms). Easing comes in productive/expressive pairs: Standard productive `cubic-bezier(0.2, 0, 0.38, 0.9)`, Standard expressive `cubic-bezier(0.4, 0.14, 0.3, 1)`, Entrance productive `cubic-bezier(0, 0, 0.38, 0.9)`, Entrance expressive `cubic-bezier(0, 0, 0.3, 1)`, Exit productive `cubic-bezier(0.2, 0, 1, 0.9)`, Exit expressive `cubic-bezier(0.4, 0.14, 1, 1)`. Carbon states the overshoot exclusion directly: "do not use easing curves that suggest bounce, stretch, or sudden stops."

**Apple HIG** gives principles, not numbers: "Aim for brevity and precision in feedback animations," "generally avoid adding motion to UI interactions that occur frequently," "make motion optional." This is a genuine specification gap, not researcher negligence: Apple pushes the concrete number down to the implementation layer.

**Which duration for which transition**, combining the two token systems above: small, frequent transitions (hover, toggle, small show/hide) sit at Carbon fast-01/fast-02 (70 to 110 ms) or Material short1 to short3 (50 to 150 ms). Medium transitions (panel, dialog, card change) sit at Carbon moderate (150 to 240 ms) or Material medium (250 to 400 ms). Large, rare transitions (page change, large layout shift) sit at Material long to extra-long (450 to 1000 ms); Carbon documents nothing above 700 ms for this tier. Never interpolate a number that isn't in one of these two token sets.

**Why token discipline matters more than any single number.** Both Material and Carbon build their duration and easing values into a named, referenced token set rather than letting each component author its own value, for the same practical reason: a component never chooses its own millisecond figure or invents its own bezier curve, it refers to one of a small fixed set. That keeps every transition in a product consistent, and it turns a later global change (a product that should feel faster overall) into an edit at one place instead of a hunt through a hundred components. A project that mixes Material's numbers with Carbon's numbers, or invents intermediate values between them, has already lost that property, even if any single value in isolation looks reasonable.

## 4. Why bounce and elastic are almost always wrong

Two of the three checked systems exclude overshooting curves from their default set: Carbon by explicit statement, Material 3 by simply never including one in its official token list. Val Head supplies the reasoning: a direction reversal in motion (the overshoot-and-settle of bounce or elastic) carries extra visual information that has to be read, which tends to need more time to feel legible rather than frantic, directly opposed to the goal of fast, frequently repeated microinteractions. She ties pronounced Squash-and-Stretch or bounce to a playful brand personality instead: "probably not the personality for a bank, but could be for a game." A rare, deliberately celebrated success moment in an otherwise sober product can still use an overshoot curve; a standard transition for forms, navigation or loading states cannot.

**Spring models instead of fixed duration, but only for interruptible gestures.** Apple documents spring models for interactive, gesture-driven animation rather than fixed duration-curve pairs. `interactiveSpring(response:dampingFraction:blendDuration:)` defaults to response 0.15, dampingFraction 0.86, blendDuration 0.25, and Apple states it is "intended for driving interactive animations." UIKit offers the same idea through `UISpringTimingParameters`. The reasoning comes from WWDC18 Session 803, "Designing Fluid Interfaces": springs are "inherently interruptible and velocity-aware," and any animation should be interruptible and reversible at any point, which a fixed timing curve cannot do gracefully when a drag is released and re-grabbed mid-motion.

Material 3 and Carbon do the opposite by default: fixed cubic bezier curves with fixed durations, no documented spring parameters. The practical split: fixed curves for state changes the surface itself triggers (open, close, fade in); spring models the moment a finger drag or gesture must be interruptible mid-motion.

**The one narrow exception on a product surface: the build-up of an overlay that displaces nothing.** A slight overshoot is defensible when all four conditions hold at once: the moving thing is an overlay drawn above the layout, so nothing around it shifts position; the motion happens once, on appearance, not on every state change; the return path has no overshoot at all, it just leaves; and the element is not carrying feedback the user has to read precisely (no validation, no error, no status change). A minimized bar unfolding into its open state, or a small control opening into a pill, can take a mild overshoot on the way out and a plain decelerating curve on the way back. Everything else stays excluded: state changes, form feedback, loading, navigation, anything that repeats often, and anything where a neighbouring element would move because of it. The reasoning is unchanged from the paragraph above, a direction reversal costs reading time; the exception only holds where that cost is paid once and nothing else is competing for the same attention.

**One overshoot token, not one location.** The exception binds to a *pattern* (overlay build-up), not to a single spot in a project. Any control that independently satisfies all four conditions above may use it, including several instances of the same pattern (a set of pills, two bars) and a pattern that opens and closes many times over a session, that is still "once" per appearance, not once ever. What stays singular is the *token*: one overshoot curve, reused everywhere the pattern applies, never a second, different overshoot curve invented for a second pattern. A customer signature moment, a control that visibly overshoots on every hover by design, is this exception applied at scale, not an exception to the exception, and it still owes a measurable ceiling: label offset under 1px, squash under 10 percent, moving area under 3 percent of the viewport, per occurrence. Exceeding any of the three turns the moment from a signature into a distraction; the fix is to shrink the curve, not to grant a bigger one. Worked examples, the measurement rule and a `linear()` spring-equivalent curve sit in [product-motion.md](product-motion.md) section 6.

## 5. Accessibility

**`prefers-reduced-motion`.** A W3C Media Queries Level 5 user-preference query (`no-preference` / `reduce`) that reads an OS-level setting only, there is no browser UI of its own. Set via macOS Accessibility > Display > Reduce Motion, Windows Accessibility "Show animation effects," Android "Remove animations" (since Android 9), iOS Reduce Motion, GNOME "Reduce animation," KDE "Animation speed: Instant." A server-rendering equivalent exists as the `Sec-CH-Prefers-Reduced-Motion` client hint. Support: Chrome 76, Firefox 63, Safari 12.1, Edge 79, "widely available" since January 2020 (MDN).

**WCAG 2.3.3 "Animation from Interactions" (AAA).** Interaction-triggered motion animation must be disable-able unless essential to function or to the information conveyed. Purpose: protection against dizziness, nausea and headache for vestibular disorders; respecting `prefers-reduced-motion` is a named conforming technique.

**WCAG 2.2.2 "Pause, Stop, Hide" (A).** Applies to content that auto-starts, moves for more than five seconds, blinks or scrolls, shown alongside other content. Such content needs a mechanism to pause, stop or hide it (or a frequency control for auto-updating content), unless the motion is essential to the activity.

**WCAG 2.3.1 "Three Flashes or Below Threshold" (A).** Nothing may flash more than three times per second above the defined general-flash and red-flash thresholds; protects against photosensitive seizures.

**Vestibular triggers.** Val Head ("Designing Safer Web Animation for Motion Sensitivity," A List Apart, 2015) names concrete risk factors: motion that moves an object across a large area is "most apt to trigger a negative response"; exaggerated parallax scrolling and scrolljacking, especially with mismatched foreground/background speed; large virtual zoom or distance jumps. Comparatively safe: opacity, color and blur effects. The mechanism has peer-reviewed backing (LaViola Jr., "A Discussion of Cybersickness in Virtual Environments," ACM SIGCHI Bulletin, 2000): vection (the visually induced illusion of self-motion) correlates with large field of view and fast scene changes as triggers of visually induced motion sickness.

**A reduced state that is not a broken state.** MDN's own reference example for `prefers-reduced-motion: reduce` replaces a scaling transform animation ("pulse") with a pure opacity animation ("dissolve"): the implied rule is to replace large transform, translation or scale motion with a fade, not to strip it to nothing. No checked official source (MDN, W3C) supports a blanket "set every animation property to none" rule, and it is risky in practice: it can make state changes invisible that carried no vestibular risk in the first place (a plain fade-in on load, say). The defensible rule is narrower: remove or reduce to opacity for large positional change, parallax, zoom and autoplay motion; keep state change, focus and error feedback visible, just without the spatial shift.

## 6. The checklist

**Failure modes the sections above already rule out**, worth naming because they recur:

- A loading skeleton with a stagger animation added because a competitor's product has one: fails the second question in section 2, nothing about the wait is clearer for it.
- An overshoot easing curve set as a design system default rather than reserved for a rare success moment: contradicts section 4 and both Carbon's and Material's documented token sets.
- `animation: none !important` applied globally under `prefers-reduced-motion`, including to focus rings and error states: broader than the defensible rule in section 5, and it can hide feedback that carried no vestibular risk at all.
- A hover state borrowing Material's `medium` duration (250 to 400 ms) instead of `short`: wrong tier from section 3, reads as sluggish on a high-frequency interaction.
- A submit button disabled or hidden until its confirmation animation finishes: violates the responsiveness rule in section 2, the interface is blocking on its own decoration.

Verifiable against a finished page, not a spec document:

- [ ] Every animation on the page can name which of the four functions (orientation, spatial relationship, feedback, attention) it serves.
- [ ] For each one: is the page measurably harder to understand without it, or was it added to fill a moment that felt unfinished?
- [ ] No animation blocks input; every animation stays interruptible.
- [ ] Every duration and curve traces to a named token (section 3), not a hand-picked number.
- [ ] Gesture-driven, drag-interruptible motion uses a spring model, not a fixed duration-curve pair.
- [ ] No bounce or elastic curve appears as a standard transition; overshoot, if present at all, sits only on a rare, deliberately celebrated success moment or on the overlay-build-up pattern and its measurable ceiling from section 4.
- [ ] `prefers-reduced-motion: reduce` is respected everywhere, including decorative and canvas/WebGL effects that CSS alone cannot reach.
- [ ] The reduced-motion state is a complete design (large translate/scale/parallax/zoom removed or turned to opacity), never a half-played or blank one.
- [ ] Anything that auto-plays, blinks or scrolls for more than five seconds has a pause, stop or hide control, unless essential to the function.
- [ ] Nothing on the page flashes more than three times per second.

## 7. Binding to the `bewegung` register

This section must not contradict [registers.md](registers.md); the table there is the source of truth for what each stop permits.

| `bewegung` | Permitted under this doctrine | Forbidden |
|---|---|---|
| `0` | Instant state change only | All transitions, all reveals; the token system in section 3 is unused at this stop |
| `1` | Functional motion only: state feedback, focus, expand/collapse, page transitions, all using small/medium tokens from section 3, fixed curves unless the interaction is gesture-driven | Decorative motion, scroll-triggered reveals, any animation that fails the three-question chain in section 2 |
| `2` | Everything in `1`, plus a small number of accented moments, typically one per page, which may use a larger token (long/extra-long) or, rarely, an overshoot curve if it is a genuinely celebrated success moment | Continuous ambient motion, parallax on long pages |
| `3` | Full choreography: scroll-driven sequences, dissection, pinned scenes, ambient background motion, all still passing the purpose test in section 2 and the token discipline in section 3 | Nothing forbidden by the budget itself; every animation still answers to sections 2, 4 and 6 |

The hard rule holds at every stop without exception: a `prefers-reduced-motion` visitor gets a complete, non-broken design, never a half-played state. No `bewegung` stop, including `3`, buys an exemption from section 5 or from the checklist in section 6.

**Two calibration examples**, matching the two [registers.md](registers.md) uses directly, to show what this doctrine means at opposite ends of the dial. A traditional trade page at `bewegung: 1`: transitions exist only where they explain a state change (a menu expanding, a form field confirming), all sitting on Carbon's fast or Material's short tokens from section 3, no scroll-triggered reveal anywhere on the page, no accented moment because `1` does not grant one. A design tooling startup at `bewegung: 3`: the live demo above the fold uses spring-driven, interruptible motion for anything the visitor drags (section 4), the scroll-driven product dissection uses [scroll-choreography.md](scroll-choreography.md)'s dissection techniques and passes the purpose test because it demonstrates the product rather than merely decorating the page, and the one shader or 3D layer still ships behind the reduced-motion and viewport-pause rules in section 5 and [performance.md](performance.md). Both pages are judged by the same seven sections; only the register position changes what clears the bar.

# Presets

Six starting combinations, each a coherent stance, not a menu to mix and
match freely. A preset names a color strategy, a font pairing (see
[typography.md](typography.md)), a motion character (see
[motion.md](motion.md)), and the one technique file it leans on most, then
says plainly when it's the wrong choice. Picking a preset doesn't skip the
re-theming rule in [components.md](components.md): swap the actual palette,
type scale, and copy into the project's own voice, a preset unchanged is
still templated.

## Editorial Calm

- **Fits:** content-heavy marketing sites, blogs, documentation landing
  pages, anything where reading long text is the primary task.
- **Color strategy:** a near-neutral, warm-tinted background (not pure white)
  with one restrained accent reserved for links and CTAs only, everything
  else stays in a tight lightness range so text is the only high-contrast
  element on the page.
- **Font pairing:** serif display + grotesk UI, e.g. Fraunces for headlines,
  Schibsted Grotesk or DM Sans for body and chrome (see typography.md's
  pairing section).
- **Motion character:** understated. Fade/rise reveals on scroll with
  generous easing, no bounce, no parallax competing with reading. GSAP
  ScrollTrigger for staged reveal, nothing louder.
- **Technique file:** [layouts.md](layouts.md), specifically the
  editorial/magazine layout section, column widths and pull-quote treatment
  matter more here than any WebGL effect.
- **Doesn't fit when:** the brief wants to look technically extraordinary at
  first glance, e.g. a product launch page competing for an Awwwards-style
  reaction. This preset reads as tasteful, not as a showpiece, and is the
  wrong pick when the point of the page is spectacle.

## Kinetic Showpiece

- **Fits:** a marketing hero or product launch page where the visual layer
  itself is the pitch, the getlayers.ai/manus.im register the arsenal skill
  is built for.
- **Color strategy:** high contrast, often dark background with one or two
  saturated accent hues carried through the shader/3D palette itself, so the
  effect and the UI chrome share one deliberate color system instead of a
  generic dark mode plus a random gradient.
- **Font pairing:** grotesk headline + humanist sans body, e.g. Space
  Grotesk for oversized headlines paired with DM Sans, kept plain so it
  doesn't compete with the moving visual layer.
- **Motion character:** loud, on purpose, but budgeted. Scroll-driven
  choreography (GSAP ScrollTrigger, Lenis smooth scroll) synced to a
  shader/3D layer, physical spring easing over linear tweens, staggered
  reveals.
- **Technique file:** [shaders.md](shaders.md) or [3d.md](3d.md) depending on
  whether the centerpiece is a fragment-shader background or a 3D object/
  scene, cross-checked against [performance.md](performance.md)'s budget
  before shipping, an effect that isn't budgeted is a regression here, not a
  feature.
- **Doesn't fit when:** the project is a dense professional tool, a form-
  heavy admin flow, or anything read by the same person daily for hours.
  Spectacle motion in a tool people use as a habit becomes friction, not
  delight, fast.

## Dense Instrument

- **Fits:** dashboards, admin panels, monitoring tools, anything a power
  user opens dozens of times a day and needs to scan fast, see
  [software.md](software.md) for the underlying UI rules.
- **Color strategy:** tight, low-chroma neutrals (tinted grays, not pure
  gray) as the base, with color reserved strictly for status meaning
  (success, warning, error, active state), never for decoration. Labels and
  table headers pulled back in weight and contrast so data reads first.
- **Font pairing:** mono accent inside a sans system, a grotesk for UI
  chrome and body with JetBrains Mono for code, timestamps, and numeric
  columns.
- **Motion character:** near-silent. Transform/opacity-only transitions
  under roughly 150ms, no easing overshoot, no scroll-driven choreography.
  Motion here exists only to confirm state changes, never to entertain.
- **Technique file:** [performance.md](performance.md)'s density guidance
  plus [layouts.md](layouts.md)'s CSS Grid subgrid section for aligning
  dense tabular layouts, not the shader or 3D files, a GPU-cost centerpiece
  has no place in a tool optimized for glanceability.
- **Doesn't fit when:** the audience is a first-time or occasional user
  rather than a daily power user, or when the product's differentiation is
  emotional/brand-led rather than functional. Compressed density reads as
  cold and intimidating to someone who isn't already fluent in the tool.

## Quiet Premium

- **Fits:** fashion, beauty, hospitality, and other brand-led sites selling
  taste and restraint rather than features or price.
- **Color strategy:** an almost monochrome base (near-black or near-white,
  rarely both at once) with one desaturated, expensive-feeling accent used
  sparingly, large areas of unbroken negative space treated as the actual
  design material, not empty leftover space.
- **Font pairing:** high-contrast display serif for oversized headlines
  (e.g. Tan Pearl, license checked per source, see typography.md) paired
  with one plain grotesk for everything else, never a second display face.
- **Motion character:** slow and deliberate. Long-duration fades and
  reveals, generous scroll distance between beats, more Lenis-smoothed
  drift than staged choreography, nothing sharp or bouncy.
- **Technique file:** [layouts.md](layouts.md)'s full-bleed alternating
  sections, large uninterrupted imagery blocks doing most of the work, with
  restrained [motion.md](motion.md) reveals, not shaders or 3D.
- **Doesn't fit when:** the product needs to communicate a lot of
  information fast, comparison tables, pricing grids, or feature matrices
  undercut the whole premise of unhurried restraint. Also wrong for a
  budget or mass-market positioning, where deliberate slowness reads as
  friction rather than luxury.

## Structural Brutalist

- **Fits:** portfolios, design studios, and technical/developer-facing
  brands that want to signal confidence through raw structure rather than
  polish.
- **Color strategy:** stark, high-contrast, often just two or three flat
  values with no gradients or soft shadows, color blocking used as a layout
  device rather than a decorative accent.
- **Font pairing:** a single grotesk or mono face carried at extreme size
  contrasts (very large headlines, very small labels) instead of a
  second typeface, e.g. Space Grotesk or JetBrains Mono alone, doing all the
  work through scale rather than pairing.
- **Motion character:** abrupt and mechanical on purpose, hard cuts or
  snap transitions instead of eased curves, deliberately rejecting the
  organic spring-easing most of the other presets lean on.
- **Technique file:** [layouts.md](layouts.md)'s asymmetric/broken grid
  section, structure carries the design, not shaders, 3D, or heavy motion.
- **Doesn't fit when:** the brand needs to read as warm, approachable, or
  trustworthy to a non-technical audience, e.g. healthcare, finance for
  consumers, education. Raw structure and hard cuts read as cold or
  unfinished outside a design-literate audience that recognizes the
  reference.

## SaaS Standard Plus

- **Fits:** the common case, a B2B or B2C product site or in-app marketing
  surface that needs to look current and competent without needing to be a
  visual statement, most projects that don't have a strong reason to reach
  for one of the other five.
- **Color strategy:** one brand hue plus tinted neutrals in OKLCH, enough
  contrast for accessibility, no purple-gradient default and no
  everything-is-gray flatness, a genuine but restrained brand palette.
- **Font pairing:** grotesk headline + humanist sans body, e.g. Schibsted
  Grotesk with DM Sans, the safest, most broadly legible pairing in
  typography.md.
- **Motion character:** moderate. Staged fade/rise reveals on scroll,
  physical spring easing on hover/interactive states, no shader or 3D
  centerpiece, motion supports the layout without becoming the point of it.
- **Technique file:** [components.md](components.md) as the base component
  layer (shadcn/ui plus a motion-forward library like Motion Primitives or
  Magic UI for isolated accents), with light [motion.md](motion.md)
  choreography layered on top.
- **Doesn't fit when:** the brief explicitly wants something technically
  extraordinary, this preset is deliberately the safe, competent baseline,
  not the showpiece. If the project needs to compete on visual ambition
  specifically, start from Kinetic Showpiece instead. It's also the wrong
  starting point for a dense daily-use tool, Dense Instrument is closer to
  right there even though both are "software."

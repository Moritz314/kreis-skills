---
name: arsenal
description: Use when a design needs a technically extraordinary visual layer beyond typography, color and spacing: WebGL/GLSL shaders, 3D scenes (Three.js/React Three Fiber), advanced scroll-driven or choreographed motion, unconventional structural layouts, or concrete component references from free libraries. Complements impeccable and frontend-design: those set aesthetic direction, critique and copy; this supplies the concrete technical building blocks (curated free libraries, working code patterns, performance and accessibility budgets) to execute ambitious effects in the style of originkit.dev, getlayers.ai, or manus.im output. Applies equally to marketing websites and product/software UI. Not for basic UI polish, copy, or plain accessibility audits alone, route those to impeccable.
version: 2.1.0
user-invocable: true
argument-hint: "plan|build|register|critics|loot|behavior|db|interface|lernen [args]"
---

Runs whole projects, not just effects: `arsenal` plans a project, builds it through a workflow that enforces content-before-layout and reference-grounded generation, reviews it with six independent critics, and remembers what the user likes across projects. `impeccable` and `frontend-design` own taste, critique wording and copy; this skill owns "how do I actually build the thing and keep it from being generic."

## When to use this vs impeccable alone

Reach for `arsenal` when the task is a whole project (new build, existing project brought under management, a full review pass) or when the brief calls for something impeccable's principles don't hand you code for: a WebGL background, a 3D object, scroll-choreographed sequences, a layout structure that breaks the card-grid default. For a single isolated polish task on an already-managed project (color strategy, one component, a copy pass, an a11y spot-check), staying in `impeccable` directly is fine.

They compose in one flow, not two separate tasks: `build`'s workflow calls impeccable's `critique` and `audit` directly, as two wired-in stages named `Impeccable critique` and `Impeccable audit` inside its Critique loop phase (see [commands/build.md](commands/build.md) and [commands/critics.md](commands/critics.md)); `critics` run standalone casts its own six-agent roster with lenses drawn from impeccable's `critique`/`audit`/`personas`/`heuristics-scoring`, without calling them directly. The project's register (brand vs product) still governs every choice made here.

## Commands

No argument: show this table and stop.

| Command | Purpose | Scope | Reference |
|---|---|---|---|
| `plan` | New project: discovery interview, SOUL.md/MASK.md/ARMOURY.md, derived PRODUCT.md/DESIGN.md, workflow file, DB entry | creates a project | [commands/plan.md](commands/plan.md) |
| `build` | Flowchart artifact, comment review, runs the build workflow | project | [commands/build.md](commands/build.md) |
| `interface` | Alias for `build` with type forced to `software` | project | [commands/build.md](commands/build.md) |
| `register` | Bring an existing project under arsenal management | creates a project | [commands/register.md](commands/register.md) |
| `critics` | Six independent review agents, merged and prioritized findings, optional fix-on-confirm | project, or a single file (see [commands/critics.md](commands/critics.md)) | [commands/critics.md](commands/critics.md) |
| `loot` | Capture a confirmed reference from a URL or screenshot into the library | global (optional project tag) | [commands/loot.md](commands/loot.md) |
| `lernen` | Learn from an open source: derive measurable rules into reference/, verified against the existing canon | global | [commands/lernen.md](commands/lernen.md) |
| `behavior` | View, add, edit, delete the standing preference memory | global | [commands/behavior.md](commands/behavior.md) |
| `db` | List projects, or show one project's record | global / project detail | [commands/db.md](commands/db.md) |

## Preflight (every command)

**Reference-only mode.** If arsenal is loaded without a command, in a project folder that has no `ARMOURY.md`, none of the gates below apply: the skill is being used as a reference work, not run as a pipeline, and aborting on a missing project file would be pure obstruction. In that mode answer from `reference/` and say nothing about gates. The gates start applying the moment a command is actually invoked, or the moment the work turns into building or reviewing an arsenal-managed project.

In reference-only mode, start at [reference/_index.md](reference/_index.md) and open only the files it points at, instead of scanning the whole folder.

Every command loads its gates before doing any work. Never skip a gate silently; a missing file is an abort with a named fix, not a guess.

1. **behavior.md**, always. Load it from the sync path below. If it does not exist yet: abort, tell the user to run `behavior`, which creates it.
2. **ARMOURY.md**, for project-bound commands only (`plan` after the type question, `build`, `interface`, `register` after derivation, `critics`). Read two blocks from it:
   - `## Type` (`website` or `software`), then load the matching `reference/website.md` or `reference/software.md`.
   - `## Dials`, the five settings defined in [reference/registers.md](reference/registers.md) (`auftreten`, `bewegung`, `dichte`, `technik`, `tonfall`). They decide what this project is allowed to do, and `critics` measures findings against them rather than against a universal ideal.

   If ARMOURY.md does not exist: abort, tell the user to run `plan` (new project) or `register` (existing project). If it exists but the `## Dials` block is missing or incomplete: abort as well and ask for the missing dials. Guessing them silently is how a joinery ends up with a startup page.

   `critics --file <path>` (single file mode, see [commands/critics.md](commands/critics.md)) is the one exception to this whole gate: it targets a single rendered mockup that has neither `ARMOURY.md` nor `projects.json`, this gate does not apply, and register/type/dials come from a short task text instead.
3. `behavior`, `db` and `loot` have no single project in scope by default and skip the ARMOURY gate. `db <name>` and `loot` tagging a project still only *read* a project's stored type from `projects.json`, they never require the ARMOURY file to be present.

### State layer (sync path, not the skill folder)

The skill folder holds code and reference only. Projects, preferences and the loot library are operational state and live in a state folder of your choice so every instance sees the same data.

| OS | Path |
|---|---|
| Windows | `<dein-ordner>` |

Contents: `behavior.md` (global preference memory), `projects.json` (project database), `library/muster/<slug>.md` and `library/eigene/<slug>.md` (loot entries).

### Project files (in the project's own folder)

| File | Contains |
|---|---|
| `SOUL.md` | The project's PRODUCT.md in full: `## Register` (`brand` or `product`), `## Users`, `## Product Purpose`, `## Brand Personality`, `## Anti-references`, `## Design Principles`, `## Accessibility & Inclusion`. |
| `MASK.md` | The project's DESIGN.md in full: colors, typography, elevation, components, motion. |
| `ARMOURY.md` | `## Type` (`website` or `software`), `## Dials` (the five settings from [reference/registers.md](reference/registers.md)), `## Tools`, `## Libraries`, `## Skills`, `## Assets`, `## Project overrides` (project-specific exceptions to `behavior.md`). |

`plan` and `register` additionally write standalone `PRODUCT.md` and `DESIGN.md` at the project root, derived from SOUL.md/MASK.md, so impeccable's own context gate (`load-context.mjs`) passes without modification. SOUL.md and MASK.md stay the source of truth; the derived files are regenerated whenever SOUL.md or MASK.md changes, never hand-edited.

## Foundations (load before deciding anything, not after)

These carry the judgment layer: whether a move belongs here at all, how the page is structured, and at what settings. They rest on checked sources (see `planung/recherche-*.md`) and each one ends in a checklist that can be measured against a finished draft. Technique files below answer "how do I build it", these answer "should this exist, and in what form".

| Question | Reference |
|---|---|
| At what settings does this project run (the five dials) | [reference/registers.md](reference/registers.md) |
| Grid, type, color, perception, as measurable rules | [reference/design-foundations.md](reference/design-foundations.md) |
| Information architecture, the evidenced laws, patterns per screen type | [reference/ia-and-structure.md](reference/ia-and-structure.md) |
| Does motion belong here, and which motion | [reference/motion-doctrine.md](reference/motion-doctrine.md) |
| Which stack, how it ships, and the CSP traps | [reference/stack.md](reference/stack.md) |

## Technique references

Ready-made, self-contained building blocks (backgrounds, elements, feature demos, images, with previews): [bausteine/_index.md](bausteine/_index.md). Check there before building an effect from scratch.

Load these once `plan` or `build` has settled on a technique:

| Technique | Reference |
|---|---|
| Background/decorative WebGL effects, noise, gradients, distortion | [reference/shaders.md](reference/shaders.md) |
| 3D objects, scenes, particles (Three.js / React Three Fiber) | [reference/3d.md](reference/3d.md) |
| Scroll-driven choreography, text effects, cursor/magnetic interactions (brand register) | [reference/motion.md](reference/motion.md) |
| Product-surface motion: control morphs, expanding bars, shells, color roles, goo, overshoot exception | [reference/product-motion.md](reference/product-motion.md) |
| Structural layout patterns beyond grid-of-cards | [reference/layouts.md](reference/layouts.md) |
| Free component libraries as technical reference | [reference/components.md](reference/components.md) |
| Perf and accessibility budget for all of the above | [reference/performance.md](reference/performance.md) |
| Website-specific rules, anti-patterns, required sections | [reference/website.md](reference/website.md) |
| Software/product-UI-specific rules, states, density | [reference/software.md](reference/software.md) |
| Asset sourcing (stock, icons, fonts) | [reference/assets.md](reference/assets.md) |
| Type scale and pairing rules | [reference/typography.md](reference/typography.md) |
| Copywriting rules per register | [reference/copywriting.md](reference/copywriting.md) |
| Ready-made technique/token presets (a preset is a pre-filled set of dials) | [reference/presets.md](reference/presets.md) |
| Scroll choreography, dissection, background interaction, tool choice | [reference/scroll-choreography.md](reference/scroll-choreography.md) |

Pick 1-2 techniques, not five. An ambitious design commits to a small number of technical moves executed well; stacking a shader background *and* a 3D hero *and* scroll choreography *and* a magnetic cursor reads as a demo reel, not a product, the maximalist mirror of the generic-Tailwind failure this skill exists to avoid.

If the bundled snippet in a reference file doesn't fit, each one ends with a short list of live sources to check via WebFetch. Treat what comes back as a technical reference to adapt, not code to paste verbatim, exactly as [reference/components.md](reference/components.md) already spells out for its own libraries.

## Non-negotiables carried over from impeccable

These apply everywhere in this skill, they are not restated per reference file:

- No `#000`/`#fff`, OKLCH-tinted neutrals, deliberate color strategy.
- Never animate layout properties, transform, opacity and clip-path only. clip-path with rounded corners is paint work, not compositor work, so keep the painted area small and measure it against an idle run, see [reference/product-motion.md](reference/product-motion.md) section 1 and [reference/performance.md](reference/performance.md). For curves and durations [reference/motion-doctrine.md](reference/motion-doctrine.md) is the authority, it holds the sourced token sets and the reasoning on why bounce and elastic are almost always wrong in a product surface.
- Match implementation complexity to aesthetic ambition, a maximalist shader hero needs precise, not sloppy, code.
- If it could be captioned "AI made that," it failed, an effect that's technically impressive but generically deployed (the same particle hero on every project) still fails the slop test.
- `prefers-reduced-motion` fallback and mobile/low-power fallback are never optional, see [reference/performance.md](reference/performance.md).

## Relationship to impeccable

impeccable stays unchanged; this skill only links to it, never the reverse. `critics` casts some of its review agents from impeccable's own lenses (critique, audit, personas, heuristics-scoring) without calling those commands directly. `build`'s workflow calls impeccable's `critique` and `audit` directly, as the `Impeccable critique` and `Impeccable audit` stages inside its Critique loop phase, see [commands/build.md](commands/build.md). Hand a finished technical layer back to impeccable's `critique`/`audit`/`polish` for anything outside arsenal's own gates, this skill builds the showpiece and the project scaffolding, impeccable judges whether the whole thing still holds together.

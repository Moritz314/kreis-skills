# Registers: the dials that make one method fit every client

A joinery workshop and a design tooling startup do not need different
principles. They need the same principles held at different settings. This file
defines those settings as a small set of named dials, written into a project's
`ARMOURY.md` once and read by every command afterwards.

The dials are constraints, not a style picker. They say what is permitted and
what is forbidden. What is actually good inside those bounds still comes from
[design-foundations.md](design-foundations.md), [ia-and-structure.md](ia-and-structure.md)
and [motion-doctrine.md](motion-doctrine.md). A project whose dials allow a
WebGL background does not thereby deserve one.

## Why dials instead of presets

A preset ("Editorial Calm", "SaaS Standard") bundles decisions that do not
actually travel together. A blacksmith who does kinetic sculpture wants high
motion and low density. A fintech dashboard wants high density and almost no
motion. A preset forces one to borrow the other's mistakes. Five independent
dials cover both without inventing a preset for every combination.

[presets.md](presets.md) still exists and stays useful: a preset is now simply
a named, pre-filled set of dial positions plus a palette and type pairing, used
as a starting point that the interview then adjusts. The dials are the truth,
the preset is the shortcut.

## The five dials

### 1. `auftreten` (register)

Who the page sounds like. Four stops, ordered from most rooted to most forward.

| Stop | Reads as | Typical evidence on the page |
|---|---|---|
| `werkstatt` | A trade that has done this for a long time | Real photographs of real work, plain nouns, prices or lead times stated, no stock imagery of strangers in offices |
| `haus` | An established company with obligations | Structure and completeness, legal clarity, references, a visible chain of responsibility |
| `studio` | A practice with a point of view | Deliberate typography, editorial layout, restraint used as a signal, work shown as cases not features |
| `labor` | A product team moving fast | Live demo over description, dense product surface, technical confidence, changelog energy |

This dial governs vocabulary, image sourcing, evidence type and how much the
page is allowed to assert about itself. It does **not** govern quality: a
`werkstatt` page is not permitted to be crude, and a `labor` page is not
permitted to be sloppy.

### 2. `bewegung` (motion budget)

How much motion the project may spend. Governed in detail by
[motion-doctrine.md](motion-doctrine.md).

| Stop | Permitted | Forbidden |
|---|---|---|
| `0` | Nothing beyond instant state change | All transitions, all reveals |
| `1` | Functional only: state feedback, focus, expand and collapse, page transitions | Decorative motion, scroll-triggered reveals |
| `2` | The above plus a small number of accented moments, typically one per page | Continuous ambient motion, parallax on long pages |
| `3` | Full choreography: scroll-driven sequences, dissection, pinned scenes, ambient background motion | Nothing by budget, everything still by judgment |

Hard rule at every stop: a reduced-motion visitor gets a complete, non-broken
design, never a half-played state.

### 3. `dichte` (density)

How much information occupies one screen.

| Stop | Fits | Consequence |
|---|---|---|
| `luftig` | Marketing pages, single-purpose flows, onboarding | Generous measure, one idea per screen section, large type scale steps |
| `ausgewogen` | Most product marketing, documentation, mixed pages | Standard scale, sections carry two or three related ideas |
| `verdichtet` | Dashboards, tables, admin tools, anything operated daily | Tight rhythm, smaller steps, tabular figures, no decorative whitespace that pushes data off screen |

`verdichtet` is not permission to crowd. It shifts what counts as generous, it
does not remove the requirement for structure.

### 4. `technik` (technical budget)

What the page is allowed to ship. Governed by [stack.md](stack.md) and
[performance.md](performance.md).

| Stop | Ships | Astro consequence |
|---|---|---|
| `statisch` | HTML and CSS, no JavaScript beyond a progressive enhancement of a few lines | No islands. Motion via CSS only |
| `inseln` | Islands for the parts that need them | `client:visible` by default, `client:load` only when the element is above the fold and interactive |
| `webgl` | The above plus shader and 3D layers | Islands only, never on the critical path, always with a static fallback |

### 5. `tonfall` (voice)

How the copy speaks. Governed by [copywriting.md](copywriting.md).

| Stop | Sounds like | Avoids |
|---|---|---|
| `nüchtern` | Plain statement of fact, numbers, no adjectives that cannot be checked | Superlatives, promises, exclamation |
| `direkt` | Speaks to the reader, says what to do next, short sentences | Corporate hedging, passive constructions |
| `selbstbewusst` | Takes a position, names what it does not do, allows a strong claim when it is backed | Bluster without evidence, borrowed startup vocabulary |

## Writing the dials

In `ARMOURY.md`, exactly one block named `## Dials`, exactly these keys, one
value each:

```markdown
## Dials
auftreten: werkstatt
bewegung: 1
dichte: luftig
technik: statisch
tonfall: nüchtern
```

**Do not confuse this with `## Register` in `SOUL.md`.** That one is impeccable's
brand-versus-product distinction and answers "is this surface selling or is it
being operated". The dials here answer "at what settings". Both exist, both are
read, they are not the same field. The word register in this file's title is the
rhetorical sense, a way of speaking, which is what `auftreten` encodes.

Every command reads this block before working. A missing block is a hard stop,
not a default: the commands abort and point at `plan` or `register`, because
guessing these five values silently is how a joinery ends up with a startup
page.

Note the command `register` is the verb for bringing an existing project under
management. It has nothing to do with this file beyond filling the `## Dials`
block like `plan` does. Three different meanings of one word meet here, so each
one is named explicitly wherever it appears: the command `register`, the field
`## Register` in SOUL.md, and the dials in this file.

## Guard rails

These combinations are contradictions. A command that meets one stops and asks
rather than resolving it on its own.

| Combination | Why it breaks |
|---|---|
| `bewegung: 3` with `technik: statisch` | Choreography of that kind cannot be built without scripted timeline control |
| `bewegung: 3` with `dichte: verdichtet` | A surface operated daily is made worse by motion competing with the data |
| `technik: webgl` with a stated low-power or mobile-first audience | The budget in performance.md cannot be met, the fallback becomes the real design |
| `auftreten: werkstatt` with `tonfall: selbstbewusst` | Not forbidden, but it is the exact combination that reads as a trade business wearing borrowed clothes. Requires an explicit decision and a reason recorded in ARMOURY.md |

## Calibration examples

Two ends of the range the user named, written as dial positions rather than as
styles.

**Traditional trade, cut anew**

```markdown
auftreten: werkstatt
bewegung: 1
dichte: luftig
technik: statisch
tonfall: nüchtern
```

What that produces: a fast, quiet page carried by real photographs of real
work, a strict grid, one confident typeface pairing, prices and lead times in
the text, transitions only where they explain a state change. The modern cut
comes from typography, grid and restraint, not from effects. Ships close to
zero JavaScript.

**Design tooling startup**

```markdown
auftreten: labor
bewegung: 3
dichte: ausgewogen
technik: webgl
tonfall: selbstbewusst
```

What that produces: a live demo above the description, a scroll-driven
dissection of the product, a shader or 3D layer in one place only, dense
technical copy that names limits as well as strengths. Every heavy layer is an
island with a static fallback and a reduced-motion path.

Both pages are judged by the same rules. Only the settings differ.

## How critics uses the dials

A finding is measured against the project's dials, never against a universal
ideal. "This page has no animation" is not a finding at `bewegung: 0` or `1`.
"This hero ships a 3D scene" is a finding at `technik: statisch` and a
legitimate choice at `webgl`.

Two classes of finding ignore the dials entirely and always count:

1. Anything from [performance.md](performance.md) and the accessibility floor.
   No dial position buys an exemption from contrast, focus visibility, keyboard
   operation or a reduced-motion path.
2. Anything factually wrong: a claim the client cannot support, an invented
   number, a legal omission.

## Changing a dial mid-project

Dials are recorded decisions, not preferences to drift. Changing one is
allowed, but the change is written into `ARMOURY.md` with a date and a reason,
and `critics` re-runs against the new setting. A dial that changes without a
recorded reason is drift, and drift is how a coherent project turns into a
collection of screens.

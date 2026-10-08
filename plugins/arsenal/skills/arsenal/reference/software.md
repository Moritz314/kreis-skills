# Software path: rules, anti-patterns, mandatory components, check criteria

Applies to application UI: dashboards, admin and monitoring screens, editors,
settings, tables, forms, navigation shells, and any other product/utility
screen, the "product" side of impeccable's brand-vs-product split. Decorative
technical ambition (shaders, 3D, ambient motion) is not licensed here by
default, see the boundary already stated in [shaders.md](shaders.md), don't
re-litigate it in this file. Verbs and build mechanics are identical to
[website.md](website.md); what differs is this rule set, the check criteria,
and the critics agent roster for this project type.

Technique files ([product-motion.md](product-motion.md),
[motion.md](motion.md), [layouts.md](layouts.md),
[components.md](components.md), [performance.md](performance.md)) hold the
*how*. This file holds the *what must be true* before a software build
counts as done. Copy mechanics live in `copywriting.md`, type choices in
`typography.md`, don't duplicate those here either.

**Which motion file applies here.** For motion on a product surface, read
[product-motion.md](product-motion.md) first: control morphs, expanding and
collapsing bars, side sheet and master-detail shells, status color, the goo
filter, the overshoot exception and the measurement rule. [motion.md](motion.md)
covers brand-register techniques (scroll choreography, text splitting, magnetic
cursors, view transitions) and rules most of them out for product surfaces, so
following the pointer there and stopping leaves the question unanswered. Curves
and durations come from [motion-doctrine.md](motion-doctrine.md) in both cases.

## Rule set

Always applies on this path, no exceptions without a stated reason.

| # | Rule |
|---|---|
| 1 | System status is visible at all times: loading, processing, success, error. Never leave the user guessing what's happening. |
| 2 | Interface language is the user's language, not system or database jargon: field names, internal status codes and technical terms get translated to what the user actually calls the thing. |
| 3 | Every action, especially destructive ones, has a clear way out: undo, cancel, back. No dead ends. |
| 4 | Keyboard shortcuts and personalization are available for expert users without forcing beginners through them. Flexibility, not one mandated path. |
| 5 | Only relevant information is shown by default; rare or advanced functions are hidden behind progressive disclosure, not permanently on screen. |
| 6 | A dashboard fits on one screen without scrolling, all core metrics visible at once. If it doesn't fit, it's not a dashboard, it's a report, split it or cut it. |
| 7 | Charts use preattentively fast shapes: bar and line for metrics. No pie charts, no 3D chart effects. |
| 8 | Every KPI tile carries a comparison: change vs. prior period, vs. target, or a trend line/sparkline. A bare number with no reference point is not a finished tile. |
| 9 | Tables are designed around their four real tasks: find records, compare records, view or edit a single record, act on records. Column order follows task relevance, not database column order. |
| 10 | Table header (and first column where relevant) stays fixed on scroll; density is offered in at least a compact and a comfortable variant for professional, high-volume tools. |
| 11 | Forms with more than five fields are grouped into titled sections. Follow-up fields appear only once their trigger value is set (progressive disclosure), advanced options go at most one extra level deep. |
| 12 | Errors display only after input is complete, never mid-keystroke. Message text is human language next to the field, states the actual problem, offers a fix, never blames the user, never discards what was typed. |
| 13 | Empty states are never a blank box: a short explanation of why nothing is there plus a direct next action. Empty (task done, nothing left) and blank slate (never used yet) get different tone, confirming vs. inviting. |
| 14 | Primary navigation is a visible sidebar on desktop for apps with many, frequently switched sections, not hidden behind a hamburger, unlike marketing sites. Current position is always marked (active item, breadcrumb). Hierarchy depth stays at two levels; deeper structures get their own overview page, not a nested dropdown. |
| 15 | Dense professional tools default to compact spacing deliberately, not the looser rhythm appropriate to a consumer app; labels and table headers are visually de-emphasized (smaller, lighter weight, lower contrast) so they support the data instead of competing with it. |
| 16 | Every action in a keyboard-centric tool has a shortcut, documented visibly (inline tooltip or a command list), not hidden. Shortcuts never collide with OS or assistive-technology bindings, and have Mac/Windows equivalents. |
| 17 | Every interactive element (fields, menus, buttons, dialogs) is reachable and operable via Tab alone, no mouse required. |
| 18 | Complex professional tools allow nonlinear work: no forced step-by-step wizard where the domain doesn't require one, and no mandatory tutorial before first use. |

## Record and detail views

A screen type the rule set above does not name directly: a single customer, order, case or asset record with an activity stream, not a table and not a dashboard. Three rules specific to it:

- **The next step is above the fold.** Whatever the user came to this record to do next (confirm a status, respond to an open item, approve a change) is visible without scrolling on first load. A record view that opens scrolled to "today" or to the latest activity-stream entry, burying the record header (identity, key relationship fields) below the fold, fails this even if the scroll position feels helpful, see [product-motion.md](product-motion.md) for the honest way to auto-scroll without hiding the header.
- **Input types double as filter categories.** Where a record's activity stream mixes kinds of entries (notes, calls, status changes, documents), the same small vocabulary that labels an entry when writing it is what filters the stream when reading it. Do not invent a separate filter taxonomy that doesn't match the entry types the user actually created.
- **Detail opens as a side sheet, not a new page.** A record opened from a list stays reachable in one step back; use the side sheet pattern from [product-motion.md](product-motion.md) section 3, not a full navigation to a new route, unless the record view is itself the primary destination (a deep link, a bookmarked URL).

## Anti-patterns

The specific, nameable failures of generic AI-generated dashboards and
application UI, not a vague "make it feel less templated" note.

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| Isolated KPI number with no comparison ("1,284 users") | Worthless for a decision: good, bad, rising, falling all stay unknown | Pair every metric with a delta, a target, or a sparkline |
| Same card-in-card treatment for every content type regardless of whether it's a metric, a list, a form, or a table | Produces visual noise and hides what's actually important, nested cards compound the effect | Derive layout from content: tables as tables, forms as form sections, metrics as a compact row, cards reserved for genuinely self-contained units |
| Reflexive sidebar navigation for a flat 3-4 page app | Wastes space and clarity for structure that isn't there | Choose the nav pattern from section count and switch frequency: sidebar for many/frequent, top-nav for flat/rare, command palette for high-action-density power tools |
| No trend or comparison data anywhere, just a current snapshot | A dashboard with no history is a disguised static report, can't judge normal vs. alarming | At least one comparison dimension always present (time, target, benchmark), drill-down over a bare snapshot |
| Excess uniform whitespace and consumer-app spacing in a professional tool | Fewer information units fit per screen, power users lose overview and speed | Compact density as a deliberate choice for pro tools, whitespace used for grouping, not as default filler |
| Generic AI-slop look: a font swapped in without a stated reason against the project's existing type stack, purple gradient panels, gray text on colored backgrounds, oversized rounded icons above every heading, elastic bounce animation | Every major model trained on the same templates, interfaces become interchangeable and ignore the actual domain | Concrete decisions from content and domain: real palette, restrained icon use only where it adds function, real easing instead of bounce. The tell is an unjustified swap away from the project's established stack, not any specific font: Inter used deliberately because the surrounding system already runs on it is not a tell, and a plain system stack (`-apple-system`, `system-ui`) is a legitimate, deliberate product decision in its own right, not a default to be embarrassed out of. |
| Critical KPIs visually buried under decorative charts or illustrations | Dashboard stops being useful the moment decoration outranks the number that matters | Force a clear hierarchy: most important metric largest and first, decoration removed or subordinated |
| Data overload: as many charts and KPIs as fit, because more data implies more value | Causes analysis paralysis, buries insight in noise | Cut to what's actually actionable for the target role, rest behind drill-down or a separate view |
| One dashboard reused across a manager role and a case-worker role with no adaptation | Wrong detail level and wrong metric set for at least one of the two audiences | Content and density built for the specific role and its actual decisions, not a generic overview template |
| Fields turn red while the user is still typing | Reads as aggressive and inaccurate during exploratory input | Validate on blur or submit, never mid-keystroke |

## Mandatory components

Nothing here is optional; a build that skips one is not finished, regardless
of visual polish elsewhere.

| Component | Requirement |
|---|---|
| Status feedback | Visible loading, processing, and success/failure state for every async action |
| Undo or cancel | Present on every destructive operation |
| Empty state copy and CTA | Every list, table or panel that can be empty has explanation text and a next action, never a bare blank container |
| Error messages | Human language, positioned next to the affected field, states the problem, offers a fix, preserves the user's input |
| Full keyboard reachability | Every interactive element reachable and operable via Tab with no mouse |
| Documented shortcuts | For keyboard-centric tools, a visible list or inline hints, not undocumented bindings |
| Density variant | At least a compact option for any data-dense table or list in a professional tool |
| Current-position indicator | Active nav item and/or breadcrumb always shown |
| KPI comparison | Every dashboard tile carries a delta, target, or trend, never a bare number |
| PRODUCT.md and DESIGN.md derived files | Present alongside SOUL.md/MASK.md so impeccable-driven build stages have their required gate files |

## Check criteria

What critics and the final acceptance pass measure a software build against.

| Criterion | How it's checked |
|---|---|
| Keyboard-only walkthrough | Every core flow completed with mouse disconnected, Tab/Enter/Escape only, no unreachable control |
| Data density | Table/list density checked against the target user's actual usage pattern (occasional vs. all-day power use), compact variant present where warranted |
| Error states | Every form and destructive action reviewed for message clarity, field-adjacency, input preservation, no premature validation |
| Empty states | Every emptiable view reviewed for explanation text, correct empty-vs-blank-slate tone, and a working next action |
| Dashboard fit | Checked against the one-screen-no-scroll rule, deviations justified against a stated reason, not left as an oversight |
| KPI comparison presence | Every tile checked for a delta, target, or trend line |
| Navigation pattern fit | Sidebar/top-nav/command-palette choice checked against actual section count and switch frequency, not defaulted |
| Hierarchy depth | Menu and disclosure nesting checked against the two-level cap |
| Chart type | Every chart checked against the preattentive-shape rule, pie and 3D charts flagged |
| Shortcut collisions | Custom bindings checked against OS and assistive-technology shortcuts, Mac/Windows parity confirmed |
| Copy and jargon | Field names, labels and status text checked against the user's own vocabulary, not internal/system terms |
| Contrast and focus | Focus ring visible on every interactive element, contrast holds at the compact density level used |
| Generic-look scan | Screens checked against the anti-pattern table above (font choice, palette, icon use, animation style) for templated tells |
| Grayscale / color-alone test | Screenshot converted to grayscale per [design-foundations.md](design-foundations.md) section 5 point 8; every status, state and category distinction still legible from shape, text or icon alone, including the reverse failure where one color marks the default/normal case across most rows and the assignment should run the other way |

## What this path does not check

Explicitly out of scope for software critics/acceptance, covered instead by
[website.md](website.md): Impressum, Datenschutzerklärung, cookie consent,
say-the-opposite/one-sentence headline tests, floskel scanning, media
authenticity ranking. A product with a public marketing shell (landing page,
pricing page) routes those specific screens through the website checklist,
the application itself stays on this one. Decorative shader/3D motion stays
out of scope entirely for utilitarian screens per [shaders.md](shaders.md);
it only re-enters if a brand-adjacent surface (in-app onboarding splash,
upsell page) is explicitly built as such.

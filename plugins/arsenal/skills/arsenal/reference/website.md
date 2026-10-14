# Website path: rules, anti-patterns, mandatory components, check criteria

Applies to marketing sites, landing pages, product marketing pages, brand
sites, campaign pages. This is the path where technically ambitious decoration
(shaders, 3D hero, choreographed scroll) is licensed by impeccable's
brand-vs-product split: a website is a "brand" surface by default. It is also
the path where legal completeness and copy quality gate whether something
counts as done, not keyboard reach or data density, that's [software.md](software.md).

Technique files ([shaders.md](shaders.md), [3d.md](3d.md), [motion.md](motion.md),
[layouts.md](layouts.md), [components.md](components.md)) hold the *how*.
This file holds the *what must be true* before a website ships. Copy
mechanics live in `copywriting.md`, type choices in `typography.md`, media
sourcing mechanics in `assets.md`, don't duplicate those here either.

## Rule set

Always applies on this path, no exceptions without a stated reason.

| # | Rule |
|---|---|
| 1 | Content exists in final form before layout is finished. Content-first ordering, not layout-first with lorem ipsum. No placeholder copy survives to "done". |
| 2 | Message layering in order: clarity ("what is this") before relevance before value before differentiation. A headline that skips straight to a clever differentiation line before the visitor knows what's being sold fails, however sharp the line. |
| 3 | Every primary headline passes the one-sentence test: a visitor who reads only that sentence understands exactly what's being sold. |
| 4 | Every value claim passes the say-the-opposite test: if no competitor would ever claim the reverse, the claim is content-free and gets replaced with something checkable (a number, a mechanism, a named alternative). |
| 5 | Concrete numbers, mechanisms, timeframes and named audiences beat adjectives and superlatives. "7,123 companies signed up last week" beats "robust and efficient". |
| 6 | No entry from the floskel/banned-word list ships unreplaced (`copywriting.md` carries the full list and replacement principles). |
| 7 | Media is authentic before it is stock: real product screenshots, real team/customer photos before any stock asset. Where stock is unavoidable, it's candid and from a niche source, never an overposed model. Licensing per image documented (`assets.md`). |
| 8 | Legal pages exist and are linked from the footer on every page before the site counts as done: Impressum, Datenschutzerklärung, cookie consent banner if any non-essential script loads. See mandatory components below. |
| 9 | Decorative shader/3D/motion effects are licensed on hero and brand surfaces but stay out of content-heavy sub-pages within the same site (long-form articles, docs, dense pricing tables) per the boundary in [shaders.md](shaders.md); don't re-litigate that boundary here. |
| 10 | Every decorative effect carries the reduced-motion and mobile fallback required by [performance.md](performance.md). No exceptions for "just the hero". |
| 11 | Structural layout ([layouts.md](layouts.md)) is chosen because the content has that shape, a hero item among minor ones, two comparable things, a long homogeneous stream. Homogeneous content gets an honest grid, not a bento grid for visual interest. |
| 12 | Primary navigation may hide behind a hamburger below a breakpoint; unlike software, this is normal and expected on a shallow marketing site. |

## Anti-patterns

What typically ruins a website build. Each of these is a specific, nameable
failure, not a vague "make it less generic" note.

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| Generic hero: purple-to-blue gradient blob, oversized rounded icon, Inter, bounce-in text | Reads as originkit.dev's own signature opening move, copied past the point of reading as a decision | Pick color, type and motion from the project's actual palette and content, see [shaders.md](shaders.md) for the specific blob-on-black tell |
| Headline that is a slogan before it is a description ("Elevate your workflow") | Fails the one-sentence test, could sit on any competitor's site unchanged | Lead with what the product does, for whom, save the clever line for after clarity is established |
| Floskel-heavy copy ("seamless", "innovative solutions", "cutting-edge") | Content-free, filtered out by any competent reader or reviewer | Run every headline and value line against the floskel list in `copywriting.md` before calling copy done |
| Lorem ipsum or placeholder copy still present at "done" | Layout was built for text that doesn't exist, real copy won't fit the boxes built for it | Content-first: real copy drafted before or alongside layout, never after |
| Overposed stock photography of generic professionals | Visitors don't identify with staged stock, measurably lowers trust and conversion | Real product/team/customer imagery first, candid niche stock only as fallback |
| Missing or placeholder Impressum/Datenschutz ("Musterfirma GmbH") | Legal violation with real fine exposure (up to EUR 50,000 for missing Impressum, up to EUR 300,000 for cookie violations), and an instant abnahme blocker | Legal pages complete before any other polish work starts |
| Cookie banner with a prominent "Accept all" and a buried or absent "Reject all" | Fails current German case law requiring equally visible accept/reject | Both options equal weight, first layer, no pre-checked boxes |
| Alternating image-left/text-right sections purely for rhythm, no other variation | Reads as a template scroll, the alternation is the only design decision made | Vary section height, media treatment and copy length too, alternation becomes one axis among several ([layouts.md](layouts.md)) |
| A decorative WebGL background running on a content-heavy sub-page (blog post, long pricing table) | Competes with reading comprehension, drains mobile battery for no payoff | Confine decoration to hero/brand surfaces, static or CSS-only elsewhere |
| Diagonal split-screen cut or bento grid applied to genuinely homogeneous content | Structure implies a hierarchy or comparison that isn't actually there | Honest grid or stack when the content really is N similar items |

## Mandatory components

Nothing here is optional; a build that skips one of these is not finished,
regardless of visual polish elsewhere.

| Component | Requirement |
|---|---|
| Impressum page | All applicable items from DDG §5 present, reachable in at most two clicks from any page |
| Datenschutzerklärung page | All applicable items from DSGVO Art. 13 present, reachable in at most two clicks from any page |
| Cookie consent banner | Present whenever any non-essential script loads (analytics, marketing pixels, embeds), equal-weight accept/reject on the first layer, no pre-checked boxes, shown before the first non-essential request fires |
| Footer legal links | Impressum and Datenschutz linked from the footer on every page, not only the homepage |
| Primary headline | Passes the one-sentence test |
| Real content throughout | No lorem ipsum, no bracketed placeholder text `[insert benefit here]` |
| At least one authentic image or screenshot | Not 100% stock imagery, per the authenticity ranking above |
| PRODUCT.md and DESIGN.md derived files | Present alongside SOUL.md/MASK.md so impeccable-driven build stages (critique, polish, overdrive) have their required gate files |
| Reduced-motion fallback | For every decorative shader/3D/motion effect actually shipped, per [performance.md](performance.md) |
| Mobile fallback for any WebGL/3D hero | Static image, CSS gradient, or omission below the breakpoint defined in [performance.md](performance.md) |

## Check criteria

What critics and the final acceptance pass measure a website build against.

| Criterion | How it's checked |
|---|---|
| Legal completeness | Impressum and Datenschutz checked item-by-item against DDG §5 / DSGVO Art. 13, cookie banner checked against §25 TDDDG behavior rules |
| Floskel scan | Every headline, subhead and value line run against the floskel list in `copywriting.md`, flagged entries replaced or justified |
| Say-the-opposite test | Applied to every headline and primary value claim |
| One-sentence test | Applied to the primary headline in isolation, without supporting copy |
| Readability | Flesch Reading Ease in the 60 to 70 range for general audiences (German: Flesch-Amstad variant), lower only for stated technical/expert audiences |
| Tone consistency | NN/g four-dimension check (funny/serious, formal/casual, respectful/irreverent, matter-of-fact/enthusiastic) held constant across pages against the project's do/don't word list |
| Media authenticity | Each image checked against the authenticity ranking, stock usage justified and licensed |
| Performance | Lighthouse mobile score, CPU 4x / Fast 3G throttle test per [performance.md](performance.md), no showpiece effect allowed to tank the score |
| Reduced-motion behavior | `prefers-reduced-motion` toggled in devtools, page reloaded, result checked as a complete non-broken design, not a half-animated one |
| Contrast during animation | Text contrast checked at the darkest and brightest frame of any moving background, not just the average, against WCAG AA 4.5:1 |
| Structural intent | Each non-default layout pattern used ([layouts.md](layouts.md)) checked against its "avoid the slop version" note, is the variation tied to real content differences or applied mechanically |
| Content-first evidence | No placeholder copy anywhere on the reviewed pages at the point of critique |

## What this path does not check

Explicitly out of scope for website critics/acceptance, covered instead by
[software.md](software.md): keyboard-only operability, data table density
levels, empty/error state copy for application flows, dashboard KPI trend
requirements. A marketing site with an embedded app demo or signup flow
routes that specific screen through the software checklist, the rest of the
site stays on this one.

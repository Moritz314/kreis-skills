# Information architecture and structure

How to decide what goes where before a single screen gets drawn, then how to
apply the handful of actually-tested cognitive laws without the folklore
version of them that circulates in most AI-generated UI. Every claim below is
checked against `planung/recherche-software-aufbau.md`, which carries the
full citation list against primary sources; this file does not repeat that
list, only a short parenthetical next to each rule. Points the research
marked unverified stay marked here too, they are not dressed up as rules.

Screen-type mandatory components and check criteria that already live in
[software.md](software.md) or [website.md](website.md) are referenced, not
restated. Visual and type decisions belong to
[design-foundations.md](design-foundations.md), motion timing to
[motion-doctrine.md](motion-doctrine.md), the dial vocabulary used throughout
this file (`dichte`, `auftreten`, and the rest) is defined in
[registers.md](registers.md).

## 1. Structure before the first screen

Pick the structural model from what the content actually is, not from habit
(Rosenfeld/Morville/Arango 2015):

- **Hierarchy**: use it when every object maps cleanly to exactly one parent
  category. Default choice for content that is genuinely one-dimensional.
- **Facet classification**: use it once objects carry three or more
  independent description dimensions (price, date, category, status). A
  single hierarchy can only express one of those dimensions at a time, that
  is the signal to switch.
- **Matrix / database model**: drop fixed hierarchy in favor of metadata,
  tags, search and filtering once objects have many-to-many relationships a
  hierarchy cannot represent (a CRM contact belonging to several accounts and
  several campaigns at once).
- **Sequential structure**: not an independent navigation model. It is the
  structuring principle inside one flow (checkout, setup wizard, multi-step
  form), never the shape of the whole app.

**Depth versus breadth, the real finding, not the folklore version.** "Flat
beats deep" is real but weaker than commonly cited: Larson and Czerwinski
found two-level structures reliably faster to search than a three-level
structure with narrower categories, but their most extreme flat-and-wide
condition scored worse than a moderate-breadth one, and label clarity at the
top level mattered more than option count (Larson/Czerwinski 1998). NN/g's
own follow-up drops the numeric ceiling entirely: there is no universally
correct depth, flat suits unambiguous non-overlapping categories, deep
becomes necessary once a level would otherwise hold too many categories, and
then only works with orientation aids like breadcrumbs (Whitenton 2013).
Consequence for an LM building a nav tree: do not optimize toward "as flat as
possible" as a goal in itself. Test whether the top-level labels are
unambiguous first; if they are not, flattening makes the tree worse, not
better.

**Naming.** Use the words the user's own vocabulary, never internal system or
database terms; an accurate but unfamiliar label gets scanned past. Two
methods validate this against a real mental model rather than a guess: card
sorting, done early, participants freely group and name content (15
participants for a qualitative read, 30 to 50 for a quantitative one,
Tankala/Sherwin 2024); tree testing, done once a structure already exists,
participants try to find content inside it (Laubheimer 2023).

**Search and browse are complementary, never a substitute for the other.**
Search needs an articulable goal; navigation trades recall for recognition
and fits exploratory, goal-fuzzy behavior. Because a site's own search is
usually weaker than a general web search engine and users rarely know which
query will work on a given site, ship both (Budiu 2014).

**Register consequence.** At `dichte: verdichtet`, default toward facet or
matrix models with search-first retrieval: the whole point of a dense screen
is holding more objects and more dimensions than a hierarchy can carry, and
the audience is frequent enough to use filters instead of browsing. At
`dichte: luftig`, default toward hierarchy or a single sequential flow, one
path at a time, nothing to filter yet. On `auftreten: werkstatt` or `haus`,
lean on hierarchy with plain-language top categories, the audience is not
assumed tool-native. On `auftreten: labor` or `studio`, facet/matrix plus a
command palette or search-first pattern is the safer default, that audience
already expects it from other product tools it uses daily (this is Jakob's
law acting on the structural choice itself, not only on individual widgets).

## 2. The proven laws, applied correctly

Three lines each: what it says, what it does not say, what follows for
layout. This table is where most generic AI output gets it wrong, treat the
middle column as the actual rule.

| Law | What it says | What it does NOT say | Layout consequence |
|---|---|---|---|
| Hick's law (Hick 1952, Hyman 1953) | Decision time grows logarithmically with the number of equally likely options: T = a + b log2(n). Doubling the options does not double the decision time. | Not a case for "fewer options is always better." Applies to options actually being weighed, not to recognizing a familiar, grouped one. Categorization lowers the effective per-step count, that is the recommended technique, not deleting options outright. | Group long flat option lists (menus, dropdowns) under subheadings, put the most-used options first. |
| Fitts's law (Fitts 1954) | Time to reach a target T = a + b log2(2D/w), a function of distance D and target width w. Bigger, closer targets are reached faster and with fewer errors. | The "screen edge is an infinite target" reading is a mouse-cursor fact, not a touch fact, a finger is not stopped by the physical screen edge the way a cursor is. No license to make every target maximally large regardless of layout. | Put frequent and destructive actions large and close to the interaction that precedes them (submit next to the last field, not back at the top of the page); treat screen edges as a target-size gift only for desktop mouse targets. |
| Miller's work (Miller 1956) | Describes two separate capacities that happen to both land near seven: absolute judgment on a single-dimension stimulus, and short-term recall span without the item in view. | No statement about the right number of menu items or nav entries. Miller measured recall without sight of the item; a navigation menu is a recognition task with the options visible, the memory limit does not apply there. "Max 7 nav items" is one of the most common misapplications of HCI research in the field. | Do not size navigation breadth to the number 7. Size it to category distinctiveness (section 1) and to Hick's law for decision time. |
| Jakob's law (Nielsen, c. 2000) | Users spend most of their time on other sites and apps and carry those expectations in; they prefer an interface that works like the ones they already know. | Not a ban on innovation. NN/g's own framing: new patterns earn their place where they deliver a real, learnable advantage. | Use platform-standard patterns for baseline interactions (form behavior, icon meaning, nav position); spend originality only where it buys a genuine functional win. |
| Serial position effect (Murdock 1962) | Items at the start of a list (primacy) and the end (recency) are recalled more reliably than items in the middle. | Measures free recall from memory, not directly the scanning of a visible list. Its transfer to UI lists is a reasonable practice inference, not an independently tested interface-design finding. | Put the most important or most likely choice at the start or end of a list or menu, not buried in the middle. |
| Zeigarnik effect (Zeigarnik 1927) | Interrupted, incomplete tasks are remembered better than completed ones, they create lasting cognitive tension. | No evidence that artificially engineered incompleteness (a profile withheld as pressure) is uniformly positive, no independent check study exists for that use. | Build progress bars and onboarding checklists that show a visible, unfinished state rather than only a success message. |
| Doherty threshold (Doherty/Thadani 1982) | User productivity keeps rising as system response time drops well below the then-standard 2-second bar, with a particularly relevant point near 400 ms. | Not a general page-load budget. The original study measured interactive terminal response, not full page loads over a network. A second, sub-400ms threshold circulates in secondary sources but could not be traced to a citable primary source, do not cite it as fact. | Confirm any direct user interaction (click, keystroke) visibly within roughly 400 ms; for anything slower, use staged loading states (section 4). |

## 3. Heuristics: where they agree, where they clash

**Nielsen's ten** (Nielsen/Molich 1990, finalized 1994): visibility of system
status, match between system and the real world, user control and freedom,
consistency and standards, error prevention, recognition over recall,
flexibility and efficiency of use, aesthetic and minimalist design, help
users recognize/diagnose/recover from errors, help and documentation.

**Shneiderman's eight golden rules** (Shneiderman et al. 2016): strive for
consistency, seek universal usability, offer informative feedback, design
dialogs to yield closure, prevent errors, permit easy reversal of actions,
support internal locus of control, reduce short-term memory load.

**Norman's gulfs** (Hutchins/Hollan/Norman 1986, Norman 1988/2013): the gulf
of execution is the distance between a user's intent and the means to turn
it into action, closed by controls that visibly map to user goals. The gulf
of evaluation is the distance between actual system state and what the user
understands of it from feedback, closed by immediate, legible feedback.
Norman's 2013 revision adds affordance (what an object actually lets you do,
independent of the user) versus signifier (the perceivable signal that
communicates it): a button is technically clickable the moment a handler
exists, that alone does not make it read as clickable, only a visible cue
(shadow, contrast) does. Flat design with no signifier makes real affordances
invisible.

**ISO 9241-110:2020**, the international counterpart to the three US-rooted
catalogs above, sets seven dialogue principles: suitability for the task,
self-descriptiveness, conformity with user expectations (overlaps directly
with Jakob's law), suitability for learning, controllability, error
tolerance, suitability for individualization. It states these more
abstractly and without an example catalog, which fits a requirements
document or conformance statement better than day-to-day design decisions.

**Overlap and precedence.** Nielsen's "recognition over recall" and
Shneiderman's "reduce short-term memory load" are close to identical, and
most feedback/status rules in both catalogs reduce to Norman's evaluation
gulf, most control/reversibility rules to his execution gulf. None of the
three is an empirically tested law in the sense Fitts's or Hick's law are,
they are structured practitioner catalogs, useful for evaluation, not for
predicting an interaction time. Where two catalogs give conflicting emphasis
on the same screen, resolve toward Nielsen for day-to-day product decisions
(it is the basis for the software-path rule set already in
[software.md](software.md)), and toward ISO 9241-110 only when a formal
conformance statement or Lastenheft is actually the deliverable, not as a
daily design reference.

## 4. Patterns per screen type

Where [software.md](software.md) already states the mandatory components and
check criteria for a screen type, this section points there instead of
repeating it and adds only what the research surfaced beyond it.

- **Dashboard**: mandatory components and chart-type rules are in
  [software.md](software.md) rules 6 to 8. Underlying reason, worth keeping
  in mind when a critic has to justify a finding: bar and line charts read
  through preattentive processing (length, 2D position), pie charts and 3D
  effects do not support comparison the same way (Laubheimer 2017).
- **Large table**: task breakdown and sticky-header/density requirements are
  in [software.md](software.md) rules 9 to 10. The four tasks a table must
  support, as the research frames them, are finding a record, comparing
  records, viewing or editing one record, and acting on records in bulk
  (Laubheimer 2022); column order should follow which of those four the
  column serves, not database column order.
- **Form**: grouping and error-timing rules are in [software.md](software.md)
  rule 12 (software path) and website.md's content-first rule (site path).
  Additional form-specific finding from the research: label stays visible
  outside the input at all times, a placeholder is not a label substitute
  because it disappears on focus (Whitenton 2016).
- **Settings**: not covered in [software.md](software.md), covered here.
  Constrain customization to options with a demonstrated user benefit; a
  robust default beats option breadth (in one comparison, interface-level
  customization reached 83% task success against 66% for product-level
  customization, n=24, Nielsen 2009, small sample, treat as directional not
  conclusive). Toggle labels state the resulting condition directly and
  directionally ("Receive notifications", not "Notifications"), and toggles
  take effect immediately, no separate save step (Kendrick 2018). The
  research found no dedicated source on settings-page information
  architecture itself (categorization, search within settings), that gap is
  explicit, do not invent a rule to fill it.
- **Onboarding**: partially covered in [software.md](software.md) rule 18
  (no mandatory tutorial before first use). Additional detail: skip feature
  promotion on first launch, it is mostly skipped anyway; do not defer visual
  personalization into onboarding; only build a guided walkthrough for
  interaction patterns that are genuinely novel, not for the whole app
  (Kendrick 2020, Laubheimer 2023). Flag this pattern as leaning on NN/g's
  own internal observation rather than an independent controlled study.
- **Empty state**: mandatory-component requirement is in
  [software.md](software.md) rule 13. Additional distinction from the
  research: an empty state (task complete, nothing left) and a blank slate
  (never used yet) need different tone, confirming versus inviting, not the
  same copy (Kaplan 2021).
- **Error state**: message-quality requirement is in
  [software.md](software.md) rule 12. Nothing to add beyond what is already
  stated there.
- **Loading state**: not covered in [software.md](software.md), covered
  here. Under roughly 1 second, no indicator is needed at all. Between
  roughly 2 and 10 seconds, use skeleton screens that mirror the actual
  content structure about to load, not a generic header/footer placeholder.
  Beyond roughly 10 seconds, use a progress bar with a concrete figure, not
  an indefinite spinner (Tankala 2023, citing Mejtoft/Långström/Söderström
  2018). This ties directly to the Doherty threshold in section 2: the first
  roughly 400 ms need visible acknowledgment regardless of which of these
  three tiers the total wait falls into.

## 5. Progressive disclosure and data density

Progressive disclosure moves advanced or rarely used functions to a
secondary screen while the first view shows only what is essential (Nielsen
2006). Done right it improves learnability, efficiency and error rate at
once. The one line from the source worth keeping verbatim: designs that go
beyond two disclosure levels typically have low usability because users get
lost moving between levels. A second failure mode, independent of correct
content split: unclear navigation to the secondary functions themselves.

**Defaults are a design decision, not a neutral non-choice.** Countries with
opt-out organ donation show markedly higher consent than opt-in countries
(Johnson/Goldstein 2003); Thaler and Sunstein frame this as: a default
carries real consequences even when every option stays technically
selectable, because most users take the path of least resistance (Thaler/
Sunstein 2008, "Nudge"). The line between a legitimate default and a dark
pattern runs on three checks, not on the mere existence of a default: does
it serve the user's interest or the vendor's, is it disclosed as a default
rather than disguised as consent, is changing it exactly as easy as keeping
it (Gray et al. 2018 name the manipulative version "sneaking" / "interface
interference", Mathur et al. 2019 document it at scale on shopping sites,
the ECJ's Planet49 ruling, case C-673/17, 2019-10-01, holds that a
pre-checked box is not valid consent under EU law).

**Density in professional tools has two solid anchors, not more.** Carroll
and Rosson's "paradox of the active user" (1987) explains why goal-directed,
frequent users dive straight into the task rather than learning the full
feature set first, which is why experienced high-frequency users tolerate,
even prefer, a dense, directly accessible layout. Shneiderman's "overview
first, zoom and filter, then details-on-demand" mantra (1996) shows how
density stays controllable through an overview layer plus filter and detail
mechanisms, without cutting the information volume experts need. Beyond
these two anchors, the common claim that high density generally suits expert
tools and generally hurts casual or mobile users is practitioner belief, not
a quantitative study on its own, cite it as such.

**Register consequence, this is what `dichte` actually encodes.** At
`luftig`, keep disclosure to a single level wherever possible and density
low, that register fits onboarding and single-purpose flows where users are
not yet frequent. At `ausgewogen`, the two-level disclosure cap from section
5 is in full force and unremarked. At `verdichtet`, density stays high
without violating usability specifically by leaning on Shneiderman's
overview-zoom-filter-details structure: the dense first screen is the
overview, not the whole depth, drill-down carries the detail rather than
cramming it into the first view.

## 6. The checklist

Checkable at a finished screen, one item, one thing to look at. Items
already covered by [software.md](software.md)'s own check criteria (KPI
comparison, dashboard fit, chart type, nav pattern fit, hierarchy depth,
keyboard walkthrough, contrast, generic-look scan) are not repeated, this
list is the law/IA-grounded complement to that one.

1. Labels and navigation terms trace to a card sort, a tree test, or a
   direct user interview, not to internal system or database naming.
2. The structural model (hierarchy, facet, matrix, sequence) was chosen
   because the content has that shape, stated as a reason, not defaulted.
3. Top-level category names are checked for distinctiveness before any
   attempt to flatten the tree further.
4. No option list is judged "too flat" or "too deep" against a fixed number,
   the judgment traces to a tree-test success rate or a stated ambiguity
   check on the labels.
5. Frequent and destructive actions sit close, in interaction distance, to
   where the preceding step happened, not defaulted to page top or a
   far corner (Fitts).
6. Flat option lists at roughly eight or more entries are grouped under
   subheadings, most-used entries surfaced first (Hick).
7. No navigation width or menu length is justified by "the 7±2 rule",
   Miller's finding does not apply to a visible, recognized menu.
8. Progressive disclosure never exceeds two levels; the click path from the
   first view to the deepest hidden control has at most two intermediate
   steps.
9. Navigation to any secondary/hidden function is itself findable, not only
   the content split between primary and secondary correct.
10. The most likely or most important entry in any list or menu sits at the
    start or end, not buried in the middle (serial position).
11. Any multi-step process shows a visible, persistent progress indicator
    (step X of Y, a percentage, a checklist), not only a final success state
    (Zeigarnik).
12. Direct feedback to a click or keystroke appears within roughly 400 ms,
    even when the underlying operation takes longer (Doherty).
13. Every default value was checked against the three-question test: whose
    interest does it serve, is it disclosed as a default, is reverting it
    exactly as easy as accepting it. No pre-checked box for an upsell or a
    data-sharing choice.
14. Interactive targets measure at least 24 by 24 CSS pixels, 44 by 44 where
    the design allows it (WCAG 2.5.8 / 2.5.5).
15. Every screen makes it obvious, without hunting, what dialog the user is
    in, what actions are available, and how to perform them
    (self-descriptiveness, ISO 9241-110).
16. Multi-step processes allow stepping back or jumping between steps
    wherever the task itself does not require strict linearity
    (controllability, ISO 9241-110).
17. Search and browse/navigation are both present where the content volume
    warrants it, neither one stands in for the other.
18. Loading states follow the three-tier rule: nothing under about 1 second,
    a content-shaped skeleton for roughly 2 to 10 seconds, a concrete
    progress figure beyond that.
19. Settings screens are checked for options without a demonstrated user
    benefit; a strong default is treated as more valuable than added
    customization surface.
20. Onboarding is checked for anything that gates first use: a skippable,
    always-reachable help affordance is present instead of a forced
    walkthrough.

## 7. Anti-patterns

The ones this file's own sources uncovered that are not already listed in
[software.md](software.md) or [website.md](website.md).

| Anti-pattern | Cause |
|---|---|
| Navigation or menu artificially capped at seven entries | Miller's 7±2 misapplied to a recognition task (a visible menu) when it describes recall without sight of the item. |
| Flat design with no shadow, contrast or shape cue on clickable elements | An affordance exists but carries no signifier that communicates it (Norman). |
| Progressive disclosure nested past two levels | Users lose orientation moving between disclosure levels (Nielsen 2006). |
| Mandatory walkthrough or tutorial gating first use | Task-oriented users skip or forget instruction delivered outside the moment they need it (Laubheimer 2023, Carroll/Rosson 1987). |
| Pre-checked checkbox for an upsell or a data-sharing choice | The default serves the vendor's interest, disguised as user consent, instead of passing the three-question default test (Gray et al. 2018, ECJ C-673/17). |
| Toggle label stated neutrally ("Notifications") instead of directionally ("Receive notifications") | Current state cannot be read from the label alone (Kendrick 2018). |
| Icon-only control under 24 by 24 CSS pixels with no separating space from neighbors | Fails the WCAG target-size floor, raises mis-tap rate, especially on touch. |
| Forced linear wizard with no back-step or jump, where the task itself would allow one | Violates controllability (ISO 9241-110) and Shneiderman's internal-locus-of-control rule. |

Points the research marked unverified stay out of both the checklist and the
anti-pattern table above: the exact sub-400ms Doherty threshold circulating
in secondary sources, the claim that density-suits-experts holds as a
quantitative finding beyond Carroll/Rosson and Shneiderman, and any specific
guidance on settings-page information architecture that goes beyond section
4's default-versus-customization framing. Full source list, including these
gaps, stays in `planung/recherche-software-aufbau.md`.

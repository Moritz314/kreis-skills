# Copywriting as design material

Text is an interface decision, not filler dropped in after the layout is
done. A button label, a form error, the choice between "New" and "Updated"
are design choices with the same weight as spacing or color. All principles,
before/after examples, and the flosk list below come from
[recherche-software-content.md](../planung/recherche-software-content.md),
which cites a live-checked source for every claim, consult it for the full
citation trail. See [website.md](website.md) and [software.md](software.md)
for how tone maps onto each project type's structure.

## Order: content before layout

Write real copy before or alongside the visual design, never strictly after.
Layout-first with lorem ipsum is an anti-pattern: a layout sized for
placeholder text rarely fits the real text's length, and design decisions
made without real content tend to drift apart from it. Content-audit what
exists and what's missing before the first pixel, write realistic sample
copy in the target tone when exact final text isn't ready yet, and treat
"no more lorem ipsum on the page" as a launch gate, not a nice-to-have.

## Tone by type

- **Marketing/website copy** targets a stranger who hasn't decided anything
  yet. Lead with clarity (what is this), then relevance (is this for me),
  then value (do I want it), then differentiation (why you over the
  alternative), in that order. Wit before step one falls flat, nobody
  judges value before they understand the offer.
- **Software/product UI copy** targets someone already inside the tool,
  mid-task. It should be terser, use the user's own vocabulary for their
  domain, never internal field names, status codes, or database jargon, and
  stay out of the way of the task rather than trying to persuade. See
  [software.md](software.md) for the UI rules this pairs with.
- **Both** benefit from writing for scanners, not readers: headings, short
  paragraphs, bullet lists, front-loaded key words, since almost nobody reads
  web or app copy start to finish.

## Active, concrete formulations

- Prefer active voice and a named actor over passive constructions that hide
  who does what ("your data syncs automatically" over "data is
  automatically synced").
- Say the opposite as a test: state the reverse of a claim. If literally no
  one would ever claim the opposite ("we are inefficient and expensive"),
  the original claim ("efficient and cost-effective") is empty and needs
  replacing with something checkable, a number, a mechanism, a named
  comparison.
- Concrete numbers beat superlatives. "Last week 7,123 companies signed up"
  works because it's specific and verifiable, "robust, integrated,
  efficient" could be said by any competitor about any product.
- Cut ruthlessly. Practical drill: cut a sentence from seven words to four,
  read it aloud, listen for what's now missing versus what was actually
  needed.
- One-sentence test for a headline: does a reader who sees only this one
  sentence know exactly what's being offered? "Improve your workflow!"
  fails, "Get food delivered in 1 hour. No traffic, parking, or lines."
  passes.
- Universal value claims are worthless: "save time", "save money", "increase
  productivity" apply to nearly every product and get skimmed past unread.
  Replace with a specific, bounded outcome ("cut invoice processing from 5
  days to 4 hours").
- Borrow the customer's own words over marketing language. In real message
  testing, "on-brand docs" confused readers ("on-brand" read multiple ways,
  "docs" partly read as doctors), while "professional look", the customer's
  own phrase from reviews, tested clearly. Pull vocabulary from support
  tickets, reviews, and interviews, not from the internal deck.

## Labels that say what happens

- A UI label names the state or action precisely, not a vague category.
  "New" or "Updated" over "Modified" or "Recently Updated," whichever
  actually answers what the user wants to know at that moment.
- A button label names the result of clicking it, not a generic verb. "Find
  food" or "Start learning" continues the story the page already told,
  "Request a meeting" out of context tells the user nothing about what
  happens next.
- Loading/processing/success states get their own short, specific copy
  ("Syncing 12 files…", "3 changes saved") rather than a generic spinner
  with no label, visible system status is a core usability heuristic, not
  decoration.

## Error messages

- Plain, human language, not an error code or stack trace surfaced raw.
- Say exactly what went wrong, never a vague "an error occurred."
- Place the message directly next to the field or action it concerns, not in
  a disconnected toast the user has to hunt for the source of.
- Offer a constructive next step, what to do about it, not just a statement
  of failure.
- Never blame the user ("you entered this wrong"), describe the mismatch
  neutrally instead.
- Preserve whatever the user already typed, never clear a form on
  validation failure.
- Validate after the user finishes a field, not while they're still typing,
  showing red mid-keystroke on an incomplete entry reads as aggressive and
  frequently wrong.

## Empty states

- Never leave an empty state actually empty. Give a short status line
  explaining why there's nothing here, plus a direct path (link or button)
  to the next action. An unexplained empty container reads as a bug or a
  stuck loading state, not as "nothing here yet."
- Use the empty moment as a teaching opportunity, a short contextual pointer
  exactly where it's needed, rather than linking out to separate
  documentation the user has to leave the task to read.
- Distinguish an **empty state** (a task is done, or there's genuinely
  nothing here, e.g. "no failed jobs") from a **blank slate** (a feature
  has never been used yet, e.g. a fresh project's first dashboard) and word
  them differently: confirming and calm for the former, inviting and
  action-oriented for the latter. The same generic "Nothing here yet." for
  both situations misses the actual user state.

## The flosk list

Each entry below reads instantly as generated or hollow marketing copy.
Don't reach for a synonym, reach for the replacement principle: name the
number, mechanism, timeframe, or named alternative the vague word was
standing in for. Grouped by language, sourced from live-checked message
testing and copywriting research
(recherche-software-content.md).

### German

| # | Flosk | Replacement principle |
|---|---|---|
| 1 | nahtlos | Name exactly what happens without friction, in what time, at what volume, e.g. "syncs data in under 2 seconds" instead of "seamless sync." |
| 2 | revolutionieren, revolutionär | Show before/after in numbers (time saved, errors reduced), let the reader form the judgment. |
| 3 | innovative Lösungen | Name the solution itself, what it does, for whom, instead of the outside judgment "innovative." |
| 4 | auf Augenhöhe | Name concrete behavior that proves equal footing, e.g. "same contact person from first call to invoice." |
| 5 | ganzheitlich | List the covered areas individually so the reader judges the scope themselves. |
| 6 | maßgeschneidert | Name the adaptation mechanism, what varies, depending on which customer attribute. |
| 7 | Rundum-sorglos-Paket | List which tasks and which risk are actually taken over, and what no longer lands on the customer. |
| 8 | zukunftsfähig | Name the property that creates future-proofing, e.g. "cancel monthly" or "extendable via API." |
| 9 | Mehrwert schaffen | Quantify the value in customer metrics (euros, hours, percent). |
| 10 | kundenorientiert | Name a checkable process trait, e.g. response time, return window, availability. |
| 11 | flexibel und skalierbar | Name the limits and steps, up to what size, in what increments, at what cost. |
| 12 | Digitalisierung vorantreiben | Name the replaced paper process and the digital procedure concretely. |
| 13 | Prozesse optimieren | Name the process's before/after metric, e.g. "from 5 days to 4 hours." |
| 14 | Synergien nutzen | Name the two systems or teams that interact and what becomes unnecessary as a result. |
| 15 | auf höchstem Niveau | Name a checkable external criterion, e.g. certificate, benchmark, a rating with a number. |
| 16 | Exzellenz, exzellent | Name a performance metric or an independent award. |
| 17 | zeitgemäß | Name the concrete method or technology that justifies "current." |
| 18 | bedarfsgerecht | Describe the needs-assessment step that leads to the solution. |
| 19 | disruptiv | Name the prior alternative and what is structurally different about the new model. |

### English

| # | Flosk | Replacement principle |
|---|---|---|
| 20 | empowering | Name the new capability, what the user can now do that they couldn't before. |
| 21 | cutting-edge | Name the technology or method, with origin and age if possible, instead of a value judgment. |
| 22 | unlock your potential | Name a measurable outcome that gets unlocked, e.g. "export the reports only admins could see before." |
| 23 | seamless | Same as "nahtlos": name the time and step that disappears or runs automatically. |
| 24 | game-changing | Deliver a before/after comparison to the prior category, leave the judgment to the reader. |
| 25 | state-of-the-art | Name a spec or standard that substantiates the state of the art. |
| 26 | next-level | Name a quantitative increase (percent, factor) instead of a step metaphor. |
| 27 | elevate your | Describe the concrete result of the advertised activity, before and after. |
| 28 | unleash | Name the capability or resource being freed, what was blocking it, and what removes the block. |
| 29 | disruptive | Same as "disruptiv": named alternative plus the structural difference. |
| 30 | world-class | Name an external ranking, certificate, or referenceable customer. |
| 31 | best-in-class | Deliver a direct, named comparison against actual alternatives. |
| 32 | leverage synergies | Describe how the two parts interact and the concrete result of that interaction. |
| 33 | robust solution | Name a resilience metric, e.g. uptime percent, load limit. |
| 34 | streamline your workflow | Name the workflow step that disappears and the time saved. |
| 35 | drive more revenue | Name the mechanism through which revenue is actually generated. |
| 36 | AI-powered | Say what the AI does and with what measurable effect, the term has become an empty expectation on its own. |
| 37 | scalable | Name the limit up to which it scales without price or process changing. |
| 38 | holistic approach | Same as "ganzheitlich": list the sub-areas individually. |
| 39 | transform your business | Show a real customer's before/after scenario. |
| 40 | save time, save money | Name a number (hours per week, euros per month), otherwise it applies to every product and gets skimmed past. |

## Before/after pattern across all examples

Every strong "after" in the source research names a number, a timeframe, a
named audience, a mechanism, or a named contrast. Every weak "before" names
an adjective or a promise any competitor could make unchanged. When editing
a draft, ask which of those five it's missing and add exactly that, not a
better-sounding adjective.

## Check before shipping copy

The self-check for the skill, derived from the principles above: could this
sentence sit unedited on a competitor's site? If yes, it's generic, replace
it with a number, mechanism, audience, or named alternative. Beyond that,
run German copy through a readability check calibrated to a German formula
(Flesch after Amstad, not the English Flesch formula, which scores German
syllable counts unfavorably), target range 60 to 70 for general web copy,
lower only for a genuinely specialist audience. For legal boilerplate
(Impressum, Datenschutzerklärung) on a German-facing site, treat completeness
as a launch blocker, not a style question, see
recherche-software-content.md's legal section for the current § 5 DDG and
Art. 13 DSGVO requirements, this file doesn't repeat that list.

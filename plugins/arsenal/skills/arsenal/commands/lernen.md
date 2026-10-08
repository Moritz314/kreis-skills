# lernen

## Purpose

Grows the reference library from real sources: open college courses, canonical books and essays by
recognized designers, standards, primary studies. The point is not the knowledge itself, the model
already carries most of it. The point is the translation into measurable checkpoints, one sentence
with a threshold or a measurement procedure, that `critics` can apply to a finished screen and
either pass or fail. A source that only yields "good typography matters" has yielded nothing here.

Every run ends in a confirmation step. `lernen` never writes into `reference/` on its own judgment,
because a reference file that grew by accident is worse than one that grew slowly.

## Arguments

`lernen <topic|url> [--nur-quellen] [--quelle <url> ...]`

| Argument | Effect |
|---|---|
| `<topic>` | Topic mode: the workflow curates its own sources for the topic, then reads them. |
| `<url>` | URL mode: the named source is appraised and read directly, no curation. |
| `--quelle <url>` | Adds a source explicitly. Repeatable. Combines with a topic, in which case curated and named sources are appraised together. |
| `--nur-quellen` | Stop after curation, return the shortlist, read nothing and write nothing. Use it to see what a topic would pull in before spending a read on it. |

The main model passes two further values into the workflow that are not typed on the command line:
`datum` (today's date in ISO form) and `skill_pfad` (the absolute path to this skill folder, which
differs per platform, see SKILL.md's path table). The workflow refuses to run without either, and
never reads the clock itself: the check date belongs to the source record, not to the run.

## Preconditions (gates)

1. Load `behavior.md`. Missing: abort, run `behavior`.
2. No ARMOURY gate. `lernen` is global, it grows the skill and not a project, so no project needs
   to be in scope and no dials are read.
3. `WebFetch` reachable. Not reachable: abort in topic and URL mode alike, and say which tool
   failed. A learning run that cannot open a source has nothing to learn from.
4. `reference/_index.md` must exist. Missing: abort and say so, the reconciliation step judges
   duplicates against it and would otherwise wave through rules the stock already holds.

## Procedure

The command runs in **two passes with a confirmation between them**, both through the same
`workflows/lernen.js` file. Pass one produces candidates and writes nothing; pass two writes only
what the user approved.

### Pass one, candidates

1. **Curation** (opus, parallel, topic mode only). Four curators propose sources independently,
   one per lens: open course material, canonical books and essays, standards and official
   guidance, primary studies. A fifth agent merges and shortlists at most four in rank order, by
   expected yield of measurable rules first, citability second, accessibility third. Judging what
   deserves to be read at all is judgment, which is why this step is not delegated downward. With
   `--nur-quellen` the run ends here and returns the shortlist.
2. **Source appraisal** (sonnet, one agent per source). Title, author, year, address,
   accessibility (`open`, `registration`, `paid`), citability, and the check date taken from the
   passed-in date. Accessibility is established by actually checking the address, never guessed
   from the domain.
3. **Derivation** (sonnet, one agent per open source, inside a per-source pipeline). The agent
   reads with WebFetch in its own context and returns structured rules only. Per rule: the rule as
   one sentence with a threshold or a measurement procedure, the check a reviewer performs, one
   line saying what the rule does NOT say, exactly one dial from
   [reference/registers.md](../reference/registers.md) (`auftreten`, `bewegung`, `dichte`,
   `technik`, `tonfall`), exactly one target file under `reference/`, the citation in parentheses
   with its location, and whether the evidence is `measurable` or `unproven`. Anything that will
   not go into that format is discarded with a reason, or carried as `unproven` background. Three
   solid rules and six discards is a good result.
4. **Reconciliation** (opus, one critic per source, second stage of the same pipeline). The critic
   loads the target files and `_index.md` in full and decides per rule: `accept`,
   `accept-with-precedence` (the rule overlaps an existing one, so it arrives with a bold
   precedence line in the pattern of `reference/design-foundations.md:44` naming which file
   governs on conflict), or `reject` with a reason. It also corrects a wrong target file. Deciding
   a duplicate or a contradiction is judgment, so it stays on opus.
5. **Confirmation** (the user). The workflow returns the candidate list and stops. The main model
   puts it to the user with `AskUserQuestion`, one question per candidate group, each option showing
   the rule, its check, its target file and the critic's decision with the reason. Batch related
   candidates into one question rather than asking eight times; a candidate the critic rejected is
   still offered, marked as rejected, because the user may overrule the critic. Nothing has been
   written at this point, so a run that ends in "none of these" costs nothing but the read.

### Pass two, filing

6. **Filing** (haiku). The main model calls the same workflow again with `bestaetigt` (the approved
   slugs) and `kandidaten` (the candidate array from pass one). Filing is diligence, not judgment:
   nothing is re-derived, so a rule cannot drift between what the user saw and what lands on disk.
   Per approved rule, sequentially so two agents never edit the same file at once:
   - the rule is written into **exactly one** file under `reference/`, in that file's house style,
     with its "what the rule does NOT say" line, its check, `status: unverified`, and its
     precedence line at the top of the section where one was supplied;
   - one row is added to `reference/_index.md`;
   - one line per source is appended to `planung/recherche-lernen.md`.

## The reference index format

`reference/_index.md` is a header line naming its purpose, then a single table:

```
| slug | file | tags | one sentence | source | date | status |
```

It exists so a critic can see the whole stock at a glance without loading every reference file,
which stops working the moment the file needs paging. So it stays **under 2000 characters**. When
new rows cross that budget, the filing step moves the oldest rows whose status is still
`unverified` into `reference/_index-archiv.md` (same header, same columns) until the index fits
again. A `verified` row is never archived, and a row is never dropped instead of archived. The
archive file is created on first need; it is not built in advance.

`planung/recherche-lernen.md` is the source register, one line per source ever consulted:
`source_slug | title | author | year | url | accessibility | citable | checked | rules filed`. A
source that was appraised but not read carries `not accessible, consider author talks or open
summaries` in the last column, so a later run sees it was already considered and does not curate
it a second time.

## Output

Pass one: the source records (with what was read and what was only recorded), the candidate rules
with rule, check, target file, dial, evidence and the critic's decision, and the discards. No file
is touched.

Pass two: the rules written per reference file, the index rows added, any slugs archived out of the
index, and the source lines appended.

## Limits

- **Paid and gated sources are recorded, not read.** Anything whose accessibility is not `open` is
  filed with `not accessible, consider author talks or open summaries` and skipped. `lernen` does
  not route around a paywall, and it does not pretend a preview page is the book.
- **No verbatim text.** Principles and short cited phrases with their location only. A quotation is
  justified only where the wording itself is the evidence.
- **Context contract.** Raw material never reaches `reference/` and never reaches the workflow's
  return value. Every subagent reads in its own context and hands back structured data. This is
  what makes a learning run affordable: the cost is one read inside one subagent, not a transcript
  carried through the rest of the session.
- **One rule, one place.** A rule that seems to fit two files goes into the more specific one and
  is cross-referenced from the other. Duplication across reference files is what makes a library
  contradict itself later.
- **The dials are closed.** Rules are classified against the five dials in
  [reference/registers.md](../reference/registers.md). `lernen` never invents a sixth dial or a new
  stop on one.
- **Nothing is written without a yes.** There is no auto-confirm flag, deliberately.

## Abort conditions

- `behavior.md` missing.
- `WebFetch` unreachable.
- `reference/_index.md` missing.
- Neither a topic nor a source given.
- `bestaetigt` passed without `kandidaten`, or with slugs that were never in the candidate list.
  The filing pass refuses to write a rule that was never shown.
- Curation finds no citable source worth reading. That is a valid result, reported plainly: narrow
  the topic or name a source with `--quelle`, rather than reading something weak to have read
  something.

## Open follow-ups

- **Verification is not wired up yet.** Every rule `lernen` files carries `status: unverified`. A
  rule earns `verified` when a critic has actually applied it once in a real project and it held.
  The intended mechanism is that [critics.md](critics.md) flips the status of any rule it used to
  produce a finding, and that `_index.md` is where that flip is recorded, since it is the one file
  that already carries the status column. `critics` does not do this today and is not changed by
  this command; wiring it is the next step, and until then the whole library reads as unverified.
- **No usage signal.** Nothing yet records which filed rules critics actually reach for, so the
  index cannot be pruned by evidence of use, only by age and status.

## References

[reference/registers.md](../reference/registers.md) for the five dials,
[reference/design-foundations.md](../reference/design-foundations.md) and
[reference/ia-and-structure.md](../reference/ia-and-structure.md) as the house pattern for a filed
rule (source in parentheses, unproven marked as such, precedence line on conflict),
[workflows/lernen.js](../workflows/lernen.js) for the two entry points,
[commands/critics.md](critics.md) for the consumer of everything this command files.

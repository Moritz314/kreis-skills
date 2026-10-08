# loot

## Purpose

Turns a URL or screenshot into a confirmed, reusable reference entry in the library, section by section, with an explicit "what exactly do you like about this" checkpoint per section. Only confirmed parts get saved. This is the reference-grounding step `build` pulls from before generating anything, and the single best-evidenced lever against generic output.

## Arguments

`loot <url|screenshot-path> [type]`

`type` (`website` or `software`) tags which ruleset the entry applies to, ask if not given and not obvious from the source.

## Preconditions (gates)

1. Load `behavior.md`. Missing: abort, run `behavior`.
2. No ARMOURY gate, `loot` is global by default and only reads a project's stored type from `projects.json` if tagging an entry to a specific project.
3. Browser tools reachable for a URL (Chrome DevTools MCP or claude-in-chrome). Not reachable: abort, tell the user which tool failed.

## Procedure

1. Get the URL or screenshot from the user. A screenshot is analyzed as input only, it is never itself stored, see the rule below.
2. Analyze section by section, in this fixed order: **Hero, Navigation, Typography, Color strategy, Motion, Components, Copy tone.** Skip a section only if it genuinely doesn't exist on the source (e.g. no navigation on a single-scene landing), say so rather than silently omitting it.
3. After each section's analysis, ask: "what exactly do you like about this?" Do not proceed to save a section on a vague "looks good", press for the specific thing (the easing curve, the type pairing, the way copy is understated) that would actually transfer to a future build.
4. Only sections with a confirmed, specific answer get saved. Anything unconfirmed or rejected is dropped, it never reaches `library/`.
5. Write one entry per confirmed section (or one file with confirmed sections as subsections, whichever keeps related sections together) to `library/muster/<slug>.md` in the sync path. `loot` writes to `muster/`, never to `eigene/`. **`eigene/` is reserved and, as of 2026-09-09, not populated by any command**: `build` reads it during loot grounding but no command writes an element back into it after assembly, so its entries are hand-written for now. An empty `eigene/` is the expected state, not a fault, and `loot` must not start filling it to make the branch look used. Slug from source domain/name plus date, append a suffix on collision.
6. Entry content: **description and analysis only** (what it is, why it works, the confirmed reason the user gave), source URL, date, tags, applicable ruleset (website/software). Never store copied code or the third-party's actual assets (images, fonts, icons), the point is a reusable description `build` and `plan` can match by tag, not a copy of someone else's work.
7. **Append a row per saved entry to `library/_index.md`** (slug, branch, category, tags, one clause on what it holds, source, date). That index is what `build`'s loot grounding reads first, so an entry missing from it is an entry no build will ever find. Keep the rows terse; the index is a pointer table, not a second copy of the entry.
8. Confirm the saved entries to the user and note they're now available to `plan`/`build` via their tags.

## Output

One or more entries under `library/muster/<slug>.md` in the sync path, each with description, source, date, tags, ruleset.

## Abort conditions

- `behavior.md` missing.
- No URL/screenshot given.
- Browser tools unreachable for a URL source.
- Every section rejected or unconfirmed, nothing gets written, report that plainly rather than saving a thin entry to have something.

## References

None beyond the browser-automation tooling itself (Chrome DevTools MCP / claude-in-chrome).

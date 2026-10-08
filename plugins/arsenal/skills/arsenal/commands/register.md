# register

## Purpose

`plan` for a project that already exists. Crawls the live project or its code, derives SOUL.md/MASK.md/ARMOURY.md from what's actually there, fills whatever the crawl couldn't determine with a short interview, and adds the project to the database. Result is a project `build` and `critics` can operate on exactly as if `plan` had created it.

## Arguments

`register <project-path> [url]`

`url` is optional, if given the crawl inspects the live site/app in addition to the local code.

## Preconditions (gates)

1. Load `behavior.md`. Missing: abort, run `behavior`.
2. No ARMOURY gate, `register` is what creates it. If SOUL.md/MASK.md/ARMOURY.md already exist at `project-path`: stop and ask whether this is meant to be a re-register (overwrite) or the project is already managed, use `db <name>` to check instead.
3. Browser tools must be reachable if `url` is given (Chrome DevTools MCP or claude-in-chrome). Not reachable: fall back to code-only derivation and say so.

## Procedure

1. Crawl the project. With a URL: visit the key routes/pages, take snapshots and screenshots, read rendered text, note console/network issues worth flagging. Without a URL, or in addition: read the codebase for stack, existing design tokens, component structure.
2. Derive a SOUL.md draft: register (brand vs product, hence type website vs software), users, product purpose, brand personality, anti-references (leave open where the crawl gives no signal), design principles, accessibility notes observed.
3. Derive a MASK.md draft: colors, typography, spacing, elevation, components actually observed in the rendered output or the design tokens found in code.
4. Derive an ARMOURY.md draft: type, tools/frameworks detected, libraries in use, no skills/assets guessed, leave those sections for the interview or empty.
   **Also derive `## Dials`, this is not optional.** Set all five settings from [reference/registers.md](../reference/registers.md) (`auftreten`, `bewegung`, `dichte`, `technik`, `tonfall`), each justified from something actually observed in the crawl (existing motion, information density, JS usage, tone of the copy), not guessed. SKILL.md's preflight aborts `build` and `critics` when the block is missing or incomplete, so a project registered without it is dead on arrival. Where the crawl genuinely cannot settle a dial, that dial is an interview question in step 5, never a silent guess.
   **Conflicting source documents:** when the project holds several design or product documents that disagree, prefer the one the project itself treats as binding and read each for self-marked status. A document that labels itself a draft, a proposal or superseded does not override the binding one, and its values must not be copied. Name the sources used and the ones rejected in the report at step 13.
5. **Interview to fill gaps**, same cadence as `plan`: max 3-4 questions per round. Only ask what the crawl genuinely couldn't determine, don't re-ask what's already visible in the derived drafts.
6. Confirm the assembled SOUL.md/MASK.md/ARMOURY.md content back to the user before writing.
7. Write SOUL.md, MASK.md, ARMOURY.md at `project-path`.
   **Before step 8 touches anything, guard the two derived files.** Gate 2 only checks SOUL/MASK/ARMOURY, so a project with hand-written `PRODUCT.md` or `DESIGN.md` reaches step 8 unwarned and step 8 overwrites them. If either file already exists at `project-path`, copy it to `PRODUCT.md.vor-register` / `DESIGN.md.vor-register` first, then report in step 13 what the derived version dropped against the hand-written one. Derivation compresses reasoning: the numbers and rules survive, the argument for them shrinks, and that loss must be visible to the user rather than silent.
8. Derive standalone PRODUCT.md and DESIGN.md at the project root from SOUL.md/MASK.md, same as `plan` step 9.
   **Normative content has to survive the derivation, not just the numbers.** Compressing the argument for a rule is allowed. Dropping the rule is not. Before writing either file, diff it against its `.vor-register` copy and confirm every one of these appears in the derived text:
   - every stated threshold or measured value (contrast ratios, the colour values behind a token name, age thresholds, chroma ranges, percentage caps);
   - every prohibition, including the ones that sit as bare list items under a "forbidden" or "never" heading;
   - every usage rule bound to a token (which typeface is for what, where a colour may appear, what a component must do);
   - every instruction attributed to a person or carrying a date, for example "Anweisung the user, 2026-08-29", these exist nowhere else and are unrecoverable once dropped;
   - every cross-reference to another document.
   If one of these is missing from the derived file, **do not write it.** Carry the item into SOUL.md or MASK.md first, then derive again. A binding rule that survives only in `PRODUCT.md.vor-register` is lost in practice: impeccable's context gate reads the derived file, and nothing reads the backup. The Phase 6b run lost the whole "Symbol statt Wort" section, all four traffic-light colour values, the 4.5:1 and 3:1 contrast floors and a dated instruction from the user this way, with the backup sitting untouched beside it.
9. Copy the type-matched template, [workflows/website.js](../workflows/website.js) or [workflows/software.js](../workflows/software.js), into `project-path` as `workflow.js`.
10. **Fill every `__TOKEN__` placeholder** in the copied `workflow.js`, exactly as `plan.md` step 11 does: replace each bare `__TOKEN__` sentinel with a complete JS literal, quotes included for string values, from the derived SOUL.md/MASK.md/ARMOURY.md content and the interview answers.
    - Shared by both templates: `PROJECT_NAME`, `PROJECT_PATH`, `SKILL_PATH`, `LIBRARY_PATH`, `REGISTER`, `AUDIENCE`, `LOOT_TAGS`, `TECHNIQUES`, `VARIANT_COUNT`.
    - Website only: `SECTIONS`.
    - Software only: `COMPONENTS`, `STATES`, `PRIMARY_ACTION`, `EXISTING_SYSTEM`.
    **Completeness check**: first delete the template's own header comment block, the one documenting the placeholder convention, since it belongs to the template and not to a filled instance. That block itself contains the literal `__TOKEN__`, so a check run before deleting it always fails. Then search the remaining file for the pattern `__[A-Z_]+__`. If any occurrence remains, do not write the file, go back and fill the missing token instead.
11. **Git repository, if absent.** Run `git rev-parse --is-inside-work-tree` in `project-path`. If it fails, run `git init` there, add a `.gitignore` appropriate to the detected stack, and make one initial commit that captures the project as found plus the files just written. An existing project usually already has a repository, in which case this step is a check and nothing more; commit the newly written SOUL/MASK/ARMOURY/PRODUCT/DESIGN/workflow files rather than leaving them loose in the working tree. `build` gates on this (its Preconditions step 5). Do not commit secrets: check that no `.env` or credentials file enters the commit.
12. Add an entry to `projects.json`: name, path, type, created date, status `registered`.
13. Report the file list and point to `build` or `critics` as the next command. The report carries step 8's comparison, split into **rationale dropped** (expected, derivation compresses reasoning) and **normative content dropped** (a defect step 8 should already have caught, name it as one).

## Output

SOUL.md, MASK.md, ARMOURY.md, PRODUCT.md, DESIGN.md, workflow.js (fully filled, no `__TOKEN__` left) in the project folder; a new record in `projects.json`.

## Abort conditions

- `behavior.md` missing.
- Neither a reachable `url` nor a readable local codebase, nothing to crawl.
- Project already registered and the user declines to overwrite.
- Any `__TOKEN__` placeholder left unfilled in `workflow.js` after step 10's completeness check, in that case do not write the file, go back and fill it.

## References

[reference/website.md](../reference/website.md), [reference/software.md](../reference/software.md), [workflows/website.js](../workflows/website.js), [workflows/software.js](../workflows/software.js).

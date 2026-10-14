# plan

## Purpose

Turn a brief into a fully scaffolded project: a multi-round discovery interview, the three project files (SOUL.md, MASK.md, ARMOURY.md) plus their derived PRODUCT.md/DESIGN.md, a workflow file ready for `build`, and an entry in the project database. This is arsenal's version of impeccable's `teach`, extended with the type split and the workflow handoff.

## Arguments

`plan [project-path] [brief]`

- `project-path`: folder the project lives or will live in. Ask for it in round 1 if not given.
- `brief`: free-text starting point. Never treat it as a finished answer set, it seeds round 1's questions, it does not replace them.

## Preconditions (gates)

1. Load `behavior.md` from the sync path. Missing: abort, tell the user to run `behavior` first.
2. No ARMOURY gate, `plan` is what creates ARMOURY.md.
3. If SOUL.md/MASK.md/ARMOURY.md already exist at `project-path`: stop and ask whether to overwrite or hand off to `register` instead, `plan` is for new projects, `register` is for existing ones.

## Procedure

1. **Round 1 (max 3-4 questions).** Type is always the first question: website or software. Then purpose and audience. Do not accept a single-sentence brief as sufficient context and synthesize the rest yourself, impeccable's ban on synthesizing PRODUCT.md from the raw prompt applies here identically, wait for a real answer round.
2. Once type is known, load [reference/website.md](../reference/website.md) or [reference/software.md](../reference/software.md) and follow any type-specific interview prompts it defines, on top of the base rounds below.
3. **Round 2 (max 3-4 questions).** Website: content/sections, register (brand vs product), scope. Software: primary action, existing design system or conventions to inherit, states that matter (empty, loading, error, edge case).
4. **Round 3, only if still open (max 3-4 questions).** Visual direction, anti-references, constraints (mobile-heavy audience, low-power devices, brand guardrails). Skip with a named reason if round 1-2 answers already settle this.
5. Confirm the assembled brief back to the user in a short summary before writing anything, this is the shape-brief-confirmation gate impeccable also enforces for `craft`.
6. Write `SOUL.md` at `project-path`, structured as PRODUCT.md: `## Register`, `## Users`, `## Product Purpose`, `## Brand Personality`, `## Anti-references`, `## Design Principles` (3-5, strategic only, no visual rules), `## Accessibility & Inclusion`.
7. Write `MASK.md` at `project-path`, structured as DESIGN.md: colors, typography, elevation, components, motion.
8. Write `ARMOURY.md` at `project-path`: `## Type`, `## Dials`, `## Tools`, `## Libraries`, `## Skills`, `## Assets`, `## Project overrides` (empty unless the interview surfaced a standing-preference exception).
   **`## Dials` is not optional.** Set all five settings defined in [reference/registers.md](../reference/registers.md) (`auftreten`, `bewegung`, `dichte`, `technik`, `tonfall`), each with a one-line justification tied to a specific interview answer or SOUL.md line. SKILL.md's preflight aborts `build` and `critics` when this block is missing or incomplete, so a project written without it is dead on arrival. Derive the values from the round 2 and 3 answers, and check the guard-rail combinations registers.md lists before writing.
9. Derive standalone `PRODUCT.md` and `DESIGN.md` at the project root from SOUL.md/MASK.md, verbatim content, so impeccable's context gate passes unmodified. Never hand-edit these two, regenerate them whenever SOUL.md or MASK.md changes.
10. Copy the type-matched template, [workflows/website.js](../workflows/website.js) or [workflows/software.js](../workflows/software.js), into `project-path` as `workflow.js`.
11. **Fill every `__TOKEN__` placeholder** in the copied `workflow.js`, per that file's own header comment. Replace each bare `__TOKEN__` sentinel with a complete JS literal, quotes included for string values, from the content just written to SOUL.md/MASK.md/ARMOURY.md and from this interview:
    - Shared by both templates: `PROJECT_NAME`, `PROJECT_PATH`, `SKILL_PATH`, `LIBRARY_PATH` (the sync path resolved for the current platform, see SKILL.md's state-layer table), `REGISTER`, `AUDIENCE`, `LOOT_TAGS`, `TECHNIQUES`, `VARIANT_COUNT`.
    - Website only: `SECTIONS`.
    - Software only: `COMPONENTS`, `STATES`, `PRIMARY_ACTION`, `EXISTING_SYSTEM`.
    **Completeness check**: first delete the template's own header comment block, the one documenting the placeholder convention, since it belongs to the template and not to a filled instance. That block itself contains the literal `__TOKEN__`, so a check run before deleting it always fails. Write the file with LF line endings only (no ``, also add `*.js text eol=lf` to the project's `.gitattributes`): the Workflow tool refuses a script containing carriage returns as hidden control characters. Then search the remaining file for the pattern `__[A-Z_]+__`. If any occurrence remains, do not write the file, go back and fill the missing token instead.
12. **Git repository, if absent.** Run `git rev-parse --is-inside-work-tree` in `project-path`. If it fails, run `git init` there, add a `.gitignore` appropriate to the stack, and make one initial commit of the files just written. `build` gates on this (its Preconditions step 5) and its assembly phase depends on being able to see and undo what an agent pass changed, so a project scaffolded without a repository is a project `build` will refuse. Do not commit secrets: check that no `.env` or credentials file is in the initial commit. If the commit fails with "Author identity unknown" (fresh folder, no global git identity), set a repo-local identity with `git config user.name`/`user.email` from the user's known identity and retry, never write it globally.
13. Add an entry to `projects.json` in the sync path: name, path, type, created date, status `planned`.
14. Report the file list and point to `build` as the next command.

## Output

SOUL.md, MASK.md, ARMOURY.md, PRODUCT.md, DESIGN.md, workflow.js (fully filled, no `__TOKEN__` left) in the project folder; a new record in `projects.json`.

## Abort conditions

- `behavior.md` missing.
- Project already has SOUL/MASK/ARMOURY (use `register` or confirm overwrite explicitly).
- Discovery round skipped or answered with a single unconfirmed sentence, in that case restart the round rather than proceeding.
- Any `__TOKEN__` placeholder left unfilled in `workflow.js` after step 11's completeness check, in that case do not write the file, go back and fill it.

## References

[reference/website.md](../reference/website.md), [reference/software.md](../reference/software.md), [workflows/website.js](../workflows/website.js), [workflows/software.js](../workflows/software.js).

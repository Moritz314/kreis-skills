# db

## Purpose

Lists the projects arsenal manages, or shows one project's full record: paths, type, timestamps, last `critics` findings summary.

## Arguments

`db` (list all)
`db <name>` (single project detail)

## Preconditions (gates)

1. Load `behavior.md`. Missing: abort, run `behavior`. (This command does not use its content, the load still runs as the universal preflight contract.)
2. No ARMOURY gate, `db` only reads what `projects.json` already recorded, it never loads a project's live ARMOURY.md.

## Procedure

1. **No argument:** read `projects.json` from the sync path, list every project with name, type, path, status, `updated` date. Empty or missing file: report "no projects yet, run `plan` or `register`."
2. **`db <name>`:** look up the matching record. Show: full path, SOUL.md/MASK.md/ARMOURY.md/workflow.js paths, type, `created`/`updated` dates, status, and the stored `last_critics` summary (date plus Necessary/Recommended/Taste counts) if one exists.
3. No exact match: list close matches by name instead of failing silently.

## Output

A project list, or one project's full record, printed to the conversation. Never modifies `projects.json`.

## Abort conditions

- `behavior.md` missing.
- `projects.json` missing or empty on a bare `db` call, report it and point to `plan`/`register` rather than erroring.

## References

None. `projects.json`'s schema (name, path, type, created, updated, status, last_critics) is written by `plan`, `register`, `build` and `critics`, `db` only reads it.

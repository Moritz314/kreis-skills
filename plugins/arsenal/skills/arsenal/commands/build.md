# build

## Purpose

Runs the actual construction: shows the build plan as a flowchart, incorporates the user comments on it, then executes the fixed-order workflow (content before layout, loot references before generation, variants generated and selected, an independent critique loop, a performance/reduced-motion gate) via the Workflow tool. Without the fixed order this command is just an expensive generator, the order is the point.

### `interface` alias

`interface [args]` runs `build [args]` only for a project whose `ARMOURY.md` `## Type` is already `software`. Before doing anything else, `interface` reads `## Type` from the project's `ARMOURY.md`: if it is `software`, proceed exactly as `build` would. If it is `website`, abort: tell the user this project was set up as a website (per `plan`/`register`) and that `build` is the right command, do not silently run the website workflow under the `interface` name. `interface` never overrides `## Type`, it only gates on it.

### Partial builds

`build copy` and `build assets` run only the matching workflow stage (content generation, or asset sourcing per [reference/assets.md](../reference/assets.md)) instead of the full pipeline. Same gates. The flowchart-and-comment step (procedure steps 3-5) is skippable for these partial builds, per the handoff decision that a flowchart is not required for single-component/single-stage work; run it anyway if there's a specific change worth flagging to the user first.

## Arguments

`build [project-path] [copy|assets]`
`interface [project-path] [copy|assets]`

`project-path` defaults to the current project if unambiguous.

## Preconditions (gates)

1. Load `behavior.md`. Missing: abort, run `behavior`.
2. Load `ARMOURY.md` for the project, read `## Type`. Missing ARMOURY.md: abort, run `plan` or `register`. Under `interface`: `## Type` must already read `software`, if it reads `website` abort per the `interface alias` section above rather than proceeding.
3. SOUL.md and MASK.md must exist and be non-empty, non-placeholder (no `[TODO]` markers, each over ~200 characters), same bar as impeccable's Product gate. Missing or placeholder: abort, run `plan`.
4. `workflow.js` must exist in the project folder. Missing: abort, run `plan` (or `register`) to generate it.
5. **Git repository present.** Check with `git rev-parse --is-inside-work-tree` in the project folder. If it fails, abort with the fix: `git init` in the project folder, then re-run. The build writes across many files in several agent passes, and without version control there is no way to see what a pass changed or to undo a bad one. This gate also covers the case where a workflow's assembly step is switched to `isolation: 'worktree'`, which cannot work outside a git repository at all. `plan` and `register` create the repository, so a project scaffolded by either of them passes this gate already; a project that predates that step needs the one-line fix.

## Procedure

1. Run all Preconditions above, in order. Any failed gate stops the command with the named fix, no silent skip.
2. Resolve type from ARMOURY.md's `## Type` (`interface` already aborted above if this is not `software`). Load the matching `reference/website.md` or `reference/software.md`. Resolve the stage: `full` for a bare `build`/`interface` call, `copy` for `build copy`, `assets` for `build assets`.
3. Full builds: read `workflow.js` and render its stages as a Mermaid flowchart (Artifacts render Mermaid natively, do not load a charting library). Publish it as an Artifact. Partial builds (`copy`/`assets`): skip this and steps 4-5 per the "Partial builds" section above, unless there's a specific change worth flagging first.
4. Read the Artifact's comments (`Artifact action: "comments"`). For each one that changes a tool, library, skill, or workflow stage: update `workflow.js` and, if it's a standing tool/library choice, `ARMOURY.md`'s `## Project overrides`.
5. Re-render the flowchart with the changes applied and republish to the same Artifact URL. Repeat steps 4-5 until there are no unaddressed comments left.
6. Once the flowchart has been shown with no pending comments (or the partial-build skip applies), start `workflow.js` via the Workflow tool, passing `args` as `{ stage: "full" | "copy" | "assets" }` per step 2's resolved stage (default `"full"`). The workflow itself enforces, in this fixed order for a full build:
   1. Content before layout: real copy and real data for every section/state before any visual generation starts, no lorem-ipsum-adjacent placeholders.
   2. Reference pull: relevant entries from `library/muster/<slug>.md` and `library/eigene/<slug>.md` (sync path) matched by tag and register, loaded before generation starts, generation without checking loot first is a failure of this stage. The pull reads `library/_index.md` first and opens only the entries it names, rather than scanning the whole library; `eigene/` is reserved and currently empty by design (see [commands/loot.md](loot.md)), so zero matches there is expected, not a fault.
   3. Variant generation and selection: multiple divergent options generated and presented, not a single first draft accepted as final.
   4. Assembly writes disjoint files. Each build agent owns only its own section's or component's files and is forbidden from editing shared ones (global stylesheet, tokens, layout, route table, manifest); shared changes are reported and applied by the integration step. That is why assembly runs sequentially without a git worktree. If a project genuinely needs two agents writing the same file, switch that assembly step to `parallel(...)` with `isolation: 'worktree'`, which the git gate in Preconditions 5 already guarantees is possible.
   5. Independent critique loop: within this phase, `workflow.js` runs the five isolated role agents from [commands/critics.md](critics.md)'s roster, plus two wired-in stages named `Impeccable critique` and `Impeccable audit` that call impeccable's own `critique.md` (the two-assessment design review: AI-slop/heuristics-scoring/cognitive-load) and `audit.md` (the five-dimension technical scan: accessibility, performance, theming, and the remaining dimensions it defines) directly against the rendered result. Every finding from all of these, merged and classified exactly as `critics.md` step 7 describes, feeds back into the same fix-and-recheck stage until resolved or explicitly deferred at the cap.

      **How the cap counts, and what "deferred" means concretely.** The cap counts *fix* rounds, not review rounds, so a fix is always followed by another review: the loop reviews, fixes only while a fix round remains, then reviews again. The last fix therefore never ships unchecked. Whatever the final review still classifies as `Necessary` is returned in the workflow result under `critique_open_necessary`, and also appears in `critique_deferred` carrying a `deferred_reason`. `critique_clean` says whether the run ended with nothing necessary open. Report those findings to the user in step 9 as open work; a build that ends with `critique_clean: false` is finished, not clean, and saying otherwise is the failure this wiring exists to prevent.

   6. Performance and reduced-motion gate: [reference/performance.md](../reference/performance.md)'s four checks, run against the actual rendered output, not assumed from the code.
7. On completion, update `projects.json`: status, `updated` date.
9. Report what was built, what the critique loop found and fixed, **which necessary findings are still open** (`critique_open_necessary` from the workflow result, never silently omitted), and the performance gate result.

## Output

Built project surface (code + assets in the project's own stack), an updated `workflow.js` if comments changed it, updated `ARMOURY.md` overrides if applicable, updated `projects.json` record.

## Abort conditions

- Any Preconditions gate fails, including `interface` invoked on a project whose `## Type` is `website`, and including the project not being a git repository (fix: `git init`).
- Flowchart shown but unaddressed comments remain, never start the workflow with open comments pending.
- Performance gate fails and cannot be fixed within the run, report it as an unresolved blocker rather than shipping past it.

## References

[reference/website.md](../reference/website.md), [reference/software.md](../reference/software.md), [reference/performance.md](../reference/performance.md), [reference/assets.md](../reference/assets.md), [workflows/website.js](../workflows/website.js), [workflows/software.js](../workflows/software.js), [commands/critics.md](critics.md).

## Lehren aus dem learn.-Bau (2026-09-18)

- **Pfade nie hart im Workflow.** `PROJECT_PATH`, `SKILL_PATH`, `LIBRARY_PATH` per `args` überschreibbar machen, sonst läuft das Skript nur auf der Maschine, auf der `plan` lief.
- **Zwischenstände als Dateien übergeben.** Ein `resumeFromRunId` funktioniert nur in derselben Sitzung, und ein Resume nach Skriptänderung traf den Cache nicht und startete die ganze Inhaltsmatrix (108 Agenten) neu. Fertige Phasen als `content/inhalte.json` und `content/auswahl.json` ins Projekt schreiben und per `args` (`content_from_file`, `selections_from_file`) überspringen.
- **Die Inhaltsphase ist der Kostentreiber**: 9 Komponenten mal 6 Zustände mal Entwurf plus Prüfung sind 108 Sonnet-Agenten, die je 10 bis 15 Runden über SOUL, MASK und die Referenzen drehen. Für Mockups reicht ein Agent je Komponente, der alle Zustände auf einmal schreibt.
- Ein Bau-Agent, der `null` liefert, wird einmal wiederholt, danach meldet die Integration die Lücke.

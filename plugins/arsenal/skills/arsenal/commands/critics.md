# critics

## Purpose

Six independent review agents inspect the same surface without seeing each other's context or output, cast differently by project type. The main model merges the six reports afterward: dedupes, resolves contradictions, and sorts every finding into Necessary, Recommended, or Taste. On confirmation, `critics` implements the fixes itself rather than just handing back a list.

This is arsenal's strongest command precisely because the isolation is real: agents that see each other's output anchor on it, independent passes catch what one pass, however thorough, misses.

`critics` running standalone is this six-agent roster only. Inside `build`'s workflow, the same Critique loop phase additionally runs two wired-in stages named `Impeccable critique` and `Impeccable audit` (impeccable's own `critique.md` two-assessment design review and `audit.md` five-dimension technical scan) against the rendered result, see [commands/build.md](build.md) step 6.5. Those two stages are part of `build`'s pipeline, not of a standalone `critics` invocation.

## Arguments

`critics [project-path]` or `critics --file <path>` (single file mode, see below).

## Preconditions (gates)

1. Load `behavior.md`. Missing: abort, run `behavior`.
2. Load `ARMOURY.md`, read `## Type`. Missing: abort, run `plan` or `register`.
3. The project must be inspectable: a running dev server, a built preview, or a live URL. Nothing renderable to inspect: abort, tell the user what's missing (start the dev server, or run `build` first).

In single file mode (`critics --file <path>`), gate 2 does not apply: see "Single file mode" below.

## Procedure

1. Run all Preconditions gates.
2. Resolve type from ARMOURY.md, load the matching [reference/website.md](../reference/website.md) or [reference/software.md](../reference/software.md).
3. Determine the target surface(s): which routes/pages/viewports/states get inspected.
4. Launch all six agents **in a single message with six separate Agent tool calls**, never as forks (forks share context, defeating the isolation), never sequentially into the same conversation. Each agent gets the target surface and its role brief, nothing else, and does not see the others' output.
5. **Role casting**, common across both types:
   1. Design critique: hierarchy, taste, the AI-slop test, absolute-ban compliance, drawing on impeccable's `critique` lens.
   2. Deterministic pattern/anti-pattern detector: structural anti-patterns per the type's anti-pattern table, plus a category-reflex check, drawing on impeccable's automated critique tooling. The category-reflex check asks whether the palette or visual theme is guessable from the project's category alone (observability tools default to dark blue, healthcare to white and teal, finance to navy and gold, crypto to neon on black): a guessable result flags a training-data reflex rather than a deliberate choice, and gets a concrete fix (a specific alternative palette move) exactly like any other finding.
   3. Technical audit: accessibility and performance, measurable not impressionistic, drawing on impeccable's `audit` lens. Includes a fixed Vorgabentreue (spec-adherence) pass: walk every requirement in the brief individually rather than impressionistically, search for mockup/dummy behavior standing in for the real thing (fake states, hardcoded values, non-functional controls), and back every finding with a measured fundstelle, not an impression.
   4. Persona walkthrough: 2-3 personas relevant to this surface (impeccable's `personas.md` archetypes, or real project audience data from SOUL.md if it exists), concrete element-level red flags, not generic persona description.
   5. **Type-specific fifth agent.** Website: legal/compliance essentials (imprint, privacy notice, cookie consent where applicable) plus conversion and trust basics. Software: keyboard operability, data density, error states, empty states, instead of the legal checks.
   6. **Motion and interaction**, common across both types: motion-doctrine compliance (curves, durations, the overshoot exception) per [reference/motion-doctrine.md](../reference/motion-doctrine.md) and [reference/product-motion.md](../reference/product-motion.md); touch behavior under `hover: none` and `pointer: coarse`; keyboard operability of anything hover- or pointer-driven; `prefers-reduced-motion` behavior. Every timing and reduced-motion finding is measured against a rest run (idle baseline) per [reference/product-motion.md](../reference/product-motion.md), not asserted from reading the code.
6. Each agent's report is a list of findings, each with four mandatory fields: **Schwere** (severity), **Fundstelle** (file:line, or URL/route plus element and screenshot for a rendered surface), **Befund** (what's wrong), **Korrektur** (the concrete fix). A finding missing any of the four is not usable and gets dropped at merge time rather than passed through.
7. **Merge**, main model only: collect all six reports, dedupe overlapping findings (note where multiple agents independently flagged the same thing, that's a stronger signal), resolve contradictions by judgment, classify each surviving finding as **Necessary** (breaks something, fails a gate, violates an absolute ban), **Recommended** (real improvement, not a hard failure), or **Taste** (a defensible alternative, not a defect).

   When the assignment runs on the task scale (schwer/mittel/klein) instead of the project scale, the two map directly: **schwer = Necessary**, **mittel = Recommended**, **klein = Taste**. Use whichever scale the requesting brief is already stated in; don't translate a task-scale brief into Necessary/Recommended/Taste and back.
8. Present the merged, classified list to the user.
9. On confirmation, implement the requested fixes directly. When the user rejects or corrects a suggestion mid-implementation, ask once "save as a standing rule?", per [commands/behavior.md](behavior.md)'s automatic-entry mechanism, and record it if confirmed.
10. Update `projects.json`: `last_critics` date and a short summary (counts per Necessary/Recommended/Taste). Single file mode has no `projects.json` entry to update, skip this step.

## Single file mode

For a single rendered artifact (a standalone mockup HTML file) that has no `ARMOURY.md` and no `projects.json` entry, run `critics --file <path>` instead of `critics [project-path]`.

- Gate 2 (`ARMOURY.md`) does not apply. Gates 1 and 3 still apply unchanged.
- Register and dials are not read from `ARMOURY.md`; take them from a short task text supplied with the call (the register: brand or product, and any dial the brief states or implies). Missing dials are not a reason to abort, unlike the project-bound gate; note the assumed dial in the merged report instead.
- Step 2's type resolution still applies, taken from the task text (website or software) rather than from `ARMOURY.md`.
- Steps 4 through 9 run unchanged: same six-agent cast, same isolation, same merge and classification.
- Step 10 (the `projects.json` update) is skipped, there is no project record to write to.

## Output

Merged, classified finding list; implemented fixes where confirmed; updated `projects.json` record (skipped in single file mode); possible new `behavior.md` entries.

## Abort conditions

- Any Preconditions gate fails (gate 2 excepted in single file mode).
- Nothing renderable to inspect.
- Agents not actually isolated (shared context, sequential visibility) invalidates the run, redo it properly rather than merging a compromised set.

## References

[reference/website.md](../reference/website.md), [reference/software.md](../reference/software.md), impeccable's `critique.md`, `audit.md`, `personas.md`, `heuristics-scoring.md` (unchanged, referenced only).

## Parallelitätsgrenze des Projekts (2026-09-26)

Schreibt ein Projekt eine Obergrenze gleichzeitiger Agenten vor (z. B. "höchstens zwei"), gilt sie vor Schritt 4. Die Isolation bleibt gewahrt, wenn die Rollen in Paaren nacheinander laufen, jede mit eigenem Browser-Tab (`new_page` mit `isolatedContext` = Rollenname) und ohne Sicht auf die anderen Berichte. So im Paulis-Churros-Lauf: 8 Prüfer in 4 Paaren.

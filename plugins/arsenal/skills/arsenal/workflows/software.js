// Workflow template for building a software/application UI surface (register: product by default).
// `plan` copies this file into the project folder as `workflow.js` and fills every `__TOKEN__`
// placeholder below with a literal value before `build` (or its `interface` alias) invokes it via
// the Workflow tool.
//
// PLACEHOLDER CONVENTION: every placeholder is a bare `__TOKEN__` sentinel (no quotes around it in
// this template). `plan` replaces the token with a complete JS literal, quotes included where the
// value is a string. An unfilled placeholder for an array/number/string const below is a
// ReferenceError the moment the workflow runs (the token is not a declared identifier), that is
// intentional: it is louder than a silently wrong default.
//
// Placeholders `plan` must fill (see plan.md step 10, "pointed at this project's SOUL/MASK/ARMOURY"):
//   __PROJECT_NAME__     -> quoted string, the project's display name (SOUL.md / ARMOURY.md)
//   __PROJECT_PATH__     -> quoted absolute path to the folder holding SOUL.md, MASK.md, ARMOURY.md
//   __SKILL_PATH__       -> quoted absolute path to this arsenal skill folder (for reference/* lookups)
//   __LIBRARY_PATH__     -> quoted absolute path to the sync library folder (loot entries, per
//                           SKILL.md's cross-platform sync path table, resolve for the current platform)
//   __REGISTER__         -> quoted string, "brand" or "product", from SOUL.md's ## Register (usually
//                           "product" on this path, but a brand-adjacent onboarding splash can flip it)
//   __AUDIENCE__         -> quoted short audience description, from SOUL.md's ## Users
//   __COMPONENTS__       -> array of component/screen name strings in scope, from plan's round 2
//                           primary-action interview, e.g. ["dashboard", "settings", "record-editor"]
//   __STATES__           -> array of state name strings that matter, from plan's round 2 states
//                           question, e.g. ["standard", "empty", "loading", "error", "edge-case"]
//   __PRIMARY_ACTION__   -> quoted string, the tool's single primary action
//   __EXISTING_SYSTEM__  -> quoted string describing the design system/conventions to inherit
//                           (component library, token source), or the bare literal null if there is none
//   __TECHNIQUES__       -> array of technique file slugs, normally [] on this path (decorative
//                           technique is not licensed by default here), non-empty only for an
//                           explicitly brand-adjacent surface (in-app onboarding splash, upsell page)
//   __LOOT_TAGS__        -> array of tag strings to match library/muster/<slug>.md and
//                           library/eigene/<slug>.md entries against
//   __VARIANT_COUNT__    -> bare number, how many divergent structural/interaction variants to
//                           generate per component (2 is a reasonable default on this path, lower
//                           than the website path's default because the direction is more
//                           constrained by an existing system and by usability rules)

export const meta = {
  name: 'arsenal-build-software',
  description: 'Build an application UI surface: content first, loot grounding, variant selection, independent critique, performance gate',
  phases: [
    { title: 'Content', detail: 'real microcopy and sample data per component and state, before any layout work' },
    { title: 'Loot grounding', detail: 'pull matching confirmed references from the library before anything gets generated' },
    { title: 'Variant generation and selection', detail: 'multiple divergent structural/interaction directions per component, judged and synthesized' },
    { title: 'Assembly', detail: 'build the selected variant into the real project stack and produce a previewable app' },
    { title: 'Critique loop', detail: 'five isolated critics-style agents plus the mandatory Impeccable critique and Impeccable audit gates, merged and classified, fixed until clean or deferred' },
    { title: 'Performance gate', detail: 'the four performance.md checks against the actual rendered output' },
  ],
}

// ---- Project-specific constants, filled by plan ----
const PROJECT_NAME = __PROJECT_NAME__
const PROJECT_PATH = __PROJECT_PATH__
const SKILL_PATH = __SKILL_PATH__
const LIBRARY_PATH = __LIBRARY_PATH__
const REGISTER = __REGISTER__
const AUDIENCE = __AUDIENCE__
const COMPONENTS = __COMPONENTS__
const STATES = __STATES__
const PRIMARY_ACTION = __PRIMARY_ACTION__
const EXISTING_SYSTEM = __EXISTING_SYSTEM__
const TECHNIQUES = __TECHNIQUES__
const LOOT_TAGS = __LOOT_TAGS__
const VARIANT_COUNT = __VARIANT_COUNT__

// Partial-build support for `build copy` / `build assets` (see commands/build.md). The build
// command passes `args` as an object `{ stage: "full" | "copy" | "assets" }`, default "full".
// A missing `.stage` field falls back to "full"; an unrecognized value aborts below instead of
// silently running the full pipeline.
const VALID_STAGES = ['full', 'copy', 'assets']
const STAGE = (args && typeof args === 'object' && 'stage' in args) ? args.stage : 'full'
if (!VALID_STAGES.includes(STAGE)) {
  throw new Error(`Unknown build stage "${STAGE}" (from args.stage), expected one of ${VALID_STAGES.join(', ')}`)
}

// Existing-system constraint narrows variant scope (recherche-workflow.md software table, stage 3)
// but never removes the mechanism entirely: mechanism 3 (variant generation and selection) is
// hardwired for both project types, "a single first draft accepted as final" is never allowed here.
// Under an existing design system the variant count is pinned to this fixed number rather than
// derived from VARIANT_COUNT: the mechanism stays mandatory, but the scope to vary is genuinely
// narrower, so two divergent directions are enough and more would only produce near-duplicates.
// Two is also the floor, which is why this is a constant and not a clamp of VARIANT_COUNT.
const CONSTRAINED_VARIANT_COUNT = 2
const EFFECTIVE_VARIANT_COUNT = EXISTING_SYSTEM ? CONSTRAINED_VARIANT_COUNT : VARIANT_COUNT

const MAX_CRITIQUE_ROUNDS = 2
const MAX_PERF_ROUNDS = 2

// Cross product of components and states, the real unit of content work: every state of every
// component needs its own real copy, per software.md rule 1 (status always visible) and rule 13
// (empty vs blank-slate get different tone).
const WORK_ITEMS = COMPONENTS.flatMap((component) => STATES.map((state) => ({ component, state })))

// ---- Schemas ----
const CONTENT_SCHEMA = {
  type: 'object',
  properties: {
    component: { type: 'string' },
    state: { type: 'string' },
    copy: { type: 'string' },
    sample_data: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['component', 'state', 'copy'],
}

const ASSET_SCHEMA = {
  type: 'object',
  properties: {
    component: { type: 'string' },
    assets: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          description: { type: 'string' },
          source: { type: 'string' },
          license: { type: 'string' },
        },
        required: ['description', 'source'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['component', 'assets'],
}

const LOOT_SCHEMA = {
  type: 'object',
  properties: {
    matches: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          slug: { type: 'string' },
          summary: { type: 'string' },
          applies_to: { type: 'string' },
        },
        required: ['slug', 'summary'],
      },
    },
  },
  required: ['matches'],
}

const VARIANT_SCHEMA = {
  type: 'object',
  properties: {
    variant_id: { type: 'string' },
    description: { type: 'string' },
    approach_notes: { type: 'string' },
  },
  required: ['variant_id', 'description'],
}

const JUDGE_SCHEMA = {
  type: 'object',
  properties: {
    variant_id: { type: 'string' },
    score: { type: 'number' },
    strengths: { type: 'string' },
    weaknesses: { type: 'string' },
  },
  required: ['variant_id', 'score'],
}

const SELECTION_SCHEMA = {
  type: 'object',
  properties: {
    component: { type: 'string' },
    chosen_variant_id: { type: 'string' },
    rationale: { type: 'string' },
    grafted_ideas: { type: 'string' },
  },
  required: ['component', 'chosen_variant_id', 'rationale'],
}

const BUILD_SCHEMA = {
  type: 'object',
  properties: {
    component: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['component', 'files'],
}

const INTEGRATE_SCHEMA = {
  type: 'object',
  properties: {
    preview_method: { type: 'string' },
    preview_location: { type: 'string' },
    files_touched: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['preview_method', 'preview_location'],
}

const FINDING_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          location: { type: 'string' },
          issue: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['location', 'issue', 'fix'],
      },
    },
  },
  required: ['findings'],
}

const MERGE_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          location: { type: 'string' },
          issue: { type: 'string' },
          fix: { type: 'string' },
          classification: { type: 'string' },
          agreement_count: { type: 'number' },
        },
        required: ['location', 'issue', 'fix', 'classification'],
      },
    },
  },
  required: ['findings'],
}

const PERF_SCHEMA = {
  type: 'object',
  properties: {
    reduced_motion_ok: { type: 'boolean' },
    mobile_fallback_ok: { type: 'boolean' },
    lazy_mount_cleanup_ok: { type: 'boolean' },
    contrast_ok: { type: 'boolean' },
    lighthouse_mobile_score: { type: 'number' },
    issues: { type: 'array', items: { type: 'string' } },
  },
  required: ['reduced_motion_ok', 'mobile_fallback_ok', 'lazy_mount_cleanup_ok', 'contrast_ok', 'issues'],
}

// ---- Prompt builders ----
function contextLine() {
  return `Project "${PROJECT_NAME}" at ${PROJECT_PATH}, register ${REGISTER}, audience ${AUDIENCE}, primary action "${PRIMARY_ACTION}". Read SOUL.md and MASK.md in that folder first, they hold the confirmed brief and design tokens.${EXISTING_SYSTEM ? ` Existing design system to inherit: ${EXISTING_SYSTEM}.` : ''}`
}

function writeContentPrompt(item) {
  return `${contextLine()} Write real, final-form copy and sample data for the "${item.component}" component in its "${item.state}" state. Read ${SKILL_PATH}/reference/software.md rules 1, 2, 12, 13 before writing: interface language is the user's own vocabulary, not system/database jargon; error copy is human language next to the field, states the problem, offers a fix, never blames the user; empty states get a short explanation plus a direct next action; empty (task done) and blank slate (never used) get different tone. No lorem ipsum, no placeholder data. Return the component, state, copy and representative sample data.`
}

function auditContentPrompt(draft, item) {
  return `${contextLine()} Component "${item.component}", state "${item.state}", has a first-draft copy: ${JSON.stringify(draft)}. Check it against reference/software.md rules 1, 2, 12, 13 and the copywriting jargon rule. Fix anything that reads as internal/system language, blames the user, or leaves an empty state as a bare blank container. Return the revised, final copy and sample data.`
}

function sourceAssetPrompt(component) {
  return `${contextLine()} Source any icons or imagery needed for the "${component}" component per reference/assets.md, restrained and functional per reference/software.md's anti-pattern table (no oversized rounded icon above every heading, no decoration that outranks the data). Return the assets found with description, source and license for each.`
}

function lootPrompt() {
  return `Find loot entries in ${LIBRARY_PATH} (library/muster/<slug>.md and library/eigene/<slug>.md files) tagged with any of [${LOOT_TAGS.join(', ')}] or matching register "${REGISTER}". Read ${LIBRARY_PATH}/library/_index.md FIRST: it lists every entry with its slug, tags and one-line summary, so pick the candidates from that index and open only those files, do not read the whole library. If _index.md is missing, OR it exists but its table carries no data rows (header only, which reads the same as a missing index: there is nothing there to pick candidates from), fall back to scanning the muster/ and eigene/ folders directly for candidate files. In that fallback case, once you have the confirmed matches, also append a row per found file to library/_index.md (slug, branch, category, tags, one clause on what it holds, source, date, in the format loot.md defines) so the index catches up with what is actually on disk instead of staying empty. Skip any file whose name starts with an underscore (for example _FORMAT.md and _index.md itself), those are format and index documentation, not captured references, and must never be treated as a match even if their content looks plausible. Read each remaining candidate file. A match from eigene/ is a reusable building block with working code to use directly. A match from muster/ is a reference to learn from only, never copy its code or its assets. Return the confirmed matches with a short summary of what to ground on (the specific transferable thing the user confirmed, not a generic description) and which branch each match came from. Finding zero matches is a valid, expected state on a fresh library, return an empty list and say so plainly, never invent a match to fill the gap.`
}

function variantPrompt(component, index, componentContent, lootMatches, techniques, existingSystem) {
  const lootNote = lootMatches && lootMatches.length
    ? `Ground this in these confirmed references: ${JSON.stringify(lootMatches)}.`
    : 'No loot references matched this project, work from MASK.md tokens, the existing system and the brief alone, do not invent a reference.'
  const systemNote = existingSystem
    ? `This project inherits an existing design system (${existingSystem}), stay within its tokens and components, vary structure and interaction, not the visual identity.`
    : 'No existing system to inherit, tokens come from MASK.md.'
  const techniqueNote = techniques && techniques.length
    ? `This surface is explicitly brand-adjacent, techniques licensed for it: ${techniques.join(', ')} (see the matching files under ${SKILL_PATH}/reference/).`
    : 'Decorative shader/3D/ambient motion is not licensed on this path by default, keep this variant to structure, density, and interaction.'
  return `${contextLine()} Propose ONE divergent structural/interaction direction (variant ${index + 1}) for the "${component}" component, built on this confirmed content across its states: ${JSON.stringify(componentContent)}. ${lootNote} ${systemNote} ${techniqueNote} Vary something real: navigation pattern, table/list density, disclosure depth, chart type, KPI tile layout, not a color swap of the same structure. Check the variant against reference/software.md's rule set (status visibility, progressive disclosure, keyboard operability, dashboard one-screen-fit where relevant) and its anti-pattern table. Return a variant id and a concrete description of the direction.`
}

function judgeVariantPrompt(variant, component) {
  return `Score this proposed variant for the "${component}" component of "${PROJECT_NAME}" against reference/software.md's rule set and anti-pattern table: ${JSON.stringify(variant)}. Score 0-10. Return the variant id, score, strengths and weaknesses.`
}

function selectPrompt(component, variants, judged) {
  return `Component "${component}" of "${PROJECT_NAME}" has these variants: ${JSON.stringify(variants)}, judged as: ${JSON.stringify(judged)}. Choose the strongest overall, but graft in any specific strong idea a runner-up variant had that the winner lacks. Return the component name, the chosen variant id, the rationale, and any grafted ideas.`
}

function buildPrompt(selection) {
  return `${contextLine()} Build the selected variant for component "${selection.component}" into the project's real stack (read ARMOURY.md's ## Tools and ## Libraries first for the stack and conventions). Selection: ${JSON.stringify(selection)}. Implement every state that was scoped for this component (${STATES.join(', ')}) with real semantic code, not a mock: visible status feedback, full keyboard reachability, undo/cancel on any destructive action, documented shortcuts if the tool is keyboard-centric. EXCLUSIVE PATHS, this is a hard constraint: write only files that belong to this one component (its own component file, its own stylesheet or style block, its own tests). Never edit a shared file (global stylesheet, token file, app shell, route table, store, package manifest); if this component needs a change there, describe the needed change in the summary instead of making it, the integration step owns those files. Return the component name, the files touched, and a short summary.`
}

function integratePrompt(builtComponents) {
  return `${contextLine()} These components were built independently: ${JSON.stringify(builtComponents)}. Assemble them into one coherent app in the project's real stack, wiring navigation between [${COMPONENTS.join(', ')}] per reference/software.md rule 14 (visible current-position indicator, hierarchy depth capped at two levels). Make sure the result is actually previewable (start whatever dev server or build step ARMOURY.md's tools imply). Return how to preview it (method and location/URL), the full list of files touched, and any integration notes.`
}

// Critique roles, isolated from each other, mirroring commands/critics.md's software roster: the
// first four roles match the website path, the fifth swaps legal/trust for keyboard, density,
// error and empty-state review per software.md's check criteria. Two more, named exactly
// "Impeccable critique" and "Impeccable audit", are hardwired here as mandatory gates per
// HANDOFF.md ("impeccable critique und audit Pflichtstufen"), each running one of impeccable's
// own commands against the rendered result. All seven feed the same FINDING_SCHEMA and the same
// merge step below, none is skippable.
const CRITIQUE_ROLES = [
  {
    name: 'design-critique',
    model: undefined, // judgment, inherits the main-loop model
    prompt: (integrated) => `Inspect "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) as a design critic: hierarchy, taste, the AI-slop test, absolute-ban compliance per reference/software.md and impeccable's absolute bans. You do not see any other reviewer's output, work from the rendered result alone. Every finding needs a location (screen/component/element) and a concrete fix.`,
  },
  {
    name: 'pattern-detector',
    model: 'haiku', // mechanical checklist matching, no independent judgment required
    prompt: (integrated) => `Inspect "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) against reference/software.md's anti-pattern table, entry by entry, as a deterministic detector: bare KPI numbers, uniform card-in-card treatment, reflexive sidebar for a flat app, mid-keystroke validation, and the rest of the table. Flag every literal match. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'technical-audit',
    model: 'sonnet',
    prompt: (integrated) => `Run a measurable technical audit of "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}): accessibility (contrast, focus rings, semantic structure) and performance basics. Use available browser/devtools tools, do not estimate from reading code alone. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'persona-walkthrough',
    model: undefined, // judgment, inherits the main-loop model
    prompt: (integrated) => `Walk through "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) as 2-3 personas relevant to a ${REGISTER} tool for audience "${AUDIENCE}" performing "${PRIMARY_ACTION}" (impeccable's personas.md archetypes, or real audience data from SOUL.md). Report concrete, element-level red flags per persona, never a generic persona description. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'keyboard-density-states',
    model: 'sonnet',
    prompt: (integrated) => `Review "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) against reference/software.md's check criteria: complete every core flow with the mouse disconnected (Tab/Enter/Escape only, no unreachable control), check table/list density against the target usage pattern, review every form and destructive action for error message clarity and input preservation, and review every emptiable view for explanation text and a working next action. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'Impeccable critique',
    model: undefined, // judgment, inherits the main-loop model
    prompt: (integrated) => `Run impeccable's "critique" command against "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}), following ${SKILL_PATH}/../impeccable/reference/critique.md exactly: the two independent assessments it prescribes (LLM design review including AI-slop detection against every DON'T guideline, cognitive load checklist, emotional journey, Nielsen's heuristics scoring; and the automated detector scan), then its own merge of the two. This is a mandatory gate, not optional and not a duplicate of the design-critique role above, run it in full even if other roles already found overlapping issues. You do not see any other reviewer's output, work from the rendered result alone. Every finding needs a location (screen/component/element) and a concrete fix.`,
  },
  {
    name: 'Impeccable audit',
    model: 'sonnet',
    prompt: (integrated) => `Run impeccable's "audit" command against "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}), following ${SKILL_PATH}/../impeccable/reference/audit.md exactly: score accessibility, performance, theming, responsive design and anti-patterns 0-4 each per that file's criteria, and report every dimension that scores below 4. This is a mandatory gate, not optional and not a duplicate of the technical-audit role above, run it in full even if other roles already found overlapping issues. Every finding needs a location and a concrete fix.`,
  },
]

function mergePrompt(reports) {
  return `Seven independent critique reports on "${PROJECT_NAME}" came back, each written without seeing the others (five critics-style roles plus the mandatory Impeccable critique and Impeccable audit gates): ${JSON.stringify(reports)}. Dedupe overlapping findings (note when multiple agents independently flagged the same thing, that is a stronger signal, raise agreement_count accordingly), resolve contradictions by judgment, and classify every surviving finding as "Necessary" (breaks something, fails a gate, violates an absolute ban), "Recommended" (real improvement, not a hard failure), or "Taste" (a defensible alternative, not a defect). Return the merged, classified list.`
}

function fixPrompt(finding) {
  return `${contextLine()} Implement this fix directly in the project files: ${JSON.stringify(finding)}. Make the minimal change that resolves it without introducing a new anti-pattern from reference/software.md.`
}

// A file path mentioned inside a finding's own text, used as the grouping fallback below: a
// word-ish token ending in a short extension, e.g. "src/components/Table.tsx" or "app/page.tsx:42".
const FILE_PATH_RE = /\b[\w][\w./-]*\.[a-zA-Z0-9]{1,6}\b/

// Groups findings by the single file each is really about, so the fix round below can assign one
// agent per file instead of one agent per finding. Two findings that land on the same file and
// get fixed by two different agents in parallel is a real, observed failure mode: whichever agent
// writes last silently discards the other's fix. Grouping by file and running one sequential agent
// per group removes the collision while keeping groups (disjoint files) parallel to each other.
// Prefers an explicit field on the finding (future-proofing: the schema carries none today), falls
// back to the first file-shaped token in the finding's own text, and falls back to a shared "misc"
// bucket for findings that name no file at all.
function findingFileKey(finding) {
  const explicit = finding && (finding.file || finding.target_file || finding.path)
  if (explicit) return explicit
  const text = [finding && finding.location, finding && finding.issue, finding && finding.fix].filter(Boolean).join(' ')
  const match = text.match(FILE_PATH_RE)
  return match ? match[0] : 'misc'
}

function groupFindingsByFile(findings) {
  const groups = new Map()
  for (const f of findings) {
    const key = findingFileKey(f)
    if (!groups.has(key)) groups.set(key, [])
    groups.get(key).push(f)
  }
  return groups
}

// One prompt per file group: the agent works its group's findings sequentially and is held, as a
// hard instruction, to that single file, so a finding whose real fix needs another file gets
// skipped and reported rather than silently spilling into a file another group owns.
function groupFixPrompt(file, findings) {
  const scope = file === 'misc'
    ? 'These findings name no specific file. Use judgment on where each belongs, and still make only the minimal change each one calls for.'
    : `Every one of these findings belongs to ${file}. Touch ONLY ${file}: do not edit any other file, even if a finding's fix would be easier elsewhere. If a finding genuinely cannot be resolved without touching another file, skip it and say so instead of editing outside ${file}.`
  return `${contextLine()} Implement these fixes directly in the project files, one at a time, in the order given: ${JSON.stringify(findings)}. ${scope} Make the minimal change that resolves each finding without introducing a new anti-pattern from reference/software.md.`
}

function perfCheckPrompt(integrated) {
  return `Check "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) against ${SKILL_PATH}/reference/performance.md's four checks: prefers-reduced-motion fallback (toggle it, reload, confirm a complete non-broken design), mobile/low-power fallback where relevant, lazy mount and cleanup for any canvas/animation, and contrast/focus surviving any animation, including a visible focus ring on every interactive element at the density level actually used. Use available browser/devtools tools including a Lighthouse mobile run if available. Return each check's pass/fail and a lighthouse_mobile_score if you ran one, plus a plain-language issues list for anything that failed.`
}

function perfFixPrompt(perfResult) {
  return `${contextLine()} The performance gate found these issues: ${JSON.stringify(perfResult.issues)}. Fix them per ${SKILL_PATH}/reference/performance.md's guidance (reduced-motion CSS and JS branch, DPR cap, breakpoint fallback, IntersectionObserver pause, explicit dispose/cleanup, contrast-safe focus rings). Do not remove the effect to dodge the check unless reference/performance.md explicitly allows omitting it.`
}

// ---- Pipeline stages ----
function writeContentStage(_prev, item) {
  return agent(writeContentPrompt(item), { phase: 'Content', schema: CONTENT_SCHEMA, model: 'sonnet' })
}

function auditContentStage(draft, item) {
  return agent(auditContentPrompt(draft, item), { phase: 'Content', schema: CONTENT_SCHEMA, model: 'sonnet' })
}

function sourceAssetStage(_prev, component) {
  return agent(sourceAssetPrompt(component), { phase: 'Content', schema: ASSET_SCHEMA, model: 'sonnet' })
}

async function generateVariantsStage(_prev, component) {
  return (await parallel(
    Array.from({ length: EFFECTIVE_VARIANT_COUNT }, (_v, i) => () => agent(
      variantPrompt(component, i, contentForComponent(cachedContent, component), cachedLoot, TECHNIQUES, EXISTING_SYSTEM),
      { phase: 'Variant generation and selection', schema: VARIANT_SCHEMA, model: 'sonnet' },
    )),
  )).filter(Boolean)
}

async function selectVariantStage(variants, component) {
  const judged = (await parallel(variants.map((v) => () => agent(
    judgeVariantPrompt(v, component),
    { phase: 'Variant generation and selection', schema: JUDGE_SCHEMA },
  )))).filter(Boolean)
  return agent(selectPrompt(component, variants, judged), { phase: 'Variant generation and selection', schema: SELECTION_SCHEMA })
}

function contentForComponent(content, component) {
  return (content || []).filter((c) => c && c.component === component)
}

// ---- Run ----
log(`arsenal software build, stage "${STAGE}", ${COMPONENTS.length} component(s) x ${STATES.length} state(s), ${EFFECTIVE_VARIANT_COUNT} variant(s) per component${EXISTING_SYSTEM ? ' (narrowed: existing system to inherit)' : ''}`)

// Stage "assets": partial build, source icons/imagery only, no copy pass. `build assets` uses this.
if (STAGE === 'assets') {
  phase('Content')
  const assets = await pipeline(COMPONENTS, sourceAssetStage)
  return { stage: 'assets', project: PROJECT_NAME, assets }
}

// Mechanism 1, content before layout: real microcopy and sample data for every component/state
// pair before any visual generation.
phase('Content')
const cachedContent = await pipeline(WORK_ITEMS, writeContentStage, auditContentStage)

// Stage "copy": partial build, copy only. `build copy` uses this.
if (STAGE === 'copy') {
  return { stage: 'copy', project: PROJECT_NAME, content: cachedContent }
}

const assets = await pipeline(COMPONENTS, sourceAssetStage)

// Mechanism 2, reference pull: loot entries loaded before any generation starts. Not skippable
// even with an existing system, only the variant stage below narrows in that case.
phase('Loot grounding')
const lootResult = await agent(lootPrompt(), { phase: 'Loot grounding', schema: LOOT_SCHEMA, model: 'haiku' })
const cachedLoot = (lootResult && lootResult.matches) || []
if (cachedLoot.length === 0) {
  log('Loot grounding: no matching reference entries, this is a valid state ("no grounding available"), proceeding without inventing one')
} else {
  log(`Loot grounding: ${cachedLoot.length} matching reference entr${cachedLoot.length === 1 ? 'y' : 'ies'} for tags [${LOOT_TAGS.join(', ')}]`)
}

// Mechanism 3, variant generation and selection: divergent structural/interaction directions per
// component, judged and synthesized, never a single first draft accepted, even under an existing
// system (see EFFECTIVE_VARIANT_COUNT above for how that case is narrowed instead of skipped).
phase('Variant generation and selection')
const selections = (await pipeline(COMPONENTS, generateVariantsStage, selectVariantStage)).filter(Boolean)

// Assembly is the connective step the fixed order implies but does not name: variants must
// become real, renderable code before the critique loop has anything to inspect.
//
// Sequential, and deliberately WITHOUT `isolation: 'worktree'`. A worktree requires the project to
// be a git repository, which nothing in this pipeline creates: build.md now gates on one, but a
// gate that passes on a freshly initialized repo is still a thin guarantee. It is also
// unnecessary here, because buildPrompt pins every agent to its own component's files and forbids
// shared ones, so the writes are disjoint and running them one after another costs wall-clock
// time only. Switch back to `parallel(...)` with `isolation: 'worktree'` only for a project where
// two components genuinely must write the same file, and only where the project is a git repository.
phase('Assembly')
const builtComponents = []
for (const sel of selections) {
  const built = await agent(buildPrompt(sel), { phase: 'Assembly', schema: BUILD_SCHEMA, model: 'sonnet' })
  if (built) builtComponents.push(built)
}
const integrated = await agent(integratePrompt(builtComponents), { phase: 'Assembly', schema: INTEGRATE_SCHEMA, model: 'sonnet' })

// Mechanism 4, independent critique loop: five isolated agents plus the mandatory, non-skippable
// Impeccable critique and Impeccable audit gates, merged by the main model, findings fixed and
// re-checked until clean or the round cap is hit (deferred, not dropped).
// The cap counts FIX rounds, not review rounds, so every fix round is followed by a review: the
// loop reviews, and only fixes while it still has a fix round left. The last fix is therefore
// always re-checked, and whatever the final review still reports is what gets carried out of the
// phase. `latestFindings` holds that final merged report regardless of which exit was taken, so
// "deferring rather than dropping" is a fact about the return value and not just a log line.
phase('Critique loop')
let fixRounds = 0
let latestFindings = []
let openNecessary = []
for (;;) {
  const reports = (await parallel(CRITIQUE_ROLES.map((role) => () => agent(
    role.prompt(integrated),
    { phase: 'Critique loop', schema: FINDING_SCHEMA, ...(role.model ? { model: role.model } : {}) },
  )))).filter(Boolean)
  const merged = await agent(mergePrompt(reports), { phase: 'Critique loop', schema: MERGE_SCHEMA })
  latestFindings = merged.findings || []
  openNecessary = latestFindings.filter((f) => f.classification === 'Necessary')
  if (openNecessary.length === 0) break
  if (fixRounds >= MAX_CRITIQUE_ROUNDS) break
  log(`Critique fix round ${fixRounds + 1}: ${openNecessary.length} necessary finding(s), fixing`)
  // Grouped by file (see groupFindingsByFile above) rather than one agent per finding: two
  // findings on the same file running as separate parallel agents would race and one fix would
  // silently overwrite the other. One agent per group, sequential within the group, groups
  // themselves in parallel since each owns a disjoint file.
  const fileGroups = groupFindingsByFile(openNecessary)
  await parallel(Array.from(fileGroups.entries()).map(([file, findings]) => () => agent(
    groupFixPrompt(file, findings), { phase: 'Critique loop', model: 'sonnet' },
  )))
  fixRounds++
}
const deferredFindings = latestFindings
  .filter((f) => f.classification !== 'Necessary')
  .concat(openNecessary.map((f) => ({ ...f, deferred_reason: 'Necessary, still open after the last critique review at the fix-round cap' })))
if (openNecessary.length) {
  log(`Critique loop hit its fix-round cap (${MAX_CRITIQUE_ROUNDS}) with ${openNecessary.length} necessary finding(s) still open after the final review, returning them in critique_deferred rather than dropping them silently`)
}

// Mechanism 5, performance and reduced-motion gate: run against the actual rendered output. Still
// applies here even though decorative motion is not licensed by default, any transition/animation
// that does exist (loading states, panel transitions) still owes reduced-motion and focus safety.
phase('Performance gate')
let perfRound = 0
let perfResult = null
let perfPassed = false
while (perfRound < MAX_PERF_ROUNDS) {
  perfResult = await agent(perfCheckPrompt(integrated), { phase: 'Performance gate', schema: PERF_SCHEMA })
  perfPassed = !!(perfResult && perfResult.reduced_motion_ok && perfResult.mobile_fallback_ok
    && perfResult.lazy_mount_cleanup_ok && perfResult.contrast_ok)
  if (perfPassed) break
  log(`Performance gate round ${perfRound + 1} failed: ${(perfResult && perfResult.issues || []).join('; ')}`)
  await agent(perfFixPrompt(perfResult), { phase: 'Performance gate', model: 'sonnet' })
  perfRound++
}
if (!perfPassed) {
  log('Performance gate still failing after the round cap, reporting as an unresolved blocker rather than shipping past it')
}

return {
  stage: 'full',
  project: PROJECT_NAME,
  content: cachedContent,
  assets,
  loot: cachedLoot,
  selections,
  assembly: integrated,
  critique_deferred: deferredFindings,
  critique_open_necessary: openNecessary,
  critique_clean: openNecessary.length === 0,
  performance: perfResult,
  performance_gate_passed: perfPassed,
}

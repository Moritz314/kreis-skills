// Workflow template for building a marketing/brand website surface (register: brand by default).
// `plan` copies this file into the project folder as `workflow.js` and fills every `__TOKEN__`
// placeholder below with a literal value before `build` ever invokes it via the Workflow tool.
//
// PLACEHOLDER CONVENTION: every placeholder is a bare `__TOKEN__` sentinel (no quotes around it
// in this template). `plan` replaces the token with a complete JS literal, quotes included where
// the value is a string. An unfilled placeholder for an array/number/string const below is a
// ReferenceError the moment the workflow runs (the token is not a declared identifier), that is
// intentional: it is louder than a silently wrong default.
//
// Placeholders `plan` must fill (see plan.md step 10, "pointed at this project's SOUL/MASK/ARMOURY"):
//   __PROJECT_NAME__   -> quoted string, the project's display name (SOUL.md / ARMOURY.md)
//   __PROJECT_PATH__   -> quoted absolute path to the folder holding SOUL.md, MASK.md, ARMOURY.md
//   __SKILL_PATH__     -> quoted absolute path to this arsenal skill folder (for reference/* lookups)
//   __LIBRARY_PATH__   -> quoted absolute path to the sync library folder (loot entries, per SKILL.md's
//                         cross-platform sync path table, resolve for the current platform)
//   __REGISTER__       -> quoted string, "brand" or "product", from SOUL.md's ## Register
//   __AUDIENCE__       -> quoted short audience description, from SOUL.md's ## Users
//   __SECTIONS__       -> array of section name strings, the site's planned sections in build order,
//                         from plan's round 2 content/sections interview, e.g. ["hero", "features", "pricing", "footer"]
//   __TECHNIQUES__     -> array of technique file slugs chosen in plan's round 3 visual direction,
//                         e.g. ["shaders", "motion"], or [] if the project stays plain content
//   __LOOT_TAGS__      -> array of tag strings to match library/muster/<slug>.md and
//                         library/eigene/<slug>.md entries against
//   __VARIANT_COUNT__  -> bare number, how many divergent variants to generate per section (3 is a
//                         reasonable default for a brand surface, plan may raise it for high-ambition briefs)

export const meta = {
  name: 'arsenal-build-website',
  description: 'Build a marketing/brand website: content first, loot grounding, variant selection, independent critique, performance gate',
  phases: [
    { title: 'Content', detail: 'real copy per section, self-audited against the floskel and one-sentence tests, before any layout work' },
    { title: 'Loot grounding', detail: 'pull matching confirmed references from the library before anything gets generated' },
    { title: 'Variant generation and selection', detail: 'multiple divergent directions per section, judged and synthesized, never a single first draft' },
    { title: 'Assembly', detail: 'build the selected variant into the real project stack and produce a previewable page' },
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
const SECTIONS = __SECTIONS__
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

const MAX_CRITIQUE_ROUNDS = 2
const MAX_PERF_ROUNDS = 2

// ---- Schemas ----
const CONTENT_SCHEMA = {
  type: 'object',
  properties: {
    section: { type: 'string' },
    copy: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['section', 'copy'],
}

const ASSET_SCHEMA = {
  type: 'object',
  properties: {
    section: { type: 'string' },
    assets: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          description: { type: 'string' },
          source: { type: 'string' },
          license: { type: 'string' },
          authenticity: { type: 'string' },
        },
        required: ['description', 'source'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['section', 'assets'],
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
    section: { type: 'string' },
    chosen_variant_id: { type: 'string' },
    rationale: { type: 'string' },
    grafted_ideas: { type: 'string' },
  },
  required: ['section', 'chosen_variant_id', 'rationale'],
}

const BUILD_SCHEMA = {
  type: 'object',
  properties: {
    section: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['section', 'files'],
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
  return `Project "${PROJECT_NAME}" at ${PROJECT_PATH}, register ${REGISTER}, audience ${AUDIENCE}. Read SOUL.md and MASK.md in that folder first, they hold the confirmed brief and design tokens.`
}

function writeContentPrompt(section) {
  return `${contextLine()} Write real, final-form copy for the "${section}" section. No lorem ipsum, no bracketed placeholders. Read ${SKILL_PATH}/reference/website.md rules 1-6 and ${SKILL_PATH}/reference/copywriting.md's floskel list before writing. Lead with clarity (what is this) before relevance, value and differentiation. Return the section name and the copy.`
}

function auditContentPrompt(draft, section) {
  return `${contextLine()} Section "${section}" has a first-draft copy: ${JSON.stringify(draft)}. Run it against reference/website.md's one-sentence test (for headlines), say-the-opposite test (for value claims), and the floskel list in reference/copywriting.md. Replace anything content-free with a checkable number, mechanism, timeframe or named audience. Return the revised, final copy for this section.`
}

function sourceAssetPrompt(section) {
  return `${contextLine()} Source media for the "${section}" section per reference/assets.md and reference/website.md rule 7 (authenticity ranking: real product/team/customer imagery before any stock, candid niche stock only as fallback, licensing documented per image). Return the assets found with description, source and license for each.`
}

function lootPrompt() {
  return `Find loot entries in ${LIBRARY_PATH} (library/muster/<slug>.md and library/eigene/<slug>.md files) tagged with any of [${LOOT_TAGS.join(', ')}] or matching register "${REGISTER}". Read ${LIBRARY_PATH}/library/_index.md FIRST: it lists every entry with its slug, tags and one-line summary, so pick the candidates from that index and open only those files, do not read the whole library. If _index.md is missing, OR it exists but its table carries no data rows (header only, which reads the same as a missing index: there is nothing there to pick candidates from), fall back to scanning the muster/ and eigene/ folders directly for candidate files. In that fallback case, once you have the confirmed matches, also append a row per found file to library/_index.md (slug, branch, category, tags, one clause on what it holds, source, date, in the format loot.md defines) so the index catches up with what is actually on disk instead of staying empty. Skip any file whose name starts with an underscore (for example _FORMAT.md and _index.md itself), those are format and index documentation, not captured references, and must never be treated as a match even if their content looks plausible. Read each remaining candidate file. A match from eigene/ is a reusable building block with working code to use directly. A match from muster/ is a reference to learn from only, never copy its code or its assets. Return the confirmed matches with a short summary of what to ground on (the specific transferable thing the user confirmed, not a generic description) and which branch each match came from. Finding zero matches is a valid, expected state on a fresh library, return an empty list and say so plainly, never invent a match to fill the gap.`
}

function variantPrompt(section, index, sectionCopy, lootMatches, techniques) {
  const lootNote = lootMatches && lootMatches.length
    ? `Ground this in these confirmed references: ${JSON.stringify(lootMatches)}.`
    : 'No loot references matched this project, work from MASK.md tokens and the brief alone, do not invent a reference.'
  const techniqueNote = techniques && techniques.length
    ? `Techniques licensed for this project's hero/brand surfaces: ${techniques.join(', ')} (see the matching files under ${SKILL_PATH}/reference/).`
    : 'No decorative technique was chosen for this project, keep this variant to typography, color, spacing and layout.'
  return `${contextLine()} Propose ONE divergent visual/structural direction (variant ${index + 1}) for the "${section}" section, built on this confirmed copy: ${JSON.stringify(sectionCopy)}. ${lootNote} ${techniqueNote} This must read as a genuinely different decision from the other variants being generated in parallel for this section, not a palette swap of the same layout. Avoid every anti-pattern listed in reference/website.md's anti-pattern table. Return a variant id and a concrete description of the direction (layout shape, media treatment, motion if any).`
}

function judgeVariantPrompt(variant, section) {
  return `Score this proposed variant for the "${section}" section of "${PROJECT_NAME}" against reference/website.md's rule set and anti-pattern table, and against the AI-slop test: ${JSON.stringify(variant)}. Score 0-10. Return the variant id, score, strengths and weaknesses.`
}

function selectPrompt(section, variants, judged) {
  return `Section "${section}" of "${PROJECT_NAME}" has these variants: ${JSON.stringify(variants)}, judged as: ${JSON.stringify(judged)}. Choose the strongest overall, but graft in any specific strong idea a runner-up variant had that the winner lacks. Return the section name, the chosen variant id, the rationale, and any grafted ideas.`
}

function buildPrompt(selection) {
  return `${contextLine()} Build the selected variant for section "${selection.section}" into the project's real stack (read ARMOURY.md's ## Tools and ## Libraries first for the stack and conventions). Selection: ${JSON.stringify(selection)}. Write real, semantic, production code, not a mock. If a decorative shader/3D/motion technique is used, stub the reduced-motion and mobile fallback per ${SKILL_PATH}/reference/performance.md now, the performance gate later checks it does not verify it exists from scratch. EXCLUSIVE PATHS, this is a hard constraint: write only files that belong to this one section (its own component/partial file, its own stylesheet or style block, its own assets). Never edit a shared file (global stylesheet, token file, layout, route entry, index page, package manifest); if this section needs a change there, describe the needed change in the summary instead of making it, the integration step owns those files. Return the section name, the files touched, and a short summary.`
}

function integratePrompt(builtSections) {
  return `${contextLine()} These sections were built independently: ${JSON.stringify(builtSections)}. Assemble them into one coherent page (or route set) in the project's real stack, in the section order [${SECTIONS.join(', ')}]. Make sure the result is actually previewable (start whatever dev server or build step ARMOURY.md's tools imply). Return how to preview it (method and location/URL), the full list of files touched, and any integration notes.`
}

// Critique roles, isolated from each other, mirroring commands/critics.md's website roster: the
// first five mirror critics.md's roster, and two more, named exactly "Impeccable critique" and
// "Impeccable audit", are hardwired here as mandatory gates per HANDOFF.md ("impeccable critique
// und audit Pflichtstufen"), each running one of impeccable's own commands against the rendered
// result. All seven feed the same FINDING_SCHEMA and the same merge step below, none is skippable.
const CRITIQUE_ROLES = [
  {
    name: 'design-critique',
    model: undefined, // judgment, inherits the main-loop model
    prompt: (integrated) => `Inspect "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) as a design critic: hierarchy, taste, the AI-slop test, absolute-ban compliance per reference/website.md and impeccable's absolute bans. You do not see any other reviewer's output, work from the rendered result alone. Every finding needs a location (route/section/element) and a concrete fix.`,
  },
  {
    name: 'pattern-detector',
    model: 'haiku', // mechanical checklist matching, no independent judgment required
    prompt: (integrated) => `Inspect "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) against reference/website.md's anti-pattern table and the category-reflex check, entry by entry, as a deterministic detector. Flag every literal match. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'technical-audit',
    model: 'sonnet',
    prompt: (integrated) => `Run a measurable technical audit of "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}): accessibility (contrast, focus rings, semantic structure) and performance basics. Use available browser/devtools tools, do not estimate from reading code alone. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'persona-walkthrough',
    model: undefined, // judgment, inherits the main-loop model
    prompt: (integrated) => `Walk through "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) as 2-3 personas relevant to a ${REGISTER} site for audience "${AUDIENCE}" (impeccable's personas.md archetypes, or real audience data from SOUL.md). Report concrete, element-level red flags per persona, never a generic persona description. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'legal-and-trust',
    model: 'sonnet',
    prompt: (integrated) => `Check "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) against reference/website.md's mandatory components: Impressum, Datenschutzerklärung, cookie consent banner behavior, footer legal links, plus basic conversion and trust signals. Every finding needs a location and a concrete fix.`,
  },
  {
    name: 'Impeccable critique',
    model: undefined, // judgment, inherits the main-loop model
    prompt: (integrated) => `Run impeccable's "critique" command against "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}), following ${SKILL_PATH}/../impeccable/reference/critique.md exactly: the two independent assessments it prescribes (LLM design review including AI-slop detection against every DON'T guideline, cognitive load checklist, emotional journey, Nielsen's heuristics scoring; and the automated detector scan), then its own merge of the two. This is a mandatory gate, not optional and not a duplicate of the design-critique role above, run it in full even if other roles already found overlapping issues. You do not see any other reviewer's output, work from the rendered result alone. Every finding needs a location (route/section/element) and a concrete fix.`,
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
  return `${contextLine()} Implement this fix directly in the project files: ${JSON.stringify(finding)}. Make the minimal change that resolves it without introducing a new anti-pattern from reference/website.md.`
}

// A file path mentioned inside a finding's own text, used as the grouping fallback below: a
// word-ish token ending in a short extension, e.g. "src/components/Hero.tsx" or "app/page.tsx:42".
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
  return `${contextLine()} Implement these fixes directly in the project files, one at a time, in the order given: ${JSON.stringify(findings)}. ${scope} Make the minimal change that resolves each finding without introducing a new anti-pattern from reference/website.md.`
}

function perfCheckPrompt(integrated) {
  return `Check "${PROJECT_NAME}" at ${integrated.preview_location} (${integrated.preview_method}) against ${SKILL_PATH}/reference/performance.md's four checks: prefers-reduced-motion fallback (toggle it, reload, confirm a complete non-broken design), mobile/low-power fallback (viewport below breakpoint, capped DPR, no blocked first paint), lazy mount and cleanup (canvases pause off-screen, no leaked contexts), and contrast/focus surviving any animation (darkest and brightest frame, WCAG AA 4.5:1). Use available browser/devtools tools including a Lighthouse mobile run if available. Return each check's pass/fail and a lighthouse_mobile_score if you ran one, plus a plain-language issues list for anything that failed.`
}

function perfFixPrompt(perfResult) {
  return `${contextLine()} The performance gate found these issues: ${JSON.stringify(perfResult.issues)}. Fix them per ${SKILL_PATH}/reference/performance.md's guidance (reduced-motion CSS and JS branch, DPR cap, breakpoint fallback, IntersectionObserver pause, explicit dispose/cleanup, contrast-safe overlay). Do not remove the effect to dodge the check unless reference/performance.md explicitly allows omitting it on mobile.`
}

// ---- Pipeline stages ----
function writeContentStage(_prev, section) {
  return agent(writeContentPrompt(section), { phase: 'Content', schema: CONTENT_SCHEMA, model: 'sonnet' })
}

function auditContentStage(draft, section) {
  return agent(auditContentPrompt(draft, section), { phase: 'Content', schema: CONTENT_SCHEMA, model: 'sonnet' })
}

function sourceAssetStage(_prev, section) {
  return agent(sourceAssetPrompt(section), { phase: 'Content', schema: ASSET_SCHEMA, model: 'sonnet' })
}

async function generateVariantsStage(_prev, section) {
  return (await parallel(
    Array.from({ length: VARIANT_COUNT }, (_v, i) => () => agent(
      variantPrompt(section, i, contentFor(cachedContent, section), cachedLoot, TECHNIQUES),
      { phase: 'Variant generation and selection', schema: VARIANT_SCHEMA, model: 'sonnet' },
    )),
  )).filter(Boolean)
}

async function selectVariantStage(variants, section) {
  const judged = (await parallel(variants.map((v) => () => agent(
    judgeVariantPrompt(v, section),
    { phase: 'Variant generation and selection', schema: JUDGE_SCHEMA },
  )))).filter(Boolean)
  return agent(selectPrompt(section, variants, judged), { phase: 'Variant generation and selection', schema: SELECTION_SCHEMA })
}

function contentFor(content, section) {
  const match = (content || []).find((c) => c && c.section === section)
  return match || { section, copy: '' }
}

// ---- Run ----
log(`arsenal website build, stage "${STAGE}", ${SECTIONS.length} section(s), ${VARIANT_COUNT} variant(s) per section`)

// Stage "assets": partial build, source media only, no copy pass. `build assets` uses this.
if (STAGE === 'assets') {
  phase('Content')
  const assets = await pipeline(SECTIONS, sourceAssetStage)
  return { stage: 'assets', project: PROJECT_NAME, assets }
}

// Mechanism 1, content before layout: real copy for every section before any visual generation.
phase('Content')
const cachedContent = await pipeline(SECTIONS, writeContentStage, auditContentStage)

// Stage "copy": partial build, copy only. `build copy` uses this.
if (STAGE === 'copy') {
  return { stage: 'copy', project: PROJECT_NAME, content: cachedContent }
}

const assets = await pipeline(SECTIONS, sourceAssetStage)

// Mechanism 2, reference pull: loot entries loaded before any generation starts.
phase('Loot grounding')
const lootResult = await agent(lootPrompt(), { phase: 'Loot grounding', schema: LOOT_SCHEMA, model: 'haiku' })
const cachedLoot = (lootResult && lootResult.matches) || []
if (cachedLoot.length === 0) {
  log('Loot grounding: no matching reference entries, this is a valid state ("no grounding available"), proceeding without inventing one')
} else {
  log(`Loot grounding: ${cachedLoot.length} matching reference entr${cachedLoot.length === 1 ? 'y' : 'ies'} for tags [${LOOT_TAGS.join(', ')}]`)
}

// Mechanism 3, variant generation and selection: divergent directions per section, judged and
// synthesized, not a single first draft accepted. Generation and selection overlap across
// sections here (no section's selection needs another section's variants), a genuine pipeline.
phase('Variant generation and selection')
const selections = (await pipeline(SECTIONS, generateVariantsStage, selectVariantStage)).filter(Boolean)

// Assembly is the connective step the fixed order implies but does not name: variants must
// become real, renderable code before the critique loop has anything to inspect.
//
// Parallel after a single scaffold step (see below), and deliberately WITHOUT `isolation: 'worktree'`. A worktree requires the project to
// be a git repository, which nothing in this pipeline creates: build.md now gates on one, but a
// gate that passes on a freshly initialized repo is still a thin guarantee. It is also
// unnecessary here, because buildPrompt pins every agent to its own section's files and forbids
// shared ones, so parallel writes stay disjoint. Add `isolation: 'worktree'` only for a project
// where two sections genuinely must write the same file, and only where it is a git repository.
phase('Assembly')
// Parallel assembly (behavior.md 2026-09-18): ONE agent first lays down the shared scaffold
// (stack, tokens from MASK.md, base layout, one route per page, an empty mount point per section,
// all packages from ARMOURY.md). Only then do the section agents run in parallel, each owning
// nothing but src/sections/<slug>/ (plus its own src/pages/api/<slug>/ and src/lib/<slug>/ when it
// needs server code), so their writes stay disjoint without a worktree.
const scaffold = await agent(`${contextLine()} Lay down the shared scaffold before any section is built. Read ARMOURY.md (## Tools, ## Libraries, ## Project overrides) and MASK.md. Set up the project's stack per ${SKILL_PATH}/reference/stack.md in ${PROJECT_PATH}, install every library ARMOURY.md lists, write the design tokens (colors, type, scale) as one global stylesheet, a base layout with navigation and a footer mount point, and one route per page that mounts its sections from src/sections/<slug>/index.astro (or the stack's equivalent). Sections in order: ${JSON.stringify(SECTIONS)}. Create an empty placeholder per section and return the section -> slug mapping. The build command must pass. No secrets, only a .env.example.`, { phase: 'Assembly', schema: INTEGRATE_SCHEMA, model: 'sonnet' })
const builtSections = (await parallel(selections.map((sel) => () => agent(
  `${buildPrompt(sel)} The shared scaffold already exists: ${JSON.stringify(scaffold)}. Your section lives only in src/sections/<slug>/ (slug per the scaffold), server code only under src/pages/api/<slug>/ and src/lib/<slug>/. Other agents build other sections at the same time: touch nothing outside your paths and install no packages, name missing ones in the summary instead.`,
  { phase: 'Assembly', schema: BUILD_SCHEMA, model: 'sonnet' },
)))).filter(Boolean)
const integrated = await agent(integratePrompt(builtSections), { phase: 'Assembly', schema: INTEGRATE_SCHEMA, model: 'sonnet' })

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

// Mechanism 5, performance and reduced-motion gate: run against the actual rendered output.
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

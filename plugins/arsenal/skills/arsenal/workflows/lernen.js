// arsenal `lernen`: turns a real design source (an open course, a canonical book, a standard, a
// primary study) into measurable checkpoints inside reference/, so the critics gain something new
// to measure against. The gain is not the knowledge itself, the model already holds most of it,
// the gain is the translation into thresholds and check procedures that a critic can apply to a
// finished screen and either pass or fail.
//
// Invocation (see commands/lernen.md):
//   /arsenal lernen <topic or URL> [--nur-quellen] [--quelle URL ...]
//
// TWO ENTRY POINTS, both through this one file:
//   1. Candidate run: `args` without `bestaetigt`. Curates sources (topic mode) or takes the given
//      ones (URL mode), appraises each source, derives rules from the readable ones, has a critic
//      check every rule against the existing stock, then RETURNS the candidate list. Nothing is
//      written anywhere, this run is read-only by construction.
//   2. Filing run: `args` with `bestaetigt` (the rule slugs the user approved) plus `kandidaten`
//      (the `candidates` array returned by run 1). Only those rules get written.
//
// args fields:
//   thema        string, the topic to curate sources for, or null when sources are given directly
//   quellen      array of URL strings (a bare URL argument plus every --quelle value)
//   nur_quellen  true to stop after curation and return the source candidates only
//   datum        REQUIRED string, the check date in ISO form, for example "2026-09-09". The main
//                model passes today's date; this script never calls Date, so a run is reproducible
//                and the record of a source carries the date it was actually checked.
//   skill_pfad   REQUIRED string, absolute path to the arsenal skill folder (the folder holding
//                SKILL.md, reference/ and planung/). Platform dependent, so it is passed in rather
//                than hardcoded, exactly like the sync paths in SKILL.md.
//   bestaetigt   array of approved rule slugs, present only on the filing run
//   kandidaten   the `candidates` array from the candidate run, required alongside `bestaetigt`
//
// CONTEXT CONTRACT (holds for every agent below, and is repeated inside every prompt):
// raw source material never enters reference/ and never enters this workflow's return value.
// Subagents read in their own context and hand back structured data only: derived rules, short
// cited phrases with their location, appraisal fields. No transcripts, no chapter dumps, no
// pasted lecture notes.

export const meta = {
  name: 'arsenal-lernen',
  description: 'Turn a design source into measurable checkpoints in reference/: curate or take sources, appraise them, derive rules with thresholds, reconcile them against the existing stock, and file only what the user confirmed',
  phases: [
    { title: 'Curation', detail: 'opus, parallel: find candidate sources for a topic and shortlist them by expected yield, citability and accessibility (skipped when sources are given directly)' },
    { title: 'Source appraisal', detail: 'sonnet: record title, author, year, address, accessibility, citability and check date per source; paid or gated sources are recorded and never read' },
    { title: 'Derivation and reconciliation', detail: 'per source: sonnet reads and derives rules in the fixed checkable format, then an opus critic checks each rule against the target file and the index and decides accept, accept with precedence line, or reject' },
    { title: 'Filing', detail: 'haiku, filing run only: write each approved rule into exactly one reference file, add its index row, append one source line to planung/recherche-lernen.md' },
  ],
}

// ---- Arguments ----
const ARGS = (args && typeof args === 'object') ? args : {}
const TOPIC = (typeof ARGS.thema === 'string' && ARGS.thema.trim()) ? ARGS.thema.trim() : null
const GIVEN_SOURCES = Array.isArray(ARGS.quellen) ? ARGS.quellen.filter(Boolean) : []
const SOURCES_ONLY = ARGS.nur_quellen === true
const CHECKED_ON = (typeof ARGS.datum === 'string' && ARGS.datum.trim()) ? ARGS.datum.trim() : null
const SKILL_PATH = (typeof ARGS.skill_pfad === 'string' && ARGS.skill_pfad.trim()) ? ARGS.skill_pfad.trim() : null
const CONFIRMED = Array.isArray(ARGS.bestaetigt) ? ARGS.bestaetigt.filter(Boolean) : []
const CANDIDATES_IN = Array.isArray(ARGS.kandidaten) ? ARGS.kandidaten.filter(Boolean) : []

if (!CHECKED_ON) {
  throw new Error('args.datum is required (ISO date string). The workflow never reads the clock itself, the check date belongs to the source record.')
}
if (!SKILL_PATH) {
  throw new Error('args.skill_pfad is required (absolute path to the arsenal skill folder holding SKILL.md, reference/ and planung/).')
}
if (CONFIRMED.length > 0 && CANDIDATES_IN.length === 0) {
  throw new Error('args.bestaetigt was given without args.kandidaten. The filing run needs the candidate list from the candidate run, it never re-derives rules.')
}
if (CONFIRMED.length === 0 && !TOPIC && GIVEN_SOURCES.length === 0) {
  throw new Error('Nothing to learn from: pass args.thema (topic mode), args.quellen (URL mode), or args.bestaetigt plus args.kandidaten (filing run).')
}

// ---- Fixed vocabulary ----
// The five dials are defined in reference/registers.md and the set is closed: this command
// classifies a rule against them, it never invents a sixth dial or a new stop on one.
const DIALS = ['auftreten', 'bewegung', 'dichte', 'technik', 'tonfall']

// A rule lands in exactly one of these files. registers.md and presets.md are deliberately absent:
// learning does not extend the dial vocabulary, and a preset is a pre-filled set of dials, not a
// place for evidence.
const TARGET_FILES = [
  'design-foundations.md',
  'ia-and-structure.md',
  'motion-doctrine.md',
  'typography.md',
  'copywriting.md',
  'layouts.md',
  'components.md',
  'performance.md',
  'software.md',
  'website.md',
  'stack.md',
  'shaders.md',
  '3d.md',
  'motion.md',
  'scroll-choreography.md',
  'assets.md',
  'product-motion.md', // product-surface motion: control morphs, expanding bars, shells, color roles, goo
]

const ACCESSIBILITY_LEVELS = ['open', 'registration', 'paid']
const NOT_ACCESSIBLE_NOTE = 'not accessible, consider author talks or open summaries'
const INDEX_FILE = `${SKILL_PATH}/reference/_index.md`
const ARCHIVE_FILE = `${SKILL_PATH}/reference/_index-archiv.md`
const SOURCE_LOG_FILE = `${SKILL_PATH}/planung/recherche-lernen.md`
const INDEX_CHAR_BUDGET = 2000
const MAX_SOURCES = 4
const MAX_RULES_PER_SOURCE = 8

// Curation lenses. Each one is a separate agent so the shortlist is not four variations of the
// same first search hit. The first two are named in the user brief for this command.
const CURATOR_LENSES = [
  'open university and college course material: syllabi, lecture notes, open courseware, published reading lists',
  'canonical books and long-form essays by recognized designers, typographers and art directors',
  'standards, specifications and official platform guidance (W3C, WCAG, ISO, vendor human interface guidelines)',
  'primary research papers and empirical studies that the practitioner literature on this topic keeps citing',
]

const CONTEXT_CONTRACT = 'Context contract: return structured data only. Never return raw source text, transcripts, chapter dumps or long verbatim passages. A quotation is allowed only as a short phrase with its exact location (page, section, timestamp), and only where the wording itself is the evidence.'

// ---- Schemas ----
const SOURCE_CANDIDATE_SCHEMA = {
  type: 'object',
  properties: {
    candidates: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          author: { type: 'string' },
          year: { type: 'string' },
          url: { type: 'string' },
          accessibility: { type: 'string' },
          citable: { type: 'boolean' },
          why: { type: 'string' },
        },
        required: ['title', 'url', 'accessibility', 'why'],
      },
    },
  },
  required: ['candidates'],
}

const SHORTLIST_SCHEMA = {
  type: 'object',
  properties: {
    shortlist: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          author: { type: 'string' },
          year: { type: 'string' },
          url: { type: 'string' },
          accessibility: { type: 'string' },
          citable: { type: 'boolean' },
          why: { type: 'string' },
          rank: { type: 'number' },
        },
        required: ['title', 'url', 'accessibility', 'why'],
      },
    },
    rejected: { type: 'array', items: { type: 'string' } },
  },
  required: ['shortlist'],
}

const APPRAISAL_SCHEMA = {
  type: 'object',
  properties: {
    source_slug: { type: 'string' },
    title: { type: 'string' },
    author: { type: 'string' },
    year: { type: 'string' },
    url: { type: 'string' },
    accessibility: { type: 'string' },
    citable: { type: 'boolean' },
    checked_on: { type: 'string' },
    scope: { type: 'string' },
    note: { type: 'string' },
  },
  required: ['source_slug', 'title', 'url', 'accessibility', 'checked_on'],
}

const DERIVED_SCHEMA = {
  type: 'object',
  properties: {
    source_slug: { type: 'string' },
    rules: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          slug: { type: 'string' },
          rule: { type: 'string' },
          check: { type: 'string' },
          not_says: { type: 'string' },
          dial: { type: 'string' },
          target_file: { type: 'string' },
          citation: { type: 'string' },
          evidence: { type: 'string' },
          tags: { type: 'array', items: { type: 'string' } },
          one_sentence: { type: 'string' },
        },
        required: ['slug', 'rule', 'check', 'not_says', 'dial', 'target_file', 'citation', 'evidence'],
      },
    },
    discarded: { type: 'array', items: { type: 'string' } },
  },
  required: ['source_slug', 'rules'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    source_slug: { type: 'string' },
    decisions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          slug: { type: 'string' },
          decision: { type: 'string' },
          reason: { type: 'string' },
          collides_with: { type: 'string' },
          precedence_line: { type: 'string' },
          target_file: { type: 'string' },
        },
        required: ['slug', 'decision', 'reason'],
      },
    },
  },
  required: ['source_slug', 'decisions'],
}

const FILING_SCHEMA = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    written_slugs: { type: 'array', items: { type: 'string' } },
    section: { type: 'string' },
    notes: { type: 'string' },
  },
  required: ['file', 'written_slugs'],
}

const INDEX_SCHEMA = {
  type: 'object',
  properties: {
    rows_added: { type: 'array', items: { type: 'string' } },
    index_size_chars: { type: 'number' },
    archived_slugs: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['rows_added'],
}

const SOURCE_LOG_SCHEMA = {
  type: 'object',
  properties: {
    lines_added: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['lines_added'],
}

// ---- Prompt builders ----
function curatePrompt(lens) {
  return `Find candidate sources on the design topic "${TOPIC}" through exactly one lens: ${lens}. This feeds the arsenal skill's reference library, whose purpose is measurable design rules a reviewer can pass or fail a finished screen against, not general reading. Judge every candidate on three things: is it citable (a named author or issuing body, a fixed edition or version, a stable address), is it specific enough to yield thresholds rather than slogans, and how accessible is it. Set accessibility to exactly one of ${ACCESSIBILITY_LEVELS.join(', ')}: "open" means readable at the address without an account or payment, "registration" means an account or email wall, "paid" means purchase or subscription. Do not soften a paywall into "open" because a preview page loads. Return at most 6 candidates with title, author, year, url, accessibility, citable, and one sentence on why it earns a read. ${CONTEXT_CONTRACT}`
}

function shortlistPrompt(pools) {
  return `Four independent curators proposed sources on "${TOPIC}" for the arsenal reference library: ${JSON.stringify(pools)}. Dedupe them, drop anything that is a summary of a stronger candidate already in the list, and shortlist at most ${MAX_SOURCES} in rank order. Rank by expected yield of measurable rules first, citability second, accessibility third: a paid canonical work still belongs on the shortlist if it is the actual authority, it will simply be recorded and not read. Do not pad the list to reach ${MAX_SOURCES}, a shortlist of one strong source is a better answer than four weak ones. Return the shortlist with title, author, year, url, accessibility, citable, why and rank, plus a short list of what you rejected and why. ${CONTEXT_CONTRACT}`
}

function appraisePrompt(source) {
  return `Record and appraise one source for the arsenal reference library: ${JSON.stringify(source)}. Establish title, author, year and the exact address. Set accessibility to exactly one of ${ACCESSIBILITY_LEVELS.join(', ')} by actually checking the address with WebFetch where there is one, never by assuming from the domain. Set citable true only when the source has a named author or issuing body and a stable, dated or versioned form that a rule can point back to later. Set checked_on to exactly "${CHECKED_ON}", do not substitute your own idea of today. Build source_slug as a short lowercase hyphenated identifier from author or issuer plus year, for example "muellerbrockmann-1981". In scope, name in one sentence which part of the source is worth deriving from. If the address is unreachable, gated or paid, say so in note and still return the record: a source that cannot be read is still worth having on file so a later run does not curate it again. ${CONTEXT_CONTRACT}`
}

function derivePrompt(appraisal) {
  return `Read this openly accessible source and derive checkable design rules from it: ${JSON.stringify(appraisal)}. Use WebFetch on the address, read the part named in scope, and stop reading once you have what you need.

Format per rule, every field mandatory:
- slug: short lowercase hyphenated identifier, unique within this source, for example "line-length-45-75".
- rule: ONE sentence carrying a threshold or a measurement procedure. "Body text runs 45 to 75 characters per line" qualifies. "Typography should be readable" does not.
- check: how a reviewer verifies it on a finished screen in one or two steps, concretely enough that two reviewers reach the same verdict.
- not_says: one line naming what the rule does NOT say, the over-reading a reader would otherwise commit. This field exists because the failure mode of design folklore is a real finding stretched past its evidence.
- dial: exactly one of ${DIALS.join(', ')}, the register dial from reference/registers.md whose position this rule depends on or constrains.
- target_file: exactly one name from this list, the single place the rule belongs: ${TARGET_FILES.join(', ')}. Pick the most specific fit. A rule that seems to belong in two files belongs in the more specific one and is cross-referenced from the other, never duplicated.
- citation: the source in parentheses in the house form, for example "(Mueller-Brockmann 1981)", plus the location (page, section, lecture number) where the claim sits. A short quoted phrase is allowed only where the wording itself is the evidence.
- evidence: "measurable" when the rule carries a real threshold or procedure, "unproven" when the source asserts it without evidence or the claim resists measurement. An unproven rule is background, never a binding check, and stays marked as such wherever it is written.
- tags: two to four short lowercase tags for the index row.
- one_sentence: the index row's one sentence description, at most 120 characters.

Discard rather than dress up: anything that will not go into this format goes into discarded with one line on why. Three solid rules and six discards is a good result; inventing a threshold the source does not carry is a failure of the run. At most ${MAX_RULES_PER_SOURCE} rules. ${CONTEXT_CONTRACT}`
}

function reconcilePrompt(derived, appraisal) {
  const files = Array.from(new Set((derived.rules || []).map((r) => r && r.target_file).filter(Boolean)))
  return `Check derived rules against the existing stock BEFORE anything is written. Source: ${JSON.stringify(appraisal)}. Proposed rules: ${JSON.stringify(derived.rules)}.

Load ${INDEX_FILE} and every target file named here, in full: ${files.map((f) => `${SKILL_PATH}/reference/${f}`).join(', ')}. Judge each proposed rule against what is already there and return exactly one decision per rule:
- "accept": genuinely new, or a sharper measurable form of something the stock only gestures at. Say in reason what it adds.
- "accept-with-precedence": it overlaps a rule already in the stock and the two could be read as conflicting. Then supply precedence_line, one bold sentence in the house pattern of reference/design-foundations.md line 44, naming which file governs on conflict, for example "**On any conflict between this section and typography.md, typography.md governs**". Name the collision in collides_with.
- "reject": a duplicate that adds nothing, a contradiction the existing rule wins outright, folklore the stock already refuses, or a rule whose threshold the source does not actually support. Give the reason plainly, a rejected rule is a normal outcome and not a failure.

Correct target_file where the proposed one is wrong and return the corrected value; a rule still ends up in exactly one file. Every rule keeps status "unverified" regardless of your decision: a rule counts as verified only once a critic has applied it in a real project. ${CONTEXT_CONTRACT}`
}

function writeRulesPrompt(file, rules) {
  const path = `${SKILL_PATH}/reference/${file}`
  return `File these approved rules into ${path}, and into no other file. Rules: ${JSON.stringify(rules)}.

Read the file first and match its house style exactly: a rule is one bullet, the source in parentheses at the end, and a rule marked unproven says "unproven" inline and reads as background rather than a binding check. Put each rule into the section it belongs to, open a new section only when none fits. Under each rule, on their own lines, add the "what the rule does NOT say" line and the check procedure. Every new rule carries "status: unverified" at the end of its entry. Where a rule arrived with a precedence_line, place that line at the top of its section in bold, in the pattern already used in design-foundations.md.

Do not touch any other file, do not restate a rule that is already there, and never paste source material into the file. Return the file you touched and the slugs you wrote.`
}

function indexPrompt(rules, sources) {
  return `Update the reference index at ${INDEX_FILE} with one row per newly filed rule. Rules: ${JSON.stringify(rules)}. Sources: ${JSON.stringify(sources)}.

The index is a short header line naming its purpose, then one table with exactly these columns: slug | file | tags | one sentence | source | date | status. Fill source with the citation in the house form, date with "${CHECKED_ON}", status with "unverified". Keep the whole file under ${INDEX_CHAR_BUDGET} characters: it exists so a critic can see the whole stock at a glance without loading every reference file, and it stops doing that the moment it needs paging. If the new rows cross the budget, move the OLDEST rows whose status is still "unverified" to ${ARCHIVE_FILE} (same table, same columns, create the file with the same header if it does not exist) until the index fits again, and report which slugs you moved. Never move a "verified" row, and never drop a row instead of archiving it. Return the rows you added, the resulting index size in characters, and the archived slugs.`
}

function sourceLogPrompt(sources, ruleCount) {
  return `Append the source record for this learning run to ${SOURCE_LOG_FILE}: ${JSON.stringify(sources)}, ${ruleCount} rule(s) filed on ${CHECKED_ON}.

Exactly ONE line per source, in a single table with the columns: source_slug | title | author | year | url | accessibility | citable | checked | rules filed. A source that was appraised but not read carries "${NOT_ACCESSIBLE_NOTE}" in the rules-filed column instead of a count, so a later run can see it was considered and why it was skipped rather than curating it again. If the file does not exist, create it with a frontmatter block in the pattern of the other planung/recherche-*.md files (title, updated: ${CHECKED_ON}, stand: laufend), one short paragraph naming what the file is, then the table header. Never copy source content into this file, it is a register of what was consulted, not a reader. Return the lines you added.`
}

// ---- Pipeline stages ----
function appraiseStage(_prev, source) {
  return agent(appraisePrompt(source), {
    label: `appraise ${(source && (source.title || source.url)) || 'source'}`,
    phase: 'Source appraisal',
    schema: APPRAISAL_SCHEMA,
    model: 'sonnet',
  })
}

// Stage 1 of the per-source pipeline: read and derive. Execution against a fixed format, so sonnet.
// A source that is not openly accessible is never fetched, it is carried through with the standing
// note instead, and the pipeline moves on.
async function deriveStage(_prev, appraisal) {
  if (!appraisal) return null
  if (appraisal.accessibility !== 'open') {
    log(`Source "${appraisal.source_slug}" is ${appraisal.accessibility}: ${NOT_ACCESSIBLE_NOTE}`)
    return { appraisal, rules: [], discarded: [], skipped: NOT_ACCESSIBLE_NOTE }
  }
  const derived = await agent(derivePrompt(appraisal), {
    label: `derive rules from ${appraisal.source_slug}`,
    phase: 'Derivation and reconciliation',
    schema: DERIVED_SCHEMA,
    model: 'sonnet',
  })
  const rules = ((derived && derived.rules) || []).filter(Boolean)
    .filter((r) => TARGET_FILES.includes(r.target_file) && DIALS.includes(r.dial))
  return { appraisal, rules, discarded: (derived && derived.discarded) || [], skipped: null }
}

// Stage 2 of the per-source pipeline: check against the stock. Judging a duplicate or a
// contradiction is judgment, so opus.
async function reconcileStage(derived) {
  if (!derived) return null
  if (!derived.rules.length) return { ...derived, decisions: [] }
  const verdict = await agent(reconcilePrompt(derived, derived.appraisal), {
    label: `reconcile ${derived.appraisal.source_slug} against the stock`,
    phase: 'Derivation and reconciliation',
    schema: VERDICT_SCHEMA,
    model: 'opus',
  })
  return { ...derived, decisions: ((verdict && verdict.decisions) || []).filter(Boolean) }
}

function candidateRows(processed) {
  return processed.flatMap((entry) => (entry.rules || []).map((rule) => {
    const verdict = (entry.decisions || []).find((d) => d && d.slug === rule.slug)
    return {
      slug: rule.slug,
      rule: rule.rule,
      check: rule.check,
      not_says: rule.not_says,
      dial: rule.dial,
      target_file: (verdict && verdict.target_file) || rule.target_file,
      citation: rule.citation,
      evidence: rule.evidence,
      tags: rule.tags || [],
      one_sentence: rule.one_sentence || rule.rule,
      status: 'unverified',
      decision: (verdict && verdict.decision) || 'reject',
      decision_reason: (verdict && verdict.reason) || 'no verdict came back for this rule, treated as rejected rather than waved through',
      collides_with: (verdict && verdict.collides_with) || null,
      precedence_line: (verdict && verdict.precedence_line) || null,
      source: entry.appraisal,
    }
  }))
}

// ---- Run ----

// Entry point 2, filing. Runs only on explicit confirmation, and only over the candidate list the
// first run produced. Nothing is re-derived here, so a rule cannot drift between what the user saw
// and what gets written.
if (CONFIRMED.length > 0) {
  phase('Filing')
  const approved = CANDIDATES_IN.filter((c) => c && CONFIRMED.includes(c.slug))
  if (approved.length === 0) {
    throw new Error('None of the confirmed slugs appear in args.kandidaten, refusing to write rules that were never shown.')
  }
  const misfiled = approved.filter((r) => !TARGET_FILES.includes(r.target_file))
  const writable = approved.filter((r) => TARGET_FILES.includes(r.target_file))
  if (misfiled.length) {
    log(`Skipping ${misfiled.length} confirmed rule(s) without exactly one valid target file: ${misfiled.map((r) => r.slug).join(', ')}`)
  }
  const rejectedButConfirmed = writable.filter((r) => r.decision === 'reject')
  if (rejectedButConfirmed.length) {
    log(`Filing ${rejectedButConfirmed.length} rule(s) the critic rejected, on explicit confirmation: ${rejectedButConfirmed.map((r) => r.slug).join(', ')}`)
  }

  const byFile = {}
  for (const rule of writable) {
    if (!byFile[rule.target_file]) byFile[rule.target_file] = []
    byFile[rule.target_file].push(rule)
  }

  // Sequential on purpose: several agents editing reference files and then the one index
  // concurrently is how an index quietly loses rows.
  const written = []
  for (const file of Object.keys(byFile)) {
    const result = await agent(writeRulesPrompt(file, byFile[file]), {
      label: `write ${byFile[file].length} rule(s) into ${file}`,
      phase: 'Filing',
      schema: FILING_SCHEMA,
      model: 'haiku',
    })
    if (result) written.push(result)
  }

  const filedSources = []
  for (const rule of writable) {
    if (rule.source && !filedSources.some((s) => s && s.source_slug === rule.source.source_slug)) {
      filedSources.push(rule.source)
    }
  }

  const indexUpdate = await agent(indexPrompt(writable, filedSources), {
    label: 'update reference/_index.md',
    phase: 'Filing',
    schema: INDEX_SCHEMA,
    model: 'haiku',
  })
  const sourceLog = await agent(sourceLogPrompt(filedSources, writable.length), {
    label: 'append source lines to planung/recherche-lernen.md',
    phase: 'Filing',
    schema: SOURCE_LOG_SCHEMA,
    model: 'haiku',
  })

  return {
    mode: 'filed',
    date: CHECKED_ON,
    filed: writable.map((r) => ({ slug: r.slug, target_file: r.target_file, status: 'unverified' })),
    skipped: misfiled.map((r) => ({ slug: r.slug, reason: 'no valid single target file' })),
    files_touched: written.filter(Boolean),
    index: indexUpdate,
    source_log: sourceLog,
    follow_up: 'Every filed rule carries status "unverified" until a critic applies it in a real project and flips it to "verified".',
  }
}

// Entry point 1, candidates. Read-only from here to the return.
log(`arsenal lernen, ${TOPIC ? `topic mode ("${TOPIC}")` : `URL mode (${GIVEN_SOURCES.length} source(s) given)`}, checked on ${CHECKED_ON}`)

let sources = GIVEN_SOURCES.map((url) => ({ url }))

if (TOPIC) {
  // Curation is judgment about what deserves to be read at all, so opus, and it is the one place
  // this workflow fans out: four lenses proposing independently beats one agent proposing four
  // times from the same first hit.
  phase('Curation')
  const pools = (await parallel(CURATOR_LENSES.map((lens) => () => agent(curatePrompt(lens), {
    label: `curate: ${lens.split(':')[0]}`,
    phase: 'Curation',
    schema: SOURCE_CANDIDATE_SCHEMA,
    model: 'opus',
  })))).filter(Boolean)
  const shortlist = await agent(shortlistPrompt(pools), {
    label: 'shortlist sources',
    phase: 'Curation',
    schema: SHORTLIST_SCHEMA,
    model: 'opus',
  })
  const picked = ((shortlist && shortlist.shortlist) || []).filter(Boolean).slice(0, MAX_SOURCES)
  if (picked.length === 0) {
    return {
      mode: 'sources',
      topic: TOPIC,
      date: CHECKED_ON,
      sources: [],
      note: 'Curation found no citable source worth reading on this topic. That is a valid outcome: narrow the topic, or name a source directly with --quelle, rather than reading something weak to have read something.',
    }
  }
  if (SOURCES_ONLY) {
    return {
      mode: 'sources',
      topic: TOPIC,
      date: CHECKED_ON,
      sources: picked,
      rejected: (shortlist && shortlist.rejected) || [],
      next_step: 'Rerun with --quelle <url> for the sources worth reading. Nothing was read and nothing was written.',
    }
  }
  sources = sources.concat(picked)
} else if (SOURCES_ONLY) {
  return {
    mode: 'sources',
    date: CHECKED_ON,
    sources,
    note: '--nur-quellen with sources already named: there is nothing to curate, the given sources are the list.',
  }
}

phase('Source appraisal')
const appraisals = (await pipeline(sources, appraiseStage)).filter(Boolean)
const unreadable = appraisals.filter((a) => a.accessibility !== 'open')
if (unreadable.length) {
  log(`${unreadable.length} of ${appraisals.length} source(s) recorded but not read: ${NOT_ACCESSIBLE_NOTE}`)
}

// One pipeline per source: read, then check. Never the other way round, and never a write.
phase('Derivation and reconciliation')
const processed = (await pipeline(appraisals, deriveStage, reconcileStage)).filter(Boolean)
const candidates = candidateRows(processed)
const accepted = candidates.filter((c) => c.decision === 'accept' || c.decision === 'accept-with-precedence')

log(`${candidates.length} candidate rule(s) from ${appraisals.length} source(s), ${accepted.length} recommended by the critic`)

return {
  mode: 'candidates',
  topic: TOPIC,
  date: CHECKED_ON,
  sources: appraisals.map((a) => ({
    source_slug: a.source_slug,
    title: a.title,
    author: a.author,
    year: a.year,
    url: a.url,
    accessibility: a.accessibility,
    citable: a.citable,
    checked_on: a.checked_on,
    read: a.accessibility === 'open',
    note: a.accessibility === 'open' ? (a.note || null) : NOT_ACCESSIBLE_NOTE,
  })),
  candidates,
  discarded: processed.flatMap((p) => (p.discarded || [])),
  next_step: 'Nothing has been written. Put the candidates to the user with AskUserQuestion, then rerun this workflow with args.bestaetigt (the approved slugs) and args.kandidaten (this candidates array).',
}

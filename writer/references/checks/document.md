# Document checks

These are deterministic release gates, not isolated reviewer roles. Run only
the sections whose trigger is active; brief chat answers and local lookups do
not require this document gate. Do not use this file to create a second writing
or evidence policy. The prose scan below detects violations of
`../common/writing.md`; it does not add new style rules.

## For document artifacts: prose

Apply `../common/writing.md` and the active type/format modules as a
pass/fail gate. Pass only when sections have clear purposes, paragraphs have
one principal job, and formulas, code, figures, tables, and lists have
contextual prose and local interpretation. Confirm that required definitions
precede use and that conclusions follow the established evidence without
introducing new results.

For a substantial artifact, also confirm a recoverable topic-sentence chain as
defined in `writing.md`. If reconstructing that reverse outline from the draft
is hard, fail and require a skeleton revision before release.

### Mechanical scan

A mental pass is not a run. Search the draft for the patterns below, record a
per-category hit count, and either fix each hit or keep it with an explicit
reason. Do not report this gate as passed without those counts.

**Keep-vs-cut for contrast.** For every “不是……而是……”, “并非……而是……”,
“而不是……”, “not X but Y”, or equivalent: would the sentence lose factual
content if the negation were removed and rewritten as a positive assertion?
If no, it was rhetorical; rewrite. Retain only contrasts that pass the two
conditions in `writing.md`.

**Process meta and throat-clearing.** Delete sentence openers whose only job
is to announce writing, importance, or a section change:

| English | Chinese |
|---|---|
| It is important/worth noting that | 需要注意的是 / 值得一提的是 |
| In this section we will discuss | 本节将讨论 / 接下来我们将 |
| We now turn our attention to | 下面我们来看 |
| In today's rapidly evolving | 在当今快速发展的 |
| This serves as a testament; it goes without saying | 这充分说明了 / 不难发现 |
| In order to, when *To* suffices | 为了能够 / 进行了深入分析 |

Keep an introduction roadmap that names forthcoming sections. Keep a heading
that names a required template part.

**Empty closers.** Delete a paragraph-final sentence that restates the
paragraph with no new fact, limitation, or next step.

**Generic adjectives and filler verbs.** Flag *novel*, *significant*,
*substantial*, *impressive*, *promising*, *comprehensive*, *robust*,
*powerful*, *delve*, *leverage*, *tapestry*, *realm*, *underscore*,
*multifaceted*, *nuanced*, *cornerstone*, *paradigm*, *synergy*, *holistic*,
*groundbreaking*, and Chinese equivalents 深入剖析, 赋能, 深刻揭示, 具有重要意义.
The bare emphasis words 核心, 关键, 重要, 主要, 本质, and 显著 count as hits when
they stand in for evidence; 关键路径 or a field-standard collocation is exempt.
Replace with a number, a named mechanism, or the field's term, or delete. If
the word is standard terminology in the active field (robust estimator,
paradigm in philosophy of science), it is exempt.

**Label-colon paragraph openers.** Flag openings like `**核心思想**：…`,
`**关键问题**：…`, or a bold label followed by a colon that replaces the first
sentence; rewrite the label into the sentence it introduces.

**Synonym cycling.** If one paragraph uses three or more near-synonyms for
the same concept, converge on the established term.

**Rule of three.** Do not pad a list or argument to three items. Two
load-bearing points beat three padded ones.

**Rhythm (warn only).** If five or more consecutive sentences fall in a
narrow length band, vary them. Methods, procedures, and proof steps may stay
even. Do not fail the gate on rhythm alone.

Do not ban hedging, passive voice, or em-dashes as such. Uncertainty,
conditions, and constructions such as “is given by” remain legitimate in
reports, textbooks, and derivations.

## If a claim ledger exists: source and claims

For each substantive claim, confirm its source, conditions, comparator, and
strength. Verify every cited source exists and supports the nearest claim. Keep
claims from different active objects and explanatory inferences visibly
separate. Remove invented results, citations, interfaces, state transitions,
defaults, formulas, and numerical details.

For experiments, trace every quantitative statement to measured or supplied
data. When the claim ledger is non-empty, use it to preserve source locations,
version scope, and uncertainty boundaries where active sources omit a behavior
needed to interpret the subject.

## If a rendered artifact exists: rendered document

Ensure the artifact is successfully compiled or rendered through the active
build workflow, then inspect the actual output. Check page breaks (chapter-like
titles start a page when the format requires it), first-line indent after
headings, heading gaps, orphaned headings, overflow, font fallback,
math, tables, figures, captions, cross-references, citation resolution, and
image readability. Correct the source and rerender until the observed artifact
matches the requested template and no material layout defect remains.

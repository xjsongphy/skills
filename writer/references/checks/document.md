# Document checks

These are deterministic release gates, not isolated reviewer roles. Run only
the sections whose trigger is active; do not use this file to create a second
writing or evidence policy.

## Always: prose

Apply `../common/writing.md` and the active type/format modules as a
deterministic pass/fail gate. Pass only when sections have clear purposes,
paragraphs have one principal job, and formulas, code, figures, tables, and
lists have contextual prose and local interpretation. Confirm that required
definitions precede use and that conclusions follow the established evidence
without introducing new results.

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

When a rendered artifact is requested, compile it successfully and inspect the
actual output. Check page breaks, orphaned headings, overflow, font fallback,
math, tables, figures, captions, cross-references, citation resolution, and
image readability. Correct the source and rerender until the observed artifact
matches the requested template and no material layout defect remains.

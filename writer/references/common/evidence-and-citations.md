# Evidence and citations

This file is the single canonical owner of source identity, claim-ledger, and
citation policy. Narrative style belongs to `writing.md`.

## Claim ledger contract

When a document makes source-dependent claims, maintain a compact working ledger
with one row per substantive claim:

```text
claim → evidence source → source location → evidence kind → confidence/boundary
```

The ledger is object-independent infrastructure. Active object policies define
the allowed evidence kinds, source locations, version scope, and unknown
boundary; a lens may ask a question but does not define source categories. The
ledger supports source review and claim checks, but is not copied into
reader-facing prose.

Use the strongest available primary source. Keep these identities distinct:

1. what a paper, handout, dataset, or other source states;
2. what an identified official implementation does;
3. a clearly labeled explanatory inference or simplification.

Third-party material may provide background or a comparison point when the
active object policy permits it. It does not upgrade an interpretation into a
claim made by the active primary source. Official project material is also a
separate source record unless the active object policy explicitly treats it as
part of the source scope.

Do not let a later code revision silently redefine a paper's evaluated method.
Do not create citations, bibliographic fields, data values, results, or source
locations. If a source does not establish an operational detail, omit it or
state the narrowest useful `not specified` boundary.

Treat source-specific operational disclosure as closed-world. A diagram arrow
or high-level verb establishes only the relation shown. Do not infer schemas,
defaults, state lifetimes, prompt fields, ranking operations, filters, or failure
paths. When a central question matters but the active sources are silent, retain
the smallest useful `not specified` boundary.

Place citations beside the claim they support. A citation must support the
nearest claim's scope, comparator, conditions, and strength; a broad method
citation does not prove an undisclosed API, default, state lifetime, filter, or
ranking rule.

Do not fabricate unavailable source identities, locations, APIs, configuration,
or implementation behavior. When source material is incomplete, use only its
disclosed algorithms, figures, appendices, and clearly labeled pseudocode.

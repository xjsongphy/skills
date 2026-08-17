# Explanation

Use for a standalone explanation that lets the target reader understand an
active subject without constantly returning to its sources. The subject may be
a paper, repository, experiment, theorem, system, or a paper/repository pair.
Load `../common/evidence-and-citations.md`, the active object policy, and the
generic reviewer roles when their respective phases are reached. Add
`../lenses/mechanism-analysis.md` or `../lenses/derivation-analysis.md` only
when the subject requires them.

## Evidence model

Audit each active source according to its object policy. Build a working claim
ledger for each central operational claim with: claim, identity (source,
implementation, inference, or `not specified`), exact evidence location, and
permitted wording. Do not turn the ledger into reader-facing prose.

Treat source-specific operational disclosure as closed-world. A diagram arrow
or high-level verb establishes only the relation shown. Do not infer schemas,
defaults, state lifetimes, prompt fields, ranking operations, or failure paths.

## Content and workflow

Center the explanation on the concrete question or problem, the shortest
complete overview, one end-to-end mechanism or reasoning chain, design rationale
and trade-offs, then decisive evidence and limitations. Background and result
tables support that chain; they do not displace it.

Before drafting, set `subject`, `audience_contract`, `assumed_known`, and
`explain_in_draft`. Subject-specific names, symbols, components, state, and
prompts always belong in the latter. Explain every central component as
disclosed:

`producer → input → selection/transformation → state/update → output → consumer`.

Introduce and interpret visuals locally. For a source-faithful prompt, schema,
algorithm, or decisive code artifact, show the material that determines behavior
and label any omitted portions. Label explanatory pseudocode or diagrams as
such; never present a reconstruction as source material.

Run a source-grounded Reviewer pass against all active object policies, fix its
blocker and major findings, then run a draft-only Reader pass and fix unresolved
P0/P1 issues. Do not use source knowledge to silently repair a Reader gap.

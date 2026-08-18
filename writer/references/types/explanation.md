# Explanation

Use for a standalone explanation that lets the target reader understand an
active subject without constantly returning to its sources. The subject may be
a paper, repository, experiment, theorem, system, or a paper/repository pair.
Load `../common/narrative.md`, `../common/evidence-and-citations.md`, the active
object policy, and the relevant analysis modules. Reviewer and check
activation follows the writer routing contract. Add
`../lenses/mechanism-analysis.md` or `../lenses/derivation-analysis.md` only
when the subject requires them.

Unless the user specifies another audience, target an informed but ordinary
reader in the active subject's relevant subfield. Record the audience contract
as `assumed_known` and `explain_in_draft`; never put subject-specific names,
symbols, modules, prompts, or state transitions in `assumed_known`.

## Evidence model

Audit each active source according to its object policy and use the shared claim
ledger. Do not redefine ledger fields or source identities here, and do not turn
the ledger into reader-facing prose.

## Content and workflow

Center the explanation on the concrete question or problem, the shortest
complete overview, one end-to-end mechanism or reasoning chain, design rationale
and trade-offs, then decisive evidence and limitations. Background and result
tables support that chain; they do not displace it.

For a paper or source-grounded technical explanation, keep the contribution or
central question at the center. Background and related work establish only the
needed context; experiments explain setup, fairness, decisive trends,
counterexamples, and limits rather than transcribing result grids.

### Prerequisite mode

Activate prerequisite mode when the user requests background knowledge or when
an omitted concept would make the main argument unreadable. Add only the
smallest concept chain needed by the first dependent section, place it before
that section, and add the concepts to `explain_in_draft` while reducing
`assumed_known`. Do not turn the explanation into an unrelated textbook.

Before drafting, set `subject`, `audience_contract`, `assumed_known`, and
`explain_in_draft`. Subject-specific names, symbols, components, state, and
prompts always belong in the latter. When `mechanism-analysis` is active,
explain every central stage as disclosed:

`producer → input → selection/transformation → state/update → output → consumer`.

Audit all available figures and tables before selecting visuals. Introduce and
interpret selected visuals locally. For a source-faithful prompt, schema,
algorithm, or decisive code artifact, show the material that determines behavior
and label any omitted portions. Label explanatory pseudocode or diagrams as
such; never present a reconstruction as source material.

Follow the reviewer and check activation contract in `../../SKILL.md`. Do not
use source knowledge to silently repair a Reader gap.

# Writer maintenance map

This file is the maintenance index for the modular writer skill. Update the
smallest canonical module that owns a rule; do not patch `SKILL.md` with a
local exception when a type, lens, object, domain, format, reviewer, or check
already owns the concept.

## Placement decision

| Feedback or rule | Canonical location |
|---|---|
| Shared narrative wording | `references/common/narrative.md` |
| Claim ledger, source identity, evidence boundaries, or citation policy | `references/common/evidence-and-citations.md` |
| What the deliverable is and who reads it | one file under `references/types/` |
| A bounded type variant or component | `references/type-addons/`, e.g. `type-addons/report-experiment.md` |
| Cross-type questions about derivations or mechanisms | `references/lenses/` |
| What a paper or repository can prove | `references/objects/` |
| Domain-specific terms, metrics, or evidence | `references/domains/` |
| Markdown, LaTeX, or Typst source syntax | `references/formats/` |
| Irreducible type-format/package interaction | `references/format-integrations/` |
| Isolated agent role and verdict/output contract | `references/reviewers/` |
| Deterministic release or rendering gate | `references/checks/` |
| Routing, module selection, and hard boundaries | `SKILL.md` |

## Updating from feedback

When `/update-skill writer` is invoked:

1. Read the feedback and identify whether it concerns a type, type add-on, lens,
   object, domain, format, format integration, reviewer, check, or routing rule.
2. Read this file and the target canonical module before editing.
3. Update only that module unless the feedback exposes a cross-module contract;
   in that case update the canonical module first, then the smallest routing or
   link change needed to keep the contract discoverable.
4. Search for stale links, duplicate wording, and old skill names. During the
   migration window, retain only thin compatibility wrappers for old user
   entry points; wrappers may route and set defaults but may not own rules.
5. Validate frontmatter, referenced paths, and relevant eval assertions. Compile
   or render only when the changed module affects source or layout.

Use the module map in `SKILL.md` as the public index. Keep this file procedural
and short; detailed writing rules belong in the referenced modules. Narrative
rules are defined in `references/common/narrative.md`. The shared claim ledger,
source identity, and citation contract are defined in
`references/common/evidence-and-citations.md`; objects define how their
evidence fills it, and reviewers/checks consume it.

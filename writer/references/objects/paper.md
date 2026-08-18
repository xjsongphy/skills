# Paper source object

Load this object when a paper is an active evidence source. It defines paper
evidence boundaries; `types/explanation.md` defines the prose deliverable.

## What the paper can establish

Use the paper body, figures, tables, appendix, and supplement first for the
stated problem, method, equations, experiments, and conclusions. Project
metadata, errata, and a paper's identified supplement may clarify source
identity and scope. Record exact section, figure, algorithm, table, or page
locations for central claims. A diagram arrow or high-level verb establishes
only the relation shown.

When the paper directly identifies author or project material, official slides,
talks, project pages, release notes, and errata may clarify terminology, source
scope, or implementation context. Keep those records distinct from the paper's
evaluated claims; inspect an actual repository or runtime artifact under
`objects/repository.md` when implementation behavior matters. Third-party
articles, tutorials, and background sources may support context or comparison,
but cannot establish what the paper itself states.

Treat undisclosed schemas, defaults, prompt fields, state lifetimes, ranking
operations, filters, and failure paths as `not specified` unless the paper or
its identified supplement establishes them.

## Claim ledger mapping

For claims supported by this object, populate the shared ledger with:

- the paper section, figure, algorithm, table, appendix, supplement, or page;
- the paper's stated or directly shown scope;
- the narrowest supported wording and any `not specified` boundary.

If a paper points to an official artifact and that repository, source, config,
test, or runtime behavior is actually inspected, activate
`objects/repository.md` as well. `paper.md` does not define repository/code
evidence semantics. Do not use repository evolution or a project website to
silently rewrite what the evaluated paper method said; when paper and
implementation conflict, preserve both source records and report the conflict.

# Repository source object

Load this object when an official repository, configuration, test, runtime
trace, or commit is an active evidence source. Repository evidence explains
implementation behavior; it does not retroactively become a paper fact.

## Evidence order

Prefer source code, configuration, tests, generated artifacts, and reproducible
runtime observations. Use README files and official project pages for stated
interfaces and version context. Record repository path, line or symbol, commit
or release, and observation conditions for central claims.

## Claim ledger mapping

For claims supported by this object, populate the shared ledger with:

- repository path, symbol or line, commit/release, and observation conditions;
- the artifact kind: source, configuration, test, generated artifact, or runtime
  observation;
- the narrowest implementation wording and any version or uncertainty boundary.

## Boundaries

- Label implementation details explicitly and keep them separate from paper
  claims.
- Do not infer runtime behavior from a name, comment, README slogan, or common
  framework convention when source or observation is available.
- Distinguish current repository behavior from the version used in a paper.
- Preserve unknowns as `not specified`; do not fill missing defaults, state
  lifetimes, filters, or error paths from intuition.
- With both `paper` and `repository` active, ask the source reviewer to check
  agreement, divergence, and version scope explicitly.

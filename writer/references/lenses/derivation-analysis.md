# Derivation-analysis lens

Load this lens when formulas or proofs carry the argument of a report,
explanation, or textbook. It governs the narrative of a derivation; the active
format module governs Markdown, LaTeX, or Typst syntax.

## Derivation contract

1. State the target quantity, assumptions, and applicability conditions before
   manipulating symbols.
2. Define every symbol near first use and keep notation stable across steps.
3. Explain why the next transformation is valid before displaying it. Preserve
   intermediate equalities that carry a non-obvious idea or dimension check.
4. Name intermediate results when later steps depend on them; distinguish a
   definition, lemma, approximation, identity, and conclusion.
5. After the derivation, reconnect the result to the physical or algorithmic
   question, units, limiting cases, and evidence boundary.

Do not invent omitted proof steps or silently upgrade an intuitive argument to
a theorem. If a source gives only a result or sketch, label the reconstruction
as explanatory and retain `not specified` where the source leaves a gap.

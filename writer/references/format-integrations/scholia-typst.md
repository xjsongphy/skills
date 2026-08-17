# Scholia + Typst format integration

Load only when the document uses the Scholia Typst package. This integration owns
the package interaction, not general Typst syntax or explanation/report prose.

Pin the requested Typst Universe release explicitly (for the initial integration,
`@preview/scholia:0.1.0` when that is the project version) and compile a small
smoke document before integrating it into the full artifact. Use the package's
native formal constructs for `definition`, `theorem`, `lemma`, `proposition`,
`corollary`, `proof`, `example`, and `remark`; use native Typst labels and `@`
references for cross-references. Confirm the pinned package API rather than
assuming LaTeX environment names or syntax.

Check stable numbering, labels and `@` references, page breaks around formal
blocks, bibliography output, and the interaction between package styling and
local `#set`/`#show` rules. Keep package-specific calls here; keep general
Typst syntax in `formats/typst.md` and derivation narrative in
`lenses/derivation-analysis.md`.

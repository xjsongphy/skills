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

## Book layout after `scholia.with`

`prose: "book"` is not a Chinese textbook layout. In `@preview/scholia:0.1.0` it
sets first-line indent to `1.2em` without indenting the paragraph after a
heading, treats level-1 headings as in-page sections (number + title + rule,
`block(above: 20pt, below: 8pt)`), and sets level-2/3 gaps to about `11pt` /
`0.5em` and `8pt` / `0.5em`. Those heading shows *replace* the heading with a
new `block`, so a later `#show heading: set block(above, below)` does not
change the gap.

After `#show: scholia.with(...)`, apply the document layout in
`formats/typst.md` by redefining `#show heading.where(level: 1|2|3)`: weak
pagebreak on level 1, visible above/below on sections and subsections, and skip
the printed `0` when `it.numbering == none` (preface, contents, bibliography).
Keep `#set par(first-line-indent: (amount: 2em, all: true))` for Chinese body
text. Disable indent on outline, bibliography, and lists; inside
`figure.where(kind: "frame")` use `all: false` so the knot title line stays
flush. Each `#include`d chapter must `#import "@preview/scholia:0.1.0": *`
itself.

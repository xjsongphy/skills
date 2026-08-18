# Typst syntax

Use this module only for Typst language and source syntax. Load a document-type
module separately for report, paper, or textbook writing rules. The guidance is
organized for current Typst 0.15.x syntax and follows the useful separation used
by mature Typst agent skills: basics, styling, mathematics, structured content,
and modules.

## Three modes

Typst source normally starts in **markup mode**. A `#` enters **code mode** for
expressions, bindings, functions, and commands. Dollar delimiters enter
**math mode**. Return to markup after the code expression or closing math
delimiter.

```typst
= Markup heading
This is *bold*, _italic_, `inline code`, and a [link].

#let twice(x) = x * 2
The result is #twice(3).

Inline math is $a^2 + b^2 = c^2$.
$ sum_(i=1)^n i = (n(n+1))/2 $
```

Do not write LaTeX commands in markup. Use Typst's own markup, code, and math
forms; use a conversion strategy only when the user explicitly asks for one.

## Markup essentials

- `=`, `==`, `===` create heading levels.
- `*text*` is bold and `_text_` is italic.
- `` `code` `` is inline raw text; fenced raw blocks can name a language with
  the `python` info string.
- `- item` creates an unordered list; `+ item` creates an ordered list.
- `/ Term: explanation` creates a terms-style list when that structure is
  appropriate.
- `#emph[content]`, `#strong[content]`, and `#underline[content]` are code-mode
  functions for explicit text styling.
- `\` followed by a markup character escapes that character when literal text is
  needed, for example `\#`.

Prefer semantic markup and functions over manually inserted spacing or repeated
layout characters.

## Values, bindings, and functions

Use `#let` for bindings and functions. Arrays use `(a, b, c)`, dictionaries
use `(key: value, other: value)`, and named arguments use `key: value`.
Access fields with `.field`, index collections with `[index]`, and use `#if`,
`#else`, and `#for` for control flow.

```typst
#let author = (name: "Ada", affiliation: "Example Lab")
#let names = ("Ada", "Grace")
#let label(name, year: none) = [#name#if year != none [ (#year)]]

#for name in names [• #name ]
#label(author.name, year: 1843)
```

Keep code expressions in `#(...)` or `#{...}` when a block contains multiple
statements. Use `return`, `if`, `for`, `while`, and `context` only in code mode.

## Set and show rules

Use `#set` to change defaults for an element and `#show` to redefine how an
element renders. A `#set` rule affects later content in its scope; a `#show`
rule can match an element or selector and transform it.

```typst
#set page(paper: "a4", margin: 2cm)
#set text(font: ("Libertinus Serif", "Noto Serif"), size: 10.5pt)
#set heading(numbering: "1.1")

#show heading.where(level: 1): it => {
  set text(weight: "bold", size: 16pt)
  it
}
```

Keep reusable style in scoped `#set`/`#show` rules and reusable components in
`#let` functions. Do not encode a style system by copying formatted fragments.

## Math syntax

Use `$...$` for inline or display mathematics. Spaces inside the delimiters
make a display expression. Subscripts use `_`, superscripts use `^`, fractions
use `/` with grouping, and aligned equations can use `&` and a single `\` for
alignment and line breaks inside a matrix or aligned structure.

```typst
$ x_i^2 $
$ (a + b) / (c + d) $
$ mat(1, 0; 0, 1) $
```

Use Typst symbols and functions in math mode; do not assume every LaTeX macro
has a direct name. Define symbols in surrounding prose before presenting a
formula when the document type requires it.

## Figures, tables, and references

Use `#figure` with `image`, `table`, or another block as its body. Put a
`<label>` after the element and refer to it with `@label`. Use `#table` for
structured cells and `table.cell`/`table.hline` when spans or rules are needed.

```typst
#figure(
  image("figures/setup.png", width: 80%),
  caption: [Experimental setup.],
) <fig:setup>

See @fig:setup for the apparatus layout.

#table(
  columns: (auto, 1fr),
  [Variable], [Value],
  [Mass], [$m$],
)
```

Use a bibliography file with `#bibliography("refs.bib")` and cite a key with
`@key`. Keep labels stable and use references instead of manually typed figure,
table, section, or equation numbers.

## Imports and packages

Use `#import "path.typ": item` to import selected definitions and
`#include "section.typ"` to include another source file's content. Use
`#import "@preview/name:version": item` for a Typst Universe package when its
version and API are known. Keep package and local module boundaries explicit;
do not silently replace a project template with a similarly named package.

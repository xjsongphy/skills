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

## Document layout

The prose and academic-table defaults below describe long-form documents.
For teaching slides, let the slide theme and
`../format-integrations/teaching-slides-typst.md` own frame geometry, headings,
paragraph indentation and table styling; do not apply book-layout overrides.

Put page, paragraph, and heading policy in one document-level `#set`/`#show`
cluster. Do not insert blank lines, `#v(...)`, or per-chapter spacing to fake
chapter breaks or heading gaps.

Typst has no heading page-break field. Start a new page at chapter-like titles
with `#show heading.where(level: 1): it => { pagebreak(weak: true); it }`.
Control heading gaps with `#show heading.where(level: n): set block(above: …,
below: …)` and `sticky: true` on non-chapter headings. If a later package
`#show heading` replaces the heading with its own `block`, that `set block`
rule no longer applies; override the heading show after the package wrapper
(see `format-integrations/scholia-typst.md` when Scholia is active).

For Chinese long-form body text, use two-character first-line indent on every paragraph,
including the first paragraph after a heading:

```typst
#set par(first-line-indent: (amount: 2em, all: true), justify: true)
```

`all: false` (Typst’s default) leaves that first paragraph flush. Turn paragraph
first-line indent off for outlines, bibliographies, lists, and tables. In Chinese
lecture notes, indent unordered list markers and their items together by `2em`
using `#set list(indent: 2em)`, with continuation lines aligned to item text;
do not add a separate paragraph first-line indent inside list items. Headings must not inherit
the body indent. For CJK documents, set `lang` and a font list that actually
provides the needed weights; Songti SC has no usable bold, so map `#show strong`
to PingFang SC or another sans.

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

Give a numbered display equation a label after the math block and refer to it
with `@eq:name`:

```typst
$ F = k x $ <eq:hooke>

如 @eq:hooke 所示，恢复力与位移成正比。
```

Style tables like ruled academic tables: `table.hline` for the top, header,
and bottom rules (booktabs style, no vertical rules), `table.header` for the
header row, and a fixed number of decimal places in each numeric column so
values stay comparable. Keep table width appropriate to content. Put units in
the column header (`T (°C)`, `$V_"D0"$ / V`), not in every cell.

Build multi-panel figures as a `grid` of panels inside one `#figure` with a
shared caption; label each panel `(a)`, `(b)` in its top-left corner or
caption line. Size each panel between 0.3 and 0.8 of the text width so its
labels stay legible.

## Imports and packages

Use `#import "path.typ": item` to import selected definitions and
`#include "section.typ"` to include another source file's content. An included
file does not inherit the parent’s `#import` or `#let` bindings; each chapter
file that uses those names must import them itself. Use
`#import "@preview/name:version": item` for a Typst Universe package when its
version and API are known. Keep package and local module boundaries explicit;
do not silently replace a project template with a similarly named package.

## Code blocks and CJK fallback

Raw text uses the document's mono font list. In a Chinese document, a Latin-only
stack (`Menlo`, `DejaVu Sans Mono`) leaves Chinese comments to the body CJK
fallback, which is often a serif such as Songti SC; comments then read like
prose rather than code. Add an installed CJK sans to the raw stack:

```typst
#show raw: set text(font: ("Menlo", "PingFang SC", "DejaVu Sans Mono"))
```

Set inline raw to body size so API names in prose do not shrink:

```typst
#show raw.where(block: false): set text(size: 1em)
```

For Scholia documents, set the same stack through `fonts.mono` instead; see
`../format-integrations/scholia-typst.md`.

Give block code a quiet full-width background so fragments do not merge with
prose. Use a light fill, rounded corners, and padding; keep this separate from
the inline-code pill, which stays at text size.

```typst
#show raw.where(block: true): it => block(
  width: 100%,
  fill: rgb("#F6F8FA"),
  inset: (x: 10pt, y: 8pt),
  radius: 3pt,
  above: 8pt,
  below: 8pt,
  it,
)
```

## Callout boxes and internal spacing

A callout with smaller text than body prose needs its own spacing scale. To make
line and paragraph gaps visually equal, keep `spacing` slightly below `leading`;
at 10.5pt, `leading: 1.35em` with `spacing: 1.15em` matches the body's rhythm.
Use `first-line-indent: 2em` to keep paragraph boundaries visible, and
`list(indent: 1.2em, spacing: 1em)` with
`#show list: set par(first-line-indent: 0em)` so list items do not inherit the
indent. Do not use a larger paragraph spacing for callouts; the gap then reads
as a separate block.

Give the title explicit space rather than a bare `#parbreak()`:

```typst
#text(font: "PingFang SC", size: 10pt, fill: rgb("#6B7686"))[Title]
#v(10pt)
#body
```

Render a box containing a title, two paragraphs, and a two-item list; inspect
the title gap, inter-paragraph gap, inter-item gap, and the gap after the list
as one spacing system. Keep the box's line leading close to the body's so the
smaller text does not look denser than the surrounding page. Keep short callouts
unbreakable (`breakable: false`); moving the whole box to the next page is better
than splitting its title from its body.

## API entry boxes

Give each API entry a full-width signature box with a light fill and a top rule,
then the summary, then a two-column parameter block: the bold `参数：` label sits
at the body indent and the list starts in a separate right-hand column. Do not
stack the label and list at the same left edge, and do not tighten the list into
a paragraph.

Format the text inside the parameter block, not just its geometry. Parameter
names take the accent color in regular-weight monospace; the input/output
annotation is italic and muted, and literal identifiers in descriptions use
inline code with a tinted background. Monospace text looks larger than CJK at
the same point size, so set the signature to `0.9em` to match the body's apparent
size; keep parameter text at body size. Set list item spacing to about `1.3em`
so a wrapped continuation and the next item keep the same baseline distance;
the usual body list spacing makes wrapped lines bunch against the next item.
Inline code stays at `1em` in regular weight with about 3.5pt of horizontal
padding inside the highlight, so it never touches the surrounding characters.
Do not wrap inline code in a box that raises the line height, or the parameter
rows will have visibly different gaps. Do not bold the signature, parameter names, or inline code; the box, top rule,
color, and background already distinguish them, and extra weight reads as a
separate tier.

```typst
#let api(signature) = block(
  width: 100%, above: 1.4em, below: 1.2em,
  fill: rgb("#EAF2FB"), stroke: (top: 2.5pt + rgb("#2F5EA8")),
  inset: (left: 12pt, right: 12pt, top: 12pt, bottom: 12pt),
)[
  #set par(first-line-indent: 0em, justify: false)
  #text(font: ("Menlo", "PingFang SC"), weight: "regular", size: 0.9em)[#signature]
]

#let api-name(name) = text(
  font: ("Menlo", "PingFang SC"),
  fill: rgb("#2F5EA8"),
  weight: "regular",
)[#name]

#let api-dir(body) = text(style: "italic", fill: rgb("#6B7686"))[（#body）]

#let api-params(body) = block(
  width: 100%, above: 1em, below: 1.2em,
  inset: (left: 2em),
)[
  #table(
    columns: (auto, 1fr),
    column-gutter: 3em,
    stroke: none,
    inset: (x: 0pt, y: 0pt),
    align: (left + top, left + top),
    [*参数：*],
    [
      #set par(first-line-indent: 0em, spacing: 1.15em, justify: false)
      #set list(indent: 0.5em, spacing: 1.3em)
      #show raw.where(block: false): it => highlight(
        fill: rgb("#EBEEF2"),
        radius: 3pt,
        extent: 2pt,
        text(
          font: ("Menlo", "PingFang SC"),
          size: 1em,
          weight: "regular",
          fill: rgb("#414B5A"),
        )[#h(3.5pt)#it.text#h(3.5pt)],
      )
      #body
    ],
  )
]
```

Write a parameter line as `- #api-name[comm]#api-dir[输入]：通信器。`; multiple
names repeat `api-name`. Set the signature block to `justify: false`; long
signatures otherwise stretch. Escape `*` and leading `__` in C signatures, or
Typst will parse them as markup. Render a long signature and a list of eight
parameters; confirm the box wraps without clipping, the two parameter columns
stay aligned, and the color, italic annotation, and inline-code background all
survive on continuation lines.

## Source-first review

Check content, terminology, duplicated passages, markup, and cross-references in
the `.typ` source. Compile and inspect rendered pages only for layout: page
breaks, heading and paragraph spacing, overflow, font fallback, and callout
geometry. Do not transcribe or proofread content from page images.

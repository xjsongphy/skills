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
text. Disable paragraph first-line indent on outline, bibliography, and lists;
apply the unordered-list marker indent in `formats/typst.md`. Inside
`figure.where(kind: "frame")` use `all: false` so the knot title line stays
flush.

For a Chinese textbook, separate ordinary figure captions from Scholia's
formal blocks. `frame-it` implements a definition/theorem/example as a
`figure(kind: "frame")` and uses `figure.caption` as an internal transport
object. Therefore a global caption `set text` rule placed after
`scholia.with(...)` leaks the caption font and size into the body of every
formal block.

Register the ordinary-caption rule **before** `scholia.with(...)`, and let
frame-it metadata pass through unchanged. The following is the tested house
style: captions are 9.5pt gray KaiTi; formal-block body text remains the body
font and 11.5pt.

```typst
#import "@preview/scholia:0.1.0": *
#import "macros.typ": *

#let frame-it-marker = "_THIS-IS-METADATA-USED-FOR-FRAME-IT-FRAMES"
#let is-frame-caption(body) = {
  if body == none or "children" not in body.fields() {
    false
  } else {
    let first = body.children.first()
    if first == none or "value" not in first.fields() {
      false
    } else {
      let value = first.value
      value != none and value.len() > 0
        and value.at(0, default: none) == frame-it-marker
    }
  }
}
#show figure.caption: it => {
  if is-frame-caption(it.body) {
    it
  } else {
    text(
      font: ("Kaiti SC", "Songti SC", "Optima", "Libertinus Serif"),
      size: 9.5pt,
      fill: rgb("#6B7686"),
    )[ #it ]
  }
}

#show: scholia.with(...)

#show figure.where(kind: "frame"): set block(
  above: 16pt,
  below: 16pt,
)
#show figure.where(kind: "frame"): set par(
  leading: 1.25em,
  spacing: 0.9em,
  first-line-indent: (amount: 2em, all: false),
)
```

The `figure.where(kind: "frame")` selector preserves Scholia's box styling and
only increases the gap from surrounding prose. Do not patch the Typst package
cache. Do not place an unconditional `#show figure.caption: set text(...)`
after `scholia.with(...)`, and do not replace Scholia's later caption show with
a custom function: either choice can make formal-block bodies inherit the
caption style or prevent frame reconstruction. Render at least one ordinary
figure caption and one formal block after changing these rules.

## Default layout for Chinese lecture notes and textbooks

For a new Typst course handout, lecture note, or textbook using Scholia, use
this established book layout, derived from the user's differential geometry
handout and adjusted to give section headings balanced space above and below.
It provides actual settings, rather than relying on Scholia's book defaults. Respect explicit user direction and an existing project template;
use a suitable installed substitute if a named font is unavailable and verify
the rendered result. Keep the normal-caption rule from the preceding section
before `scholia.with`; do not import an unrelated `macros.typ` merely to apply
this layout. The package's A4 page and marginalia defaults remain in effect.

```typst
#show: scholia.with(
  prose: "book",
  fonts: (
    body: ("Songti SC", "STIX Two Text", "Libertinus Serif"),
    heading: ("Kaiti SC", "Songti SC", "Optima", "Libertinus Serif"),
    sans: ("PingFang SC", "Avenir Next", "Libertinus Serif"),
  ),
)

#set text(lang: "zh", size: 11.5pt)

// 版式：Typst 对段落与标题的统一接口。
// scholia 的 book 主题把一级标题当节排、间距偏紧，且标题后首段默认不缩进；
// 下面用 #set par / #show heading 覆盖这三件事。
#set par(
  leading: 1.35em,
  spacing: 1.15em,
  first-line-indent: (amount: 2em, all: true),
  justify: true,
)
#show outline: set par(first-line-indent: 0em)
#show bibliography: set par(first-line-indent: 0em)
#set list(indent: 2em)
#show list: set par(first-line-indent: 0em)
#show enum: set par(first-line-indent: 0em)
#show table: set par(first-line-indent: 0em)
// Scholia formal blocks：frame-it 默认上下各 10pt；教材版增加留白，
// 让定义、定理、例题框与相邻正文形成清晰的视觉段落。
#show figure.where(kind: "frame"): set block(
  above: 16pt,
  below: 16pt,
)
#show figure.where(kind: "frame"): set par(
  leading: 1.25em,
  spacing: 0.9em,
  first-line-indent: (amount: 2em, all: false),
)

#let heading-font = ("Kaiti SC", "Songti SC")
#let heading-blue = rgb("#2F5EA8")
#let heading-teal = rgb("#0F766E")
#let heading-muted = rgb("#6B7686")

#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  counter(figure.where(kind: "frame")).update(0)
  block(breakable: false, above: 0.3em, below: 1.35em, width: 100%)[
    #if it.numbering != none {
      text(font: heading-font, weight: "bold", size: 11pt, fill: heading-muted)[#counter(heading).display()]
      h(0.7em)
    }
    #text(font: heading-font, weight: "bold", size: 16pt, fill: heading-blue)[#it.body]
    #v(0.45em)
    #line(length: 100%, stroke: 1.1pt + heading-blue)
  ]
}
#show heading.where(level: 2): it => block(
  breakable: false,
  sticky: true,
  above: 1.4em,
  below: 1.4em,
  width: 100%,
)[
  #set par(first-line-indent: 0em)
  #text(font: heading-font, weight: "bold", size: 13pt, fill: heading-teal)[
    #if it.numbering != none [#counter(heading).display() ]
    #it.body
  ]
]
#show heading.where(level: 3): it => block(
  breakable: false,
  sticky: true,
  above: 1.4em,
  below: 1.4em,
  width: 100%,
)[
  #set par(first-line-indent: 0em)
  #text(font: ("PingFang SC", "Kaiti SC"), weight: "semibold", size: 12pt, fill: heading-blue)[
    #if it.numbering != none [#counter(heading).display() ]
    #it.body
  ]
]

// Songti SC 没有足够重的粗体，概念加粗改用苹方。
#show strong: it => {
  set text(font: ("PingFang SC", "Heiti SC", "Songti SC"), weight: "medium")
  it
}

```

The `heading-font` and three heading shows above are the canonical heading
style: chapter number in muted 11pt, title in blue 16pt with a rule; level 2
in teal 13pt with 1.4em above and below; level 3 in blue 12pt with
1.4em above and below. Body text is 11.5pt with 1.35em leading and 1.15em
paragraph spacing. Adjust content-specific details such as cover, figures,
and chapter names independently. Render representative headings, body text,
ordinary captions and a Scholia formal block, and inspect pagination after
applying the style.

The older differential geometry reference uses asymmetric level-2 gaps of
1.85em above and 0.95em below (and level-3 gaps of 1.4em / 0.8em). The
balanced values above are the newer user preference, not an exact copy of that
older file. Inspect the *rendered* gaps between a heading and adjacent body
text: font metrics, neighboring blocks, and page boundaries affect the visible
space. For a heading between ordinary paragraphs, target visually balanced
space; do not force equal gaps at page boundaries or after large figures.
Keep level-specific font and size choices unless the document intentionally
maps a different structural level to the reference's appearance.

## Proof spacing and body typography

Scholia 0.1.0's native `proof` component uses `above: 6pt` and `below: 8pt`
and leaves the proof body text implicit. In a Chinese textbook with body
paragraph spacing `1.15em`, the QED-to-next-paragraph gap therefore looks
visibly tighter. A classic textbook distinction also lightens the proof body:
same size as body prose, one weight step thinner. Songti SC ships a Light
face, so `weight: "light"` genuinely thins the strokes; verify this with a
large-size side-by-side test render before trusting it, because a family
without a Light face silently falls back to regular. Keep the `#proof[...]`
call syntax, but shadow the imported component in the shared local macro file,
which is imported after Scholia in each chapter:

```typst
#import "@preview/scholia:0.1.0": active

#let proof(body) = context {
  let p = active.get()
  block(above: 6pt, below: 1.15em)[
    #text(
      font: ("Kaiti SC", "Songti SC", "STIX Two Text", "Libertinus Serif"),
      style: "italic",
      fill: p.muted,
    )[Proof.]
    #h(0.4em)
    #set text(
      font: ("Songti SC", "STIX Two Text", "Libertinus Serif"),
      size: 11.5pt,
      weight: "light",
      fill: p.ink,
    )
    #body
    #h(1fr)
    #box(
      baseline: 1pt,
      rect(width: 6pt, height: 6pt, fill: p.thm, stroke: none, radius: 0.5pt),
    )
  ]
}
```

Use the document's actual body font list and size in this override rather than
assuming Scholia's defaults; the proof body keeps the body size and ink colour
and differs only by `weight: "light"`. The `below` value should track the
document's paragraph spacing. Do not modify the package cache; after the
override, render a proof whose QED mark is followed by ordinary prose and
compare stroke weight and vertical gap against adjacent body paragraphs. Each
`#include`d chapter must `#import "@preview/scholia:0.1.0": *` itself.

## Code blocks with Chinese comments

Scholia applies `show raw: set text(font: f.mono)`, and `f.mono` defaults to
`("Menlo", "DejaVu Sans Mono")`. Both faces lack Chinese glyphs, so Chinese
comments fall back to the document's CJK body font, usually Songti SC; at small
sizes they read as prose rather than code.

Add an installed CJK sans to the `mono` stack through the `fonts` override:

```typst
#show: scholia.with(
  fonts: (
    // ...
    mono: ("Menlo", "PingFang SC", "DejaVu Sans Mono"),
  ),
)
```

Latin code keeps Menlo; only missing CJK glyphs fall back to PingFang SC.
Render a code block containing Chinese comments at high resolution, because the
fallback is easy to miss at body size.

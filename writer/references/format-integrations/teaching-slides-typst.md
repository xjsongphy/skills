# Teaching slides + Typst

Load with `../types/teaching-slides.md` and `../formats/typst.md` for Typst
classroom decks. This integration owns slide-theme interaction and the reusable
classroom preset, not lesson prose or algorithm verification.

## Select and reuse a template

An explicit reference deck wins. Inspect its source and rendered pages before
editing. “Use the 1023 style” means locating that actual deck / theme in the
workspace, not choosing a similarly named new theme. Copy the reusable style,
local vendor and license as a unit into the target project; preserve fonts,
page geometry, code highlighting and header/footer conventions. Do not copy
the old lesson content, deleted pages or answer list.

For a similar programming exercise deck without a contrary reference, use the
bundled preset at `../../assets/typst/teaching-slides/` (resolved from this file).
Copy it to the output project's `slides/` directory, then replace the illustrative
content in `starter.typ` and rename it to the project's entrypoint if desired.
The preset is the tested classroom adaptation of Calmly Touying 0.2.0 with
Touying 0.6.1 pinned; its MIT license and upstream metadata remain in `vendor/`.
Keep all relative files together. Do not patch a global Typst package cache.

Preset: 16:9, light Paper colors, minimal header; Arial / PingFang SC body,
Menlo / PingFang SC code; cover 34pt, titles 28pt, body / tables 20pt, code
18pt, page numbers 14pt. These are this classroom preset's choices, not a rule
for unrelated presentations. Use available substitutes if fonts are missing,
and check the rendered fallback. A supplied different template takes priority.

## Frame layout

Use the theme's own page and heading configuration. The book-style paragraph
indent, chapter-page-break, and Scholia defaults do not apply to slides. Do not
load Scholia merely because the deck is Chinese or academic. Keep body text
flush and the theme's code/table styling intact.

Put reusable additions in a local `style.typ`; place lesson sections in separate
files when the deck warrants it. Each included section imports the helpers it
uses. Do not hardcode an absolute personal workspace path into copied assets.
Resolve external figure paths inside the chosen project root, or copy the
needed figures into that project.

One source frame should have one teaching purpose. Move overflow to another
frame instead of lowering the font size. Check the actual title length, code
line length and table cells: matching the number of source lines is not proof
that a frame fits. Keep multiline Python syntactically indented; explicit
line breaks in parentheses are preferable to visual wrapping.

Build execution diagrams as editable Typst tables, grids, or an appropriate
native diagram package. For stepwise examples, keep coordinates and geometry
stable across frames, and vary the current / pending / processed state. Use the
lesson's actual data or a clearly labeled teaching example.

## Build and inspect

Typical commands from the copied `slides/` directory:

```sh
typst compile starter.typ lesson.pdf
typst compile --format png --ppi 110 starter.typ 'review/page-{p}.png'
```

Create `review/` first. If a source reads figures outside `slides/`, set `--root`
to their common project parent. A PDF export is a deck, not a native PPTX;
provide the `.typ` source for edits and preserve a native-format requirement
when one was explicit.

After assembling content, reconcile the frame order / titles with actual PDF
pages, then follow the rendered-image review in the teaching-slides type. A
page manifest is useful for longer decks, but a source heading count alone
does not catch overflow or a stale PDF. Keep contact sheets, build diagnostics,
benchmark metadata and review records outside student-facing pages. Recheck
changed pages after every material revision.

# LaTeX format

Use the supplied class and template before generic guidance. Keep document
semantics in sections, environments, labels, captions, and bibliography entries;
do not force presentation choices into prose.

- Use labels for display equations that will be referenced. Prefer `siunitx`
  for units when the template supports it.
- Give each figure and table a complete caption and stable label. Keep table
  width appropriate to content rather than filling a line by default.
- Use theorem-like environments consistently for textbook material. State
  language and font settings explicitly for CJK documents.
- Keep source files modular when a project has several chapters or sections;
  keep paths portable and references resolvable.

For XeLaTeX compilation, errors, reference resolution, or warnings, invoke the
separate `latex-compile` skill. Compile until cross-references stabilize and
inspect the rendered output when layout matters.

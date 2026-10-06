# LaTeX format

Use the supplied class and template before generic guidance. Keep document
semantics in sections, environments, labels, captions, and bibliography entries;
do not force presentation choices into prose.

- Use labels for display equations that will be referenced. Prefer `siunitx`
  for units when the template supports it.
- Use `\begin{equation}...\label{eq:name}...\end{equation}` for numbered
  display equations, and `\autoref{eq:name}` / `\eqref{eq:name}` (or
  `\autoref{fig:...}`, `\autoref{tab:...}`) for cross-references to
  equations, figures, and tables.
- Prefer a ruled style for tables — `ruledtabular` or booktabs rules — and
  align numeric columns on the decimal point (a `d{a.b}`-style column format
  when the class provides it). Give each figure and table a complete caption
  and stable label. Keep table width appropriate to content rather than
  filling a line by default.
- Build multi-panel figures with `subcaption`/`subfigure`: each panel gets a
  label and a one-line caption, the shared caption states the decisive
  reading. Size each panel between 0.3 and 0.8 `\linewidth` so its labels
  stay legible.
- Use theorem-like environments consistently for textbook material. State
  language and font settings explicitly for CJK documents.
- Keep source files modular when a project has several chapters or sections;
  keep paths portable and references resolvable.

For XeLaTeX compilation, errors, reference resolution, or warnings, invoke the
separate `latex-compile` skill. Compile until cross-references stabilize and
inspect the rendered output when layout matters.

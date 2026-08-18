# Markdown format

Use ordinary Markdown for headings, paragraphs, lists, code, links, tables, and
images. Keep heading depth proportional to the argument; do not create a
heading for every short paragraph.

Use Markdown list, table, code-fence, link, and image syntax as supported by the
target renderer. Cite real source excerpts by portable repository path and line
location where available; label illustrative code and pseudocode explicitly.

For figures, use portable image paths and visible captions where the renderer
supports them. Alt text is accessibility metadata, not a visible caption.

Use Mermaid only when a flow, state transition, or hierarchy is harder to recover
from prose. A four-or-more meaningful-node threshold is a heuristic, not a gate.
Use `graph TD` or `graph LR` according to reading direction, keep node labels
short, put detail in surrounding prose, and use subgraphs only for semantic
groups. Connect subgraphs through their actual nodes. Prefer a plain text tree
for a file hierarchy or simple nesting; if Mermaid styling is used, prefer
stroke-only emphasis over filled decorative nodes.

**Bad:** draw a three-level file tree as Mermaid, or put a dozen sentences into
node labels and explain all of them after several unrelated figures.

**Good:** use a text tree for simple nesting; use a compact `graph TD`/`graph LR`
for a real flow, keep labels to roles or transitions, and explain the decisive
branch immediately after the diagram.

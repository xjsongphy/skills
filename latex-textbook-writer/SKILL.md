---
name: latex-textbook-writer
description: Compatibility entry point. Route LaTeX textbook work through writer with textbook as the primary type and the LaTeX textbook format integration.
---

# LaTeX textbook writer compatibility entry point

Route this request to the canonical `writer` skill with:

```text
primary type: textbook
format: LaTeX
format integration: textbook-latex
```

Activate `type-addons/textbook-exercises` only when exercises are part of the
deliverable. The canonical rules and preserved LaTeX assets live in
`../writer/`; this wrapper owns no textbook rules.

---
name: paper-explainer
description: Compatibility entry point. Route paper explanations through writer with explanation as the primary type and paper as the active source object.
---

# Paper explainer compatibility entry point

Route this request to the canonical `writer` skill with:

```text
primary type: explanation
active object: paper
format: preserve an existing source format; otherwise default to Markdown
```

Load additional lenses, domains, repository objects, reviewers, and format
integrations only when the request requires them. The canonical rules live in
`../writer/`; this wrapper owns no paper-explanation rules.

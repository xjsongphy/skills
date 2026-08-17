---
name: md-report-writer
description: Compatibility entry point. Route Markdown reports through writer with report as the primary type and Markdown as the format.
---

# Markdown report writer compatibility entry point

Route this request to the canonical `writer` skill with:

```text
primary type: report
format: Markdown
```

Add a report type add-on, source object, lens, domain, reviewer, or check only
when the request requires it. The canonical rules live in `../writer/`; this
wrapper owns no Markdown report rules.

---
name: experiment-report-writer
description: Compatibility entry point. Route experiment reports through writer with report as the primary type and the experiment report type add-on.
---

# Experiment report writer compatibility entry point

Route this request to the canonical `writer` skill with:

```text
primary type: report
type add-on: report-experiment
format: preserve an existing source format; otherwise default to LaTeX
```

The canonical rules live in `../writer/`; this wrapper owns no experiment
report rules.

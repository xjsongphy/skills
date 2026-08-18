# Mechanism-analysis lens

Load this lens when a document must explain how a technical system works, not
only what it claims. It can be combined with a report, explanation, or
textbook, and with any active source object.

## Analysis chain

For each central stage, trace the smallest complete chain:

```text
producer → representation/input → selection or transformation
         → state/update → condition or branch → output → consumer
```

For every link, preserve the evidence source and boundary required by the
active object policies. This lens asks what must be explained; it does not
define evidence categories. A generic verb such as “processes”, “retrieves”, or
“optimizes” is insufficient when its hidden input, selection rule, state
lifetime, or output determines the conclusion.

## Required questions

- What object enters the stage, and who produced it?
- What information is visible, filtered, ranked, aggregated, normalized, or
  omitted before the operation?
- What computation or decision changes the object?
- What state is read or updated, and how long does it persist?
- Which conditions choose a branch, reject an item, stop a loop, or consume a
  budget?
- What output is emitted, who consumes it, and why is it sufficient there?
- Which failure, empty-input, disagreement, timeout, or termination paths are
  actually disclosed?
- Which design choice matters, and what simpler alternative or limitation is
  supported by the sources?

Use `mechanism-analysis/depth-checklist.md` for domain-shaped prompts about
agents, memory, retrieval, profiling, compilation, or execution feedback.

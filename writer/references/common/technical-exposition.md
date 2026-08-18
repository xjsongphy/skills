# Technical exposition

Use this module with reader-facing documents when the task requires deciding how
much technical detail to expose and which representation best carries it. It
defines cross-type drafting behavior; `narrative.md` owns sentence shape and
prose style, formats own source-language syntax, and types own deliverable
semantics.

## Clarity before detail

- Prefer the shortest explanation that preserves correctness, needed context,
  and recoverability.
- Do not explain every term, code line, or implementation detail by default.
  Expand when a later claim depends on it, the audience is unlikely to know it,
  the code is non-obvious, or a conclusion depends on a fine distinction.
- Do not repeat the same contribution or conclusion in the introduction, body,
  and summary unless each occurrence performs a different reader-facing job.

## Semantic density

- Give each paragraph one principal idea or one tightly coupled abstraction
  level. A paragraph carrying roughly four or five independent information
  points is a warning signal, not an automatic split instruction.
- Do not split a continuous causal argument mechanically. Instead, move exact
  mappings to a table, parallel conditions to a list, multi-stage flow to a
  diagram or pseudocode block, and mathematical relations to formulas.
- Use prose for causal reasoning and conceptual interpretation; use structured
  elements when their parallel or sequential structure is itself informative.

### Good / bad

**Bad:** one paragraph introduces four components, traces their data flow,
explains a branch, states a lifetime, and interprets an experiment.

**Good:** introduce the component roles first, show the data flow as a compact
diagram or table, explain the branch in a focused paragraph, and interpret the
experiment where its result is introduced.

## Concept before dependence

- Define a core noun, component, quantity, or acronym before analysis, code,
  diagrams, or formulas depend on it.
- Ordinary field terms need not receive standalone definitions. Keep one light
  parenthetical expansion for an acronym, and do not pack several definitions
  into one parenthesis.
- Distinguish a general mechanism from the current project or implementation
  when a survey or explanation moves between them.

**Bad:** “The retriever uses memory” appears before `memory` or the retriever's
selection operation has been defined.

**Good:** define the stored representation and selection step first, then state
how the current implementation uses them and which details remain unspecified.

## Selective code and artifact explanation

- Give code or pseudocode context before the block and its behavioral takeaway
  after it. Short code needs only a concise before/after explanation.
- Explain line-level details only for non-obvious control flow, hidden
  assumptions, state changes, or decisive APIs. Do not use long code or comments
  as a substitute for conceptual explanation.
- Mark illustrative pseudocode and reconstructions explicitly. Source-faithful
  excerpts must follow the active object policy and include a path/line or other
  precise location when available.

**Bad:** paste a long function and expect comments to explain the algorithm.

**Good:** show the few behavior-determining lines, identify their source
location, and explain the input, branch, state change, and output around them.

## Representation choice

Choose the smallest representation that makes the structure recoverable:

- prose for causal chains and interpretation;
- lists for parallel conditions, constraints, or procedures;
- tables for exact repeated mappings or comparisons;
- diagrams for architecture, pipelines, state transitions, or feedback loops;
- pseudocode for complex control flow;
- formulas for mathematical relationships.

Introduce each figure, table, code block, formula, or list with its purpose and
interpret it locally. For formulas that form part of a sentence, use punctuation
that completes the surrounding sentence. This is a prose rule, not a LaTeX-only
syntax rule.

**Bad:** place three figures together and explain them in a later “Figure
discussion” paragraph.

**Good:** state why each selected visual is needed, place it near the relevant
argument, and give its decisive reading immediately afterward.

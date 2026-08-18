# Shared writing rules

This file is shared by writing-oriented skills. Read it when the parent skill
links here; do not copy its rules into individual skills. It combines narrative
style with cross-type technical exposition. Progressive depth is conditional:
use that section only when a survey, explanation, or teaching document needs
layered technical depth.

## Narrative requirements

- Write for the reader's understanding, not to document the agent's research process.
- Start with the subject, mechanism, evidence, or consequence. Remove meta-commentary about what was searched, what the writer intends to do, or what the writer will avoid.
- Do not emit defensive process disclaimers. If a source limitation changes the interpretation, state the concrete limitation at the point where it matters; do not repeat it as a drafting explanation.
- Prefer positive, evidence-bearing sentences over negation-based assurances. State what the source establishes, what the excerpt illustrates, and where the boundary lies.
- Use the field's established term and verify it against the source. Do not coin a non-standard term or import a term from another document unless the current document uses it. If a Chinese rendering is needed, anchor it to the standard term on first use and use one term consistently.

## Contrast economy

Default to direct assertions. Do not use “不是……而是……”, “并非……而是……”,
“而不是……”, “而非……”, “不等于……” or equivalent contrast merely to add
emphasis, announce the writer's process, or restate a fact in negative form.
Rewrite the sentence as a positive description of what the thing is and does.

Keep a contrast only when both conditions hold:

1. The rejected interpretation is genuinely plausible from the immediately
   surrounding text, figure, formula, or common reading.
2. Rejecting it materially changes the reader's understanding of a mechanism,
   evidence boundary, metric, or decision.

## Quotation and sentence shape

Use quotation marks only for direct quotation, the first introduction of a
coined or scoped term, and code/identifier/schema-token references. Do not wrap
colloquial paraphrases, metaphor labels, or long explanatory clauses in quotes.

Every sentence should be grammatically complete and express one clear thought.
Write mechanisms as declarative prose. Do not use rhetorical self-questioning
as a substitute for stating the producer, transformation, output, consumer, or
rationale. Define a component or quantity directly before using an analogy or
contrast to clarify it.

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

## Progressive technical depth

Use this conditional sequence when a survey, paper explanation, or technical
teaching document must move from a readable map to operational detail and then
to the research or implementation-specific layer. It is not mandatory for
every report or textbook.

1. **Reader map**: state the problem, contribution, major objects, and the
   shortest complete end-to-end picture.
2. **Mechanism layer**: expose the representations, transformations, choices,
   state updates, interfaces, and consumers needed to trace one complete run.
3. **Research layer**: explain the design rationale, assumptions, comparison
   points, limitations, and evidence that distinguish this work from a generic
   mechanism.

Do not jump to implementation detail before the reader can place it in the map.
Do not stop at a slogan when the omitted mechanism determines the conclusion.
Use the active object policies to mark which layer is source-established and
which is inference or simplification.

When relevant to retrieval or memory systems, trace these paths separately:

- source → index or storage;
- query → selected context;
- trajectory or feedback → memory update or replacement.

State what is represented, how selection is made, who consumes the result, and
which observations update or replace old information. If the source is silent on
an operational detail, retain the smallest useful `not specified` boundary.

## Final prose check

Before returning a document, search for and remove sentences whose only purpose
is to justify the writing process, source-search process, or avoidance of
hallucination. Scan for contrastive constructions and quotation marks wrapping
paraphrases; retain them only when they resolve a real ambiguity or carry
reader-facing information.

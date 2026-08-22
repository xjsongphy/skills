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

## Optional deep-dive checklist

Use only the groups relevant to the active subject and sources. The purpose is
to expose hidden mechanism details, not to force every document into an
agent-system template.

### Evidence gate

Use each question to interrogate the active sources, not to complete a plausible
design. For every answer, preserve the source location, version scope, and
uncertainty boundary required by the active object policies. This checklist is
source-agnostic; active object policies define the evidence label, source
location, version scope, and uncertainty boundary for each answer.

When a source omits a field, default value, state lifetime, selection rule,
ranking operation, or failure path, retain that omission. Do not infer ordinary
behavior such as an empty first query, clearing a resolved error, appending only
failures, filtering a candidate, or subtracting a ranking penalty. A complete
explanation of a partially disclosed mechanism contains both its known relations
and its explicit unknown boundary.

First satisfy the base mechanism contract above. The following is an optional
question bank for deepening that contract in specialized subjects; it does not
define a second universal mechanism model.

### Agent and multi-component systems

When the subject contains agents, planners, reviewers, generators, optimizers,
or judges, explain:

- each role's exact inputs and output format;
- whether roles see the full history, a selected window, summaries, exemplars, or only the current state;
- who constructs prompts and where each placeholder value originates;
- whether execution, compiler, profiler, or retrieval feedback is raw or preprocessed;
- which role can modify the artifact and which role only advises or scores;
- how conflicts or invalid outputs are resolved;
- how control passes between roles and when the loop stops.

Do not infer hidden prompts, private chain-of-thought, or undisclosed orchestration.

### Profiling, compilation, and execution feedback

When a method consumes runtime evidence, explain:

- what is measured or logged;
- at what granularity and under which input/configuration;
- how records are grouped, sorted, deduplicated, thresholded, or sampled;
- whether raw traces/counters/logs are given to the model or reduced to summaries;
- which metrics are withheld because of cost, noise, or tool availability;
- how correctness failures, compile failures, runtime failures, and performance results differ;
- whether stale errors are cleared after repair;
- how noise, warm-up, repetitions, outliers, and hardware variation are handled.

### Memory and experience systems

For any “memory”, “experience”, “lesson”, “skill”, “case”, or history pool, explain:

- write trigger: which events are eligible to create a memory;
- source material: code, feedback, metrics, trajectories, documents, or human labels;
- abstraction: how raw events become a reusable record;
- validation and filtering: frequency, confidence, deduplication, clustering, correctness, or performance gates;
- schema: fields stored and the meaning of each important field;
- scope and lifetime: local/long-term, per-task/cross-task, replacement/append-only/expiry;
- update rule: merge, overwrite, increment, rerank, or version;
- read path: who queries it and at which step;
- injection: how retrieved memory enters the next computation or prompt;
- negative cases: when memory is ignored, cleared, or unsafe to reuse.

### Retrieval and RAG

For retrieval systems, explain as many disclosed stages as exist:

- corpus construction and document provenance;
- unit of retrieval: document, chunk, code block, case, trajectory, or structured record;
- metadata and indexing fields;
- query construction and whether failure feedback modifies the query;
- candidate generation: lexical, embedding, symbolic, graph, or hybrid;
- hard filters and eligibility conditions;
- ranking/reranking score and diversity control;
- top-k or context-budget selection;
- retrieved content format and prompt/context insertion point;
- fallback when no suitable item exists;
- update or refresh policy.

When progressive exposition is active, keep these paths distinct where they are
disclosed: source → index or storage; query → selected context; and trajectory
or feedback → memory update or replacement. State what is represented, how
selection is made, who consumes the result, and which observations update or
replace old information.

If a source only says “uses RAG”, explicitly mark which stages are unspecified.

### Search and optimization algorithms

Explain:

- search state and candidate representation;
- legal action or mutation space;
- initialization or seed choice;
- objective, reward, or multi-objective ordering;
- feasibility and correctness constraints;
- candidate selection, expansion, pruning, rollback, or acceptance;
- exploration versus exploitation mechanism;
- history or population update;
- budget and stopping criteria;
- returned artifact and whether it is revalidated end to end.

### Learning or training methods

Explain:

- data source, task construction, and train/test separation;
- label, preference, reward, or self-supervision source;
- model inputs and prediction target;
- objective terms and symbol definitions;
- batching, sampling, curriculum, or filtering central to the contribution;
- parameter update and what remains frozen;
- inference-time differences from training;
- leakage, distribution shift, and evaluation boundaries.

### Compiler, systems, and hardware methods

Explain:

- source representation and target representation;
- pass order and invariants between passes;
- analysis results consumed by transformations;
- legality checks versus profitability checks;
- hardware constraints encoded explicitly or learned indirectly;
- fallback path when a transformation is invalid;
- compile-time/runtime split;
- interfaces between generated code, runtime, and benchmark;
- which results are architecture-specific.

### Experimental evidence

Use experiments to answer design questions:

- What hypothesis does each main experiment test?
- Are baselines given comparable models, budgets, hardware, inputs, and correctness rules?
- Which metric direction is better and what denominator defines ratios?
- Which ablation isolates which component?
- Do averages hide failed tasks or incorrect outputs?
- Which counterexample or negative result limits the claim?
- Are community cases, competition results, and main controlled experiments directly comparable?
- Does the source isolate the claimed cause with an ablation or explicit analysis? A recovery curve, before/after sequence, or temporal association alone does not prove which internal component caused the result.

Keep only enough numerical detail to support these answers.

# Mechanism Depth Checklist

Use only the groups relevant to the active subject and sources. The purpose is
to expose hidden mechanism details, not to force every document into an
agent-system template.

## Evidence gate

Use each question to interrogate the active sources, not to complete a
plausible design. For every answer, preserve the source location, version
scope, and uncertainty boundary required by the active object policies. This
checklist is source-agnostic; active object policies define the evidence label,
source location, version scope, and uncertainty boundary for each answer.

When a source omits a field, default value, state lifetime, selection rule, ranking operation, or failure path, retain that omission. Do not infer ordinary behavior such as an empty first query, clearing a resolved error, appending only failures, filtering a candidate, or subtracting a ranking penalty. A complete explanation of a partially disclosed mechanism contains both its known relations and its explicit unknown boundary.

## Universal mechanism questions

For each central stage or component, determine:

- What object enters it, who produced that object, and in what representation?
- What information is actually visible to the component?
- What is filtered, aggregated, ranked, truncated, normalized, sampled, or omitted first?
- What transformation, decision, or computation occurs?
- What conditions choose among branches or reject an item?
- What state is read and what state is updated?
- How long does that state live: one call, one iteration, one task, or across tasks?
- What output is produced, who consumes it, and why is it sufficient for the next stage?
- For failure, empty input, disagreement, timeout, or budget exhaustion paths that actually exist or affect the main flow, what happens next?
- Which design choice is essential, and what simpler alternative does the
  source compare against?

## Agent and multi-component systems

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

## Profiling, compilation, and execution feedback

When a method consumes runtime evidence, explain:

- what is measured or logged;
- at what granularity and under which input/configuration;
- how records are grouped, sorted, deduplicated, thresholded, or sampled;
- whether raw traces/counters/logs are given to the model or reduced to summaries;
- which metrics are withheld because of cost, noise, or tool availability;
- how correctness failures, compile failures, runtime failures, and performance results differ;
- whether stale errors are cleared after repair;
- how noise, warm-up, repetitions, outliers, and hardware variation are handled.

## Memory and experience systems

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

## Retrieval and RAG

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

If a source only says “uses RAG”, explicitly mark which stages are unspecified.

## Search and optimization algorithms

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

## Learning or training methods

Explain:

- data source, task construction, and train/test separation;
- label, preference, reward, or self-supervision source;
- model inputs and prediction target;
- objective terms and symbol definitions;
- batching, sampling, curriculum, or filtering central to the contribution;
- parameter update and what remains frozen;
- inference-time differences from training;
- leakage, distribution shift, and evaluation boundaries.

## Compiler, systems, and hardware methods

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

## Experimental evidence

Use experiments to answer design questions:

- What hypothesis does each main experiment test?
- Are baselines given comparable models, budgets, hardware, inputs, and correctness rules?
- Which metric direction is better and what denominator defines ratios?
- Which ablation isolates which component?
- Do averages hide failed tasks or incorrect outputs?
- Which counterexample or negative result limits the claim?
- Are community cases, competition results, and main controlled experiments directly comparable?
- Does the source isolate the claimed cause with an ablation or explicit
  analysis? A recovery curve, before/after sequence, or temporal association
  alone does not prove which internal component caused the result.

Keep only enough numerical detail to support these answers.

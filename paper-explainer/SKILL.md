---
name: paper-explainer
description: Use when writing, revising, or auditing a standalone Markdown explanation of a research paper. Produces image-supported, source-verified explanations for an average reader in the paper's field, prioritizes the paper's mechanisms and algorithms over background or benchmark dumps, checks appendices/code/official web resources, follows md-report-writer information-density rules, and runs separate Reviewer and Reader subagents.
---

# Paper Explainer

## Shared narrative rules

Read and follow [the shared narrative and evidence rules](../shared/narrative-and-evidence.md). This skill adds paper-specific evidence and review rules but does not duplicate the shared wording policy.

## Overview

Create a self-contained paper explanation that lets a reader understand the paper without repeatedly returning to the original. The explanation must answer not only “what modules exist”, but also “what each module receives, what it filters or changes, what state it updates, what it outputs, and why the next stage needs that output”.

The target reader is an **average reader in the paper's relevant subfield**. Before drafting, make that audience concrete with two short internal lists: `assumed_known` for concepts the reader may be expected to know, and `explain_in_draft` for concepts that must be introduced. Never place paper-specific names, symbols, modules, prompt fields, state transitions, or implementation choices in `assumed_known`.

The Main agent owns source collection, outlining, writing, revision, and final decisions. Two read-only subagents provide independent checks:

- **Reviewer** verifies factual accuracy and coverage against all in-scope evidence. Load [references/reviewer-agent.md](references/reviewer-agent.md).
- **Reader** simulates a human reader and checks comprehension, information density, and hidden assumptions using only the draft. Load [references/reader-agent.md](references/reader-agent.md).

If delegation is unavailable, perform the two passes sequentially with the same role boundaries. For the Reader pass, deliberately restrict the pass to the draft and audience requirement; do not use source knowledge to fill gaps silently.

## When to Use

Use this skill when the user asks to:

- explain, interpret, walk through, or summarize a research paper in depth;
- produce or revise a Markdown paper explanation;
- add figures, algorithms, implementation details, appendix material, or prerequisite knowledge to an explanation;
- audit whether an existing explanation is correct, complete, readable, or appropriately detailed;
- improve a paper explanation after several rounds of user edits.

Do not use the full workflow for a single factual question about a paper, a citation lookup, or a short abstract summary unless the user asks for a persistent explanation document.

## Required Writing Skill

Load and follow `md-report-writer` before outlining or editing prose. Treat it as the authority for narrative flow, concept-definition order, code explanation, figure placement, Mermaid use, professional tone, and paragraph information density.

This skill adds paper-specific source and review rules. It does not replace `md-report-writer`.

## Source Model

### Evidence priority

Use sources in this order:

1. Paper body, including all figures, tables, algorithms, footnotes, and limitations.
2. Appendix and supplementary material, including prompts, pseudocode, proofs, cases, ablations, and implementation settings.
3. Official artifact tied to the paper: project page, author repository, released code, configs, documentation, and model cards.
4. Official web material: author slides, talks, blogs, errata, release notes, or issue discussions that clarify the paper.
5. Third-party material only for background or comparison, never as stronger evidence than the paper or official artifact.

When local PDFs need extraction, use the available PDF-extraction skill or tool and retain extracted images. When network access is available and the user has not forbidden it, check official online resources after the local audit. Prefer primary sources and direct links.

### Keep evidence identities separate

Label claims by origin when the distinction matters:

- **The paper states**: directly supported by the paper or appendix.
- **The released implementation does**: visible in the official code/config version inspected.
- **A reasonable inference is**: follows from short, explicit evidence but is not stated verbatim.
- **Not specified**: the paper and artifact do not expose the detail.

Never let a later repository version silently redefine the paper's method. If paper and code differ, report the difference and use the paper's experiment version for interpreting paper results.

### Evidence-boundary style

Follow the shared narrative and evidence rules. Mark a boundary only where it changes how the reader should interpret the claim or code; keep the qualifier local and concise.

### Existing-document and Git audit

When revising an existing explanation:

1. Read the current document before editing.
2. Inspect `git diff` to identify the user's uncommitted improvements.
3. Inspect relevant `git log -p` history when it helps reveal stable preferences or prior corrections.
4. Preserve unrelated user edits and do not restore removed material merely because it existed in an older version.

Git history is evidence of writing preferences and revision intent, not evidence about the paper's facts.

## Content Priority

The paper's own contribution must occupy the explanatory center:

1. Problem and motivation: what concrete limitation creates the need for the method.
2. Overall design: the shortest complete view of how the proposed method addresses it.
3. Core process, principle, algorithm, architecture, or design: detailed enough to trace one complete run.
4. Design rationale and trade-offs: why components, filters, objectives, or representations are arranged this way.
5. A concrete example or implementation excerpt when it materially connects abstraction to behavior.

Background, related work, experiments, and performance comparisons must still be clear, but they are supporting sections:

- Background defines only concepts needed later.
- Related work identifies the gap and the paper's position; do not write a literature survey unless requested.
- Experiments explain setup, fairness, metrics, decisive trends, counterexamples, and limits; do not transcribe tables.
- Performance numbers support claims; they are not a substitute for explaining the method.

If the outline gives more attention to benchmark enumeration or related work than to the central mechanism, rebalance it unless the user explicitly requests an experiment-focused review.

## Depth Standard for the Main Method

For every central component, recover the mechanism chain:

```text
producer → input → selection/transformation → state change → output → consumer
                         ↑                         ↓
                   condition/failure        update/lifetime
```

Ask the questions in [references/method-depth-checklist.md](references/method-depth-checklist.md). They are generic mechanism questions; examples such as agents, profiling, memory, and RAG illustrate the required depth and do not limit this skill to agent or kernel papers.

Do not stop at verbs such as “processes feedback”, “updates memory”, “retrieves experience”, “profiles the program”, or “optimizes the candidate”. Explain the paper-disclosed operation behind the verb:

- What exact information is available?
- Is it raw, aggregated, ranked, filtered, truncated, clustered, or normalized?
- Which information is withheld or discarded?
- What condition triggers the action?
- Is the resulting state local to one step, one task, or shared across tasks?
- What does the next stage actually consume?

If the sources do not answer one of these questions, say so. Do not invent a plausible implementation.

## Prerequisite Knowledge Mode

Add prerequisite knowledge only when the user asks for it or when a missing concept would otherwise make the main method unreadable.

When the user explicitly requests prerequisites:

1. Identify the smallest concept chain needed for the paper's method.
2. Add a compact prerequisite section before the first dependent method section.
3. Define each concept through its role in this paper, with one small example or diagram when useful.
4. Do not turn the explanation into a textbook chapter.
5. Tighten the audience contract passed to the Reader: reduce `assumed_known` and add the prerequisite concepts to `explain_in_draft`. Do not use a vague instruction such as “assume one level less knowledge”.

Without an explicit prerequisite request, define paper-specific concepts and uncommon terms in place. Do not explain every common field term.

## Figures, Tables, Prompts, and Visual Evidence

### Select figures for explanatory value

Inspect every figure and table, including the appendix, before deciding what to include. Prefer visuals that clarify:

- the overall architecture or pipeline;
- a central algorithm, state transition, or feedback loop;
- a prompt, memory record, data structure, or interface whose fields matter;
- a concrete case that connects method to implementation;
- a decisive experiment, ablation, failure case, or limitation.

Do not include decorative figures or a large result grid merely for completeness. A figure omitted from the explanation must still be considered during source coverage review.

### Place and explain each visual locally

Use portable relative image paths whenever possible. Avoid editor-specific absolute paths.

For each included image:

1. Introduce why the reader should look at it.
2. Insert the image.
3. Add a visible centered italic HTML caption below it.
4. Immediately explain how to read it: orientation, regions, arrows, legends, inputs, outputs, and the conclusion it supports.

The caption names the figure; it does not replace interpretation. Do not stack several images and explain them later.

If the source figure is too crowded, keep the original for evidence and optionally add a clearly labeled simplified Mermaid diagram. Do not present a redraw as the paper's original figure.

### Prompt and template figures

For every important placeholder such as `[Task]`, `<memory>`, `{profile}`, or a named slot, explain:

- what runtime value replaces it;
- where that value comes from;
- whether it is raw or filtered;
- which stage uses it;
- when it is updated, replaced, cleared, or omitted.

If the paper does not publish the exact template or serialization, state that boundary instead of reconstructing one.

### Tables

Explain what the rows and columns compare, which direction is better, what baseline and conditions apply, and which trend matters. Do not narrate every cell. Keep only a few numbers that establish scale, validate a design choice, expose a counterexample, or define a limit.

## Algorithms, Mathematics, and Code

### Algorithms

An algorithm explanation should identify, when applicable:

- inputs and outputs;
- state carried across steps;
- objective or reward;
- selection and filtering rules;
- branch conditions and failure paths;
- update equations;
- stopping conditions;
- invariants or correctness constraints.

Define symbols next to first use. Use formulas when they compress a relationship more clearly than prose. Use pseudocode or Mermaid for multi-stage control flow; do not force an algorithm into a dense paragraph.

When the paper provides pseudocode and the explanation is line-oriented, preserve a source-faithful listing and add concise `//` comments on the relevant lines to explain state and data flow. Prefer this annotated listing over a row-by-row mapping table when the table would separate control flow. Keep the original operations and symbols unchanged, and clearly label added comments as explanatory.

### Code

Use code only when it reveals behavior that the prose or figure cannot show as clearly. Prefer small excerpts around the decisive condition, update, data structure, or kernel mapping.

Always distinguish:

- paper listing;
- official repository source;
- simplified pseudocode written for explanation.

Cite repository paths and line locations when available. Explain what the excerpt proves and what it does not prove. Never paste a long implementation and substitute comments for conceptual explanation.

## Information-Density Control

Apply `md-report-writer`'s density rules semantically, not mechanically.

### Reader-Relevance Filter

Every sentence should advance the explanation with a fact, mechanism, relation, evidence boundary, or interpretation. Remove meta-commentary about preserving fidelity, the author's process, the purpose of a paragraph, or why an omission was made. Do not write that a detail cannot be inferred merely because it is not public; omit unsupported details, or state the concrete evidence limitation only when it changes the paper's interpretation.

### Use direct exposition instead of rhetorical self-questioning

Write the mechanism as declarative prose. Do not pose a reader question and immediately answer it in the explanation, such as “这条链回答了‘谁产生什么、谁消费什么’” or “这里要问的是……答案是……”. The drafting checklist may contain questions, but those questions are internal checks and should not appear as a substitute for explanation. State the producer, transformation, output, and consumer directly; reserve rhetorical questions for cases where the user explicitly requests a Q&A or tutorial format.

### Define directly, not by analogy or negation

State what a component or quantity IS — its input, the operation performed, its output, and its role in the next stage. Do not lead with an analogy and do not lead with a negation.

Two anti-patterns to avoid as the opening or main mode of a paragraph:

- **Analogy-led opening**: a paragraph that introduces a mechanism by quoting a term and glossing it with a metaphor, such as “锦标赛选择”可以理解成若干次小组赛：……. An analogy may follow a direct statement to aid intuition, but it must not be the load-bearing explanation and must not open the paragraph.
- **Negation-led clarification**: a paragraph that defines a term primarily by saying what it is not, such as 这里的“策略性能”不是给自然语言策略 $S_i$ 单独打分。……. If a term is ambiguous, first state what it refers to and how it is measured; only then, if still needed, add one compact sentence noting the contrast that is likely to be misread.

Both patterns push the real explanation (what produces the value, what consumes it, how it is computed) below the fold. Rewrite them as positive declarative prose: for the analogy case, write “锦标赛选择从当前种群中分组比较适应度，胜者进入 parent 集合”；for the negation case, write “策略的性能由它所产生的修订内核 $K'_i$ 经编译、功能检查、NCU profiling 与计时后的延迟和硬件利用率度量” directly, and drop the “不是……单独打分” lead.

### Prefer specific descriptions over vague emphasis

Do not use broad emphasis words such as “核心”“关键”“重要” or “显著” as a substitute for evidence. State the component's position in the process, its input and output, the measured effect, or the source supporting the claim. For example, write “数据流如下” or “该文件供 Phase B 消费”，不要在没有进一步说明时把图表或结果称为“核心”或“关键”。

A paragraph should normally answer one reader question, express one main claim, or stay at one level of abstraction. Split or change representation when a paragraph mixes several of these dimensions:

- component inventory;
- data flow;
- control conditions;
- filtering or selection;
- state lifetime;
- design rationale;
- experimental evidence;
- limitations.

Choose the representation that matches the information:

- sequential process or feedback loop → Mermaid or pseudocode;
- exact field/component mappings → table;
- parallel constraints or failure modes → list;
- mathematical relation → formula;
- causal reasoning or interpretation → prose.

Do not split merely because a paragraph is long. Keep tightly coupled causal reasoning together. Conversely, several short paragraphs should be merged if they fragment one continuous argument. Paragraph length is a warning signal, not a pass/fail metric.

Avoid two opposite failures:

- **Compression by deletion**: removing the filtering rule, state update, data source, or design reason that makes a mechanism understandable.
- **Expansion by accumulation**: adding every appendix number, baseline detail, related work, or implementation fact without showing why it matters.

The correct target is the shortest explanation that preserves the mechanism chain and its evidence.

## Default Document Shape

Adapt section names to the paper; do not force this exact template. A typical explanation follows:

```text
Title and one-paragraph contribution
1. Problem and motivation
2. Overall method and main figure
3-N. Core method in causal or algorithmic order
N+1. Concrete case or implementation detail, if useful
N+2. Experimental evidence and what it does not prove
N+3. Related work, limitations, and conclusion
```

If prerequisites were requested, place them before the first section that depends on them. Integrate useful appendix details into the relevant method section rather than dumping them at the end.

Use enough headings to reveal the reasoning structure. Do not create a heading for every paragraph, and do not use callout blocks as decoration.

Keep the section hierarchy shallow and meaningful: use level-2 headings for the main argument and level-3 headings only when a method section contains genuinely distinct mechanisms. Parallel headings should describe parallel concepts. Avoid skipped heading levels and isolated subsections. For a long explanation, add a compact table of contents only when the renderer does not provide one automatically or the user requests it.

## Workflow

### Phase 1: Frame the task

1. Determine the paper/version, output location, language, and whether the task is new writing, revision, or audit.
2. Record explicit audience requirements. Default to the average reader in the paper's relevant subfield, inferred from the paper's problem and venue rather than a broad label such as “computer science”.
3. Define the audience contract: `assumed_known`, `explain_in_draft`, and whether prerequisite knowledge was requested.
4. For a revision, inspect the current document and relevant Git differences before planning changes.

Ask the user only when a missing choice would materially change scope and cannot be inferred from local context.

### Phase 2: Audit sources

1. Locate the paper body, appendix, supplementary files, extracted images, and local repository.
2. Read the paper and appendix completely enough to enumerate contributions, method sections, algorithms, figures, tables, experiments, and limitations.
3. Inspect official code/configs for central mechanism details not explicit in prose.
4. Check official web resources for supplements, errata, slides, project documentation, or version differences.
5. Build an internal evidence map: each central claim → source location → confidence → whether it belongs in the explanation.

Do not begin polished prose from the abstract alone.

### Phase 3: Build the explanation outline

1. State the paper's problem and contribution in plain language.
2. Identify the minimal complete mechanism chain.
3. Choose the figures, formulas, algorithms, and code excerpts that reveal that chain.
4. Assign background, related work, experiments, and appendix details supporting roles.
5. Check that every paper-specific concept is introduced before it becomes necessary.

### Phase 4: Draft method-first

1. Write the problem and overall method first.
2. Explain central components in causal order, even when the paper's presentation order is less readable.
3. Preserve explicit links between component input, transformation, output, and downstream use.
4. Place and interpret visuals locally.
5. Add experiments only after readers can understand what is being tested.
6. End with supported conclusions and limitations, not a generic summary.

### Phase 5: Reviewer pass

Dispatch the Reviewer after a complete draft exists. Give it:

- the draft path;
- all in-scope local paper, appendix, image, code, and artifact locations;
- official web sources already found;
- the paper/version and user scope.

The Reviewer remains read-only and returns the contract in [references/reviewer-agent.md](references/reviewer-agent.md). The Main agent fixes all blocker and major findings, resolves unsupported claims, and records any deliberate non-changes.

### Phase 6: Reader pass

After factual revisions, dispatch the Reader. Give it only:

- the revised draft path;
- the target subfield and audience contract (`assumed_known` and `explain_in_draft`);
- whether prerequisite mode is active and which prerequisite concepts were requested;
- any explicit user constraints on length or emphasis.

Do not give the Reader the paper, repository, evidence map, Reviewer findings, or answers to likely questions. The Reader must expose what the explanation itself fails to communicate.

The Main agent fixes P0 and justified P1 issues. Do not blindly implement every question: reject requests that fail the dependency, scope, or evidence tests in the Reader role.

### Phase 7: Targeted recheck and finish

If Reader-driven edits alter technical claims, formulas, algorithms, or conclusions, run a targeted Reviewer recheck on those sections. Repeat only while blocker/P0 issues remain or major/P1 fixes materially improve the document.

Finish when:

- Reviewer verdict is `PASS`, or `PASS_WITH_FIXES` with all blocker/major findings resolved;
- Reader reports no P0 and no unresolved justified P1;
- the main mechanism can be traced end to end;
- figures and tables are interpreted where they appear;
- appendix and official web resources were checked or explicitly unavailable;
- unsupported details are removed or labeled;
- `md-report-writer` checks and Markdown/file-link checks pass.

## Main Agent Decision Rules

The two subagents advise; the Main agent decides.

- Reviewer evidence overrides Reader preference on factual content.
- Reader confusion overrides stylistic brevity when it blocks the central mechanism.
- A request for more detail is accepted only if it is necessary for the contribution, explains a paper-disclosed mechanism, or was explicitly requested by the user.
- A request for deletion is rejected if it would break input/output flow, a decision condition, a state update, or the evidence behind a conclusion.
- When sources are silent, preserve the boundary rather than satisfying curiosity with invention.

## Final Quality Gate

Before completion, verify:

1. The reader can state the problem, contribution, and overall method.
2. The reader can trace one complete run through the central mechanism.
3. Central components expose inputs, processing/selection, outputs, state, and conditions where the paper provides them.
4. Memory, retrieval, feedback, profiling, compilation, data preparation, or optimization details are not hidden behind generic verbs.
5. Every important formula defines its symbols and role.
6. Every included figure/table has local context, visible caption, and immediate interpretation.
7. Appendix mechanisms and official artifacts were considered.
8. Paper claims, implementation facts, and inferences remain distinguishable.
9. Experiments establish evidence and boundaries without displacing the method.
10. Paragraphs control semantic load without blind splitting or deletion.
11. The document uses portable paths and cites real source locations.
12. The final conclusion does not claim more than the evidence supports.

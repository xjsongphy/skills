# Shared writing rules

This file is shared by writing-oriented skills. Read it when the parent skill
links here; do not copy its rules into individual skills. It combines narrative
style with cross-type technical exposition. Three sections are conditional:
progressive depth, topic sentences for substantial artifacts, and length
revision. Do not apply those sections to a brief chat answer or local lookup.

## Narrative requirements

- Write for the reader's understanding, not to document the agent's research process.
- Start with the subject, mechanism, evidence, or consequence. Remove meta-commentary about what was searched, what the writer intends to do, or what the writer will avoid.
- Do not emit defensive process disclaimers. If a source limitation changes the interpretation, state the concrete limitation at the point where it matters; do not repeat it as a drafting explanation.
- Prefer positive, evidence-bearing sentences over negation-based assurances. State what the source establishes, what the excerpt illustrates, and where the boundary lies.
- Use the field's established term. When source objects are active, verify
  source-specific terminology against them. Do not coin a non-standard term or
  import a term from another document unless the current document uses it. If a
  Chinese rendering is needed, anchor it to the standard term on first use and
  use one term consistently. Do not cycle near-synonyms for one concept inside
  a paragraph; technical repetition of the established term is clarity.
- Prefer a number, a named mechanism, or the field's term over a generic
  quality adjective such as significant, novel, or 具有重要意义, unless that
  word is standard terminology in the active field. The same applies to 核心,
  关键, 重要, 主要, 本质, and 显著 used as a substitute for evidence: state the
  component's position, input and output, measured effect, or supporting source
  instead.

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

Operational test: would the sentence lose factual content if the negation were
removed and the remainder rewritten as a positive assertion? If yes, keep the
contrast. If no, it was rhetorical; cut it and state what the thing is or does.

## Quotation and sentence shape

Use quotation marks only for direct quotation, the first introduction of a
coined or scoped term, and code/identifier/schema-token references. Do not wrap
colloquial paraphrases, metaphor labels, or long explanatory clauses in quotes.
Match the document language's quotation glyphs: Chinese documents use “”,
English documents use ASCII `"..."`, and one document does not mix the two.

Every sentence should be grammatically complete and express one clear thought.
Write mechanisms as declarative prose. Do not use rhetorical self-questioning
as a substitute for stating the producer, transformation, output, consumer, or
rationale. Do not open a paragraph with an analogy or define a term primarily
by negation; both push the real explanation below the fold. State the input,
operation, output, and role first; an analogy may follow as intuition, and one
compact contrast sentence may follow when a term is likely to be misread.

**Bad:** “‘锦标赛选择’可以理解成若干次小组赛：……” opens the paragraph; “这里的
‘策略性能’不是给自然语言策略单独打分” carries the definition.

**Good:** “锦标赛选择从当前种群中分组比较适应度，胜者进入 parent 集合” states the
mechanism first; “策略性能由其产生的修订内核经编译与计时后的延迟度量” states what
the term measures, before any contrast.

## Emphasis

Use bold sparingly, for genuinely important concepts, conclusions, or warnings,
integrated into complete sentences. Do not bold every introduced term and do
not open a paragraph with a bold label and a colon. Do not use italics for
emphasis; italics remain legitimate for paper titles, mathematical variables,
and conventional notation.

**Bad:** “**算法思路**：该算法使用动态规划解决问题。” / “该图是本方法的核心。”

**Good:** “该算法基于**动态规划**解决问题。” / “该图给出了从候选内核到执行反馈的
完整数据流。”

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

Worked example — one dense paragraph carrying eleven coupled points:

**Bad:**

> 图 2 左侧的 Adapt 按箭头形成一个跨任务闭环。首先，`Seed Program` 与
> `Documentation` 提供已有 PyTorch 示例和可用算子说明，二者经由 `Synthesize`
> 生成新的 `Training Program`；它是可执行的高层参考任务，而不是最终优化目标。
> 随后，agent 根据该任务执行 `Generate Kernel`，尝试写出对应的 Triton 内核。
> `Testing` 将生成内核与参考任务一起运行，`Get Execution Feedback` 返回编译
> 错误、运行错误或正确性结果。`Extract Failure Patterns` 只从失败候选及其反馈
> 中提炼重复出现的限制；`Clustering` 将语义相近的限制合并，写入
> `Update Skill Memory`。最后，更新后的记忆沿 `Injecting` 箭头加入下一轮
> `Generate Kernel` 的提示词，使后续候选能够避开已知陷阱。图中的环形箭头表示
> 该过程会在多个合成任务上持续重复，因而记忆是跨任务积累的。

**Good:** lead with the loop's arc, then one list item per stage:

> 图 2 左侧的 Adapt 形成一个跨任务学习闭环：从合成任务开始，收集失败模式，
> 更新记忆，再注入下一轮生成。该闭环包含四个阶段：
>
> - **任务合成**：`Seed Program` 与 `Documentation` 提供现有示例和算子说明，
>   经由 `Synthesize` 生成新的 `Training Program`——高层参考任务，而非最终
>   优化目标。
> - **内核生成与测试**：agent 依据 `Training Program` 执行 `Generate Kernel`；
>   `Testing` 将生成内核与参考任务一起运行，`Get Execution Feedback` 返回编译
>   错误、运行错误或正确性结果。
> - **失败模式提取**：`Extract Failure Patterns` 只从失败候选及其反馈中提炼
>   重复出现的限制；`Clustering` 合并语义相近的限制，写入 `Update Skill Memory`。
> - **记忆注入与循环**：更新后的记忆注入下一轮 `Generate Kernel` 的提示词；
>   环形箭头表示该过程在多个合成任务上持续重复。

When the surrounding figure already shows the stages clearly, a two-sentence
summary may replace the list; choose by how much the reader must retain from
the prose alone.

## Topic sentences for substantial artifacts

Use this section only for a substantial or persistent document artifact.
Brief chat answers, citation lookups, and local lookups skip it.

Before writing a section's full prose, write the topic sentences first.
Read them in sequence; they must form a coherent argument on their own.
Fill in the paragraphs only after that sequence holds.

Each topic sentence is a contract for the paragraph that follows. State the
paragraph's message in the first sentence. If a paragraph cannot be tied to a
topic sentence, either the paragraph does not belong or a topic sentence is
missing.

After drafting a section, reverse-outline it:

1. Write the section's central claim or teaching goal.
2. Write each paragraph's topic sentence.
3. Write the evidence or explanation points under each paragraph.
4. Confirm every topic sentence maps to the section claim, and every evidence
   point maps to its topic sentence.
5. Revise, merge, or delete any paragraph that cannot be mapped.

A textbook section may introduce a concrete object or example before naming
it; the topic-sentence chain must still recover the teaching arc. Do not
require claim-first headings. Topic headings remain appropriate when they name
a required report, experiment, or textbook part.

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

A parenthesis carries at most one light expansion. Do not pack several
definitions into one:

**Bad:** “PrimFunc 是 TIR（Tensor IR，TVM 的低层中间表示）层的 IR 单元，包含
buffer（TIR 中表示一块有形状和数据类型的线性内存区域，通过多维索引访问）访问
代码。”

**Good:** “PrimFunc 是 TVM 低层中间表示 TIR（Tensor IR）的 IR 单元。它包含完整
的循环嵌套，循环体内是对 buffer 的读写。buffer 是 TIR 层的数据容器：一个有形状
和数据类型的内存块，通过多维索引访问其中元素。”

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
When source objects are active, use their policies to distinguish which layer is
source-established and which is inference or simplification. When the mechanism
layer contains retrieval, memory, agents, compilers, or another structured
system, use the active mechanism-analysis contract rather than defining a second
system-specific checklist here.

## Length revision

Use this section only when the user asks to shorten, compress, or meet a page
or word limit. Do not run it after every draft. Do not target a percentage
reduction.

Write the full argument first. Then ask of every paragraph: does this serve
one of the section's topic sentences? If not, delete it. Do not pad to fill a
page or word limit. A short document that preserves the argument is better than
a padded one that reaches a quota.

Allowed operations, in order:

1. **Shorten sentences.** Remove a clause that can go without losing meaning,
   needed context, or recoverability.
2. **Merge paragraphs** that make the same point with different examples; keep
   the strongest example.
3. **Replace generic adjectives** with a number, a named mechanism, or nothing.
   Keep a term that is standard in the active field.
4. **Delete tutorial material** only when it is in `assumed_known` or the
   audience contract says the reader already has it. Explanations and textbooks
   keep the smallest bridge listed in `explain_in_draft`.
5. **Promote dense numerical comparisons** to a table or figure and leave a
   local interpretation in prose. This applies the representation-choice rule
   as a revision; it does not add a new policy.
6. **Delete a closing sentence** whose only job is to restate the paragraph
   without a new fact, limitation, or next step.

Refuse deletion that would break an input/output, condition, state-update,
derivation, evidence chain, or a `not specified` boundary. After compression,
the topic-sentence chain must still read as a complete argument. Re-run the
document prose gate.

## Final prose check

Before returning a document, search for and remove sentences whose only purpose
is to justify the writing process, source-search process, or avoidance of
hallucination. Delete a paragraph-final sentence that restates the paragraph
without adding a fact, limitation, or next step. Scan for contrastive
constructions and quotation marks wrapping paraphrases; retain them only when
they resolve a real ambiguity or carry reader-facing information. Apply the
keep-vs-cut test to every retained contrast.

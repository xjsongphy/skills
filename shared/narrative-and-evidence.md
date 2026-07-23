# Shared Narrative and Evidence Rules

This file is shared by writing-oriented skills. Read it when the parent skill links here; do not copy its rules into individual skills.

## Narrative requirements

- Write for the reader's understanding, not to document the agent's research process.
- Start with the subject, mechanism, evidence, or consequence. Remove meta-commentary about what was searched, what the writer intends to do, or what the writer will avoid.
- Do not emit defensive disclaimers such as “没有找到对应仓库，因此以下说明严格以论文为准” or “不会把其他项目的实现细节误归于本文”. These are process notes, not reader-facing explanation.
- If source availability changes the interpretation, state the concrete scope at the point where it matters: for example, “下例为依据论文方法写出的简化伪代码” or “论文未公开该接口的具体实现”. Do not explain the same limitation again in later paragraphs.
- If a detail is unsupported and does not affect the conclusion, omit it. If it affects the conclusion, use a short factual label such as “论文未说明”“未找到官方实现” or “这里是解释性展开”.
- Prefer positive, evidence-bearing sentences over negation-based assurances. Explain what the source establishes, what the excerpt illustrates, and where the boundary lies.

## Source and code boundary

Keep these identities separate:

1. what the paper states or shows;
2. what an official artifact implements;
3. what is an explanatory simplification or inference.

When no official repository is available, do not invent repository paths, APIs, configuration details, or implementation behavior. Use paper-disclosed algorithms, figures, appendices, and clearly labeled pseudocode instead. Mention the absence of the repository only when it changes how a code example or implementation claim should be read.

## Final prose check

Before returning a document, search for and remove sentences whose only purpose is to justify the writing process, source-search process, or avoidance of hallucination. Preserve concise source-boundary statements when deleting them would make a code example, implementation claim, or conclusion misleading.

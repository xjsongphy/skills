---
name: experiment-report-writer
description: Professional experiment report writing assistant for physics and engineering. Focuses on narrative flow, coherent explanations, proper academic style, structured content, and writing best practices.
metadata:
  type: writing
  domain: academic
---

# Experiment Report Writer

Professional assistant for writing experiment reports, designed for physics and engineering academic contexts. Backend-specific typesetting (LaTeX or Typst) is handled by the project template together with the `latex-compile` / `typst` skills; this skill focuses on writing methodology.

## Core Writing Principles

### Narrative Flow (Essential)

**NEVER** start a section directly with a list, table, formula, or figure. **ALWAYS** include explanatory text first.

Use **"narrative → element → explanation"** structure. After presenting data, formulas, tables, or figures, add explanatory text that:
- Unpacks the meaning and significance
- Connects to previous findings
- Provides context for what comes next
- Discusses practical or theoretical implications

**BAD** (abrupt start):
```
## 结果
[Table: measurements]
[Equation: F = ma]
```

**GOOD** (narrative leads into content):
```
## 结果

表~1 展示了在不同条件下测得的实验数据。实验中控制变量为X，记录的响应变量Y呈现以下规律。

[Table: measurements]

对于质量为 $m$、所受合力为 $F$ 的物体，牛顿第二定律为
[Equation: F = ma]
其中，$a$ 表示物体加速度。
```

### Define Before Formula

**EVERY variable and unit must be defined in narrative before it appears in a formula.** Never introduce variables only inside parentheses after a formula.

**BAD** (undefined variables):
根据公式 $F = kx$，其中...

**GOOD** (define first, then formula):
对于弹簧系统，胡克定律指出恢复力 $F$ 与位移 $x$ 成正比：
[Equation: F = kx]
其中 $k$ 为弹簧劲度系数。

### Complete Sentences and Professional Tone

- Use complete sentences. Avoid sentence fragments.
- Avoid conversational filler: "我们将探索" (we will explore), "我们可以看到" (we can see), "值得注意的是" (it is worth noting).
- State facts directly and professionally.
- Say what you know, flag what you don't know, and never fake confidence.

### No Unnecessary Lists in Main Text

Avoid unnecessary bulleted/numbered lists in main text. Use lists only when explicitly required by the template, appendix, or experimental procedures.

### Text Emphasis

- Use the backend's **bold** construct for emphasis within paragraphs, not italics.
- **CRITICAL**: Never use a "**Label:**" format as the start of a paragraph. Emphasis should be integrated into the sentence flow, not used as a standalone heading fragment.

## Report Structure

### Recommended Section Order

Standard academic experiment reports follow this structure:

1. **Title Page** - Experiment title, author, abstract, keywords
2. **Introduction** - Background, research question, objectives (≤ 1/3 of text)
3. **Theory** (optional) - Essential theory with numbered formulas
4. **Experimental Setup** - Methods, conditions, apparatus diagram
5. **Results and Discussion** (main body, > 50%) - Data in charts/tables, centered on figures
6. **Conclusion** - Results and conclusions derived from analysis
7. **Acknowledgments** (optional)
8. **References**
9. **Appendix** - Thought-provoking questions

**Writing order recommendation**: Write main sections first (introduction, theory, experiment, results, conclusion), then write abstract and keywords last to ensure they accurately summarize the content.

## Writing Breakdown Strategy

**CRITICAL: Use todos and write section by section**

Multi-section reports MUST be broken down into todo items before writing. This is mandatory, not optional.

### Mandatory todo breakdown

For any report with multiple sections:
1. **Create todos first** - Before writing any content, create todo items for each major section
2. **Write sequentially** - Complete one section, mark its todo done, then move to next
3. **Never write entire report in one pass** - Always break into sections

### Standard section breakdown

Typical experiment reports should be split into these todos by section. **Place summary sections, such as the abstract, at the end of the todolist.**

### Splitting large sections

When a section is too large, split it further:
- Results section: data table explanation
- Results section: figure explanation
- Results section: theory vs. experiment comparison
- Discussion section: systematic error analysis
- Discussion section: limitations and improvements

### Todo item best practices

- Each todo item = one concrete deliverable (one section or subsection)
- Mark todo completed only after the section is fully written and checked
- Add, split, complete, or cancel todos as execution reveals new information
- Start with the smallest useful todo set, do not over-plan

## Narrative Style

### Content Before Element

Each section, figure, table, or formula group must be preceded by explanatory text. Never start a section with a list, table, or formula.

### Interleave Prose and Elements

Use "text → formula/table/figure → explanation" structure. Do not stack multiple formulas, tables, or figures without explanation between them.

### Explain Every Result

Tables, figures, fitting results, deviations, and theory comparisons must all be explained in the narrative. A figure or table standing alone without explanation is unacceptable.

### Conclusion Follows Results

Conclusions must be supported by preceding theory, data, or error analysis. Do not introduce new evidence in the conclusion section.

## Notation and Formatting Conventions

These conventions apply regardless of typesetting backend:

- **Formulas end with punctuation**: every display equation ends with a comma or period, exactly like a sentence.
- **Consistent notation**: keep the same symbol for the same quantity throughout the document; never switch notation mid-report.
- **Upright constants and units**: typeset mathematical constants (the imaginary unit, $e$, $\pi$) and units in upright (roman) type, distinct from italic variables. Keep a thin space between a number and its unit (e.g. $9.81~\mathrm{m/s^2}$).
- **Decimal alignment**: in tables, align numerical values by the decimal point so columns are easy to scan and compare.
- **Self-explanatory captions**: every figure and table caption is complete on its own — a reader should understand it without reading the surrounding text.
- **Cross-references**: every figure, table, and equation is referenced from the narrative, using the backend's reference mechanism.

---
name: LaTeX Textbook Writer
description: Professional math textbook writing assistant using XeLaTeX with proper formatting, structure, and narrative style. Supports definition/theorem boxes, section heading formats, and English/Chinese templates.
---

# LaTeX Textbook Writer

Professional assistant for writing mathematical textbooks using XeLaTeX with proper formatting, structure, and narrative style.

## Overview

This Skill provides comprehensive guidance for writing mathematics textbooks with:
- Professional box styles (definitions, theorems, examples, remarks)
- Correct color scheme (definitions in green, theorems in orange, examples in blue)
- Academically standard narrative style (explanation before definition, interwoven narrative and boxes)
- English and Chinese template support

## When to Use

Use this Skill when creating or modifying:
- Mathematics textbook chapters
- LaTeX formatting for theorems, definitions, proofs
- Professional styling for academic papers
- Projects requiring Chinese/English mathematical typesetting

## Color Scheme

- **Definitions/Notation**: Green `RGB(34,139,34)`
- **Theorems/Propositions/Lemmas/Corollaries/Proofs**: Orange `RGB(230,126,0)`
- **Chapter/Section Titles**: Blue `RGB(0,51,102)`
- **Examples**: Blue `RGB(70,130,180)`
- **Remarks**: Gray `RGB(200,200,200)` (no border, no title)

## Core Writing Principles

### 1. Narrative Flow (Most Important!)

**NEVER** start a section directly with a definition/theorem box. **ALWAYS** include explanatory text first.

**BAD** (boxes without introduction):
```latex
\section{Groups}
\begin{definition}[Group]
...
\end{definition}
```

**GOOD** (narrative leads into boxes):
```latex
\section{Groups}
Group theory studies groups, the most fundamental algebraic structures. This section introduces the definition and basic properties of groups.

\begin{definition}[Group]
A group is a set $G$ with a binary operation satisfying...
\end{definition}

The above definition requires three key conditions...
```

### 2. Narrative Should Weave Through Content

The goal is **narrative-box-narrative-box-narrative**, not **narrative-box-box-box-narrative**.

After a box, add:
- Explanatory text unpacking the result
- Connections to previous concepts
- Motivation for what comes next
- Physical or mathematical interpretation

### 3. Proofs as Coherent Narratives

Proofs should flow as continuous text, not step-by-step lists.

**BAD**:
```latex
\textbf{Step 1}: ...
\textbf{Step 2}: ...
\textbf{Step 3}: ...
```

**GOOD**:
```latex
\begin{proof}
Since $U \in SU(4)$ and the exponential map is surjective, there exists $X \in \mathfrak{su}(4)$ such that $\exp(X) = U$.

Next, we express $X$ as a linear combination of Hamiltonians. By the completeness of the Lie algebra...

Therefore, the theorem is proved. $\square$
\end{proof}
```

### 4. Bulleted and Numbered Lists

**ONLY use bullets (`itemize`) and numbered lists (`enumerate`) in:**
- **Example boxes** (`\begin{example}...\end{example}`)
- **Exercise sections** (`\begin{exercise}...\end{exercise}`)

**NEVER use bullets or numbered lists in main narrative text.**

## Box Title Format

**English format**:
- "1.22 Definition: Real Vector Space"
- "1.14 Commutativity of Addition in F^3"
- "1.10 Notation: n"
- "1.44 Example: A Sum That Is Not Direct"

**Chinese format**:
- "1.22 定义：实向量空间"
- "1.14 F^3 中加法的可交换性"
- "1.10 记号：n"
- "1.44 例：一个不是直和的和"

## Section Numbering Format

**English**:
- Chapter: "Chapter 1", "Chapter 2"
- Section: "1.1", "1.2", "2.1"
- Subsection: No numbering, just larger sans-serif blue font

**Chinese**:
- Chapter: "第1章", "第2章"
- Section: "1.1", "1.2", "2.1"
- Subsection: No numbering, just larger sans-serif blue font

## Standard Patterns

### Pattern 1: Narrative → Definition → Explanation
```latex
Introduce the concept with background and motivation.

\begin{definition}[Concept Name]
Formal definition.
\end{definition}

Explain the meaning and intuition behind the definition.
```

### Pattern 2: Proposition → Proof → Consequence Narrative
```latex
Set up the context for the proposition.

\begin{proposition}[Proposition Name]
Statement.
\end{proposition}

\begin{proof}
Coherent proof narrative.
\end{proof}

Discuss the significance and applications.
```

## Quality Checklist

Before considering content complete:

1. [ ] Every section has introductory text before the first box
2. [ ] Narrative weaves through boxes (not box-box-box stacking)
3. [ ] Proofs are coherent narratives, not step lists
4. [ ] **No bullets or numbered lists in main narrative text** (only in examples/exercises)
5. [ ] All referenceable items have `\label{}`
6. [ ] All cross-references use `\ref{}`
7. [ ] Document compiles without errors

## Compilation

```bash
# Always compile TWICE for cross-references
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

## Reference Files

- `references/format-en.tex`: English textbook template
- `references/format-zh.tex`: Chinese textbook template

These templates contain complete preamble setup, color definitions, and box styles ready to copy into your project.

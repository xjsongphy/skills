---
name: laTeX-textbook-writer
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

## Language Settings (Critical!)

When using `ctex` package for Chinese support, theorem names and figure captions automatically become Chinese. **Always add these overrides for English documents:**

```latex
\usepackage{ctex}
\usepackage{amsmath,amssymb,amsthm}
\renewcommand{\proofname}{Proof}         % Force English "Proof"
\renewcommand{\contentsname}{Contents}   % Force English "Contents" instead of "目录"
\usepackage{caption}
\captionsetup{figurename=Figure,tablename=Table}  % Force English captions
```

## Color Scheme

- **Definitions/Notation**: Green `RGB(34,139,34)`
- **Theorems/Propositions/Lemmas/Corollaries/Proofs**: Orange `RGB(230,126,0)`
- **Chapter/Section Titles**: Blue `RGB(0,51,102)`
- **Examples**: Blue `RGB(70,130,180)`
- **Exercises**: Brown `RGB(139,69,19)`
- **Remarks**: Gray `RGB(200,200,200)` (no border, no title)

## Box Style Specifications

All theorem/definition/example boxes use `\newtcbtheorem` with:
- **Title inside border** (no separate boxed title bar for cleaner look)
- **Title format**: "2.2.1 Coin Flip Counting" (number, then title)
- **Title font**: Sans-serif bold white text on colored background
- **Content font**: Upright/roman (not italic)
- **Padding**: left=10pt, right=10pt, top=15pt, bottom=8pt
- **Border**: 1pt colored line with 6pt rounded corners
- **Title spacing**: toptitle=1mm, bottomtitle=1mm
- **Syntax**: `\begin{definition}{Title}{label}` (two arguments, not `[Title]`)

## Core Writing Principles

### 1. Narrative Flow (Most Important!)

**NEVER** start a section directly with a definition/theorem box. **ALWAYS** include explanatory text first.

**BAD** (boxes without introduction):
```latex
\section{Groups}
\begin{definition}{Group}{def:group}
...
\end{definition}
```

**GOOD** (narrative leads into boxes):
```latex
\section{Groups}
Group theory studies groups, the most fundamental algebraic structures. This section introduces the definition and basic properties of groups.

\begin{definition}{Group}{def:group}
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

### 4. No Italics - Use Bold for Emphasis

**DO NOT use italics** in mathematical textbooks. Use **bold** for:
- Emphasis on important concepts
- Proper nouns (names of mathematicians, special terms)
- Key terms being introduced

**BAD**:
```latex
Let $V$ be a *vector space*. The \textit{Hahn-Banach theorem} states...
```

**GOOD**:
```latex
Let $V$ be a vector space. The \textbf{Hahn-Banach theorem} states...
```

### 5. Bulleted and Numbered Lists

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

\begin{definition}{Concept Name}{def:concept}
Formal definition.
\end{definition}

Explain the meaning and intuition behind the definition.
```

### Pattern 2: Proposition → Proof → Consequence Narrative
```latex
Set up the context for the proposition.

\begin{proposition}{Proposition Name}{prop:name}
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
5. [ ] **No italics** - use bold for emphasis/proper nouns
6. [ ] All environments use new syntax: `\begin{definition}{Title}{label}` (not `[Title]`)
7. [ ] All referenceable items have unique labels in second argument
8. [ ] All cross-references use `\ref{}`
9. [ ] **For English documents**: Added `\renewcommand{\proofname}{Proof}` and `\captionsetup{figurename=Figure,tablename=Table}`
10. [ ] Document compiles without errors

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

## Exercise and Answer Appendices

If an `习题/` (exercises) directory exists in the project, create two appendix files:

### File Structure

```
project/
├── main.tex          # Main document
├── exercise.tex      # Appendix: Exercises (自动编号, no narrative text)
├── answers.tex       # Appendix: Reference Answers (答案 only, no questions repeated)
└── 习题/             # Exercise source files (Markdown format)
    ├── hw1.md
    ├── hw2.md
    └── ...
```

### exercise.tex Format

```latex
% 附录A 习题
\appendix
\chapter{习题}

\section{作业一}

\begin{enumerate}
    \item Question content here...

    \begin{enumerate}
        \item Subquestion (a)
        \item Subquestion (b)
    \end{enumerate}

    \item Next question...
\end{enumerate}
```

**Important:**
- Use `\appendix` before first `\chapter{}`
- Use `\begin{enumerate}...\end{enumerate}` for auto-numbering (1., 2., 3., ...)
- No narrative text like "习题1" or "Problem 1" - let enumerate handle numbering
- Nested enumerate for subquestions (a, b, c...)
- In main.tex, include after chapters: `\include{exercise}` and `\include{answers}`

### answers.tex Format

```latex
% 附录B 参考答案
\chapter{参考答案}

\section{作业一参考答案}

\begin{enumerate}
    \item \begin{enumerate}
        \item Subanswer (a)...

        \item Subanswer (b)...
    \end{enumerate}

    \item \begin{enumerate}
        \item Next subanswer...
    \end{enumerate}
\end{enumerate}
```

**Important:**
- Do NOT repeat questions - only provide answers
- Use `\begin{enumerate}...\end{enumerate}` for auto-numbering (1., 2., 3., ...)
- Nested enumerate for subanswers if needed
- No section titles within enumerate - let numbering speak for itself

### Translation Guide

When translating from English problem sets to Chinese:

| English | Chinese |
|---------|---------|
| Problem Set 1 | 作业一 |
| Problem 1 | 1. (use enumerate) |
| (a), (b), (c) | (a), (b), (c) (nested enumerate) |
| Compute/Calculate | 计算 |
| Show/Prove/Demonstrate | 证明/说明 |
| Determine | 判断/确定 |
| Isomorphic | 同构 |
| Dimension | 维数 |
| Independent constraint equations | 独立约束方程 |
| Matrix Lie groups | 矩阵李群 |
| Conjugacy classes | 共轭类 |

## Environment Syntax Reference

**New syntax (using `\newtcbtheorem`):**
```latex
% Definition with label
\begin{definition}{Title}{def:label}
    Content here...
\end{definition}

% Theorem with label
\begin{theorem}{Title}{thm:label}
    Statement here...
\end{theorem}

% Example with label
\begin{example}{Title}{ex:label}
    Content here...
\end{example}

% Remark (different syntax, no label)
\begin{remark}[Optional Title]
    Content here...
\end{remark}

% Proof (inline style, no colon)
\begin{proof}
    Proof content here...
\end{proof}
```

**Important notes:**
- Two arguments: `{Title}{label}` instead of `[Title]`
- Second argument is required (use descriptive labels like `def:vector_space`)
- The box title shows "Number Title" (e.g., "2.2.1 Coin Flip Counting")
- Proof environment uses `\quad` (two spaces) instead of colon after "Proof"
- Remark environment still uses optional `[Title]` syntax (no label needed)

---
name: latex-textbook-writer
description: Use when writing math textbook content in XeLaTeX, including definitions, theorems, proofs, and section formatting in English or Chinese.
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
\renewcommand{\contentsname}{Contents}   % Force English "Contents"
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

### 6. Chinese Quote Marks (CRITICAL for Chinese Documents!)

**When writing Chinese text in LaTeX (with `ctex` package), ALWAYS use proper quote marks:**

**Chinese Double Quotes:**
- Left double quote: `` `` `` (two backticks)
- Right double quote: `''` (two single quotes/apostrophes)

**Chinese Single Quotes:**
- Left single quote: `` ` `` (one backtick)
- Right single quote: `'` (one single quote/apostrophe)

**How to type:**
- Press backtick key (`` ` ``) twice for left double quote: ``
- Press apostrophe key (`'`) twice for right double quote: ''
- Press backtick key once for left single quote: `
- Press apostrophe key once for right single quote: '

**Examples:**
```latex
% CORRECT - Chinese quotes
The concept of ``closeness'' and ``continuity''...
This is a ``simple'' definition.

% INCORRECT - ASCII straight quotes (ugly in PDF)
The concept of "closeness" and "continuity"...
```

**IMPORTANT:** Always use `` `` and `''` for quotes in Chinese text, never use `"`, corner brackets, or any other form!

### 7. Specify Variable Domains Before Formulas

**ALWAYS** state which set each variable belongs to **before** writing formulas, not after.

**BAD** (domain specified after formula):
```latex
We can verify
$$
\langle \operatorname{ad}_{X}(Y), Z \rangle = \langle Y, \operatorname{ad}_{X^{*}}(Z) \rangle
$$
for $X \in \mathfrak{r}$ and $Y, Z \in \mathfrak{g}$.
```

**GOOD** (domain specified first):
```latex
Take any $X \in \mathfrak{r}$ and $Y, Z \in \mathfrak{g}$. We can verify
$$
\langle \operatorname{ad}_{X}(Y), Z \rangle = \langle Y, \operatorname{ad}_{X^{*}}(Z) \rangle
$$
```

Use phrases like: "Take any...", "For...", "Let...", "For any...".

## Box Title Format

**English format**:
- "1.22 Definition: Real Vector Space"
- "1.14 Commutativity of Addition in F^3"
- "1.10 Notation: n"
- "1.44 Example: A Sum That Is Not Direct"

**Chinese format** (for Chinese documents):
- "1.22 定义：实向量空间"
- "1.14 $F^3$ 中加法的可交换性"
- "1.10 记号：$n$"
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

### Pattern 1: Narrative -> Definition -> Explanation
```latex
Introduce the concept with background and motivation.

\begin{definition}{Concept Name}{def:concept}
Formal definition.
\end{definition}

Explain the meaning and intuition behind the definition.
```

### Pattern 2: Proposition -> Proof -> Consequence Narrative
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
10. [ ] **For Chinese documents**: All quotes use `` `` and `''`, NOT `"` or corner brackets
11. [ ] **Variable domains specified BEFORE formulas**, not after
12. [ ] **For answers.tex**: Each solution uses `\textbf{解：}` / `\textbf{Solution:}` with **one formula per line** format
13. [ ] **For answers.tex**: No paragraph contains multiple inline formulas - use display math for each formula
14. [ ] Document compiles without errors

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

**IMPORTANT FORMAT REQUIREMENT**: All solutions in `answers.tex` must use **"one formula per line" (一行一公式)** format. Each formula should be on its own line using display math (`$$...$$` or `\begin{equation*}...\end{equation*}`). Never stack multiple inline formulas in one paragraph.

If an `习题/` (exercises) directory exists in the project, create two appendix files:

### File Structure

```
project/
├── main.tex              # Main document
├── chapters/             # Chapter and appendix files
│   ├── chapter01.tex
│   ├── chapter02.tex
│   ├── exercise.tex      # Appendix: Exercises (auto-numbered, no narrative text)
│   └── answers.tex       # Appendix: Reference Answers (solutions only, no questions repeated)
└── 习题/                 # Exercise source files (Markdown format)
    ├── hw1.md
    ├── hw2.md
    └── ...
```

### exercise.tex Format

```latex
% Appendix A: Exercises
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
- No narrative text like "Problem 1" - let enumerate handle numbering
- Nested enumerate for subquestions (a, b, c...)
- In main.tex, include after chapters: `\include{chapters/exercise}` and `\include{chapters/answers}`

### answers.tex Format

```latex
% Appendix B: Reference Answers
\chapter{参考答案}

\section{作业一参考答案}

\begin{enumerate}
    \item \textbf{解：} [Detailed solution process, step-by-step format]

    \begin{enumerate}
        \item \textbf{解：} [Detailed solution for subproblem...]

        \item \textbf{解：} [Another subproblem solution...]
    \end{enumerate}

    \item \textbf{解：} [Next problem solution...]
\end{enumerate}
```

**CRITICAL: "One Formula Per Line" Format (一行一公式)**

Solutions must use **display math for EACH formula**, with step-by-step derivation. **DO NOT** stack multiple inline formulas in one paragraph.

**CORRECT format** (一行一公式):
```latex
\item \textbf{解：} We need to find $\alpha \in \mathfrak{h}$ such that
        \begin{equation*}
        \langle \alpha, H \rangle = 2a
        \end{equation*}
        for $H = aH_{1} + bH_{2}$.

        Let $\alpha = cH_{1}$. Then
        \begin{equation*}
        \langle cH_{1}, aH_{1} + bH_{2} \rangle = ca\langle H_{1}, H_{1} \rangle
        \end{equation*}
        Since
        \begin{equation*}
        \langle H_{1}, H_{1} \rangle = 2,
        \end{equation*}
        we have
        \begin{equation*}
        \langle cH_{1}, aH_{1} + bH_{2} \rangle = 2ca
        \end{equation*}
        For this to equal $2a$, we need
        \begin{equation*}
        c = 1
        \end{equation*}
        Therefore
        \begin{equation*}
        \boxed{\alpha = H_{1}}
        \end{equation*}
```

**WRONG format** (一段话堆砌公式 - **禁止**):
```latex
\item \textbf{解：} We need to find $\alpha \in \mathfrak{h}$ such that $\langle \alpha, H \rangle = 2a$ for $H = aH_{1} + bH_{2}$. Let $\alpha = cH_{1}$, then $\langle cH_{1}, aH_{1} + bH_{2} \rangle = ca\langle H_{1}, H_{1} \rangle = 2ca$ since $\langle H_{1}, H_{1} \rangle = 2$. For this to equal $2a$, we need $c = 1$, therefore $\alpha = H_{1}$.
```

**Key principles for solution formatting (IMPORTANT!):**

1. **Each formula on its own line** - Use `$$...$$` or `\begin{equation*}...\end{equation*}` for EVERY formula
2. **Step-by-step derivation** - Show each intermediate step as a separate display formula
3. **Minimal text between formulas** - Short phrases like "Then", "Since", "Therefore" are OK, but keep them brief
4. **Use `\boxed{}` for final answers** - Clearly mark the final result
5. **No formula stacking in paragraphs** - Never write `... $A$ ... $B$ ... $C$` in one paragraph

**Example with algebraic derivation:**

```latex
\item \textbf{解：} Compute the dimension of $Sp(2n, \mathbb{R})$. A matrix $M \in Sp(2n, \mathbb{R})$ satisfies
        \begin{equation*}
        M^{T}\Omega M = \Omega
        \end{equation*}
        where $\Omega$ is the standard symplectic form. This gives
        \begin{equation*}
        \frac{(2n)(2n-1)}{2} = n(2n-1)
        \end{equation*}
        independent real constraints.

        Since $GL(2n, \mathbb{R})$ has dimension
        \begin{equation*}
        (2n)^{2} = 4n^{2},
        \end{equation*}
        the dimension of $Sp(2n, \mathbb{R})$ is
        \begin{equation*}
        \boxed{\dim Sp(2n, \mathbb{R}) = 4n^{2} - n(2n-1) = n(2n+1)}
        \end{equation*}
```

**For English documents:** Use `\textbf{Solution:}` instead of `\textbf{解：}`

**Anti-examples to avoid:**

```latex
% WRONG - too much preamble
\item \textbf{解：} Our goal is to compute the dimension of $USp(2n)$. First, let us understand the structure...

% WRONG - vague, no actual derivation
\item \textbf{解：} We can see that, due to the unitarity condition, there are constraints...

% WRONG - skipping steps
\item \textbf{解：} After detailed analysis (omitting the tedious block computation), the dimension is...

% WRONG - result only, no process
\item \textbf{答：} $n(2n+1)$.

% WRONG - formulas stacked in paragraph
\item \textbf{解：} Compute $\langle \alpha, H \rangle = 2a$ for $H = aH_1 + bH_2$. Let $\alpha = cH_1$, then $\langle cH_1, H \rangle = 2ca$ since $\langle H_1, H_1 \rangle = 2$, so $c=1$ and $\alpha = H_1$.
```

**Additional writing guidelines:**
- Use `\textbf{解：}` (not `\textbf{答：}`) to emphasize process over result
- Do not repeat the question - start the solution directly
- May use `\begin{proof}...\end{proof}` for proof-type solutions
- Keep text between formulas minimal - just "Then", "Since", "Therefore", etc.
- Use blank lines to separate major steps in long derivations

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

## Figures and Illustrations

Figures can be created using **TikZ code inline** in chapter `.tex` files, or using **Python scripts** (matplotlib) stored in a `figures/` directory.

### TikZ Figures (inline in chapter files)

For mathematical diagrams (group-algebra relationships, commutative diagrams, etc.), use TikZ code directly in chapter `.tex` files:

```latex
\begin{center}
\begin{tikzpicture}[
    box/.style={draw, rounded corners=4pt, ...},
    ...
]
    \node[box] (A) at (0,0) {$SU(2)$};
    ...
    \draw[->, thick] (A) -- (B);
\end{tikzpicture}
\end{center}
```

### Python Figures (external scripts)

For plots, curves, and complex illustrations, use Python scripts:

```
project/
├── figures/              # Python scripts and generated images
│   ├── draw_xxx.py       # matplotlib scripts
│   ├── xxx.png           # Generated images
│   └── ...
```

- **Runtime**: `conda run -n py313 python figures/draw_xxx.py`
- Save as PNG with `dpi=200, bbox_inches='tight', facecolor='white'`
- Include via `\includegraphics[width=0.85\textwidth]{figures/xxx.png}`

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

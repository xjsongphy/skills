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
11. [ ] **For answers.tex**: Each solution uses `\textbf{解：}` / `\textbf{Solution:}` and shows detailed reasoning
12. [ ] Document compiles without errors

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
    \item \textbf{解：} [Detailed solution process, narrative style like main text]

    \begin{enumerate}
        \item \textbf{解：} [Detailed solution for subproblem...]

        \item \textbf{解：} [Another subproblem solution...]
    \end{enumerate}

    \item \textbf{解：} [Next problem solution...]
\end{enumerate}
```

**Critical: Solutions MUST follow narrative style (like the main text)**

Solutions are NOT just answer dumps. They should have complete reasoning and narrative logic like the main text. Each solution should include:

1. **Start with `\textbf{解：}`** - clearly mark the solution start
2. **State the approach** - method, theorem, or strategy used
3. **Step-by-step derivation** - show key steps, do not skip intermediate calculations
4. **Logical connectors** - use "therefore", "hence", "since", "note that", "now", etc.
5. **Final conclusion** - clearly state the answer

**Example style (direct, no preamble):**

```latex
\item \textbf{解：} Let $M \in USp(2n)$ be a $2n \times 2n$ complex matrix, partitioned into $n \times n$ blocks:
        \begin{equation*}
        M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}, \quad J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}
        \end{equation*}
        $M$ must satisfy both unitarity $M^{\dagger}M = I$ and symplecticity $M^{T}JM = J$. From unitarity, $M^{-1} = M^{\dagger}$. Substituting into the symplectic equation gives $JM = \bar{M}J$. Expanding the block multiplication yields $D = \bar{A}$ and $C = -\bar{B}$. Therefore matrices in $USp(2n)$ must have the form:
        \begin{equation*}
        M = \begin{pmatrix} A & B \\ -\bar{B} & \bar{A} \end{pmatrix}
        \end{equation*}

        Now substitute this form into the unitarity condition $M^{\dagger}M = I$:
        \begin{equation*}
        \begin{pmatrix} A^{\dagger} & -B^{T} \\ B^{\dagger} & A^{T} \end{pmatrix} \begin{pmatrix} A & B \\ -\bar{B} & \bar{A} \end{pmatrix} = \begin{pmatrix} I & 0 \\ 0 & I \end{pmatrix}
        \end{equation*}
        This yields two independent matrix equations. The diagonal block equation $A^{\dagger}A + B^{T}\bar{B} = I$ is a Hermitian matrix equation, providing $n$ real constraints on the diagonal and $\frac{n(n-1)}{2}$ complex constraints off-diagonal, totaling $n^{2}$ real constraints. The off-diagonal block equation $A^{\dagger}B - B^{T}\bar{A} = 0$ means $A^{\dagger}B$ is symmetric, giving $n(n-1)$ real constraints.

        Therefore the total number of constraints is $n^{2} + n(n-1) = 2n^{2}-n$. Subtracting from $4n^{2}$ initial real parameters gives the real dimension of $USp(2n)$:
        \begin{equation*}
        \dim_{\mathbb{R}} USp(2n) = 4n^{2} - (2n^{2}-n) = 2n^{2} + n = n(2n+1)
        \end{equation*}
```

**Anti-examples (avoid):**

```latex
\item \textbf{解：} Our goal is to compute the dimension of $USp(2n)$. First, let us understand the structure of this group... (too much preamble)
\item \textbf{解：} We can see that, due to the unitarity condition, there are constraints between the matrix blocks... (vague, no actual derivation)
\item \textbf{解：} After detailed analysis (omitting the tedious block computation), the dimension is $n(2n+1)$... (skipping steps)
\item \textbf{答：} $n(2n+1)$. (result only, no process)
```

**Writing guidelines:**
- Use `\textbf{解：}` (not `\textbf{答：}`) to emphasize process over result
- Do not repeat the question - start the solution directly
- Use complete mathematical sentences and paragraphs, not bullet points
- Explain reasoning at key steps ("since...therefore...", "note that...hence...")
- Split long computations into multiple paragraphs for clarity
- May use `\begin{proof}...\end{proof}` for proof-type solutions

**Paragraph separation (important):**

In LaTeX, blank lines create paragraph breaks. Long solutions should be split into paragraphs for readability:

```latex
\item \textbf{解：} The symplectic group $Sp(2n,\mathbb{R})$ consists of matrices satisfying $M^{T}\Omega M = \Omega$, where $\Omega$ is the standard symplectic form. This equation gives $\frac{(2n)(2n-1)}{2} = n(2n-1)$ independent real constraints.

The general linear group $GL(2n,\mathbb{R})$ has dimension $(2n)^{2} = 4n^{2}$, so $Sp(2n,\mathbb{R})$ has dimension $4n^{2} - n(2n-1) = 2n^{2} + n = n(2n+1)$.
```

**Paragraph principles:**
- One logical paragraph = one main point or step
- Separate paragraphs with blank lines (press Enter twice in LaTeX)
- Use transitional words at paragraph starts: "therefore", "hence", "now"
- Standalone formulas use `$$...$$` or `\[...\]`

**For English documents:** Use `\textbf{Solution:}` instead of `\textbf{解：}`

```latex
\item \textbf{Solution:} $USp(2n)$ is the intersection of $Sp(2n,\mathbb{C})$ and $SU(2n)$. Starting from $SU(2n)$ (real dimension $4n^{2}-1$), the symplectic constraints in the unitary framework give $2n^{2}-n$ independent real constraints. Therefore, the dimension of $USp(2n)$ is $(4n^{2}-1) - (2n^{2}-n) = 2n^{2}+n = n(2n+1)$.
```

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

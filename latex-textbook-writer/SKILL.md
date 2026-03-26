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

### 6. Chinese Quote Marks (CRITICAL for Chinese Documents!)

**When writing Chinese text in LaTeX (with `ctex` package), ALWAYS use proper quote marks:**

**Chinese Double Quotes:**
- Left double quote: `` ``, `` (two backticks)
- Right double quote: `''` (two single quotes/apostrophes)

**Chinese Single Quotes:**
- Left single quote: `` ` `` (one backtick)
- Right single quote: `'` (one single quote/apostrophe)

**How to type (with Chinese input method):**
- Press backtick key (`` ` ``) twice for left double quote: ``
- Press apostrophe key (`'`) twice for right double quote: ''
- Press backtick key once for left single quote: `
- Press apostrophe key once for right single quote: '

**Examples:**
```latex
% CORRECT - Chinese quotes
我们关于``接近''和``连续''的概念...
这是一个``简单的定义。

% INCORRECT - ASCII straight quotes
我们关于"接近"和"连续"的概念...
这是一个"简单"的定义。

% INCORRECT - Corner brackets (do NOT use in LaTeX)
我们关于「接近」和「连续」的概念...
```

**Why this matters:**
- LaTeX with `ctex` package renders `` `` and `''` as proper Chinese quotation marks ("" and "")
- Using ASCII straight quotes (`"`) will display as ugly straight quotes in the PDF
- Using corner brackets (`「」`) is not standard for LaTeX Chinese typesetting

**IMPORTANT:** Always use `` `` and `''` for quotes in Chinese text, never use `"`, `「`, or `」`!

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
10. [ ] **For Chinese documents**: All quotes use `` `` and `''`, NOT `"`, `「`, or `」`
11. [ ] **For answers.tex**: Each solution uses \textbf{解：}/\textbf{Solution:} and shows detailed reasoning process, not just final answer
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
│   ├── chapter01.tex     # Chapter files
│   ├── chapter02.tex
│   ├── exercise.tex      # Appendix: Exercises (自动编号, no narrative text)
│   └── answers.tex       # Appendix: Reference Answers (答案 only, no questions repeated)
└── 习题/                 # Exercise source files (Markdown format)
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
- In main.tex, include after chapters: `\include{chapters/exercise}` and `\include{chapters/answers}`

### answers.tex Format

```latex
% 附录B 参考答案
\chapter{参考答案}

\section{作业一参考答案}

\begin{enumerate}
    \item \textbf{解：} [详细解题过程，类似正文的叙述方式]

    \begin{enumerate}
        \item \textbf{解：} [子问题的详细解答...]

        \item \textbf{解：} [另一个子问题的详细解答...]
    \end{enumerate}

    \item \textbf{解：} [下一题的详细解答...]
\end{enumerate}
```

**Critical: Solutions MUST follow narrative style (类似正文的叙述方式)**

解答不是简单的答案堆砌，而是应该像正文一样具有完整的推理过程和叙述逻辑。每个解答应包括：

1. **以 \textbf{解：} 开头** - 明确标记解答开始
2. **阐明解题思路** - 说明使用的方法、定理或策略
3. **逐步推导过程** - 展示关键步骤，中间计算不要省略
4. **逻辑连接** - 使用"因此"、"从而"、"由于"、"注意到"等连接词
5. **最终结论** - 清晰地给出答案

**示例风格：**

```latex
\item \textbf{解：} $USp(2n)$ 是 $Sp(2n,\mathbb{C})$ 与 $SU(2n)$ 的交集。从 $SU(2n)$（实维数 $4n^{2}-1$）出发，在酉群框架下辛约束给出 $2n^{2}-n$ 个独立实约束。因此 $USp(2n)$ 的维数为 $(4n^{2}-1) - (2n^{2}-n) = 2n^{2}+n = n(2n+1)$。
```

**反面示例（应避免）：**

```latex
\item \textbf{答：} $n(2n+1)$。
```

**书写要点：**
- \textbf{解：} 而非 \textbf{答：} - 强调过程而非仅结果
- 不要重复题目内容，直接开始解答
- 使用完整的数学句子和段落，而非要点列表
- 关键步骤需解释理由（"因为...所以..."、"注意到...从而..."）
- 复杂计算可分多段叙述，保持逻辑清晰
- 可使用 \begin{proof}...\end{proof} 环境包含证明类解答

**段落分隔（重要）：**

在 LaTeX 中，空行用于创建段落分隔。长解答应适当分段以提高可读性：

```latex
\item \textbf{解：} 辛群 $Sp(2n,\mathbb{R})$ 由满足 $M^{T}\Omega M = \Omega$ 的矩阵构成，其中 $\Omega$ 是标准辛形式。这个方程给出 $\frac{(2n)(2n-1)}{2} = n(2n-1)$ 个独立实约束，因为反对称矩阵有 $\frac{N(N-1)}{2}$ 个独立分量。

一般线性群 $GL(2n,\mathbb{R})$ 的维数是 $(2n)^{2} = 4n^{2}$，因此 $Sp(2n,\mathbb{R})$ 的维数为 $4n^{2} - n(2n-1) = 2n^{2} + n = n(2n+1)$。
```

**分段原则：**
- 一个逻辑段落说明一个主要观点或步骤
- 段落间使用空行分隔（LaTeX 中按两次 Enter 键）
- 每段开头可以适当承接上文，使用"因此"、"故"、"从而"等
- 公式独立成段时使用 `$$...$$` 或 `\[...\]`

**For English documents:** Use \textbf{Solution:} instead of \textbf{解：}

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

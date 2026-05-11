# Exercise and Answer Appendix Format

**Core rule**: All solutions must use **"one formula per line" (一行一公式)** format. Each formula on its own line using display math. Never stack inline formulas in one paragraph.

If a `习题/` (exercises) directory exists in the project, create two appendix files.

## File Structure

```
project/
├── main.tex              # Main document
├── chapters/             # Chapter and appendix files
│   ├── exercise.tex      # Appendix: Exercises (auto-numbered, no narrative text)
│   └── answers.tex       # Appendix: Reference Answers (solutions only, no questions repeated)
└── 习题/                 # Exercise source files (Markdown format)
    ├── hw1.md
    └── ...
```

## exercise.tex Format

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

- Use `\appendix` before first `\chapter{}`
- Use `\begin{enumerate}...\end{enumerate}` for auto-numbering
- No narrative text like "Problem 1" — let enumerate handle numbering
- Nested enumerate for subquestions (a, b, c...)
- In main.tex: `\include{chapters/exercise}` and `\include{chapters/answers}`

## answers.tex Format

```latex
% Appendix B: Reference Answers
\chapter{参考答案}

\section{作业一参考答案}

\begin{enumerate}
    \item \textbf{解：} [Detailed solution, one formula per line]

    \begin{enumerate}
        \item \textbf{解：} [Subproblem solution...]
    \end{enumerate}
\end{enumerate}
```

### CORRECT (一行一公式)

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

### WRONG (一段话堆砌公式 — 禁止)

```latex
\item \textbf{解：} We need to find $\alpha \in \mathfrak{h}$ such that $\langle \alpha, H \rangle = 2a$ for $H = aH_{1} + bH_{2}$. Let $\alpha = cH_{1}$, then $\langle cH_{1}, aH_{1} + bH_{2} \rangle = ca\langle H_{1}, H_{1} \rangle = 2ca$ since $\langle H_{1}, H_{1} \rangle = 2$. For this to equal $2a$, we need $c = 1$, therefore $\alpha = H_{1}$.
```

## Key Principles

1. **Each formula on its own line** — `$$...$$` or `\begin{equation*}...\end{equation*}` for EVERY formula
2. **Step-by-step derivation** — Show each intermediate step separately
3. **Minimal text between formulas** — "Then", "Since", "Therefore" only
4. **Use `\boxed{}` for final answers**
5. **No formula stacking** — Never write `... $A$ ... $B$ ... $C$` in one paragraph

## Anti-Examples

```latex
% WRONG - too much preamble
\item \textbf{解：} Our goal is to compute the dimension of $USp(2n)$. First, let us understand the structure...

% WRONG - vague, no derivation
\item \textbf{解：} We can see that, due to the unitarity condition, there are constraints...

% WRONG - skipping steps
\item \textbf{解：} After detailed analysis (omitting the tedious block computation), the dimension is...

% WRONG - result only
\item \textbf{答：} $n(2n+1)$.
```

## Additional Guidelines

- Use `\textbf{解：}` (not `\textbf{答：}`) to emphasize process over result
- For English documents: `\textbf{Solution:}` instead of `\textbf{解：}`
- Do not repeat the question — start solution directly
- May use `\begin{proof}...\end{proof}` for proof-type solutions
- Use blank lines to separate major steps in long derivations

## Translation Guide

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

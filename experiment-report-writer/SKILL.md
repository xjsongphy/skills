---
name: experiment-report-writer
description: Professional LaTeX experiment report writing assistant for physics and engineering. Focuses on narrative flow, coherent explanations, proper academic style, structured content, and LaTeX best practices.
metadata:
  type: writing
  domain: academic
  format: latex
---

# Experiment Report Writer

Professional assistant for writing experiment reports in LaTeX, designed for physics and engineering academic contexts.

## Core Writing Principles

### Narrative Flow (Essential)

**NEVER** start a section directly with a list, table, formula, or figure. **ALWAYS** include explanatory text first.

Use **"narrative → element → explanation"** structure. After presenting data, formulas, tables, or figures, add explanatory text that:
- Unpacks the meaning and significance
- Connects to previous findings
- Provides context for what comes next
- Discusses practical or theoretical implications

**BAD** (abrupt start):
```latex
\section{结果}

\begin{table}
...
\end{table}

\begin{equation}
...
\end{equation}
```

**GOOD** (narrative leads into content):
```latex
\section{结果}

表~\ref{tab:measurements}展示了在不同条件下测得的实验数据。实验中控制变量为X，记录的响应变量Y呈现以下规律。

\begin{table}
...
\end{table}

对于质量为 $m$、所受合力为 $F$ 的物体，牛顿第二定律为
\begin{equation}
  F = ma .
\end{equation}
其中，$a$ 表示物体加速度。
```

### Define Before Formula

**EVERY variable and unit must be defined in narrative before it appears in a formula.** Never introduce variables inside parentheses after a formula.

**BAD** (undefined variables):
```latex
根据公式 $F = kx$，其中...
```

**GOOD** (define first, then formula):
```latex
对于弹簧系统，胡克定律指出恢复力 $F$ 与位移 $x$ 成正比：
\begin{equation}
  F = kx
\end{equation}
其中 $k$ 为弹簧劲度系数。
```

### Complete Sentences and Professional Tone

- Use complete sentences. Avoid sentence fragments.
- Avoid conversational filler: "我们将探索" (we will explore), "我们可以看到" (we can see), "值得注意的是" (it is worth noting).
- Do not use broad emphasis words such as "核心", "关键", "重要", "主要", "本质", or "显著" as a substitute for evidence. State the component's role, its input and output, the measured effect, or the source supporting the claim instead.
- State facts directly and professionally.
- Say what you know, flag what you don't know, and never fake confidence.

### Reader-Relevance Filter

Every sentence must provide reader-facing content: a fact, definition, relation, procedure, result, limitation, or interpretation. Remove meta-commentary about the writing process or the author's intention, such as "我需要保持忠实", "这段话的目的是", or "没有公开资料，因此不能推测", unless the limitation changes the report's conclusion.

Do not justify an omission or wording choice merely because it was made. If the source does not support a claim, omit it or state the specific evidence limitation only when it affects the analysis. When revising a report, do not restore deleted explanatory filler simply because it explains why the text was written that way.

### No Unnecessary Lists in Main Text

Avoid unnecessary `itemize` and `enumerate` in main text. Use lists only when explicitly required by the template, appendix, or experimental procedures.

### Text Emphasis in LaTeX

- Use `\textbf{}` for emphasis within paragraphs, NOT `\textit{}` or `\emph{}`.
- **CRITICAL**: Never use `\textbf{Title:}` format as the beginning of a paragraph. Emphasis should be integrated into the sentence flow, not used as a standalone heading fragment.

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

Typical experiment report should be split into these todos by sections. **Place summary sections, such as the abstract, at the end of the todolist.**

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

## LaTeX Best Practices

### Mathematics

- Use `\begin{equation}...\label{eq:name}...\end{equation}` for numbered display equations
- Reference equations: `\autoref{eq:name}` or `Eq.~\eqref{eq:name}`
- Imaginary unit and exponential: use `\ii`, `\jj`, `\ee` for upright notation
- All formulas should end with appropriate punctuation (comma or period)

### Figures and Tables

- Use `ruledtabular` environment for tables with double top/bottom rules
- Align numbers by decimal point: use `d{a.b}` column format
- Reference figures/tables: `\autoref{fig:name}`, `\autoref{tab:name}` or `Fig.~\ref{fig:name}`, `Table~\ref{tab:name}`
- Insert figures: `\includegraphics[width=0.8\textwidth]{path}`
- Each figure/table caption should be complete and self-explanatory

### Units and Notation

- Recommended: use siunitx package: `\qty{9.81}{\meter\per\second\squared}`
- Manual format: `$9.81~\mathrm{m/s^2}$` with `\mathrm{}` for units and `~` for thin space
- Maintain consistent notation throughout the document

### Chinese Language

- Chinese support via document class, no additional packages needed
- Abstract automatically indented with two characters
- Localized references: `\sectionautorefname` → "小节"

## Example: Good Report Section

```latex
\subsection{倍频法}

实验中观察到的倍频曲线如\autoref{double-frequency}所示。未加样品以及在电光晶体后放置云母片时，利用倍频法测量得到的结果如\autoref{double-frequency-table}所示。

\begin{figure}[H]
  \centering
  \includegraphics[width=0.5\linewidth]{fig/倍频}
  \caption{倍频曲线}
  \label{double-frequency}
\end{figure}

\begin{table}[H]
  \centering
  \caption{倍频法测量结果}
  \setlength{\tabcolsep}{0.4cm}{
    \begin{tabular}{ccc}
      \hline
      光路 & $V_\text{D0}$/V & $V_\text{DP}$/V \\
      \hline
      电光晶体 & -106$\pm$5 & 1269$\pm$5 \\
      加入云母片 & -619$\pm$5 & 996$\pm$5 \\
      \hline
    \end{tabular}}
  \label{double-frequency-table}
\end{table}

因此，半波电压为

\begin{equation}
  V_{\pi}= V_\text{DP}-V_\text{D0}=1375\text{ V}
\end{equation}

由\autoref{r63}，晶体的电光系数为

\begin{equation}
  r_{63} = \frac{\lambda}{2 n_\text{o}^3 V_{\pi 2}} = 16.8\text{ (}10^{-10}\text{cm/V)}
\end{equation}

其中 $V_{\pi 2} = 4V_\pi$ 为四块串联晶体的总半波电压，$\lambda = 632.8~\mathrm{nm}$ 为激光波长，$n_\text{o}$ 为晶体寻常光折射率。
```

**Points to note**:

1. **Narrative first**: Explanatory text introduces figure and table before they appear
2. **Variables defined before use**: $\lambda$, $n_\text{o}$ defined after formula, $V_{\pi 2}$ defined inline
3. **Proper cross-references**: `\autoref{}` used for figures, tables, and equations
4. **Complete captions**: Figure and table captions are self-explanatory
5. **Results explained**: Numerical results are interpreted in context

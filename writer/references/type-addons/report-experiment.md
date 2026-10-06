# Experiment report

Load with `../types/report.md` for physics and engineering laboratory reports.

State the measured scope, apparatus or setup, controlled conditions, analysis
method, and traceable source of every quantitative result. Let actual measured
data and supplied requirements define scope; mark unsupported requested items
instead of fabricating them.

## Structure and proportions

Use the usual order when no template overrides it: title page; introduction;
necessary theory; setup and procedure; results and discussion; conclusion;
acknowledgments (optional); references; appendix.

- The introduction stays within about one third of the body text.
- Results and discussion form the main body — more than half of the text —
  because they connect measurement, uncertainty, theory, and interpretation.
- Write the main sections first and draft the abstract (and keywords) last, so
  it summarizes what was actually written.

## Writing breakdown

Break a multi-section report into one todo per major section before writing,
and complete the sections one at a time; never draft the whole report in a
single pass. Place summary sections such as the abstract at the end of the
list. Split an oversized section further — data-table interpretation, figure
interpretation, theory–experiment comparison, systematic-error analysis,
limitations and improvements — rather than writing it in one burst. Mark a
todo complete only after its section is fully written and checked.

## Professional tone

- Use complete sentences and state facts directly. Say what you know, flag
  what you do not know, and never fake confidence.
- Do not use conversational filler such as “我们将探索”, “我们可以看到”,
  “值得注意的是”, "we will explore", "we can see", or "it is worth noting".

## Reader-relevance filter

Every sentence must give the reader content: a fact, definition, relation,
procedure, result, limitation, or interpretation. Remove meta-commentary
about the writing process or the author's intention — “这段话的目的是”,
“没有公开资料，因此不能推测” — unless the limitation changes the report's
conclusion. Do not justify an omission or wording choice merely because it
was made. When revising a report, do not restore deleted explanatory filler
simply because it explains why the text was written that way.

## Detail economy

An expert reader wants the argument, not the transcript of the measurement
session. Concretely:

- The abstract and the conclusion are mostly qualitative. Include a number
  only when the number itself is the headline result; do not enumerate ten
  values in an abstract.
- State each measured or fitted value once, where it is interpreted. Reuse it
  by cross-reference instead of restating the same number in theory, results,
  discussion, and appendix.
- Keep instrument operation sequences, switch settings, unit-conversion
  checks, and on-the-fly self-checks out of the report; they belong in a lab
  notebook, or in a procedure appendix only when the template demands it.
- Do not reproduce the full raw data grid in the main text. A compact table of
  the points the argument uses, or a plot, replaces the grid; ship a complete
  data appendix only when the course or template requires it.
- Discuss uncertainty in prose and name only the material components with
  their justification; do not build a component-by-component bookkeeping
  table when the budget is dominated by one or two terms.
- Verification side-trips — endpoint recomputation, alternative fits,
  residual spot checks — support confidence; report their conclusion, not
  every intermediate comparison.
- A discussion paragraph answers one question. When a result deviates from
  expectation, give the observation, the decisive check, and the resulting
  limitation in one paragraph; longer alternative-exclusion chains (competing
  models, frequency scans, control samples) belong in the analysis artifact —
  the report keeps their conclusion and the strongest single counter-evidence.
- Figure and table captions stay within one or two sentences: what is shown
  and its decisive reading. Captions do not restate selection criteria, data
  file names, or conclusions established elsewhere.
- Answer appended thought questions in a few sentences each; they are not
  mini-essays and must not restate the body.

## Define before formula

**EVERY variable and unit must be defined in the narrative before it appears
in a formula.** Never introduce variables inside parentheses after a formula
as their first definition.

**Bad** (undefined variables):

> 根据公式 $F = kx$，其中……

**Good** (define first, then formula):

> 对于弹簧系统，胡克定律指出恢复力 $F$ 与位移 $x$ 成正比：
>
> $$F = kx$$
>
> 其中 $k$ 为弹簧劲度系数。

## Main-text lists

Avoid `itemize` and `enumerate` in the main text; an experiment report reads
as continuous prose. Use a list only when the template requires it, for
appendix data, or for genuinely parallel procedural steps.

## Worked example

A good section introduces its elements in prose, defines every variable, and
interprets each result (LaTeX):

```latex
\subsection{倍频法}

实验中观察到的倍频曲线如\autoref{double-frequency}所示。未加样品以及在电光
晶体后放置云母片时，利用倍频法测量得到的结果如\autoref{double-frequency-table}
所示。

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
  r_{63} = \frac{\lambda}{2 n_\text{o}^3 V_{\pi 2}} = 16.8\times10^{-10}\,\mathrm{cm/V}
\end{equation}

其中 $V_{\pi 2} = 4V_\pi$ 为四块串联晶体的总半波电压，$\lambda = 632.8~\mathrm{nm}$
为激光波长，$n_\text{o}$ 为晶体寻常光折射率。
```

Points to note:

1. **Narrative first**: explanatory text introduces the figure and table
   before they appear.
2. **Variables defined before use**: $V_{\pi 2}$, $\lambda$, $n_\text{o}$ are
   defined where the formula that uses them is interpreted.
3. **Proper cross-references**: `\autoref{}` for figures, tables, equations.
4. **Complete captions**: figure and table captions are self-explanatory.
5. **Results explained**: each numerical result is interpreted in context,
   once.

The same section in Typst (identical narrative shape; only the syntax
differs):

```typst
=== 倍频法

实验中观察到的倍频曲线如 @double-frequency 所示。未加样品以及在电光晶体后
放置云母片时，利用倍频法测量得到的结果如 @double-frequency-table 所示。

#figure(
  image("fig/倍频.png", width: 50%),
  caption: [倍频曲线],
) <double-frequency>

#figure(
  table(
    columns: 3,
    table.hline(),
    table.header([光路], [$V_"D0"$ / V], [$V_"DP"$ / V]),
    table.hline(),
    [电光晶体], [$-106 plus.minus 5$], [$1269 plus.minus 5$],
    [加入云母片], [$-619 plus.minus 5$], [$996 plus.minus 5$],
    table.hline(),
  ),
  caption: [倍频法测量结果],
) <double-frequency-table>

因此，半波电压为

$ V_pi = V_"DP" - V_"D0" = 1375 "V" $

由 @r63，晶体的电光系数为

$ r_63 = lambda / (2 n_o^3 V_(pi2)) = 16.8 times 10^(-10) "cm/V" $

其中 $V_(pi2) = 4 V_pi$ 为四块串联晶体的总半波电压，$lambda = 632.8 "nm"$ 为
激光波长，$n_o$ 为晶体寻常光折射率。
```

Discuss systematic and random uncertainty only to the extent the data or
method supports it. Compare theory with measurement where the design permits
it, and state which conclusions are limited by measurement scope, data
coverage, or uncontrolled conditions.

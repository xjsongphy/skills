# LaTeX textbook format integration

Load with `../types/textbook.md` and `../formats/latex.md` for a mathematics
textbook.
Use the user's template first; otherwise start from
`../../assets/latex/textbook-template.tex` and adapt its language settings.

Use consistent theorem-like environments for definitions, theorems, examples,
remarks, and exercises. Introduce a formal box with prose and follow it with
explanation, proof, example, or consequence; do not stack formal blocks without
narrative. Use upright body text and bold only for meaningful term introduction
or controlled emphasis. For English documents that load `ctex`, explicitly set
the proof name, contents name, and figure/table captions to English.

Compile through `latex-compile` at least twice after changing labels, theorem
numbering, or cross-references. Keep TikZ figures inline only when they are
small and local; put generated figures in portable external files.

## Exercise and answer appendices

When `type-addons/textbook-exercises.md` is active and a `习题/` directory is
present, use separate exercise and answer appendix files when the template
supports them:

```text
project/
├── main.tex
├── chapters/
│   ├── exercise.tex
│   └── answers.tex
└── 习题/
```

Use `\appendix` before the first appendix chapter, `\chapter{习题}` and
`enumerate` for automatic numbering. Use nested `enumerate` for subquestions;
do not type “Problem 1” as prose when the environment can number it. The
answers appendix should contain solutions without repeating the questions
unless the template requires repetition.

For solutions, use one displayed formula per line. Show decisive intermediate
steps, use `\boxed{}` for a final answer when appropriate, and keep text
between formulas short. Do not stack several opaque transformations in one
paragraph or skip the central derivation with “after simplification”. Use
`\textbf{解：}` in Chinese documents and `\textbf{Solution:}` in English
documents when the local template uses an explicit solution label.

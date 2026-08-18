# LaTeX textbook format integration

Load with `../types/textbook.md` and `../formats/latex.md` for a mathematics
textbook.
Use the user's template first. For a complete chapter-based textbook without a
user template, use the language-appropriate `book` starter:
`../../assets/latex/textbook-format-en.tex` or
`../../assets/latex/textbook-format-zh.tex`. The compact
`../../assets/latex/textbook-template.tex` is an `article`-class starter for
short examples and isolated sections; it is not the default for chapter-based
textbooks or chapter-based appendices.

Use the environment, numbering, label, and typography conventions supplied by
the selected template. Follow narrative placement and formal-block sequencing
from `../types/textbook.md`; this integration does not redefine textbook
pedagogy. For English documents that load `ctex`, explicitly set the proof
name, contents name, and figure/table captions to English.

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

---
name: latex-compile
description: LaTeX compilation assistant for XeLaTeX projects. Handles compilation errors, cross-references, and diagnostics.
---

# LaTeX Compile

LaTeX compilation assistant for XeLaTeX projects, handling compilation errors, cross-references, and diagnostics.

## Overview

This skill provides the standard XeLaTeX compilation workflow for LaTeX projects, including error diagnosis and fixes.

## Standard Compilation Commands

**VSCode LaTeX Workshop recipe (XeLaTeX):**

```bash
# XeLaTeX compilation (first pass)
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex

# XeLaTeX compilation (second pass - update cross-references)
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

**Parameters:**
- `-synctex=1`: Generate SyncTeX data for PDF viewer synchronization
- `-interaction=nonstopmode`: Continue compilation on errors (shows all errors at once)
- `-file-line-error`: Display error messages with file and line numbers
- `main.tex`: Main LaTeX file

**Compilation passes:**
- **Must compile twice**: First pass generates `.aux` files, second pass updates cross-references
- If labels or references change, compile again

## Common Compilation Error Diagnosis

### 1. Environment Mismatch Error

**Symptom:**
```
! LaTeX Error: \begin{document} ended by \end{remark}.
```

**Cause:** Mismatched environment begin/end tags

**Diagnosis command:**
```bash
grep -n "begin{remark}\|end{remark}" chapters/*.tex
```

**Fix:**
- Check each `\begin{remark}` has corresponding `\end{remark}`
- Remove extra `\end{remark}` tags

### 2. Missing Required Parameter Error

**Symptom:**
```
! Package pgfkeys Error: I do not know the key '/tcb/Title'...
```

**Cause:** Incorrect theorem environment format

**Correct format:**
```latex
% CORRECT format (using \newtcbtheorem)
\begin{remark}{Title}{label}
  Content...
\end{remark}

% WRONG format
\begin{remark}[Title]
  Content...
\end{remark}
```

### 3. Chinese Character Error

**Symptom:**
```
! Package pgfkeys Error: I do not know the key '/tcb/中文标题'...
```

**Cause:** Chinese title in square brackets

**Fix:** Ensure using `{Title}{label}` format

### 4. Undefined Reference Warning

**Symptom:**
```
LaTeX Warning: Reference `eq:label' undefined...
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
```

**Fix:** Run compilation again (second pass)

## Compilation Output Interpretation

### Successful compilation
```
Output written on main.pdf (93 pages).
Transcript written on main.log.
```

### Warnings but successful
```
Package hyperref Warning: Token not allowed in a PDF string (Unicode)...
Output written on main.pdf (93 pages).
```
- hyperref warnings are usually ignorable (Unicode in PDF bookmarks)

### Failed compilation
```
! LaTeX Error: ...
l.123 \begin{remark}
```
- Line number indicates error location
- Must fix error before recompiling

## Quick Diagnosis Commands

### Check all remark environments
```bash
grep -n "begin{remark}\|end{remark}" chapters/*.tex
```

### View specific line range
```bash
sed -n '1500,1550p' chapters/chapter02.tex
```

### View compilation error summary
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | grep -E "Error|Warning" | head -20
```

### View last few lines (success/fail status)
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | tail -10
```

## Compilation Workflow

### Standard compilation (recommended)
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex && \
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

### Compilation with error filtering
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | grep -E "Error|! " | head -30
```

### Full compilation output (for debugging)
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

## Common Issues

### Q: PDF not updated?
A: Delete `.aux` and `.synctex.gz` files and recompile:
```bash
rm -f *.aux *.synctex.gz *.log
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

### Q: VSCode compiles successfully, but command line fails?
A: Check VSCode LaTeX Workshop settings to ensure same compilation command

### Q: Compilation is slow?
A: This is normal, XeLaTeX compiling large documents takes time. First compilation is usually slower.

## File Dependencies

Compilation requires:
- `main.tex` (main file)
- `chapters/*.tex` (chapter files)
- `figures/` (image files, if any)
- `.cls` or `.sty` files (if using custom class)

## References

- XeLaTeX documentation: https://texdoc.org/pkg/xelatex
- tcolorbox documentation (theorem boxes): https://texdoc.org/pkg/tcolorbox
- ctex documentation (Chinese support): https://texdoc.org/pkg/ctex

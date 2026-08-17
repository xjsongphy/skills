---
name: latex-compile
description: Use when compiling LaTeX documents with XeLaTeX, or encountering compilation errors, missing cross-references, or diagnostic warnings.
---

# LaTeX Compile

LaTeX compilation assistant for XeLaTeX projects, handling compilation errors, cross-references, and diagnostics.

## Overview

This skill provides the standard XeLaTeX compilation workflow for LaTeX projects, including error diagnosis and fixes.

**Important: When users invoke this skill, they typically have compilation problems that need solving. Always display sufficient error information for diagnosis — do not over-filter the output!**

## When to Use

**Use when:**
- Compiling `.tex` files with XeLaTeX
- Encountering LaTeX compilation errors (environment mismatch, undefined references, Chinese character issues)
- Diagnosing compilation warnings or failed builds

**Don't use when:**
- Compiling with pdfLaTeX or LuaLaTeX (commands differ)
- Setting up a new LaTeX project from scratch (use the `writer` LaTeX and
  textbook-LaTeX route, including its template assets, instead)

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

**⚠️ Important: When diagnosing compilation errors, do not over-filter the output! Error information may be anywhere in the output. Using `head` or `tail` may miss critical errors.**

### Recommended Error Diagnosis Methods

**Method 1: Show all errors and warnings (recommended)**
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | grep -E "Error|! |Warning"
```
This displays all errors, warnings, and fatal errors starting with `!`.

**Method 2: Limit line count but don't use head/tail**
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | grep -E "Error|! " | head -50
```
If the output is truly too large, you can use `head -50` to limit to the first 50 errors, but never use `tail`!

**Method 3: Check specific types of errors**
```bash
# Check all environment mismatch errors
grep -E "begin|end" main.tex | grep -v "%"

# Check remark environments in specific files
grep -n "begin{remark}\|end{remark}" chapters/*.tex
```

### Not Recommended (will miss errors)

❌ **Don't do this:**
```bash
# Only see last 10 lines, will miss errors in the middle
xelatex ... 2>&1 | tail -10

# Only see first 30 lines, won't see later errors
xelatex ... 2>&1 | head -30

# Only see last 20 lines, may miss main errors
xelatex ... 2>&1 | tail -20
```

### Other Useful Diagnostic Commands

**View specific line range:**
```bash
sed -n '1500,1550p' chapters/chapter02.tex
```

**Check specific labels:**
```bash
grep -n "label{eq:" chapters/*.tex | sort | uniq -d
```

## Compilation Workflow

**⚠️ Important Principle: When users invoke this skill, they have compilation problems. Must display sufficient error information to help diagnose!**

### Step 1: Get Complete Error Information

**Recommended approach: Show all errors without using head/tail**
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | grep -E "Error|! "
```

**If output is truly too large (over 100 lines), you can limit the count:**
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex 2>&1 | grep -E "Error|! " | head -50
```

**❌ Never use tail to view errors:**
```bash
# Wrong! This will miss most errors
xelatex ... 2>&1 | tail -10
```

### Step 2: Diagnose Problems Based on Error Messages

After viewing error messages, locate the specific file and line number:
- Error format: `./filename.tex:line_number: error_description`
- Use Read tool to view content around that line

### Step 3: Fix Errors and Recompile

After fixing errors, recompile to verify:
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex
```

### Standard Two-Pass Compilation (only after first pass succeeds)
```bash
xelatex -synctex=1 -interaction=nonstopmode -file-line-error main.tex && \
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

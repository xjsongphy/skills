---
name: beamer
description: Use when creating LaTeX Beamer presentation slides from documents, especially for academic presentations. Use when source document contains structured content with sections, subsections, or clear hierarchical organization that should be preserved in slides.
---

# Beamer Slides from Documents

## Overview

Create LaTeX Beamer presentation slides by converting structured document content into academic-style slides. Focus on preserving the original document's narrative and structure while ensuring proper page layout and academic presentation standards.

## When to Use

**Use when:**
- Converting academic papers, technical reports, or structured documents into presentation slides
- Source document has clear hierarchical structure (sections, subsections, headers)
- Need to maintain original document's narrative flow and terminology
- Creating academic or technical presentations requiring formal structure
- Document contains mathematical formulas, figures, tables that need proper formatting

**Don't use when:**
- Creating highly visual or creative presentations (consider other tools)
- Source material lacks structure or is unorganized text
- Need minimal slide decks (3-5 slides) - manually create instead

## Core Pattern: Structure Preservation

### Document Structure Mapping

Map document hierarchy to slide structure:

```
Document Title        → Title slide
Main sections (##)     → New sections with table of contents
Subsections (###)     → Individual frames
Content within         → Frame content (bullet points, math, figures)
```

### Section Processing Logic

```latex
% Main section in document → Beamer section
\section{Section Title}

% Subsection content → Individual frame
\begin{frame}
  \frametitle{Subsection Title}
  [Content from document]
\end{frame}
```

### Automatic Table of Contents

Generate TOC slides at beginning of each section:

```latex
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{内容提要}
    \tableofcontents[currentsection]
  \end{frame}
}
```

## Quick Reference

### Required File Structure

```
slides/
├── slides.tex              # Main file
├── sections/
│   ├── part1_title.tex    # Section files
│   ├── part2_title.tex
│   └── part3_title.tex
└── images/                 # Image files
```

### Main Template (slides.tex)

```latex
\documentclass[10pt,aspectratio=169]{beamer}

% 中文支持
\usepackage{ctex}

% 常用宏包
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{physics}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{multirow}
\usepackage[backend=biber,style=numeric,sorting=none,sortcites=true,url=false]{biblatex}
\usefonttheme[onlymath]{serif}

% 主题设置
\usetheme{Madrid}
\usecolortheme{default}

% 页边距设置
\setbeamersize{text margin left=1.2cm,text margin right=1.2cm}

% 图片路径
\graphicspath{{../images/}}

% 全局行间距
\renewcommand{\baselinestretch}{1.15}

% 每节开始时显示目录
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{内容提要}
    \tableofcontents[currentsection]
  \end{frame}
}

\begin{document}
  % 标题页
  \frame{\titlepage}
  
  % 目录页
  \begin{frame}
    \frametitle{内容提要}
    \tableofcontents
  \end{frame}

  % 各部分内容
  \input{sections/part1_xxx.tex}
  \input{sections/part2_xxx.tex}
  ...

  % 感谢页
  \begin{frame}
    \centering
    \Huge{感谢聆听！}
    \vspace{1cm}
    \Large{欢迎提问与讨论}
  \end{frame}
\end{document}
```

### Section File Template

```latex
%=============================================================================
% 第N部分：章节名称
%=============================================================================
\section{章节名称}

\begin{frame}
  \frametitle{帧标题}
  
  [使用原文档的叙述内容]
  
  \vspace{0.3cm}
  
  [支持数学公式、图表、列表等]
\end{frame}
```

## Content Conversion Rules

### 1. Narrative Preservation (CRITICAL)

**Use original document's exact wording and structure:**

- Copy text directly from source document
- Preserve original terminology and expressions
- Maintain document's logical flow
- Keep original emphasis (bold, italics) where meaningful

**What to preserve:**
- Original definitions and explanations
- Mathematical formulas and derivations
- Author's original examples and illustrations
- Paper's conclusions and contributions

**What to adapt:**
- Long paragraphs → bullet points or shorter sentences
- Complex sentence structures → clearer academic Chinese
- Very long sections → multiple frames

**Examples:**

```latex
% ❌ BAD: Rewording original content
\textbf{QTurbo的核心优势}在于方程系统优化

% ✅ GOOD: Using original wording
\textbf{QTurbo的工作流程}：首先，QTurbo通过将全局混合方程系统分解为全局线性方程系统和多个局部混合方程系统...
```

### 2. Academic Style Requirements

**Language and tone:**
- Use formal academic Chinese (学术汉语)
- Avoid colloquial expressions (口语化表达)
- Maintain professional terminology
- Use precise technical language

**Prohibited patterns:**
- ❌ "核心"、"关键"、"重要"等过度强调词语
- ❌ "不是...而是..."的重复句式
- ❌ 段落开头使用粗写短语+冒号（如"**核心**："）

**Better alternatives:**
- Use specific descriptive terms: "设计原理"、"主要优势"、"显著进展"
- Vary sentence structure to avoid monotony
- Integrate emphasis naturally into full sentences

### 3. Layout and Formatting

**Image sizing rules:**
- Use `keepaspectratio` to prevent distortion
- Limit height: `height=0.45\textheight` maximum
- Limit width: `width=0.9\textwidth` maximum
- Test compile to ensure no overflow

**Recommended image sizes:**
```latex
% Full-width images
\includegraphics[width=0.85\textwidth,height=0.45\textheight,keepaspectratio]{figure.jpg}

% Column images
\includegraphics[width=0.95\textwidth,height=0.4\textheight,keepaspectratio]{figure.jpg}
```

**Text density rules:**
- Use `\vspace{0.2cm}` to separate content blocks
- Limit frame content to avoid overflow
- Use columns for side-by-side content
- Split long sections across multiple frames

**Column layout pattern:**
```latex
\begin{columns}[T]
  \column{0.5\textwidth}
    [Left content]
  \column{0.5\textwidth}
    [Right content]
\end{columns}
```

### 4. Content Completeness

**Default: Include all content from document**

- Include all main sections from source document
- Preserve all figures and tables
- Keep mathematical derivations
- Include experimental data and results

**Only simplify when user explicitly requests:**
- User says "简化为X页" (simplify to X pages)
- User says "只讲主要结论" (only cover main conclusions)
- User specifies specific sections to include/exclude

**When content exceeds reasonable slide count:**
- Ask user which sections to prioritize
- Suggest splitting into multiple presentations
- Create detailed vs. abbreviated versions

## Implementation

### Step-by-Step Process

1. **Analyze source document structure**
   - Identify main sections (##)
   - Map subsections to potential frames
   - Locate figures, tables, formulas

2. **Create file structure**
   - Create main `slides.tex`
   - Create `sections/` directory
   - Copy images to `images/` or reference existing location

3. **Generate section files**
   - Create one `.tex` file per main section
   - Map subsections to frames
   - Preserve original narrative

4. **Compile and verify**
   - Run `xelatex slides.tex` twice
   - Check for layout issues
   - Verify image loading
   - Ensure no content overflow

### Image Path Configuration

**Option 1: Copy images to slides directory**
```latex
\graphicspath{{../images/}}  % Relative to sections/
```

**Option 2: Reference existing assets**
```latex
\graphicspath{{../../assets/}}  % Adjust path as needed
```

## Common Mistakes

### ❌ Rewording Original Content

**Mistake:** Summarizing or paraphrasing instead of using original text

```latex
% ❌ BAD
QTurbo通过优化方程系统提高了编译效率

% ✅ GOOD
QTurbo通过将全局混合方程系统分解为全局线性方程系统和多个局部混合方程系统，优化了用于脉冲设计的方程系统构建。这种方法通过降低计算复杂度和提高可扩展性，显著增强了方程求解过程。
```

**Fix:** Copy content directly from source document, only adapting paragraph structure.

### ❌ Overusing Emphasis Words

**Mistake:** Excessive use of "核心"、"关键"、"重要"

**Fix:** Use specific, descriptive language:
- "核心思想" → "设计原理" or "基本思想"
- "关键问题" → "研究问题" or "主要挑战"
- "重要突破" → "显著进展"

### ❌ Image Overflow

**Mistake:** Images exceeding page boundaries

**Symptoms:** Compilation warnings, content cut off

**Fix:** Always use `keepaspectratio` and reasonable height limits:
```latex
% ❌ BAD: No height limit
\includegraphics[width=\textwidth]{figure.jpg}

% ✅ GOOD: Constrained dimensions
\includegraphics[width=0.85\textwidth,height=0.45\textheight,keepaspectratio]{figure.jpg}
```

### ❌ Text Overflow

**Mistake:** Too much content on single frame

**Symptoms:** Content extends beyond slide boundary

**Fix:** Split into multiple frames or use columns:
```latex
% ❌ BAD: One long frame with 20 bullet points
\begin{frame}
  \frametitle{技术细节}
  \begin{itemize}
    \item [20 items...]
  \end{itemize}
\end{frame}

% ✅ GOOD: Split into logical groups
\begin{frame}
  \frametitle{技术细节（一）}
  [First group of items]
\end{frame}

\begin{frame}
  \frametitle{技术细节（二）}
  [Second group of items]
\end{frame}
```

## Real-World Impact

Using this skill produces academic presentations that:
- **Accurately represent** original research or documentation
- **Maintain narrative flow** and technical precision
- **Follow academic standards** for formal presentations
- **Avoid layout issues** that distract from content
- **Preserve all important content** unless explicitly simplified

**Example outcomes:**
- 30-40 page academic presentations from papers
- Conference presentation slides with proper structure
- Technical talks that preserve original terminology and logic
- Research group presentations maintaining complete technical accuracy

## Compilation and Testing

### Compilation Commands

```bash
# First compilation
xelatex slides.tex

# Second compilation (for references and TOC)
xelatex slides.tex

# Output: slides.pdf
```

### Verification Checklist

Before considering slides complete:

- [ ] All sections from document included (unless user requested simplification)
- [ ] Original narrative preserved and accurately represented
- [ ] No prohibited emphasis words ("核心", "关键", etc.)
- [ ] All images load correctly with proper sizing
- [ ] No text or image overflow on any frame
- [ ] Mathematical formulas render correctly
- [ ] Tables formatted properly with booktabs
- [ ] Compilation completes without errors
- [ ] PDF page count reasonable for content scope

## Advanced Customization

### Theme Selection

Standard academic themes:
- `Madrid` (default, clean and professional)
- `CambridgeUS` (red/grey color scheme)
- `Beaver` (MIT color scheme)
- `Warsaw` (formal, dark blue)

### Color Themes

```latex
\usecolortheme{default}   % Standard
\usecolortheme{dolphin}   % Light blue
\usecolortheme{rose}      % Subtle color
\usecolortheme{orchid}    % Purple tones
```

### Custom Styling

```latex
% Remove navigation symbols
\setbeamertemplate{navigation symbols}{}

% Custom colors
\definecolor{primarycolor}{RGB}{0,102,204}
\setbeamercolor{structure}{fg=primarycolor}

% Custom frame titles
\setbeamercolor{frametitle}{bg=primarycolor,fg=white}
```

## Supporting Templates

### Title Page Configuration

```latex
\title[短标题]{完整标题}
\subtitle{副标题（可选）}
\author[作者简称]{作者全名}
\institute[机构简称]{
  机构全名 \\
  Department name
}
\date{日期或事件名称}
```

### Bibliography Integration

```latex
% In main file
\addbibresource{references.bib}

% At end of document
\begin{frame}[allowframebreaks]{参考文献}
  \printbibliography[heading=none]
\end{frame}
```

---
name: lecture-notes-enhancement
description: Use when enhancing existing lecture notes with multiple course source materials (recordings, PPT slides, existing notes)
---

# Lecture Notes Enhancement

## Overview

Systematic process for cross-referencing recordings, PPTs, and existing notes to identify gaps and enhance lecture notes with narrative-first writing. Uses parallel subagents for efficiency.

## When to Use

**Use when:**
- Enhancing existing lecture notes (讲义.md) with course recordings and PPTs
- Course has multiple source materials (records/, extracted/, existing notes)
- Need systematic gap identification and content supplementation
- Following md-report-writer narrative style (narrative flow before technical content)

**Don't use when:**
- Creating lecture notes from scratch (use brainstorming + writing-plans instead)
- Simple formatting or proofreading (use simplify skill instead)
- Single source material only (direct editing is sufficient)

## Nature of Source Materials

Each source type has distinct role and limitations:

**Slides (PPT extracted/) — Simplified outline only.** Contain key formulas and section outlines — the final results, not the path to them. No detailed derivations, intermediate steps, or physical intuition. Treat slides as a *what* checklist, not the full content.

**Recordings (records/) — Full content with caveats.** Contain detailed derivations, step-by-step reasoning, and additional formulas not on slides. However: (a) teachers may not read every formula aloud — extract **keywords** to identify which formulas are being discussed; (b) ASR transcriptions introduce errors, especially for technical terms — always cross-reference with slides for precise formulas.

**Existing notes — Baseline.** Provide current structure and coverage level to supplement, not replace.

## Core Pattern

The enhancement process follows four phases:

**Phase 1: Parallel Analysis** - Dispatch subagents to analyze each source material independently
**Phase 2: Gap Synthesis** - Identify missing content, inconsistencies, and improvement opportunities
**Phase 3: Systematic Enhancement** - Edit lecture notes section-by-section with narrative-first style
**Phase 4: Verification** - Ensure all improvements follow md-report-writer guidelines

### Phase 1: Parallel Analysis Dispatch

For each course record or PPT file, dispatch a subagent with specific analysis scope:

```
Analyze records/week03.md:
- Focus: Numerical methods for PDE solving
- Extract: Discretization schemes, boundary conditions, solver algorithms
- Output: Structured summary with key formulas and implementation details
```

**Why parallel?** Each source is independent. Processing concurrently saves time and prevents context overflow.

### Phase 2: Gap Identification Matrix

Create structured gap analysis organized by priority:

| Priority | Content Category | Missing Details | Source Location |
|----------|----------------|-----------------|-----------------|
| High | Theoretical foundations | Fundamental equation derivation | records/week02.md L30-40 |
| High | Numerical methods | Iterative solver details | records/week03.md L170-190 |
| Medium | Implementation tips | Optimization techniques | records/week04.md L330-360 |

### Phase 3: Narrative-First Enhancement

Apply md-report-writer style principles:

**✅ DO:**
- Start sections with explanatory narrative
- Use **bold** for emphasis (never italics)
- Write complete, grammatical sentences
- Embed code snippets to support claims
- Weave narrative through content (narrative → content → narrative)

**❌ DON'T:**
- Start sections abruptly with lists/formulas
- Use bullet points for main narrative explanations
- Use conversational filler ("we will explore", "as we can see")
- Use vague emphasis words ("核心", "关键", "重要", "主要", "本质", "显著") as a substitute for evidence — state the role, input/output, or measured effect instead
- Write multi-paragraph docstrings or comment blocks
- Add meta-commentary about the editing process, source fidelity, or why a sentence was written a certain way
- Explain that an unsupported detail cannot be inferred unless that limitation changes the lecture content

#### Segment Length Principle

Break complex explanations into focused segments, giving the user a chance to respond after each. If answering 3+ distinct questions, deliver them as separate segments. Avoid massive single responses.

### Phase 4: Section-by-Section Editing

Edit the lecture notes systematically by section:

1. **Read current section** in existing lecture notes
2. **Read relevant analysis** from supplement reports
3. **Identify specific improvement** needed
4. **Apply narrative-first edit** using Edit tool
5. **Update todo list** to track progress

## Quick Reference

| Source Type | What to Extract | Typical Locations | Limitations |
|-------------|----------------|-------------------|-------------|
| Course records (records/) | Physical intuition, detailed derivations, additional formulas not on slides | Usually lines 50-200 | Transcription inaccuracies; teachers may not read every formula verbatim |
| PPT content (extracted/) | Key formulas, section structure, topic checklist | Throughout file | Simplified only — missing derivations, intuition, and content spoken in class |
| Existing notes | Current structure, what needs enhancement | Full file | May inherit gaps from whichever source was used previously |

## Common Enhancement Categories

**Theoretical Foundations:** Missing derivations, physical intuition, intermediate steps between slide formulas.

**Numerical Methods:** Solver details, algorithm choices, convergence analysis not shown on slides.

**Implementation Details:** Practical considerations, edge cases, boundary conditions discussed orally.

**Writing Style:** Narrative-first structure, symbol definitions at first use, **bold** for key terms, complete sentences.

## Implementation

```markdown
## Example Enhancement: Adding Cauchy Momentum Equation

**Before** (abrupt start):
### 1.1 Navier-Stokes方程
流体运动的数学描述建立在连续介质力学假设之上。Navier-Stokes方程是...

**After** (narrative-first):
### 1.1 连续介质力学基础
流体仿真的理论基础建立在**连续介质假设**之上：将流体视为连续分布的物质，而非离散的分子集合。在这一假设下，我们关注流体中每个**小体积元**的受力与运动。对于连续介质中的小体积元，它受到的力可以分为两大类。**体力**（body force）作用于整个体积，如重力场和磁场。**表面力**（surface force）通过表面接触传递，如流体内部的摩擦和压力。柯西动量方程（Cauchy Momentum Equation）是适用于所有连续介质的普适方程...
```

## Common Mistakes

| Mistake | Why Bad | Fix |
|---------|---------|-----|
| Editing without reading current content | May duplicate or miss context | Always Read before Edit |
| Answering questions without editing notes | User needs enhanced documentation, not conversation | Edit the lecture notes directly |
| Adding too much content at once | Hard to verify, high error risk | Edit section-by-section with todo tracking |
| Forgetting narrative flow | Technical content feels abrupt | Start each section with explanatory text |
| Using italics for emphasis | Md-report-writer specifies **bold** only | Replace all italics with bold |
| Writing conversational filler | Unprofessional, wastes tokens | Use direct, professional tone |
| Skipping parallel analysis | Sequential processing is slower, loses context | Dispatch subagents for independent sources |
| Leaving symbols unexplained | Readers can't follow formulas | Always define $w_i$, $w_p$, and other notation at first use |
| Treating slides as complete content | Misses majority of lecture material | Slides provide *what* topics, recordings provide *how* they're explained |
| Trusting transcription text blindly | ASR errors in technical terms | Cross-reference with slides; use recording for explanation, slides for precise formulas |
| Expecting formulas to be spoken verbatim in recordings | Teachers gesture at slides, don't read every symbol | Extract keywords to identify which formulas are being discussed |

## Real-World Impact

Before: Lecture notes missing key theoretical foundations, numerical details, and implementation context that only existed in recordings.

After: Enhanced notes with full derivations, physical intuition, and practical implementation details — all following narrative-first style. Each section now explains *why* before *what*.

## Red Flags - STOP and Re-Read

- About to Edit without Reading current section first
- About to answer a question without editing the notes
- Starting a section with a list or formula (no narrative intro)
- Using italics instead of **bold** for emphasis
- Writing "we will explore" or "as we can see"
- Processing course records sequentially instead of in parallel
- Editing entire document at once without todo tracking
- About to use a symbol ($w_i$, $\mathbf{u}_i$, etc.) without defining it first
- Assuming slide content is the complete lecture — slides are outlines, not full content
- Copying transcription text into notes without cross-referencing slides for accuracy
- Expecting every formula to be read aloud in the recording — extract keywords instead

**All of these mean:** Stop, re-read the skill, and follow the correct approach.

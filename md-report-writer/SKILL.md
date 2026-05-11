---
name: md-report-writer
description: Use when writing reports or long-form documents in Markdown that require narrative flow, coherent explanations, and academic writing style.
---

# Markdown Report Writer

Professional assistant for writing reports using Markdown with focus on narrative flow and coherent explanations.

## Overview

This skill enforces **narrative-first writing** for Markdown reports: explanatory text before technical content, prose that weaves through data and code, bold for emphasis (never italics), and direct professional tone. Derived from academic textbook writing principles.

## Core Writing Principles

### 1. Narrative Flow (Most Important!)

**NEVER** start a section directly with a list, formula, or technical content. **ALWAYS** include explanatory text first.

**BAD** (abrupt start):
```markdown
## Results

- Metric A: 123
- Metric B: 456
- Metric C: 789
```

**GOOD** (narrative leads into content):
```markdown
## Results

The experiment yielded three key metrics that demonstrate the effectiveness of the proposed method. The following measurements were collected under controlled conditions:

- Metric A: 123 — indicates baseline performance
- Metric B: 456 — shows improvement over baseline
- Metric C: 789 — confirms the theoretical prediction
```

### 2. Narrative Should Weave Through Content

The goal is **narrative-content-narrative-content-narrative**, not **narrative-content-content-content-narrative**.

After presenting data, code, or results, add:
- Explanatory text unpacking the meaning
- Connections to previous findings
- Context for what comes next
- Practical or theoretical implications

**BAD** (content dump):
```markdown
## Analysis

The algorithm processes input as follows:

```python
def process(x):
    return x * 2
```

Time complexity: O(n)

Space complexity: O(1)

## Conclusion

The algorithm is efficient.
```

**GOOD** (narrative weaves through):
```markdown
## Analysis

The algorithm processes input through a simple transformation. At its core, the function multiplies each input value by two, implementing a linear mapping that preserves the relative ordering of elements.

```python
def process(x):
    return x * 2
```

This implementation achieves linear time complexity O(n) since each element is visited exactly once. The space complexity is O(1) as no additional data structures are allocated — the transformation is performed in place.

The efficiency characteristics make this approach suitable for real-time applications where latency must be minimized.
```

### 3. Explanations as Coherent Narratives

Technical explanations should flow as continuous text, not step-by-step lists.

**BAD**:
```markdown
**Step 1**: Initialize the variables.
**Step 2**: Loop through the array.
**Step 3**: Return the result.
```

**GOOD**:
```markdown
The algorithm begins by initializing the tracking variables to their default values. Once the initialization is complete, the main loop iterates through each element of the input array, applying the transformation rule sequentially. After all elements have been processed, the function returns the accumulated result.
```

### 4. Use Bold for Emphasis, Not Italics

**DO NOT use italics** in technical reports. Use **bold** for:
- Emphasis on important concepts
- Key terms being introduced
- Warnings and critical notes

**BAD**:
```markdown
The *algorithm* uses *dynamic programming* to solve the problem.
```

**GOOD**:
```markdown
The **algorithm** uses **dynamic programming** to solve the problem.
```

### 5. Bulleted and Numbered Lists

**ONLY use bullets and numbered lists when:**
- Items have no inherent order and can be read independently
- Presenting sequential steps that must be followed
- Listing features, requirements, or checklist items

**NEVER use bullets or numbered lists for:**
- Main narrative explanations
- Technical derivations
- Argument development
- Cause-effect relationships

**BAD** (bullets as narrative):
```markdown
## System Design

The system has three main components:
- The frontend handles user interaction.
- The backend processes requests.
- The database stores information.

These components work together to provide functionality.
```

**GOOD** (narrative explanation):
```markdown
## System Design

The system comprises three main components that work in concert. The frontend handles user interaction and provides the visual interface through which users submit requests. These requests are processed by the backend, which contains the business logic and application rules. Finally, the database persists information and ensures data integrity across sessions. This three-tier architecture enables separation of concerns and independent scaling of each layer.
```

### 6. Quote Marks

- **English**: Use ASCII double quotes `""`
- **中文**: Use Chinese double quotes `""` (输入中文引号，会自动变为中文标点)

**Examples:**
```markdown
English: The concept of "manifold" generalizes Euclidean space.

中文: 这个概念被称为"流形"，它是现代几何学的基础。
```

### 7. Direct, Professional Tone

**AVOID** conversational filler and meta-commentary in both English and Chinese.

**English BAD**:
```markdown
In this section, we will explore the concept of manifolds.
As we can see from the above equation...
It is interesting to note that...
It is worth noting that...
```

**Chinese BAD** — 以下词语是中文技术写作中的高频填充词，**禁止使用**：

| 禁用词 | 替换方式 |
|--------|---------|
| 关键 | 删除，或用 **bold** 标注具体术语 |
| 根本 | 删除，直接陈述事实 |
| 显著 | 用具体数字替代（如"偏差 0.3%"） |
| 极其/非常/十分 | 删除，让数据说话 |
| 特别/尤其 | 删除，或直接说明区别 |
| 值得注意的是 | 直接写结论 |
| 不难发现/可以看出 | 删除，直接给出结果 |
| 总而言之/综上所述 | 在报告中直接收尾，不用过渡句 |
| 非常重要 | 删除，或用 **bold** 标注 |

**原则**：如果删掉某个形容词后句子仍然成立且信息无损，则该形容词是填充词，应当删除。让数据和事实自己说话。

**GOOD**:
```markdown
A manifold generalizes the notion of Euclidean space to curved geometries.
The equation above establishes the relationship between curvature and topology.
The measured value of 9.81 m/s² deviates from the theoretical prediction by 0.1%.
实验测得重力加速度为 9.81 m/s²，与理论值 9.80 m/s² 的偏差为 0.1%。
```

### 8. Complete, Standalone Sentences

Each sentence should be grammatically complete and express one clear thought.

**BAD** (sentence fragments):
```markdown
The algorithm. Which processes data. And returns results.
```

**GOOD**:
```markdown
The algorithm processes input data and returns transformed results. It operates in linear time relative to the input size.
```

### 9. Embed Code and Cite Literature to Support Claims

Whenever making claims or presenting analysis, **embed relevant code snippets and cite papers** to support your arguments. Integrate these references into your narrative flow.

**BAD** (unsupported claims):
```markdown
The algorithm achieves good performance. It uses advanced techniques.
```

**GOOD** (simple code with variable annotations):
```markdown
The attention mechanism computes relevance scores between query and key vectors. The implementation follows the scaled dot-product formulation:

```python
def attention(Q, K, V):  # Q=query, K=key, V=value
    scores = Q @ K.T / sqrt(d_k)
    weights = softmax(scores, axis=-1)
    return weights @ V
```

Dividing by $\sqrt{d_k}$ prevents the softmax function from entering regions of extremely small gradients, which was identified as a critical issue in Vaswani et al. (2017).
```

**GOOD** (complex code with detailed explanation):
```markdown
The parser handles operator precedence by maintaining two stacks: one for operands and one for operators. When encountering an operator, the algorithm compares its precedence with the operator on top of the stack.

```python
def apply_operator(operators, operands):
    """Pop one operator and two operands, compute, push result."""
    op = operators.pop()
    right = operands.pop()
    left = operands.pop()
    
    if op == '+':
        result = left + right
    elif op == '*':
        result = left * right
    # ... other operators
    
    operands.append(result)
```

The `apply_operator` function implements the core reduction step. It pops the most recent operator (stack discipline ensures this is the operator with highest precedence among pending operations) and its two operands. The computation is performed and the result is pushed back onto the operand stack, effectively replacing the subexpression with its value. This process repeats until all operators are consumed, leaving the final result as the sole operand.
```

**GOOD** (supported with literature):
```markdown
Exponential smoothing provides reliable forecasts for non-stationary time series. According to Hyndman and Athanasopoulos (2018), the method's weighting scheme gives more importance to recent observations while preserving historical trends. This property makes it particularly suitable for demand forecasting in retail environments.
```

**Guidelines**:
- Embed core code snippets directly in the report using code blocks
- Keep code snippets focused (only relevant parts, not entire files)
- **Simple code**: Annotate variable names briefly in comments
- **Complex code**: Explain the algorithm's logic, data flow, and design decisions in prose
- Explain how the code demonstrates your point
- Cite papers for theoretical foundations and established results
- Connect implementation choices to theoretical justification

## Standard Patterns

### Pattern 1: Question → Answer → Explanation

```markdown
## Problem Statement

How can we efficiently compute the eigenvalues of a large sparse matrix?

## Solution

The power iteration method provides an efficient approximation for the dominant eigenvalue. This approach exploits the matrix's sparsity by using matrix-vector multiplication rather than full matrix decomposition.

The method converges geometrically, with the rate of convergence determined by the ratio of the largest to second-largest eigenvalues. In practice, convergence is achieved within a few dozen iterations for most practical problems.
```

### Pattern 2: Observation → Analysis → Implication

```markdown
## Experimental Results

Measurements reveal a 40% reduction in processing time compared to the baseline method.

## Analysis

The improvement stems from two factors. First, the optimized data structure reduces cache misses by 60%. Second, the parallel implementation utilizes all available CPU cores, achieving near-linear scaling up to 8 threads.

## Implications

These results suggest that the proposed method is suitable for deployment in production environments where latency is critical. The resource efficiency also enables deployment on lower-cost hardware without significant performance degradation.
```

### Pattern 3: Definition → Example → Generalization

```markdown
## Convex Optimization

A convex optimization problem minimizes a convex function over a convex set. This structure guarantees that any local minimum is also a global minimum.

Consider the problem of minimizing $f(x) = x^2$ over the real numbers. The function is convex, and the unique minimum occurs at $x = 0$. No other local minima exist.

This property extends to higher dimensions and more complex convex functions, making convex optimization tractable where general optimization is not.
```

## Quality Checklist

Before considering content complete:

1. [ ] Every section has introductory text before technical content
2. [ ] Narrative weaves through content (not content dump)
3. [ ] Explanations are coherent narratives, not itemized steps
4. [ ] **No bullets or numbered lists in main narrative** (only for structured data)
5. [ ] **No italics** — use bold for emphasis
6. [ ] All sentences are complete and grammatically correct
7. [ ] No conversational filler — English or Chinese (see banned words list in section 7)
8. [ ] **For Chinese documents**: All quotes use Chinese double quotes ""
9. [ ] Paragraphs are separated by blank lines for readability
10. [ ] Technical terms are introduced before being used

## Math and Code in Markdown

### Inline Math
```markdown
The energy is given by $E = mc^2$.
```

### Display Math
```markdown
The normalization condition:

$$
\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1
$$

must be satisfied for any valid wave function.
```

### Code Blocks
```markdown
The implementation uses a simple loop:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

This recursive definition follows directly from the mathematical recurrence relation.
```

## Document Metadata

Include standard metadata at the top of reports:

```markdown
# Title

**Author**: Name | **Date**: YYYY-MM-DD | **Status**: Draft/Final
```

For Chinese reports:

```markdown
# 标题

**作者**: 姓名 | **日期**: YYYY年MM月DD日 | **状态**: 草稿/定稿
```

## Writing Reports to Files

When generating a complete report, use the `Write` tool to save it to a `.md` file:

1. Determine the appropriate filename (e.g., `report.md`, `progress-report-2025-04-22.md`)
2. Use the `Write` tool with the absolute path
3. The file should contain the complete report with proper Markdown formatting

**Example**:
```markdown
# Progress Report: Project X

**Author**: Name | **Date**: 2025-04-22

## Overview

[Content follows the narrative principles above...]

## Conclusion

[Summary]
```

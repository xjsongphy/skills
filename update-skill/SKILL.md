---
name: update-skill
description: Use when updating existing skills based on conversation feedback, user corrections, or identified improvements.
---

# Update Skill

Update existing skills based on user feedback and corrections during conversation. This skill learns from the conversation to improve future outputs.

## When to Use

Call this skill when:
1. A skill-generated output required manual corrections during conversation
2. User provided specific feedback on style, format, or content preferences
3. Multiple iterations were needed to get the output right
4. User expressed satisfaction after corrections and wants these preferences remembered

## How to Use

After the conversation reaches a satisfactory state, invoke this skill:

```
/update-skill <skill-name>
```

Example:
```
/update-skill md-report-writer
```

When called, the AI will:
1. Manually review the conversation for feedback and corrections
2. Read the target skill file
3. Identify which guidelines need updating based on the conversation
4. Manually apply updates to the skill file
5. Commit changes to git

## What Gets Updated

The skill looks for these types of feedback in the conversation:

### Style Corrections
- Tone changes (formal → casual, etc.)
- Formatting preferences (bullet points vs paragraphs, etc.)
- Emphasis changes (bold vs italics, etc.)

### Content Structure
- Section ordering preferences
- What content should come first (narrative before data, etc.)
- Level of detail desired

### Language-Specific Rules
- Quote mark preferences
- Punctuation conventions
- Terminology preferences

### Code Presentation
- When to include full code vs snippets
- How much explanation code needs
- Comment style preferences

### Citation and References
- When to cite papers/code
- How to format citations
- What level of documentation is required

## Process

When you invoke `/update-skill <skill-name>`, the AI will:

1. **Review the conversation** to identify your feedback, corrections, and refinements

2. **Read the target skill file** to understand current guidelines

3. **Identify what needs updating** by matching your feedback to specific guidelines

4. **Update the skill file** manually based on what was learned
   - Add new guidelines if needed
   - Clarify ambiguous existing guidelines
   - Add examples from the conversation if helpful

5. **Commit to git** with a descriptive message explaining what was learned

## Example Scenarios

**Scenario 1**: User asked for more detailed code explanations
```
Conversation: User said "这个代码太复杂了，需要详细解释每一步的作用"
Action: Update the code explanation guidelines to require detailed explanations
for complex code, not just variable annotations.
```

**Scenario 2**: User preferred different quote marks
```
Conversation: User said "中文用中文的双引号！"
Action: Update the quote marks guideline to specify Chinese quotes for Chinese text.
```

**Scenario 3**: User wanted narrative before data
```
Conversation: User said "不要直接开始列表，先解释一下背景"
Action: Add/clarify the "narrative first" principle with stronger language.
```

## Output Format

After updating, the skill reports:
- Which skill was updated
- What changes were made
- Git commit details

Example:
```
✓ Updated md-report-writer
  - Added: Complex code requires detailed logic explanation
  - Modified: Distinguished simple vs complex code handling
  - Committed: a5e0e09
```

## Limitations

- Only updates skills in `/Users/xjsongphy/.claude/skills/`
- Cannot modify skill metadata (name, description)
- Requires user to explicitly call the skill
- Does not automatically update from every conversation

## Best Practices

1. **Call when satisfied**: Invoke this skill only after the output meets user expectations
2. **Be specific**: The skill works best with concrete feedback patterns
3. **Review changes**: The skill will show what it changed; verify it captured the right lesson
4. **Iterative refinement**: Multiple conversations may be needed to fully capture a preference

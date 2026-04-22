# Claude Code Skills

[中文版 README](README_zh.md)

A collection of specialized skills for Claude Code to enhance AI performance on specific tasks.

## Overview

These skills provide professional guidance for Claude Code in specific domains, ensuring outputs meet expected format, style, and quality requirements.

## Available Skills

### latex-textbook-writer

**Purpose**: Write professional mathematics textbooks using XeLaTeX

**Features**:
- Definition/theorem box styles
- Correct color scheme (definitions in green, theorems in orange, examples in blue)
- Academic narrative style (explanation before definition)
- English and Chinese template support

**Use Cases**: Mathematics textbook chapters, LaTeX paper formatting, academic documents

**Invoke**: `/latex-textbook-writer`

---

### md-report-writer

**Purpose**: Write professional Markdown reports

**Features**:
- Narrative flow (explanation before technical content)
- Coherent explanations (not step-by-step lists)
- Direct, professional tone (no conversational filler)
- Bold emphasis (no italics)
- Embed code snippets and cite literature
- Simple code: annotate variables; complex code: explain logic in detail

**Use Cases**: Technical reports, progress reports, project documentation, meeting notes

**Invoke**: `/md-report-writer`

---

### update-skill

**Purpose**: Update existing skills based on conversation feedback

**Workflow**:
1. Generate output with a skill
2. Refine through conversation until satisfied
3. Call `/update-skill <skill-name>` to update the skill
4. Next invocation applies the improvements automatically

**Use Cases**: Any situation where skill output needs iterative refinement

**Invoke**: `/update-skill <skill-name>`

---

## Repository Structure

```
skills/
├── latex-textbook-writer/    # LaTeX textbook writing
│   └── SKILL.md
├── md-report-writer/         # Markdown report writing
│   └── SKILL.md
├── update-skill/             # Skill update utility
│   └── SKILL.md
└── README.md                 # This file
```

## Usage

### Invoking a Skill

Use the command directly in Claude Code:

```
/skill-name
```

Examples:
```
/latex-textbook-writer
/md-report-writer
```

### Updating a Skill

When a skill's output needs adjustment:

1. Provide feedback in the conversation
2. Once satisfied, call:
   ```
   /update-skill skill-name
   ```
3. AI analyzes the conversation and updates the skill file
4. Changes are automatically committed to git

## Development

### Adding a New Skill

1. Create a new folder under `skills/`
2. Create `SKILL.md` with:
   - Frontmatter (name, description)
   - Detailed usage guidelines
   - Examples and best practices
3. Commit to git

### Skill File Format

```markdown
---
name: skill-name
description: Brief description
---

# Skill Title

Detailed skill documentation...

## When to Use
...

## Core Principles
...

## Examples
...
```

## Contributing

These skills are customized for personal use. To modify:
1. Edit the corresponding `SKILL.md` file directly
2. Commit to git
3. Or use `/update-skill` to iteratively improve through conversation

## License

MIT License

---

**Author**: xjsongphy
**Repository**: [github.com:xjsongphy/skills.git](https://github.com/xjsongphy/skills)

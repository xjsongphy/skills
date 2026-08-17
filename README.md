# Claude Code Skills

[中文版 README](README_zh.md)

A collection of specialized skills for Claude Code to enhance AI performance on specific tasks.

## Overview

These skills provide professional guidance for Claude Code in specific domains, ensuring outputs meet expected format, style, and quality requirements.

## Available Skills

### writer

**Purpose**: Route modular academic and technical writing across report,
explanation, and textbook primary types, with bounded variants, source objects,
cross-type lenses, Markdown, LaTeX, or Typst formats.

**Features**:
- Shared narrative, evidence, citation, and review rules
- Language-neutral document-type modules
- Markdown, LaTeX, and Typst syntax modules
- Format integrations only where a type-format or package interaction adds real rules
- LaTeX textbook templates and source-grounded explanation review assets

**Use Cases**: Reports, lab reports, paper explanations, mathematics textbooks,
technical Markdown, LaTeX, and Typst documents

**Invoke**: `/writer`

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

### syncthing-cleanup

**Purpose**: Clean up unexpected items in Syncthing sync folders

**Features**:
- Automatically identify and clean conflict files (`.sync-conflict-*`)
- Delete empty directories in encrypted folders
- Clean temporary files (`*.swp`, `*~`, `.DS_Store`, `Thumbs.db`, `*.tmp`)
- Remove broken symbolic links
- Integrated with Syncthing REST API for automatic rescan after cleanup
- Includes executable Python cleanup script
- Supports dry-run mode to preview deletions
- Cross-platform support (Linux, macOS, Windows WSL)

**Use Cases**: Syncthing showing unexpected items, sync conflicts, periodic cleanup of sync folders

**Invoke**: `/syncthing-cleanup`

**Script Usage**:
```bash
# Interactive mode
python3 scripts/cleanup_syncthing.py

# Preview mode
python3 scripts/cleanup_syncthing.py --dry-run

# Automatic cleanup
python3 scripts/cleanup_syncthing.py --yes

# Clean specific folders
python3 scripts/cleanup_syncthing.py --folders ~/Develop ~/Codes
```

---

### browser

**Purpose**: Control Chrome browser via REST API for browser automation tasks

**Features**:
- Full Selenium control via HTTP endpoints
- Anti-detection (background playback, automation hiding)
- Element find/click/input/screenshot/JS execution
- Window management (switch/close)
- Auto random delays to simulate human behavior

**Use Cases**: Web automation, auto-login, course watching, form filling, web scraping with browser

**Invoke**: `/browser`

**Server Project**: `D:\Develop\AgentInBrowser`

---

## Repository Structure

```
skills/
├── writer/                   # Modular writing router and references
│   ├── SKILL.md
│   ├── MAINTENANCE.md
│   └── references/
├── update-skill/             # Skill update utility
│   └── SKILL.md
├── syncthing-cleanup/        # Syncthing cleanup utility
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── cleanup_syncthing.py
│   │   └── test_skill.py
│   ├── references/
│   │   └── implementation_details.md
│   └── evals/
│       └── evals.json
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
/writer
```

### Updating a Skill

When a skill's output needs adjustment:

1. Provide feedback in the conversation
2. Once satisfied, call:
   ```
   /update-skill skill-name
   ```
3. AI analyzes the conversation and updates the skill file
4. Review the diff and commit only when explicitly requested

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

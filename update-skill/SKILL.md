---
name: update-skill
description: Use when updating an existing skill based on conversation feedback, user corrections, or identified improvements; classify feedback and edit the canonical module without creating duplicate rules.
---

# Update Skill

Update an existing skill from explicit conversation feedback. Read the target
skill before editing, identify the smallest canonical file that owns the rule,
apply the change, and validate links and metadata afterwards.

## Use

Call this skill only after feedback or a correction is concrete enough to store:

```
/update-skill <skill-name>
```

Do not update a skill merely because an output was generated. The conversation
must contain a durable preference, rule, boundary, or workflow correction.

## Writer routing

When the target is `writer`, first read:

```
/Users/xjsongphy/.agents/skills/writer/MAINTENANCE.md
```

Classify the feedback as a shared rule, primary type, type add-on, lens,
source object, domain, format, format integration, reviewer, check, or routing
rule. Edit
the corresponding canonical module. Update `writer/SKILL.md` only when the
feedback changes module selection or a hard boundary. If a feedback item says
that a repository implementation must not be treated as a paper fact, update
`writer/references/objects/paper.md` and/or `objects/repository.md`, not a
generic explanation paragraph.
If it changes module selection, reviewer activation, format precedence, or
compatibility behavior, update `writer/SKILL.md` only for that routing contract.

Keep one rule in one canonical location. Do not create a compatibility wrapper,
copy an old skill, or add a format integration merely to repeat rules already
expressed by a type and a format. During an approved migration window, an
existing legacy entry point may remain as a thin wrapper that routes to the
canonical writer modules; it must not own copied rules. If a cross-module
contract changes, update the owning module first and make only the smallest
link or route adjustment.

## Process

1. Review the conversation and state the durable feedback in one sentence.
2. Locate the target skill under the active skills root. Do not assume
   `~/.claude/skills`; use the actual configured skills repository.
3. Read the target `SKILL.md` and any maintenance/index file it names.
4. Read the canonical module and nearby references needed to avoid duplication.
5. Apply the smallest edit that captures the feedback; preserve unrelated user
   changes.
6. Search for stale paths, duplicate wording, and old entry-point names. For
   writer, check `MAINTENANCE.md`, the module map, format integrations, and
   any retained thin wrappers.
7. Validate YAML frontmatter, referenced files, and relevant evals. Compile or
   render only when the changed rule affects source or layout.
8. Report the changed files, the learned rule, and validation results. Create a
   git commit only when the user explicitly requests one or the surrounding
   workflow explicitly requires it.

## Feedback categories

- Style: tone, sentence shape, paragraph density, punctuation, or emphasis.
- Structure: section order, narrative before elements, or argument shape.
- Source policy: citations, evidence hierarchy, claim identity, or unknowns.
- Format syntax: Markdown, LaTeX, Typst, or another source language.
- Type behavior: report, explanation, textbook, or a bounded variant.
- Workflow: routing, reviewer isolation, rendering, or validation gates.

Prefer a concise rule with a concrete trigger and expected behavior. Preserve
examples only when they clarify a fragile boundary.

---
name: writer
description: Route the creation, revision, audit, or explanation of academic and technical documents. Use for reports, experiment reports, paper or repository explanations, textbook material, and their Markdown, LaTeX, or Typst source; compose one primary type with optional lenses, source objects, domains, format, and format integrations.
---

# Writer

`writer` is the directory and routing contract for academic and technical
writing. It is intentionally compositional:

> exactly one primary type + zero or more lenses + zero or more source objects
> + zero or more domains + one source format + optional format integrations

The module selected for a task is the canonical home of that rule. Do not copy
the same rule into a type, format integration, or reviewer.

For maintenance or feedback-driven updates, read `MAINTENANCE.md` before
choosing a file to edit.

## Route a request

1. Identify the task: draft, revise, audit, explain, translate, or compile.
2. Select exactly one primary type under `references/types/`:
   `report`, `explanation`, or `textbook`.
3. If the primary type has a bounded variant or component, load it from
   `references/type-addons/`: `report-experiment` or `textbook-exercises`. An
   add-on does not become a
   second primary type.
4. Add zero or more cross-type lenses under `references/lenses/`:
   `derivation-analysis` for derivation-heavy exposition and
   `mechanism-analysis` for input/output/state/control-flow depth. Load the
   mechanism depth checklist only when the task needs its detailed questions.
5. Add source objects under `references/objects/` when the task relies on
   identifiable evidence sources: `paper`, `repository`, or both. Add a
   domain module only when the subject has domain-specific evidence or terms.
6. For a source artifact, select exactly one format under `references/formats/`:
   Markdown, LaTeX, or Typst. Chat-only prose may omit a format.
7. Resolve exactly one format with this precedence: existing document format
   > explicit user format > compatibility-wrapper default > writer default
   (Markdown). Load a format integration only for a real type-format or package interaction that
   cannot be expressed cleanly in the type and format modules. The initial
   exception integrations are `scholia-typst` and `textbook-latex` under
   `references/format-integrations/`.
8. Load `references/common/narrative-and-evidence.md` for every reader-facing
   document. Its claim ledger contract is the shared infrastructure for
   source-dependent claims. Add `common/evidence-and-citations.md` when claims
   depend on research, measurements, code, or other sources.
9. Activate reviewers and checks by contract:
   `reviewers/reader.md` by default for `type = explanation` (otherwise only
   when requested); `reviewers/source-reviewer.md` and
   `checks/source-claims.md` whenever the claim ledger is non-empty;
   `checks/prose.md` for every writer document; and
   `checks/rendered-document.md` whenever a renderable artifact is generated
   or compiled. A reviewer
   role is not a checklist: use `reviewers/reader.md` and/or
   `reviewers/source-reviewer.md` when their isolation and output contracts
   are required.

Do not load every module by default. If the request is ambiguous, preserve the
uncertainty and ask for the missing type, object, or format rather than
silently composing a large bundle.

## Module map

| Need | Load |
|---|---|
| Any reader-facing prose | `references/common/narrative-and-evidence.md` |
| Source boundaries and citations | `references/common/evidence-and-citations.md` |
| General report | `references/types/report.md` |
| Physics/engineering experiment report | `types/report.md` + `type-addons/report-experiment.md` |
| Standalone paper or repository explanation | `types/explanation.md` + active source object(s) |
| Mathematics textbook chapter | `types/textbook.md` |
| Textbook exercises and answers | `type-addons/textbook-exercises.md` |
| Derivation-heavy exposition | `lenses/derivation-analysis.md` |
| Mechanism/deep pipeline analysis | `lenses/mechanism-analysis.md` |
| Detailed mechanism questions | `lenses/mechanism-analysis/depth-checklist.md` |
| Paper evidence policy | `objects/paper.md` |
| Repository evidence policy | `objects/repository.md` |
| GPU-kernel subject | `domains/gpu-kernel.md` |
| Markdown source | `formats/markdown.md` |
| LaTeX source | `formats/latex.md`; use the separate `latex-compile` skill for builds |
| Typst source | `formats/typst.md` |
| Scholia + Typst interaction | `format-integrations/scholia-typst.md` |
| LaTeX textbook interaction | `format-integrations/textbook-latex.md` |
| Prose audit | `checks/prose.md` |
| Source-claim audit | `checks/source-claims.md` |
| Rendered-document audit | `checks/rendered-document.md` |
| Source-grounded review | `reviewers/source-reviewer.md` |
| Draft-only reader simulation | `reviewers/reader.md` |

## Composition examples

- **Ordinary paper explanation**: common prose + evidence + explanation +
  paper object + Markdown/LaTeX/Typst format as needed. Do not load repository,
  derivation, or mechanism lenses unless requested by the source and audience.
- **Repository explanation**: common prose + evidence + explanation +
  repository object. Paper facts are out of scope unless a paper object is also
  active.
- **TENG Typst explanation**: explanation + paper + derivation-analysis +
  mechanism-analysis + Typst; add the domain module only if its subject policy
  is needed.
- **GPU-kernel paper/repository explanation**: explanation + paper + repository
  + gpu-kernel + mechanism-analysis + chosen format.
- **Ordinary Typst report**: report + Typst. Do not load `scholia-typst`.
- **Experiment report**: report + type-addons/report-experiment + chosen format; add
  measurement evidence and rendered checks when applicable.
- **LaTeX textbook**: textbook + LaTeX + textbook-latex; add exercises only
  when exercises are part of the deliverable.

## Reviewer and check activation

Use the following defaults unless the user explicitly narrows the task:

| Module | Trigger |
|---|---|
| `reviewers/reader.md` | `type = explanation`; other types only when requested. |
| `reviewers/source-reviewer.md` | claim ledger is non-empty, especially when source objects are active. |
| `checks/prose.md` | every writer document. |
| `checks/source-claims.md` | claim ledger is non-empty. |
| `checks/rendered-document.md` | a renderable document is generated or compiled. |

## Format resolution

When the user edits an existing source file, preserve its format even if the
user does not repeat it. Otherwise use explicit user format, then the default
of a compatibility wrapper, and finally Markdown as the writer default.

## Review and evidence boundaries

- `objects/` defines what a source can establish; it does not define the prose
  shape of the deliverable.
- `lenses/` adds questions or narrative behavior that can apply to more than
  one primary type.
- `reviewers/` defines isolated agent roles and structured verdicts. A source
  reviewer reads the active object policies; it is not paper-only.
- Never turn a diagram arrow, repository convention, or plausible implementation
  into a source fact without evidence. Mark an omitted detail `not specified`.
- Keep paper claims, repository behavior, and clearly labeled inference
  separate, including when both objects are active.

## Boundaries

- Do not invent data, citations, theorem steps, experimental conditions,
  implementation details, or numerical results.
- Follow a user-provided journal, course, laboratory, or house template before
  generic conventions.
- Treat `autoreport` as a separate orchestration skill. When it delegates
  report-body writing, route only the body through this skill; do not absorb its
  data analysis, plotting, or orchestration responsibilities.
- Treat `latex-compile` as a separate build and diagnosis skill. Do not embed
  its compiler workflow here.
- The canonical rules live under `writer`; any legacy user-facing entry point
  retained during migration must be a thin wrapper and must not own a copied
  rule. Update feedback against the canonical module, not the wrapper.

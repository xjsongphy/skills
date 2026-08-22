---
name: writer
description: Route the creation, revision, audit, or explanation of academic and technical documents. Use for reports, experiment reports, paper or repository explanations, textbook material, and their Markdown, LaTeX, or Typst source; compose one primary type with optional lenses, source objects, domains, format, and format integrations.
---

# Writer

`writer` is the directory and routing contract for academic and technical
writing. It is intentionally compositional:

> exactly one primary type + zero or more lenses + zero or more source objects
> + zero or more domains + one format for artifacts (zero for chat-only prose)
> + optional format integrations

The module selected for a task is the canonical home of that rule. Do not copy
the same rule into a type, format integration, or reviewer.

For maintenance or feedback-driven updates, read `MAINTENANCE.md` before
choosing a file to edit.

## Route a request

1. Identify the task: draft, revise, audit, explain, or translate. Compilation
   and build diagnosis belong to the separate `latex-compile` skill. Also identify
   whether this is a brief chat answer/local lookup or a substantial persistent
   artifact. The full source-grounded workflow applies conditionally to
   substantial explanations; reports and textbooks follow their type contracts.
2. Select exactly one primary type under `references/types/`:
   `report`, `explanation`, or `textbook`.
3. If the primary type has a bounded variant or component, load it from
   `references/type-addons/`: `report-experiment` or `textbook-exercises`. An
   add-on does not become a
   second primary type.
4. Add zero or more cross-type lenses under `references/lenses/`:
   `derivation-analysis` for derivation-heavy exposition and
   `mechanism-analysis` for input/output/state/control-flow depth. Activate a
   lens when the source or requested deliverable contains the corresponding
   analysis; do not require the user to name the lens explicitly. The
   mechanism lens contains an optional deep-dive question bank; use only the
   relevant groups.
5. Add source objects under `references/objects/` when the task relies on
   identifiable evidence sources: `paper`, `repository`, or both. Add a
   domain module only when the subject has domain-specific evidence or terms.
6. For a source artifact, select exactly one format under `references/formats/`:
   Markdown, LaTeX, or Typst. Chat-only prose selects no format.
7. Resolve exactly one format according to `Format resolution` below. Load a
   format integration only for a real type-format or package interaction that
   cannot be expressed cleanly in the type and format modules. The initial
   exception integrations are `scholia-typst` and `textbook-latex` under
   `references/format-integrations/`.
8. Load `references/common/writing.md` for every reader-facing output.
   Add `common/evidence-and-citations.md` when claims depend on research,
   measurements, code, or other sources; that module owns the shared ledger.
9. Activate reviewers and checks according to the `Reviewer and check
   activation` matrix below. A reviewer role is not a checklist: use
   `reviewers/reader.md` and/or `reviewers/source-reviewer.md` when their
   isolation and output contracts are required.

Do not load every module by default. If the request is ambiguous, preserve the
uncertainty and ask for the missing type, object, or format rather than
silently composing a large bundle.

## Module map

| Need | Load |
|---|---|
| Any reader-facing prose and technical exposition | `references/common/writing.md` |
| Source boundaries and citations | `references/common/evidence-and-citations.md` |
| General report | `references/types/report.md` |
| Physics/engineering experiment report | `types/report.md` + `type-addons/report-experiment.md` |
| Standalone paper or repository explanation | `types/explanation.md` + active source object(s) |
| Mathematics textbook chapter | `types/textbook.md` |
| Textbook exercises and answers | `type-addons/textbook-exercises.md` |
| Derivation-heavy exposition | `lenses/derivation-analysis.md` |
| Mechanism/deep pipeline analysis | `lenses/mechanism-analysis.md` |
| Layered technical survey | the conditional progressive-depth section in `common/writing.md` |
| Substantial document skeleton | the conditional topic-sentence section in `common/writing.md` |
| Shorten or compress a draft | the conditional length-revision section in `common/writing.md` |
| Detailed mechanism questions | the optional deep-dive section in `lenses/mechanism-analysis.md` |
| Paper evidence policy | `objects/paper.md` |
| Repository evidence policy | `objects/repository.md` |
| GPU-kernel subject | `domains/gpu-kernel.md` |
| Markdown source | `formats/markdown.md` |
| LaTeX source | `formats/latex.md`; use the separate `latex-compile` skill for builds |
| Typst source | `formats/typst.md` |
| Scholia + Typst interaction | `format-integrations/scholia-typst.md` |
| LaTeX textbook interaction | `format-integrations/textbook-latex.md` |
| Document gates | `checks/document.md` (run the applicable sections) |
| Source-grounded review | `reviewers/source-reviewer.md` |
| Draft-only reader simulation | `reviewers/reader.md` |

## Composition examples

- **Ordinary paper explanation**: explanation + paper object. Add lenses and
  choose the format only when the source or deliverable requires them.
- **Repository explanation**: explanation + repository object. Paper facts are
  out of scope unless a paper object is also active.
- **TENG Typst explanation**: explanation + paper + derivation-analysis +
  mechanism-analysis + Typst; add the domain module only if its subject policy
  is needed.
- **GPU-kernel paper/repository explanation**: explanation + paper + repository
  + gpu-kernel + mechanism-analysis + chosen format.
- **Ordinary Typst report**: report + Typst. Do not load `scholia-typst`.
- **Experiment report**: report + report-experiment; default to LaTeX when no
  existing or explicit format is supplied, then add evidence and rendered
  checks when applicable.
- **LaTeX textbook**: textbook + LaTeX + textbook-latex; add exercises only
  when exercises are part of the deliverable.

## Reviewer and check activation

Use the following defaults unless the user explicitly narrows the task:

| Module | Trigger |
|---|---|
| `reviewers/reader.md` | substantial/persistent `type = explanation`; other types only when requested. |
| `reviewers/source-reviewer.md` | substantial source-grounded work with a non-empty claim ledger, or an explicit source audit request. Brief answers use minimal source verification. |
| coordination rules below | both Reader and Source Reviewer are active, or a delegated persistent review is requested; not for a brief chat answer. |
| `checks/document.md` prose section | every document artifact; brief chat answers and local lookups do not require the document gate. |
| `checks/document.md` source section | claim ledger is non-empty. |
| `checks/document.md` rendered section | a renderable document is generated or compiled. |

## Reviewer coordination

Use these Main-agent rules when more than one isolated reviewer is active or a
delegated persistent review is requested. Reader comprehension and source
grounding are separate judgments; neither reviewer silently replaces the
other's role.

### Arbitration

- Evidence boundaries from the active object policies cap every completeness
  request. Reader preference cannot turn an undocumented detail into a fact.
- If a comprehension issue blocks the central mechanism, it takes priority over
  stylistic brevity. Add only the smallest source-supported bridge.
- Add detail only when it serves the contribution, is source-disclosed, or is
  explicitly requested. Refuse deletion when it would break an input/output,
  condition, state-update, derivation, or evidence chain.
- Preserve `not specified` boundaries when the source is silent. A reviewer may
  recommend narrowing or labeling a claim, not filling it from general knowledge.

### Completion and release

- For a persistent artifact or delegated review, retain the structured review
  result until the task reaches its final handoff. A chat-only answer does not
  require a Reviewer YAML file to be persisted.
- If delegation is unavailable, run the same roles sequentially with the same
  source and draft isolation boundaries.
- Finish only after the applicable Reader, Source Reviewer, active lens checks,
  figure/artifact coverage, document source-claim and prose sections, and the
  rendered section have passed or their remaining limitations are explicitly
  reported.

## Format resolution

When the user edits an existing source file, preserve its format even if the
user does not repeat it. Otherwise use explicit user format, then a bounded
type/add-on default, and finally Markdown as the writer default. The default
for `report + report-experiment` is LaTeX because the experiment contract and
its established report assets are LaTeX-oriented; an explicit format always
overrides it.

For revisions, read the current document before editing. Inspect the working
tree diff and relevant Git history when they reveal user changes or durable
revision preferences. Preserve unrelated edits and do not restore deleted
material merely because it existed in an older version.

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
- The canonical rules live under `writer`; the removed legacy entry points are
  not part of routing. Do not recreate them or copy their rules into a new
  wrapper.

# Teaching slides / 课程习题讲解幻灯片

Use for academic course slides that teach how to solve selected exercises,
especially beginner programming / 上机题讲解PPT. This is one primary type;
do not also select `report` or `textbook`. A textbook chapter, a question sheet,
a paper talk, and a product pitch are different deliverables. Apply the common
writing and evidence modules by reference rather than duplicating their rules.

## Resolve the lesson before expanding it

Identify the final exercise list and order, students' prior knowledge, the
requested solutions, and the reference deck. Treat a supplied homework set or
user-edited Markdown selection as authoritative. Match problem identity and
constraints, not just a title: two “迷宫” problems can have different movement
rules. A teacher's final “typical problems” list is a pool of possibilities,
not evidence that every algorithm was taught.

When browsing is needed, retain and verify the actual readable assignment
links. A matching problem ID does not prove that a standalone URL and a
course-scoped URL have the same access. Use the requested read-only backend
and rate limits. Do not submit solutions, edit assignments, or publish slides
without authorization.

For a multi-step deck, keep a short TODO list covering selection, content,
rendering, image review, and handoff. Continue routine authorized edits without
asking for approval after each phase.

## Classroom content contract

Default to **solution explanation, not a question booklet**. Keep full original
statements and formal sample input/output in linked Markdown when requested;
do not automatically put them on slides. A short task cue or small execution
example is enough to start a problem. Show the full statement or full judge
sample on a slide only when the user asks for it or its exact layout is the
teaching subject.

A useful progression is: goal or tiny example → reasoning → state changes →
code. Adapt the number of slides to the explanation; do not generate a fixed
quota per exercise or a mandatory agenda/recap. Reuse an existing example
across its execution steps instead of changing data halfway through.

- Teach only prerequisites needed now. Already-taught input, loops, dictionaries,
  etc. do not acquire new introductory slides merely because they appear in code.
- Put a new method where its first use needs explanation, e.g. `enumerate` in
  position tracking, `index` in digit decoding, `startswith` in parsing records.
  Common stack/queue operations may be grouped at the front when requested.
  Do not also add a duplicate “methods used in this deck” overview.
- For an operation, show its receiver, return value, and the resulting state of
  one concrete object. Say whether table rows are independent or consecutive.
  Keep mutation distinct from return value: `reverse()` modifies a list and
  returns `None`; string `index()` returns a zero-based match position.
- Derive a non-obvious update before presenting it as code. For example,
  positional notation leads to multiply-and-add accumulation, and quotient /
  remainder explains extracting the last digit. Do not substitute a formula
  slide for the bridge to the actual variables and loop.
- Prefer the simple implementation appropriate to the stated lesson and bounds.
  Honor requests such as list-based stack or small-grid list-based BFS. Keep a
  performance caution proportionate; do not replace the chosen lesson with
  an implementation survey or a systems lecture.
- Add alternative implementations when requested or pedagogically useful.
  Clearly identify the active version and complete replacements. Commented
  alternatives in an answer file must say to run one version, not both. Preserve
  indexing conventions and the restart point after a deletion.

Student-facing slides contain the lesson, not production commentary. Omit
phrases about how the deck was made, preserving a speed comparison, or having
already taught syntax. Avoid unrequested library-selection, concurrency, and
API-family comparison pages. Keep benchmark environment, repeat counts and
reproducibility details in teacher notes / data; retain the input size, units
and scope needed to interpret any displayed timing table.

## Execution diagrams

When a learner must follow a changing state (BFS, stack matching, recursion,
queue simulation), use a small trace and successive slides / reveals. Show the
current item, pending container, state update, and termination. Fix the neighbor
or traversal order and keep it identical in code, diagrams, and explanations.
Distinguish discovered/enqueued from processed/expanded when it matters.

Compute traces from the chosen algorithm or a checked simulation rather than
hand-inventing table rows. Check the whole sequence, including repeated states,
empty containers, wraparound, and stopping. A visually polished trace with one
wrong removal or queue state is still incorrect. A teaching grid may be smaller
than the judge sample; label it as a teaching example.

## Keep materials synchronized

Maintain one selected problem list and stable problem identity. If the user
removes exercises from a Markdown document, read that current file first;
do not regenerate the old selection from cached materials. When asked to
renumber or clean up, synchronize chapter headings, answer filenames, question
files, aggregates, index records, images, and relative links. Remove deselected
materials only within the authorized scope. Do not restore files or alternative
solutions the user deleted.

For programming decks, keep independent runnable answer files. A slide may show
only relevant code fragments, but their order and indentation must preserve
the actual program; do not silently change an algorithm while shortening it.
Use the prior answer style the user chose. Split long code at logical boundaries;
avoid auto-wrapped Python indentation, dangling control headers, or a separate
page containing only a stray `break`.

For similar beginner programming decks introducing APIs, include a concise
Markdown API reminder unless the user requests slides only: operation,
short description, return value, and a small example. This is a lookup aid,
not an exhaustive standard-library manual or extra overview slides.

## Release checks

Apply `../checks/document.md` for prose, source boundaries and rendering.
For this deliverable, additionally check the selected order, consistency with
answer files, operation examples and state traces. Run suitable samples and
edge cases for new/changed algorithms or variants; use an independent oracle
where it adds confidence. Do not broaden tests merely for wording edits.

Compile/export the actual deck and **read its rendered images**. A successful
build or extracted text is not visual verification. Review every page in a
consistent overview; enlarge code, formulas, diagrams and suspect pages. After
an edit, inspect the changed render and any affected neighboring layout. Fix
clipping, line wraps and ambiguous labels without shrinking the projection
font or replacing the requested design. Never claim to have read images that
were not opened. Report the actual editable source and presentation format.

## Format

Follow the explicit format and reference first. For this user's course
exercise decks with no contrary direction, default to Typst + PDF
and load `../format-integrations/teaching-slides-typst.md`. Native PPTX or Google
Slides requests should use the available presentation skill for their renderer;
keep this type's teaching-content contract and do not silently deliver PDF in
place of an explicitly requested native format.

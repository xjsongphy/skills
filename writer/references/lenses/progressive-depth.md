# Progressive technical depth

Use this optional lens when a survey, paper explanation, or technical teaching
document must move from a readable map to operational detail and then to the
research or implementation-specific layer. It is not a mandatory structure for
every report or textbook.

## Depth sequence

1. **Reader map**: state the problem, contribution, major objects, and the
   shortest complete end-to-end picture.
2. **Mechanism layer**: expose the representations, transformations, choices,
   state updates, interfaces, and consumers needed to trace one complete run.
3. **Research layer**: explain the design rationale, assumptions, comparison
   points, limitations, and evidence that distinguish this work from a generic
   mechanism.

Do not jump to implementation detail before the reader can place it in the map.
Do not stop at a slogan when the omitted mechanism determines the conclusion.
Use the active object policies to mark which layer is source-established and
which is inference or simplification.

## Retrieval and memory systems

When relevant, trace the three paths separately:

- source → index or storage;
- query → selected context;
- trajectory or feedback → memory update or replacement.

State what is represented, how selection is made, who consumes the result, and
which observations update or replace old information. If the source is silent on
an operational detail, retain the smallest useful `not specified` boundary.

// Classroom additions to Calmly Touying 0.2.0 (MIT).
// Original template: https://typst.app/universe/package/calmly-touying/
#let blue = rgb("1d4ed8")
#let ink = rgb("172554")

#let key(body) = text(fill: blue, weight: "semibold", body)
#let lead(body) = block(above: 0pt, below: 18pt)[#text(weight: "semibold", fill: ink)[#body]]
#let hint(body) = block(above: 16pt, below: 0pt)[#text(fill: blue)[#body]]
#let small(body) = body
#let lesson-table(..cells, columns: 2, widths: none) = {
  set text(size: 20pt)
  set par(leading: 0.65em)
  table(
    columns: if widths == none { range(columns).map(_ => 1fr) } else { widths },
    stroke: none,
    align: left + horizon,
    inset: (x: 12pt, y: 12pt),
    fill: (x, y) => if y == 0 { rgb("eaf0fb") } else if calc.odd(y) { rgb("f7f9fc") } else { white },
    ..cells,
  )
}

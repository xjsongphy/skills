// Minimal course-paper starter.
// This is a clean single-column layout.
// The numbered reference block is intentional: entries are ordered by first citation.

#set document(title: "Paper Title")

#set page(
  paper: "us-letter",
  margin: 1in,
  footer: context align(center)[#counter(page).display()],
)

#set text(
  font: "Times New Roman",
  size: 12pt,
  lang: "en",
)

#set par(
  justify: false,
  first-line-indent: 0.25in,
  leading: 12pt,
  spacing: 12pt,
)

#show figure.caption: set align(left)
#show figure.caption: set text(size: 10pt)

#align(center)[
  #text(size: 12pt, weight: "bold")[Paper Title]
  #v(0.5em)
  Author Name
  #linebreak()
  Course
]

#v(1em)

Body paragraph one.

Body paragraph two.

// Add a figure by placing an image beside this file and uncommenting the block.
// #figure(
//   image("figure.png", width: 80%),
//   caption: [
//     *Figure 1.* _Figure Title._ Data from Author et al. [1]. Brief reading of the figure.
//   ],
//   numbering: none,
// )
// #v(1em)

#pagebreak()

#align(center)[#text(size: 12pt, weight: "bold")[References]]
#v(1em)

#block[
  #set par(first-line-indent: 0pt, hanging-indent: 0pt, leading: 12pt, spacing: 12pt)

  #text("[1]") Author, A., & Author, B. (Year). Title of the work. _Journal Name, Volume_(Issue), pages. https://doi.org/xxxx

  #text("[2]") Author, C. (Year). Title of the work. Publisher. https://doi.org/xxxx
]
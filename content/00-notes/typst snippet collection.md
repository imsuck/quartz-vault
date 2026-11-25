---
tags:
  - atomic
up:
created: 2026-11-25
status: open
publish: true
---

Convert content to string

https://github.com/typst/typst/discussions/3876#discussioncomment-9016808

```
#let to-string(content) = {
  if content.has("text") {
    if type(content.text) == "string" {
      content.text
    } else {
      to-string(content.text)
    }
  } else if content.has("children") {
    content.children.map(to-string).join("")
  } else if content.has("body") {
    to-string(content.body)
  } else if content == [ ] {
    " "
  }
}
```

---

Flexible caption

https://forum.typst.app/t/using-flex-caption-from-a-template-yields-long-captions-instead-of-short/7054/8

```
#let in-outline = state("in-outline", false)

#show outline: it => in-outline.update(true) + it + in-outline.update(false)

#let flex-caption(short, long) = context {
  if in-outline.get() { [#short] } else {
    if (long == []) [#strong(short)] else [#strong(short). #long]
  }
}
```

---

Manually select which equation to be numbered

https://forum.typst.app/t/how-to-conditionally-enable-equation-numbering-for-labeled-equations/977/2

```
#let eq(eq, id: none) = context {
  set math.equation(
    numbering: if id == none { none } else { numbering("(1)") },
  )

  if id == none {
    eq
  } else {
    [#eq #label(id)]
  }
}

#let eqref(label) = link(label)[(#ref(label, supplement: none))]
```

## References

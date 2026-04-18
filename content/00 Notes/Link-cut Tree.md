---
categories:
tags:
  - atomic
  - cs/dsa
  - moc
up: "[[Tree data structure]]"
created: 2026-04-10
status: open
sr-due: 2026-04-21
sr-interval: 7
sr-ease: 250
publish: true
---
Inventor: Sleator & Tarjan.
Used to maintain dynamic forests and to handle path related queries. It can also [[Subtree aggregation in Link-cut tree|manage subtree information]] to some degree.
Under the hood, LCT uses [[Splay tree|splay tree]] to manage its structure. After some time complexity analysis, you get $O(log n)$ for link, cut operations.
## Related
[[Heavy-light decomposition]]
[[Top Tree]]: swiss army knife version of a link-cut tree, capable of handling heavy-duty subtree augmentation.
## Applications
[[Speeding up Dinitz's algorithm with Link-cut tree]]
## References

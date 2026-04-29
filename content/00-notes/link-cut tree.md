---
tags:
  - cs/dsa
  - moc
up: "[[tree data structure]]"
created: 2026-04-10
status: open
sr-due: 2026-04-21
sr-interval: 7
sr-ease: 250
publish: true
---

Inventor: Sleator & Tarjan.
Used to maintain dynamic forests and to handle path related queries. It can also [[subtree aggregation in link-cut tree|manage subtree information]] to some degree.
Under the hood, LCT uses [[splay tree]] to manage its structure. After some time complexity analysis, you get $O(log n)$ for link, cut operations.

## Related

[[heavy-light decomposition]]
[[top tree]]: swiss army knife version of a link-cut tree, capable of handling heavy-duty subtree augmentation.

## Applications

[[speeding up dinitz's algorithm with link-cut tree]]

## References

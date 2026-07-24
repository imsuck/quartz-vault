---
tags:
  - reference
  - math/stats
up: "[[grouped data set]]"
created: 2026-04-22
status: open
publish: true
sr-due: 2026-06-11
sr-interval: 40
sr-ease: 250
---

h
For an n-tile of a data set with $N$ elements, the i-th n-tile is defined as:

$$
q_i = L + (i/n times N - "prev")/"freq" times W
$$

Where:

- $L$: left bound of range $[L, R)$ containing $i/n times N$
- $"prev"$: sum of previous ranges (excluding current)
- $W = R - L$

The idea is to perform [[interpolation]] on the range containing the n-tile.

## Related

[[mode of grouped data]]

## References

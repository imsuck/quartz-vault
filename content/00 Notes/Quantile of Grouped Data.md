---
categories:
tags:
  - atomic
  - math/stats
up: "[[Grouped Data]]"
created: 2026-04-22
status: open
publish: true
---

For an n-tile of a data set with $N$ elements, the i-th n-tile is defined as:

$$
q_i = L + (i/n times N - "prev")/"freq" times h
$$

Where:

- $L$: left bound of range $[L, R)$ containing $i/n times N$
- $"prev"$: sum of previous ranges (excluding current)
- $h = R - L$

## Related

[[Mode of Grouped Data]]

## References

---
tags:
  - atomic
  - math/functions
up:
created: 2026-08-07
status: open
publish: true
---

Taylor series is a way to approximate a function as a polynomial at a single point. This approximation is roughly correct near the neighborhood of the point chosen. Naturally as more terms are introduced, it becomes more accurate and converges to the actual function in infinitum.

Formula for Taylor series of $f: RR->RR$ at $a in RR$:

$$
f(x) = sum_(n=0)^oo (f^((n))(a))/n!(x-a)^n
$$

Taylor series anchored at $x=0$ are called [[Maclaurin series]].

The accuracy of the approximation is bounded by [[Taylor's theorem]].

## References

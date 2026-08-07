---
publish: true
tags:
  - atomic
  - math/functions
up:
created: 2026-08-07
status: open
---

This theorem allows us to calculate the error of a [[Taylor series]] expansion.

## Statement

Let $k>=1$ be an integer, and $f: RR->RR$ be $k$ times differentiable at the point $a in RR$. With degree-$k$ Taylor expansion $P_k (x)$, we have

$$
f(x) = P_k (x) + R_k (x)
$$

where

$$
R_k (x) = (f^((k+1))(c))/(k+1)(x-a)^(k+1)
$$

for some $a<c<x$ (or $x<c<a$).

### More precise version

Let $k>=1$ be an integer, and $f: RR -> RR$ be $k$ times differentiable at the point $a in RR$. Then there exists a function $h_k: RR -> RR$ such that

$$
f(x) = sum_(i=0)^k (f^((i))(x))/i! x^i + h_k (x)(x-a)^k,
$$

and

$$
lim_(x->a) h_k (x) = 0
$$

## References

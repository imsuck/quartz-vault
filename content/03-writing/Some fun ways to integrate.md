---
categories:
  - "[[Writing]]"
title: Some fun ways to integrate
description: How unorthodoxically can you integrate a simple integral?
tags:
  - math/calc
created: 2026-10-10
publish: true
---

> _Ideas from LLMs (sad, but still interesting)._

# Today's suspect

The integral that we will be looking at is [Daily Integral](https://dailyintegral.com/)'s 9th Oct 2026 Beginner Integral

$$
integral_1^e x^2 ln x dif x
$$

When I first saw this, a thought went through my mind: "integration by parts in beginner?" Things seem to be getting stale in the beginner section, and yet, IBP was very easy to spot in this case. So, instead I wondered what other creative ways are there to solve this seemingly benign integral.

# Feynman?

Those who are familiar with "Feynman integration" or "Differentiation under the integral sign" may notice we have the $ln x$ factor poking out, begging for Feynman's trick to be used. So first, we parameterize the 2:

$$
F(alpha) = integral_1^e x^alpha dif x = (e^(alpha + 1) - 1)/(alpha + 1)
$$

Then differentiate our new function with respect to α:

$$
F'(alpha) = dif/(dif alpha) integral_1^e x^alpha dif x = integral_1^e partial/(partial alpha) x^alpha dif x = integral_1^e x^alpha ln x dif x
$$

We also have another way to write $F'(alpha)$:

$$
F'(alpha) = dif/(dif alpha) (e^(alpha + 1) - 1)/(alpha + 1) = (alpha e^(alpha+1) + 1)/(alpha + 1)^2
$$

Putting it all together:

$$
integral_1^e x^2 ln x dif x = F'(2) = (2 e^3+1)/9.
$$

# Double trouble

If you recall, natural logarithm can be defined by an integral:

$$
ln x = integral_1^x 1/t dif t
$$

So we will substitute that into our integral!

$$
integral_1^e x^2 ln x dif x = integral_1^e x^2 integral_1^x 1/t dif t dif x
$$

Now, let's swap the order of the integral. We have $1 <= t <= x <= e$, so the integral becomes

$$
integral_1^e integral_t^e x^2/t dif x dif t = integral_1^e (e^3-t^3)/(3t) dif t = e^3/3 integral_1^e 1/t dif t - 1/3 integral_1^e t^2 dif t = e^3/3 - 1/3 (e^3/3-1/3) = (2e^3 + 1)/9.
$$

# Going exterior

The previous method relied on calculating the interior weighted area of a triangle. But with [Green's theorem](https://en.wikipedia.org/wiki/Green's_theorem) --_a special case of [Generalized Stokes theorem](https://en.wikipedia.org/wiki/Generalized_Stokes_theorem), I just have to say it :)_--we can compute path integrals instead

$$
integral.double_D ((partial Q)/(partial x) - (partial P)/(partial y)) dif x dif y = integral.cont_(partial D) P dif x + Q dif y
$$

Choosing $P = 0, Q = x^3/(3y) --> Q_x = x^2/y$ (and renaming $t$ to $y$) gives us

$$
integral_1^e integral_y^e x^2/y dif x dif y = integral.cont_T x^3/(3y) dif y
$$

Where $T$ is the triangle with vertices $(1, 1), (e, 1), (e, e)$. Analyzing the edges, and their directions we get

$$
integral.cont_T x^3/(3y) dif y &= underbrace(integral_1^1 x^3/(3y) dif y, (1, 1)->(e, 1)) + underbrace(integral_1^e e^3/(3y) dif y, (e, 1)->(e, e)) + underbrace(integral_e^1 s^3/(3s) dif s, (e, e)->(1, 1) \ x = y = s) \
&= 0 + e^3/3 + (1 - e^3)/9 = (2e^3 + 1)/9.
$$

# Differential algebra

Though I admit I don't know much about this field, the suggested proof seems easy enough to understand, at least on the surface level. So, I will be sharing it here.

Consider the differential field $K = CC(x, ln x)$ equipped with derivation $D(x) = 1, D(ln x) = 1/x$. The original integrand $x^2 ln x$ lies in the subspace $C[x] ln x + C[x]$. Let $F(x)$ be a "guess" or (ansatz) for $D(F) = x^2 ln x$; it should have the form

$$
F(x) = p(x) ln x + q(x) \
==> D(F) = p'(x) ln x + p(x)/x + q'(x)
$$

This gives us

$$
p'(x) = x^2, p(x)/x + q'(x) = 0
$$

Note that a $p(x)/x + q'(x)$ has to be a polynomial, meaning the additive constant of integration of $p(x)$ has to be zero. Therefore, $p(x) = x^3/3, q(x) = -x^3/9 + C$, and

$$
F(x) = x^3/3 ln x - x^3/9 + C
$$

Since $F'(x) = x^2 ln x$ , by the fundamental theorem of calculus,

$$
integral_1^e x^2 ln x dif = F(e) - F(1) = (e^3/3 ln e - e^3/9) - (1^3/3 ln 1 - 1^3/9) = (2e^3 + 1)/9.
$$

# Conclusion

Integration is, itself, an art, the art that I still find difficult to truly wield. There are still plenty of unconventional ways to integrate $integral_1^e x^2 ln x dif x$. Sadly however, I do not yet have the knowledge required to fully grasp them. Maybe another time!

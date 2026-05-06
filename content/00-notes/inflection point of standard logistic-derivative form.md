---
tags:
  - atomic
  - math/opt
created: 2026-04-14
status: open
sr-due: 2026-05-12
sr-interval: 7
sr-ease: 130
publish: true
---

Given $f(x)=15/(1+14e^(-0.3x))$, maximize the growth $f'(x)$.

With some labor and algebra, the inflection (mirror) of this graph is when $14e^(-0.3x) = 1$, or more generally, for $f(x)=1/(c+d e^(-k x))$ the inflection is at $d e^(-k x) = c$. This is where the derivative is maximized.

Isn't this the sigmoid function (parameterized)?

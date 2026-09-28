# Calculus Notes: Second Derivative Test, Curve Sketching & Differential Equations

## 1. The Second Derivative Test

The **Second Derivative Test** uses the sign of the second derivative at a critical point (where $f'(c) = 0$) to classify whether the turning point is a local maximum or local minimum.

### Formal Statement

Given a well-behaved (continuous and differentiable) function $f(x)$ at $x = c$:

1. **Local Minimum Test:**  
   If $f'(c) = 0$ and $f''(c) > 0$ ($\text{Concave Up } \smile$), then $f(c)$ is a **local minimum**.
2. **Local Maximum Test:**  
   If $f'(c) = 0$ and $f''(c) < 0$ ($\text{Concave Down } \frown$), then $f(c)$ is a **local maximum**.

_(Note: If $f''(c) = 0$, the test is inconclusive and the first derivative sign diagram must be used)._

---

### Application to General Quadratics ($y = ax^2 + bx + c, \ a \neq 0$)

- **First Derivative:** $y' = 2ax + b$
- **Second Derivative:** $y'' = 2a$

- If **$a > 0$**: $y'' = 2a > 0 \implies$ Parabola opens upward $\implies$ **Minimum** at the turning point.
- If **$a < 0$**: $y'' = 2a < 0 \implies$ Parabola opens downward $\implies$ **Maximum** at the turning point.

---

## 2. Worked Examples & Asymptotic Limits

### Example 1: $y = x e^{-x}$

1. **First Derivative (Product Rule):**
   $$y' = (1)e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}$$
   - **Critical Point:** $y' = 0 \implies 1 - x = 0 \implies x = 1$ (since $e^{-x} > 0$).

2. **Second Derivative:**
   $$y'' = (-1)e^{-x} + (1 - x)(-e^{-x}) = (x - 2)e^{-x}$$

3. **Applying the Second Derivative Test at $x = 1$:**
   $$y''(1) = (1 - 2)e^{-1} = -\frac{1}{e} < 0$$
   - Since $y'(1) = 0$ and $y''(1) < 0$, a **local maximum** occurs at $(1, \frac{1}{e})$.

4. **Inflection Point:**
   $$y'' = 0 \implies x - 2 = 0 \implies x = 2$$

5. **Asymptotic Behavior & L'Hôpital's Rule:**
   - As $x \to -\infty$: $y \to -\infty$
   - As $x \to +\infty$: $\lim_{x \to \infty} x e^{-x} = \lim_{x \to \infty} \frac{x}{e^x}$ ($\left[\frac{\infty}{\infty}\right]$ indeterminate form).
   - **L'Hôpital's Rule:**
     $$\lim_{x \to \infty} \frac{x}{e^x} \stackrel{\text{L'H}}{=} \lim_{x \to \infty} \frac{\frac{d}{dx}(x)}{\frac{d}{dx}(e^x)} = \lim_{x \to \infty} \frac{1}{e^x} = 0$$
   - The positive $x$-axis ($y = 0$) is a **horizontal asymptote**.

---

### Example 2: $y = x e^{x}$

1. **First Derivative:** $y' = (1 + x)e^{x} \implies$ Critical point at $x = -1$.
2. **Second Derivative:** $y'' = (2 + x)e^{x}$.
3. **Evaluating Test at $x = -1$:**
   $$y''(-1) = (2 - 1)e^{-1} = \frac{1}{e} > 0 \implies \mathbf{Minimum} \text{ at } \left(-1, -\frac{1}{e}\right)$$

---

### Geometric Transformations Between $y = x e^{-x}$ and $y = x e^x$

The two functions are related via a sequence of planar reflections equivalent to a **$180^\circ$ rotation about the origin**:

1. Reflect $y = x e^{-x}$ in the $y$-axis ($x \to -x$) $\implies y = -x e^x$.
2. Reflect in the $x$-axis ($y \to -y$) $\implies y = x e^x$.

---

## 3. Introduction to Differential Equations

Differential equations express relationships between functions and their derivatives. Standard functions act as **fundamental solutions** to linear differential equations:

| Fundamental Solutions                                      | Differential Equation             | Order               |
| :--------------------------------------------------------- | :-------------------------------- | :------------------ |
| $y = e^x, \ y = e^{-x}$                                    | $y'' - y = 0$                     | $2^\text{nd}$ Order |
| $y = \sin(x), \ y = \cos(x)$                               | $y'' + y = 0$                     | $2^\text{nd}$ Order |
| $y = e^x, \ y = x e^x$                                     | $y'' - 2y' + y = 0$               | $2^\text{nd}$ Order |
| $y = e^{-x}, \ y = x e^{-x}$                               | $y'' + 2y' + y = 0$               | $2^\text{nd}$ Order |
| $e^x, \ e^{-x}, \ \sin(x), \ \cos(x)$                      | $y^{(4)} - y = 0$                 | $4^\text{th}$ Order |
| $e^x, \ e^{-x}, \ \sin(x), \ \cos(x), \ x e^x, \ x e^{-x}$ | $y^{(6)} - y^{(4)} - y'' + y = 0$ | $6^\text{th}$ Order |

---

## 4. Module Summary: Differential Calculus Protocol

### A. First Derivative ($f'(x)$)

- **$f'(x) > 0$:** Function is increasing ($\uparrow$).
- **$f'(x) < 0$:** Function is decreasing ($\downarrow$).
- **$f'(x) = 0$:** Critical point / Turning point (Local Maximum/Minimum).

### B. Second Derivative ($f''(x)$)

- **$f''(x) > 0$:** Concave Up ($\smile$) / Smiley face.
- **$f''(x) < 0$:** Concave Down ($\frown$) / Sad face.
- **Sign Change in $f''(x)$:** Point of Inflection.

### C. Differentiation Rules Overview

- **Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$
- **Product Rule:** $\frac{d}{dx}[u \cdot v] = u v' + v u'$
- **Quotient Rule:** $\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{v u' - u v'}{v^2}$

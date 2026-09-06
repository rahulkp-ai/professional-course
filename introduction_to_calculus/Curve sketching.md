## 1. Systemic Curve Sketching Checklist

To sketch any function $y = f(x)$ accurately in the Cartesian plane, systematically evaluate the following six features:

1. **$y$-intercept:** Compute $f(0)$ (if $x = 0$ is in the domain).
2. **$x$-intercepts:** Solve $f(x) = 0$ for $x$. _(Note: If algebraically difficult, an approximate sketch often reveals how many real roots exist and where they lie)._
3. **Asymptotic Behavior:**

- **Vertical Asymptotes:** Locate points where $f(x) \to \pm\infty$ (e.g., domain discontinuities where the denominator equals zero).
- **Horizontal / Oblique Asymptotes:** Examine end-behavior as $x \to \pm\infty$.

4. **First Derivative ($y'$):** Find critical points ($y' = 0$ or undefined) and build the **$y'$ sign diagram** to identify intervals of increase/decrease and local/global extrema.
5. **Second Derivative ($y''$):** Find candidates for inflection ($y'' = 0$ or undefined) and build the **$y''$ sign diagram** to identify intervals of concavity (concave up/down) and points of inflection.
6. **Synthesis:** Plot key points, construct asymptotes, and draw smooth curves matching the sign diagrams.

---

## 2. Shift / Chain Derivative Shortcut

When taking higher-order derivatives of shifted terms such as $(x - a)^n$:

$$\frac{d}{dx}\left[(x - a)^n\right] = n(x - a)^{n - 1}$$

- **Reasoning:** Shifting a graph horizontally by $a$ units does not alter the slopes of its tangent lines at corresponding points.

---

## 3. Worked Examples Analysis

### Example 1: Cubic Polynomial

$$f(x) = 2x^3 - 9x^2 + 12x - 1$$

- **Intercepts:**
- $y$-intercept: $(0, -1)$
- $x$-intercept: Graphing reveals exactly **one real root** between $x = 0$ and $x = 1$.

- **Asymptotes:** None. As $x \to +\infty$, $y \to +\infty$; as $x \to -\infty$, $y \to -\infty$.
- **First Derivative:** $y' = 6x^2 - 18x + 12 = 6(x - 1)(x - 2)$
- Critical Points: $x = 1, 2$
- $y'$ Sign Pattern: Positive $\to$ Negative $\to$ Positive
- **Local Max:** $(1, 4)$ | **Local Min:** $(2, 3)$

- **Second Derivative:** $y'' = 12x - 18 = 6(2x - 3)$
- Inflection Candidate: $x = \frac{3}{2}$
- $y''$ Sign Pattern: Negative $\to$ Positive
- **Point of Inflection:** $\left(\frac{3}{2}, \frac{7}{2}\right)$

---

### Example 2: Rational Function with No Extrema

$$g(x) = \frac{x^2 - 2}{x - 1} = x + 1 - \frac{1}{x - 1}$$

- **Intercepts:**
- $y$-intercept: $(0, 2)$
- $x$-intercepts: $(\pm\sqrt{2}, 0)$

- **Asymptotes:**
- Vertical: $x = 1$ ($\lim_{x \to 1^+} g(x) = -\infty$, $\lim_{x \to 1^-} g(x) = +\infty$)
- Oblique: $y = x + 1$ (approached from below as $x \to +\infty$, from above as $x \to -\infty$)

- **First Derivative:** $y' = 1 + \frac{1}{(x - 1)^2}$
- $y' > 0$ for all $x \ne 1$.
- **No turning points** (strictly increasing on both domain branches).

- **Second Derivative:** $y'' = -2(x - 1)^{-3} = -\frac{2}{(x - 1)^3}$
- $y''$ Sign Pattern: Positive ($x < 1$) $\to$ Negative ($x > 1$)
- **Concave Up** on $(-\infty, 1)$ | **Concave Down** on $(1, \infty)$

---

### Example 3: Rational Function with Turning Points

$$f(x) = x + 1 + \frac{1}{x - 1} = \frac{x^2}{x - 1}$$

- **Intercepts:**
- $y$-intercept: $(0, 0)$
- $x$-intercept: $(0, 0)$ (only single root at origin)

- **Asymptotes:**
- Vertical: $x = 1$ ($\lim_{x \to 1^+} f(x) = +\infty$, $\lim_{x \to 1^-} f(x) = -\infty$)
- Oblique: $y = x + 1$ (approached from above as $x \to +\infty$, from below as $x \to -\infty$)

- **First Derivative:** $y' = 1 - \frac{1}{(x - 1)^2} = \frac{x(x - 2)}{(x - 1)^2}$
- Critical Points: $x = 0, 2$ ($y'$ undefined at $x = 1$)
- $y'$ Sign Pattern: Positive $\to$ Negative $\mid$ Negative $\to$ Positive
- **Local Max:** $(0, 0)$ | **Local Min:** $(2, 4)$

- **Second Derivative:** $y'' = 2(x - 1)^{-3} = \frac{2}{(x - 1)^3}$
- $y''$ Sign Pattern: Negative ($x < 1$) $\to$ Positive ($x > 1$)
- **Concave Down** on $(-\infty, 1)$ | **Concave Up** on $(1, \infty)$

---

## 4. Summary Comparison: Rational Examples

| Feature                                | $g(x) = x + 1 - \frac{1}{x - 1}$             | $f(x) = x + 1 + \frac{1}{x - 1}$             |
| -------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| **Algebraic Form**                     | $\frac{x^2 - 2}{x - 1}$                      | $\frac{x^2}{x - 1}$                          |
| **Turning Points**                     | None                                         | Local Max at $(0,0)$, Local Min at $(2,4)$   |
| **Oblique Approach ($x \to +\infty$)** | From **below** the line $y = x + 1$          | From **above** the line $y = x + 1$          |
| **Concavity Shapes**                   | Concave Up ($x < 1$), Concave Down ($x > 1$) | Concave Down ($x < 1$), Concave Up ($x > 1$) |

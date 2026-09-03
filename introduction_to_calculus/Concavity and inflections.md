## 1. Core Definitions & Mathematical Conditions

- **Concavity:** A geometric property of a curve determined by whether the slopes of its tangent lines are increasing or decreasing as you move from left to right.
- **Concave Up (Bowl Up):**
- **Behavior:** Tangent slopes change from steep negative $\to$ zero $\to$ steep positive (slopes are **increasing**).
- **Condition:** $y'$ is an increasing function $\implies y'' > 0$.

- **Concave Down (Bowl Down):**
- **Behavior:** Tangent slopes change from steep positive $\to$ zero $\to$ steep negative (slopes are **decreasing**).
- **Condition:** $y'$ is a decreasing function $\implies y'' < 0$.

- **Point of Inflection:** A point on the curve where the concavity changes (either from concave up to down, or down to up).
- **Geometric Property:** The tangent line **crosses through the curve** at an inflection point.

---

## 2. Inflection Points & Derivatives

| Transition                        | Slope ($y'$) Behavior       | Second Derivative ($y''$)           |
| --------------------------------- | --------------------------- | ----------------------------------- |
| **Concave Up $\to$ Concave Down** | Reaches a **local maximum** | $y'' = 0$ (changes from $+$ to $-$) |
| **Concave Down $\to$ Concave Up** | Reaches a **local minimum** | $y'' = 0$ (changes from $-$ to $+$) |

> **Key Takeaway:** Changes in concavity are identified by analyzing sign changes in the **sign diagram of $y''$**.

---

## 3. Worked Examples

### Example 1: Polynomial Curve $y = 9x - x^3$

#### **1. Factorization & Derivatives**

- **Original Function:** $y = x(3 + x)(3 - x) \implies$ $x$-intercepts at $x = 0, \pm 3$; $y$-intercept at $(0, 0)$.
- **First Derivative:** $y' = 9 - 3x^2 = 3(\sqrt{3} + x)(\sqrt{3} - x)$
- **Second Derivative:** $y'' = -6x$

#### **2. Sign Diagram Analysis**

- **$y'$ Sign Diagram:**
- Critical points at $x = \pm \sqrt{3}$.
- Sign pattern: Negative $\to$ Positive $\to$ Negative.
- **Local Minimum** at $x = -\sqrt{3}$ with $y = -6\sqrt{3}$.
- **Local Maximum** at $x = \sqrt{3}$ with $y = 6\sqrt{3}$.

- **$y''$ Sign Diagram:**
- Critical point at $x = 0$.
- Sign pattern: Positive ($x < 0$) $\to$ Negative ($x > 0$).
- **Concave Up** on $(-\infty, 0)$ and **Concave Down** on $(0, \infty)$.
- **Point of Inflection** at the origin $(0, 0)$.

---

### Example 2: Cusp Curve $y = x^{2/3}$

#### **1. Differentiation**

- **First Derivative:**

$$y' = \frac{2}{3}x^{-1/3} = \frac{2}{3x^{1/3}}$$

_(Undefined at $x = 0$)_

- **Second Derivative:**

$$y'' = -\frac{2}{9}x^{-4/3} = -\frac{2}{9(x^{2/3})^2}$$

_(Undefined at $x = 0$)_

#### **2. Sign Diagram & Asymptotic Behavior**

- **$y'$ Sign Diagram:**
- Undefined at $x = 0$. Sign pattern: Negative ($x < 0$) $\to$ Positive ($x > 0$).
- Curve decreases on $(-\infty, 0)$ and increases on $(0, \infty) \implies$ **Global Minimum** at $(0,0)$.

- **Tangent Behavior near $x = 0$ (Limits):**

$$\lim_{x \to 0^-} y' = -\infty \quad \text{and} \quad \lim_{x \to 0^+} y' = +\infty$$

_(Tangent lines become vertical as $x \to 0$, creating a sharp **cusp**)._

- **$y''$ Sign Diagram:**
- Denominator contains a squared term $(x^{2/3})^2 > 0$ for all $x \ne 0$.
- $y'' < 0$ for all $x \ne 0 \implies$ Curve is **Concave Down on both sides** of $x = 0$.

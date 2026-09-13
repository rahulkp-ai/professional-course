# General Sign Diagrams & Graphing Functions

## 1. What is a Sign Diagram?

A **sign diagram** is a visual summary table representing the sign (positive, negative, zero, or undefined) of a mathematical expression across the real number line.

### Structure

- **Top Row (x-axis):** Indicates key values of $x$ where the expression becomes $0$ (roots) or $U$ (undefined/discrepancies in domain).
- **Bottom Row:** Displays the sign of the expression ($+$ or $-$) in each interval formed by these critical points, along with structural symbols for behavior:
- **First Derivative ($y'$):** Sloping lines ($\nearrow$ for positive/increasing, $\searrow$ for negative/decreasing).
- **Second Derivative ($y''$):** Concavity icons ($\cup$ for positive/concave up, $\cap$ for negative/concave down).

---

## 2. Theoretical Framework of Sign Diagrams

$$\begin{aligned} \text{Function Value } y &> 0 \implies \text{Curve sits above the } x\text{-axis} \\ \text{Function Value } y &< 0 \implies \text{Curve sits below the } x\text{-axis} \\ \text{First Derivative } y' &> 0 \implies \text{Function is \textbf{increasing}} \quad (\nearrow) \\ \text{First Derivative } y' &< 0 \implies \text{Function is \textbf{decreasing}} \quad (\searrow) \\ \text{Second Derivative } y'' &> 0 \implies \text{Graph is \textbf{concave up}} \quad (\cup, \text{bowl up/smiley face}) \\ \text{Second Derivative } y'' &< 0 \implies \text{Graph is \textbf{concave down}} \quad (\cap, \text{bowl down/sad face}) \end{aligned}$$

---

## 3. Worked Examples

### Example 1: Quadratic Function $y = x^2 - x$

#### 1. Function Behavior ($y$)

- **Factorization:** $y = x(x - 1)$
- **Roots:** $y = 0$ at $x = 0$ and $x = 1$.

| $x$          | $(-\infty, 0)$ | $0$           | $(0, 1)$       | $1$           | $(1, \infty)$  |
| ------------ | -------------- | ------------- | -------------- | ------------- | -------------- |
| **$y$**      | $+$            | $0$           | $-$            | $0$           | $+$            |
| **Position** | Above $x$-axis | $x$-intercept | Below $x$-axis | $x$-intercept | Above $x$-axis |

#### 2. First Derivative ($y'$)

- **Derivative:** $y' = 2x - 1$
- **Critical Point:** $y' = 0 \implies x = \frac{1}{2}$

| $x$       | $\left(-\infty, \frac{1}{2}\right)$ | $\frac{1}{2}$ | $\left(\frac{1}{2}, \infty\right)$ |
| --------- | ----------------------------------- | ------------- | ---------------------------------- |
| **$y'$**  | $-$                                 | $0$           | $+$                                |
| **Slope** | Decreasing ($\searrow$)             | Vertex / Min  | Increasing ($\nearrow$)            |

- **Vertex:** $\left(\frac{1}{2}, -\frac{1}{4}\right)$ is the absolute minimum point.

#### 3. Second Derivative ($y''$)

- **Derivative:** $y'' = 2$ (Constant positive value)

| $x$           | $(-\infty, \infty)$ |
| ------------- | ------------------- |
| **$y''$**     | $+$                 |
| **Concavity** | Concave Up ($\cup$) |

---

### Example 2: Cubic Polynomial $y = x^3 - x$

#### 1. Function Behavior ($y$)

- **Factorization:** $y = x(x + 1)(x - 1)$
- **Roots:** $x = -1, 0, 1$

| $x$     | $(-\infty, -1)$ | $-1$ | $(-1, 0)$ | $0$ | $(0, 1)$ | $1$ | $(1, \infty)$ |
| ------- | --------------- | ---- | --------- | --- | -------- | --- | ------------- |
| **$y$** | $-$             | $0$  | $+$       | $0$ | $-$      | $0$ | $+$           |

#### 2. First Derivative ($y'$)

- **Derivative:** $y' = 3x^2 - 1$
- **Critical Points:** $y' = 0 \implies x = \pm\frac{1}{\sqrt{3}}$

| $x$       | $\left(-\infty, -\frac{1}{\sqrt{3}}\right)$ | $-\frac{1}{\sqrt{3}}$ | $\left(-\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right)$ | $\frac{1}{\sqrt{3}}$ | $\left(\frac{1}{\sqrt{3}}, \infty\right)$ |
| --------- | ------------------------------------------- | --------------------- | ------------------------------------------------------ | -------------------- | ----------------------------------------- |
| **$y'$**  | $+$                                         | $0$                   | $-$                                                    | $0$                  | $+$                                       |
| **Slope** | Increasing ($\nearrow$)                     | Peak (Local Max)      | Decreasing ($\searrow$)                                | Trough (Local Min)   | Increasing ($\nearrow$)                   |

#### 3. Second Derivative ($y''$)

- **Derivative:** $y'' = 6x$
- **Inflection Point:** $y'' = 0 \implies x = 0$

| $x$           | $(-\infty, 0)$        | $0$                 | $(0, \infty)$       |
| ------------- | --------------------- | ------------------- | ------------------- |
| **$y''$**     | $-$                   | $0$                 | $+$                 |
| **Concavity** | Concave Down ($\cap$) | Point of Inflection | Concave Up ($\cup$) |

---

### Example 3: Rational Function $g(x) = \frac{x^2 - 2}{x - 1}$

Rewritten form via algebraic division:

$$g(x) = x + 1 - \frac{1}{x - 1}$$

#### 1. Function Behavior ($g(x)$)

- **Roots (Numerator = 0):** $x = \pm\sqrt{2}$
- **Undefined (Denominator = 0):** $x = 1$ (Vertical Asymptote)

| $x$        | $(-\infty, -\sqrt{2})$ | $-\sqrt{2}$ | $(-\sqrt{2}, 1)$ | $1$ | $(1, \sqrt{2})$ | $\sqrt{2}$ | $(\sqrt{2}, \infty)$ |
| ---------- | ---------------------- | ----------- | ---------------- | --- | --------------- | ---------- | -------------------- |
| **$g(x)$** | $-$                    | $0$         | $+$              | $U$ | $-$             | $0$        | $+$                  |

#### 2. Derivation of First Derivative ($g'(x)$)

Using limit definition for $h(x) = \frac{1}{x - 1}$:

$$h'(a) = \lim_{b \to a} \frac{h(b) - h(a)}{b - a} = \lim_{b \to a} \frac{\frac{1}{b-1} - \frac{1}{a-1}}{b - a} = \lim_{b \to a} \frac{\frac{(a-1)-(b-1)}{(b-1)(a-1)}}{b - a} = \lim_{b \to a} \frac{-(b-a)}{(b-a)(b-1)(a-1)} = -\frac{1}{(a-1)^2}$$

Thus:

$$g'(x) = 1 - h'(x) = 1 + \frac{1}{(x - 1)^2}$$

#### 3. First Derivative Sign Diagram ($g'(x)$)

Since $1 + \frac{1}{(x-1)^2} > 0$ for all $x \neq 1$:

| $x$          | $(-\infty, 1)$          | $1$       | $(1, \infty)$           |
| ------------ | ----------------------- | --------- | ----------------------- |
| **$g'(x)$**  | $+$                     | $U$       | $+$                     |
| **Behavior** | Increasing ($\nearrow$) | Undefined | Increasing ($\nearrow$) |

---

## 4. Key Terminology Summary

- **Root / Zero ($0$):** Points where $f(x) = 0$ (crosses or touches the x-axis).
- **Undefined ($U$):** Points outside the function domain (e.g., vertical asymptotes).
- **Point of Inflection:** A point on the curve where the concavity changes (from concave up to concave down, or vice-versa). Tangent lines pass _through_ the curve at inflection points.

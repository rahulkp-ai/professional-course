# Increasing and Decreasing Functions & Derivatives

## 1. Precise Definitions

### Increasing Function

A function $f(x)$ is **increasing** on an interval if, as inputs get larger, the outputs also get larger:

$$\text{If } a < b, \text{ then } f(a) < f(b)$$

- **Graphical Meaning:** Moving left to right ($+x$), the curve slopes upward ($+y$).

### Decreasing Function

A function $f(x)$ is **decreasing** on an interval if, as inputs get larger, the outputs get smaller:

$$\text{If } a < b, \text{ then } f(a) > f(b)$$

- **Graphical Meaning:** Moving left to right ($+x$), the curve slopes downward ($-y$).

---

## 2. Examples of Functions

| Function Class | Formula      | Behavior / Domain Restrictions |
| -------------- | ------------ | ------------------------------ |
| **Linear**     | $y = mx + c$ | • Increasing if $m > 0$<br>    |

<br>• Decreasing if $m < 0$<br>

<br>• Neither (constant) if $m = 0$ |
| **Quadratic** | $y = x^2$ | • Decreasing on $(-\infty, 0]$<br>

<br>• Increasing on $[0, \infty)$<br>

<br>• **Overall:** Neither (across full real line $\mathbb{R}$) |
| **Cubic** | $y = x^3$ | • Increasing on all of $\mathbb{R}$ (momentarily flattens at origin) |
| **Exponential** | $y = e^x$ | • Increasing on $(-\infty, \infty)$ |
| **Exponential Decay** | $y = e^{-x}$ | • Decreasing on $(-\infty, \infty)$ (reflection of $e^x$ across y-axis) |
| **Logarithmic** | $y = \ln(x)$ | • Increasing on $(0, \infty)$ (domain restricted to positive reals) |

---

## 3. Trigonometric Functions & Restricted Domains

Trigonometric functions fluctuate periodically, so they are **neither increasing nor decreasing across all of $\mathbb{R}$**. Restricting their domains allows them to be monotonic and satisfy the horizontal line test to form inverses:

- **Sine ($y = \sin x$):** Restricted to $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \implies$ **Increasing** $\implies$ Invertible as $\arcsin(x)$.
- **Cosine ($y = \cos x$):** Restricted to $[0, \pi] \implies$ **Decreasing** $\implies$ Invertible as $\arccos(x)$.
- **Tangent ($y = \tan x$):** Restricted to $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right) \implies$ **Increasing** on each open interval $\implies$ Invertible as $\arctan(x)$.

---

## 4. Key Theorems on Inverses & Reflections

1. **Reflection Property:** Reflecting a function graph across the y-axis (i.e., replacing $x$ with $-x$) interchanges increasing and decreasing behavior.
2. **Inverse Function Behavior:** If $f(x)$ is increasing (or decreasing), its inverse $f^{-1}(x)$ preserves that same monotonicity:

- $f$ is increasing $\implies f^{-1}$ is **increasing**.
- $f$ is decreasing $\implies f^{-1}$ is **decreasing**.

---

## 5. Relationship to the Derivative

The sign of the derivative $f'(x)$ (the slope of the tangent line / instantaneous rate of change) dictates the function's behavior over an interval:

$$\begin{aligned} f'(x) > 0 &\implies f(x) \text{ is \textbf{increasing}} \\ f'(x) < 0 &\implies f(x) \text{ is \textbf{decreasing}} \end{aligned}$$

- **Real-World Example:** In a distance-time graph of a car journey, positive speedometer readings ($v = \frac{ds}{dt} > 0$) correspond to an increasing distance function.

---

## 6. Worked Example: Analyzing $f(x) = x^3 - x$

### Step 1: Find roots (x-intercepts)

$$f(x) = x(x^2 - 1) = x(x+1)(x-1) = 0 \implies x = -1, 0, 1$$

### Step 2: Compute derivative

$$f'(x) = 3x^2 - 1$$

### Step 3: Determine intervals of sign for $f'(x)$

- **Derivative equal to zero:** $3x^2 - 1 = 0 \implies x = \pm\frac{1}{\sqrt{3}}$
- **Increasing ($f'(x) > 0$):** $3x^2 > 1 \implies x^2 > \frac{1}{3} \implies x \in \left(-\infty, -\frac{1}{\sqrt{3}}\right) \cup \left(\frac{1}{\sqrt{3}}, \infty\right)$
- **Decreasing ($f'(x) < 0$):** $3x^2 < 1 \implies x^2 < \frac{1}{3} \implies x \in \left(-\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right)$

### Step 4: Sign Diagram

| Interval               | $\left(-\infty, -\frac{1}{\sqrt{3}}\right)$ | $x = -\frac{1}{\sqrt{3}}$ | $\left(-\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right)$ | $x = \frac{1}{\sqrt{3}}$ | $\left(\frac{1}{\sqrt{3}}, \infty\right)$ |
| ---------------------- | ------------------------------------------- | ------------------------- | ------------------------------------------------------ | ------------------------ | ----------------------------------------- |
| **Sign of $f'(x)$**    | $+$                                         | $0$                       | $-$                                                    | $0$                      | $+$                                       |
| **Behavior of $f(x)$** | Increasing ($\nearrow$)                     | Local Max                 | Decreasing ($\searrow$)                                | Local Min                | Increasing ($\nearrow$)                   |

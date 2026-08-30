```mermaid
flowchart TD
    A["Continuity at x = a"] --> B["Condition 1: f(a) is defined"]
    A --> C["Condition 2: lim f(x) exists as x → a"]
    A --> D["Condition 3: lim f(x) = f(a) as x → a"]

    E["Main Obstructions to Continuity"] --> F["Zero Denominators / Division by Zero"]
    E --> G["Piecewise Endpoints Not Matching"]

    H["Types of Discontinuities"] --> I["Removable Discontinuity"]
    H --> J["Non-Removable Discontinuity"]

    I --> I1["Limit exists as x → a, but f(a) is undefined or incorrect"]
    I --> I2["Can fix by defining / redefining f(a) = lim f(x)"]

    J --> J1["Jump: Left and right limits exist but are unequal"]
    J --> J2["Asymptotic / Infinite: Vertical asymptote separates branches"]

```

---

**Core Concept: Continuity**

- **Intuitive Definition:** A function is continuous if its graph can be drawn without lifting your pen off the paper (no gaps, holes, or sudden jumps).
- **Examples of Continuous Functions:**
- Linear: $y = x$, $y = k$
- Polynomials: $y = x^2$
- Trigonometric: $y = \sin x$
- Exponential & Logarithmic: $y = e^x$, $y = \ln x$

- **Formal Definition:** A function $f(x)$ is continuous at $x = a$ if and only if:

$$\lim_{x \to a} f(x) = f(a)$$

---

**Common Causes of Discontinuity**

1. **Division by Zero:** Zero in the denominator of a fraction creates undefined points or asymptotic behavior.
2. **Piecewise Misalignments:** Sub-functions meeting at boundary points fail to connect.

---

**Comparing Piecewise Examples**

### 1. Continuous Piecewise: $f(x) = \vert{}x\vert{}$

Defined as:

$$f(x) = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$

- The two pieces meet seamlessly at the origin $(0, 0)$.
- Drawn continuously as a single V-shape without lifting the pen.

### 2. Discontinuous Jump: $f(x) = \frac{x}{\vert{}x\vert{}}$

Defined as:

$$f(x) = \begin{cases} 1 & \text{if } x > 0 \\ -1 & \text{if } x < 0 \end{cases}$$

- **Right-hand limit:** $\lim_{x \to 0^+} \frac{x}{\vert{}x\vert{}} = 1$
- **Left-hand limit:** $\lim_{x \to 0^-} \frac{x}{\vert{}x\vert{}} = -1$
- **Conclusion:** Because the one-sided limits are unequal ($\lim_{x \to 0^+} \neq \lim_{x \to 0^-}$), the overall two-sided limit does not exist, creating an unfixable jump discontinuity.

---

**Removable vs. Non-Removable Discontinuities**

```mermaid
flowchart LR
    A["Rational Function Discontinuities"] --> B["f(x) = (x² - 1)/(x - 1)"]
    A --> C["g(x) = (x² - 2)/(x - 1)"]

    B --> B1["Simplifies to x + 1 (for x ≠ 1)"]
    B1 --> B2["Limit as x → 1 equals 2"]
    B2 --> B3["Removable Hole at (1, 2)"]

    C --> C1["Long Division: (x + 1) - 1/(x - 1)"]
    C1 --> C2["Vertical Asymptote at x = 1"]
    C2 --> C3["Non-Removable Discontinuity"]

```

| Type              | Condition                                                            | Example                        | Resolution                                                    |
| ----------------- | -------------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------- |
| **Removable**     | $\lim_{x \to a} f(x)$ exists, but $f(a)$ is undefined or mismatched. | $f(x) = \frac{x^2 - 1}{x - 1}$ | Redefine $f(a) = \lim_{x \to a} f(x)$ to fill the hole.       |
| **Non-Removable** | $\lim_{x \to a} f(x)$ does not exist (infinite asymptote or jump).   | $g(x) = \frac{x^2 - 2}{x - 1}$ | Cannot be made continuous at $a$ by assigning a single value. |

---

**Classic Removable Discontinuity Case Study: $f(x) = \frac{\sin x}{x}$**

- **Domain:** All $x \neq 0$ (undefined at $x = 0$).
- **Behavior:**
- Periodic undulations dampened by the $\frac{1}{x}$ factor as $\vert{}x\vert{} \to \infty$.
- Reflectional symmetry about the $y$-axis (Even function).

- **Limit at $x = 0$:**

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

- **Continuous Extension:**

$$f(x) = \begin{cases} \frac{\sin x}{x} & \text{if } x \neq 0 \\ 1 & \text{if } x = 0 \end{cases}$$

- **Applications:** Widely used in acoustics, optics, signal processing, and spectroscopy.

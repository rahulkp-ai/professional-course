# Definition of the Derivative

## Core Concepts & Geometric Intuition

- **Average Rate of Change:** Represented by the slope of the secant line passing through two points on a curve.
- For a displacement function $s(t)$, this corresponds to **average velocity** over a time interval.

- **Instantaneous Rate of Change:** As the time interval vanishes ($h \to 0$), secant lines approach the **tangent line** at the point of interest.
- The slope of this tangent line represents **instantaneous velocity** (like a speedometer reading) and defines the **derivative**, $f'(x)$.

---

## Two Equivalent Limit Definitions

### Definition 1: Increment Definition ($h \to 0$)

Measures rate of change as an offset $h$ shrinks to zero:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### Definition 2: Endpoint Definition ($b \to a$)

Measures rate of change over an interval $[a, b]$ as the right endpoint $b$ approaches $a$:

$$f'(a) = \lim_{b \to a} \frac{f(b) - f(a)}{b - a}$$

### Proof of Equivalence

To translate Definition 2 into Definition 1:

1. Let $x = a$ and $h = b - a$ (which implies $b = x + h$).
2. As $b \to a$, the difference $h \to 0$.
3. Substitute into Definition 2:

$$f'(x) = \lim_{b \to a} \frac{f(b) - f(a)}{b - a} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

---

## Example: Derivative of $f(x) = x^3$

### Method 1: Using Definition 1

$$f'(x) = \lim_{h \to 0} \frac{(x+h)^3 - x^3}{h}$$

1. **Expand numerator:** $(x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$
2. **Cancel terms:** $(x^3 + 3x^2h + 3xh^2 + h^3) - x^3 = 3x^2h + 3xh^2 + h^3$
3. **Factor and simplify:**

$$f'(x) = \lim_{h \to 0} \frac{h(3x^2 + 3xh + h^2)}{h} = \lim_{h \to 0} (3x^2 + 3xh + h^2)$$

4. **Evaluate limit at $h = 0$:**

$$f'(x) = 3x^2 + 3x(0) + 0^2 = 3x^2$$

---

### Method 2: Using Definition 2

$$f'(a) = \lim_{b \to a} \frac{b^3 - a^3}{b - a}$$

1. **Factor difference of cubes:** $b^3 - a^3 = (b - a)(b^2 + ba + a^2)$
2. **Cancel common factor:**

$$f'(a) = \lim_{b \to a} \frac{(b - a)(b^2 + ba + a^2)}{b - a} = \lim_{b \to a} (b^2 + ba + a^2)$$

3. **Evaluate limit at $b = a$:**

$$f'(a) = a^2 + a(a) + a^2 = 3a^2 \implies f'(x) = 3x^2$$

---

## Key Takeaways & Properties of $f(x) = x^3$

- **Symmetry:** $f(x) = x^3$ is an **odd function** with $180^\circ$ rotational symmetry about the origin.
- **Inflection Point at Origin:** The tangent line at $(0,0)$ is the horizontal x-axis ($f'(0) = 0$), which uniquely crosses through the curve itself.
- **Power Rule Pattern:**
- $f(x) = x^2 \implies f'(x) = 2x$
- $f(x) = x^3 \implies f'(x) = 3x^2$
- $f(x) = x^4 \implies f'(x) = 4x^3$
- **General Power Rule:** For $f(x) = x^n$, $f'(x) = n x^{n-1}$ (verifiable for positive integers $n$ via the binomial expansion, and valid for all real $n$).

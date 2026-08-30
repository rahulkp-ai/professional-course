**Core Concept & Intuition**

- **Goal:** Approximate complex, smooth curves ($y = f(x)$) using linear tangent lines to simplify non-linear relationships into basic arithmetic.
- **Secant Line:** A straight line passing through two distinct points on a curve.
- **Tangent Line:** A line touching a curve at a single point, representing the instantaneous direction and rate of change at that point.
- **Key Mechanism:** The slope of a secant line approaches the slope of the tangent line as the horizontal distance ($h$) between the two points approaches zero.

```mermaid
graph LR
    A[Point 1: x, f of x] -->|Perturb input by h| B[Point 2: x+h, f of x+h]
    B -->|Form ratio| C[Secant Slope: Δy / Δx]
    C -->|Limit as h → 0| D[Tangent Slope / Derivative]

```

---

**Edge Cases & Non-Smooth Curves**

- **Discontinuities:** Breaks in the curve prevent a well-defined tangent line.
- **Sharp Corners & Cusps:** Sudden direction changes make tangent line selection ambiguous.
- _Cusp Exception:_ Certain symmetric cusps have a well-defined **vertical tangent line** that bisects the curve and passes through the point.

---

**Derivation: Tangent Slope of $y = x^2$**

1. **Identify Two Points on the Parabola:**

- Point 1: $(x, x^2)$
- Point 2 (Perturbed by $h$): $(x + h, (x + h)^2)$

2. **Compute Secant Slope:**

$$\text{Slope}_{\text{secant}} = \frac{\Delta y}{\Delta x} = \frac{(x + h)^2 - x^2}{h}$$

3. **Algebraic Simplification:**

$$\text{Slope}_{\text{secant}} = \frac{(x^2 + 2xh + h^2) - x^2}{h} = \frac{2xh + h^2}{h} = \frac{h(2x + h)}{h} = 2x + h$$

4. **Evaluate the Limit ($h \to 0$):**

$$\text{Slope}_{\text{tangent}} = \lim_{h \to 0} (2x + h) = 2x$$

- **Generalization for $y = kx^2$:**

$$\text{Slope}_{\text{tangent}} = 2kx$$

---

**Geometric Connection: Circles & Calculus**

| Property            | Formula       | Calculus Relationship                                    |
| ------------------- | ------------- | -------------------------------------------------------- |
| **Area ($A$)**      | $A = \pi r^2$ | Base quadratic relationship ($y = kx^2$ where $k = \pi$) |
| **Perimeter ($P$)** | $P = 2\pi r$  | Tangent slope / derivative of Area with respect to $r$   |

- **Profound Insight:** Finding tangent slopes (**Differentiation**) and calculating bounded areas (**Integration**) are inverse operations, linking geometry directly to the _Fundamental Theorem of Calculus_ (Newton & Leibniz).

---

**Formal Definition of the Derivative**

For any smooth function $y = f(x)$, the slope of the tangent line at $x$ is defined as:

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

- **Difference Quotient:** $\frac{f(x + h) - f(x)}{h}$ represents the secant slope ($\frac{\text{Vertical Rise}}{\text{Horizontal Run}}$).
- **Limit Operator ($\lim_{h \to 0}$):** Evaluates the expression as $h$ gets infinitely close to $0$ without actually equaling $0$.

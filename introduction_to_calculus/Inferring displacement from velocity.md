# Introduction to Integral Calculus & Area Under Curves

## 1. Core Concepts: Undoing Differentiation

Integral calculus focuses on using information about a derivative to gain insight into the original function.

- **Antidifferentiation:** The mathematical process of reversing differentiation (going backwards from a derivative to the original function).
- **Integration:** Mathematically, putting parts together into a whole by computing areas under curves (converting rates into total quantities via multiplication/summation).
- **Fundamental Relationship:** Since derivatives represent instantaneous rates (limits of fractions, e.g., $v = \frac{dx}{dt}$), undoing a derivative involves multiplication, which geometric intuition links to finding rectangular areas.

### Real-World Applications of Reversing Rates

| Known Rate (Derivative)            | Target Quantity (Original Function) |
| :--------------------------------- | :---------------------------------- |
| Velocity ($v = \frac{dx}{dt}$)     | Displacement ($x$)                  |
| Acceleration ($a = \frac{dv}{dt}$) | Velocity ($v$)                      |
| Rate of drug absorption            | Total amount of drug absorbed       |
| Rate of bacterial growth           | Total population size               |
| Rate of disease spread             | Total infected population           |

---

## 2. Distance Traveled as Area Under the Velocity Curve

### A. Constant Velocity (Exact Calculation)

If an object moves at a constant velocity $v(t) = c$ from time $t = a$ to $t = b$:

- **Width of region:** $\Delta t = b - a$
- **Height of region:** $c$
- **Displacement / Area:**
  $$\text{Displacement} = \text{Velocity} \times \text{Time} = c(b - a)$$
  _(Represented visually by the exact area of a rectangle)._

---

### B. Accelerating Vehicle (Numerical Estimation via Riemann Sums)

When velocity fluctuates or increases, displacement is estimated by dividing the time interval into sub-intervals of width $\Delta t$ and constructing bounding rectangles.

#### 1. First Approximation ($\Delta t = 2\text{ s}$ over $10\text{ s}$)

- **Lower Bound (Left Endpoint Sum / Rectangles Below Curve):**
  Uses the minimum (starting) velocity of each 2-second sub-interval as height.
  $$\text{Lower Bound} = \Delta t \sum v_{\text{lower}} = 2 \times (5 + 14.5 + \dots + 31) = 200\text{ m}$$

- **Upper Bound (Right Endpoint Sum / Rectangles Above Curve):**
  Uses the maximum (ending) velocity of each 2-second sub-interval as height.
  $$\text{Upper Bound} = \Delta t \sum v_{\text{upper}} = 2 \times (14.5 + \dots + 32.5) = 255\text{ m}$$

- **Mid-Estimate (Average):**
  $$\text{Estimate} = \frac{\text{Lower Bound} + \text{Upper Bound}}{2} = \frac{200 + 255}{2} = 227.5\text{ m}$$

#### 2. Refined Approximation ($\Delta t = 1\text{ s}$ over $10\text{ s}$)

Increasing sampling frequency yields tighter bounds:

- **Lower Bound:** $216\text{ m}$
- **Upper Bound:** $243.5\text{ m}$
- **Revised Mid-Estimate:**
  $$\text{Estimate} = \frac{216 + 243.5}{2} = 229.75\text{ m}$$

---

## 3. Geometric Interpretation & The Trapezoidal Rule

Taking the average of the lower and upper bounding rectangles is geometrically equivalent to approximating the area under each curve segment using a **trapezium** (trapezoid).

- **Trapezium Area Formula:**
  $$\text{Area} = \frac{h_1 + h_2}{2} \times \Delta t$$
- **Effect of Concavity:**
  - If a velocity curve is **concave down** ($\frown$), a linear diagonal between data points lies slightly _below_ the actual curve.
  - Therefore, using trapezoids (or averaging upper/lower rectangular bounds) yields a **slight underestimate** of the true area/displacement.
  - As sub-interval widths $\Delta t \to 0$, curve fragments approach straight lines, making the trapezoidal approximation extremely precise.

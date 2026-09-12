## 1. Core Definitions

- **Extrema:** The collective term for maxima (highest values) and minima (lowest values) of a function $f(x)$.
- **Local Extremum:**
- **Local Maximum:** $f(a) \ge f(x)$ for all $x$ in a small neighborhood surrounding $a$.
- **Local Minimum:** $f(a) \le f(x)$ for all $x$ in a small neighborhood surrounding $a$.

- **Global Extremum:** An extremum whose inequality holds for **all** $x$ in the entire domain of the function.
- **Neighborhood:** A small interval on the real number line centered at input $a$.

---

## 2. Key Concepts & Behavior

### Turning Points & Derivatives

- **Turning Point:** A point where a curve transitions from increasing to decreasing (local max) or decreasing to increasing (local min).
- **Derivative Criterion:** For smooth functions, the tangent line at a turning point is horizontal ($\text{slope} = 0$). Turning points occur where $f'(x) = 0$.
- **Sign Diagrams:** By testing the sign of $f'(x)$ on either side of a critical point, you can determine if it is a local max ($+ \to -$) or local min ($- \to +$).

### Behavior Across Function Types

| Function Type                       | Behavior / Extrema Features                                                                        |
| ----------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Linear ($m \ne 0$)**              | Increases or decreases smoothly without bound. **No local or global extrema exist.**               |
| **Constant ($y = k$)**              | Horizontal line. The constant value $k$ is **simultaneously a global maximum and global minimum.** |
| **Quadratic ($y = ax^2 + bx + c$)** | Parabola. The vertex (apex) is a turning point where $f'(x) = 0$. <br>                             |

<br>• $a > 0$: Vertex is the **global minimum**.<br>

<br>• $a < 0$: Vertex is the **global maximum**. |
| **Unrestricted Cubic** | Up-down-up or down-up-down pattern. Has local extrema, but **no global extrema** because $f(x) \to \pm\infty$ on $\mathbb{R}$. |

---

## 3. The Closed Interval Method

To find the **global maximum and global minimum** of a continuous function on a closed interval $[a, b]$:

1. **Find Critical Points:** Calculate where $f'(x) = 0$ or where $f'(x)$ is **undefined** inside the interval.
2. **Evaluate Values:** Compute $f(x)$ at:

- The endpoints $x = a$ and $x = b$.
- All critical points found in Step 1.

3. **Compare Results:**

- **Global Maximum:** The largest evaluated value.
- **Global Minimum:** The smallest evaluated value.

---

## 4. Worked Transcript Examples

### Example 1: Standard Quadratic

- **Function Derivative:** $f'(x) = 2x - 2 = 0 \implies x = 1$
- **Turning Point:** $(1, -2)$
- **Result:** Since the derivative changes sign from negative (left) to positive (right), the global minimum is $y = -2$.

### Example 2: Restricted Cubic on $[0, 5]$

- **Derivative:** $f'(x) = 3(x - 1)(x - 3) = 0 \implies x = 1, 3$
- **Candidate Points Evaluated:**
- Endpoints: $f(0) = 1$, $f(5) = 21$
- Critical Points: $f(1) = 5$ (Local Max), $f(3) = 1$ (Local Min)

- **Results:**
- **Global Maximum:** $21$ (at $x = 5$)
- **Global Minimum:** $1$ (achieved twice: at $x = 0$ and $x = 3$)

### Example 3: Non-Differentiable Point (Absolute Value)

- **Function:** $f(x) = \vert{}x - 1\vert{} + 3$ on $[-2, 5]$
- **Derivative Behavior:** $f'(x) = -1$ for $x < 1$ and $f'(x) = 1$ for $x > 1$. The derivative is **undefined at $x = 1$** due to a sharp corner.
- **Candidate Points Evaluated:**
- $f(-2) = 6$ (Local Maximum)
- $f(5) = 7$ (Global Maximum)
- $f(1) = 3$ (Global Minimum)

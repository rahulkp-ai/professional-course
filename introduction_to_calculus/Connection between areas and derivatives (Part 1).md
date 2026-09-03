# Lecture Notes: Proof of the Fundamental Theorem of Calculus & Area Functions

This lesson covers the conceptual foundation and proof sketch of the **Fundamental Theorem of Calculus (FTC)**, focusing on how areas and derivatives are inherently inverse processes.

---

## 1. The Core Idea: The Area Function $A(x)$

To understand why the Fundamental Theorem works, we shift perspective by replacing the fixed upper limit $b$ with a variable $x$.

```mermaid
flowchart LR
    Start["Variable t on interval [a, b]"] --> DefineA["Define Area Function: A(x) = ∫ₐˣ f(t) dt"]
    DefineA --> Differentiate["Take Derivative: A'(x)"]
    Differentiate --> Result["A'(x) = f(x)"]
    Result --> Proof["Proves A(x) is an Antiderivative of f(x)"]

```

1. **Change of Variable**: Use $t$ as the horizontal axis variable:

$$y = f(t)$$

2. **Define $A(x)$**: Let $A(x)$ represent the cumulative area under $y = f(t)$ from $t = a$ up to $t = x$:

$$A(x) = \int_{a}^{x} f(t) \, dt$$

### Boundary Values of $A(x)$

- **At $x = a$**: $A(a) = \int_{a}^{a} f(t) \, dt = 0$ (Zero width, zero area)
- **At $x = b$**: $A(b) = \int_{a}^{b} f(t) \, dt$ (The full area under the curve)

---

## 2. Rate of Change of the Area Function

To find the derivative of the area function, $A'(x)$, we use the limit definition of the derivative:

$$A'(x) = \lim_{h \to 0} \frac{A(x + h) - A(x)}{h}$$

### Geometric Sandwiching (Squeeze Theorem)

Consider a small increment $h > 0$ and an increasing, continuous function $f(t)$:

```
           y ^                  f(x+h) ---+---+ (Upper Rectangle)
             |                            |   |
             |                   f(x) ----+---+ (Lower Rectangle)
             |                            |   |
             |                            |   |
             +----------------------------+---+----> t
                                         x   x+h
                                         |<--h-->|

```

- **Change in Area**: $A(x+h) - A(x)$ is the exact area under the curve between $t = x$ and $t = x + h$.
- **Lower Bound (Blue Rectangle)**: Height $f(x)$, Width $h \implies \text{Area} = h \cdot f(x)$
- **Upper Bound (Upper Rectangle)**: Height $f(x+h)$, Width $h \implies \text{Area} = h \cdot f(x+h)$

This sets up the double inequality:

$$h \cdot f(x) \le A(x+h) - A(x) \le h \cdot f(x+h)$$

Dividing all parts by $h > 0$:

$$f(x) \le \frac{A(x+h) - A(x)}{h} \le f(x+h)$$

### Applying the Limit $h \to 0$

- As $h \to 0$, $f(x)$ remains $f(x)$.
- Because $f$ is continuous, $\lim_{h \to 0} f(x+h) = f(x)$.
- By the **Squeeze Theorem (Squeeze Law)**:

$$A'(x) = \lim_{h \to 0} \frac{A(x+h) - A(x)}{h} = f(x)$$

> **Key Discovery**: The derivative of the area function with respect to $x$ is simply the value of the curve $f(x)$ at that point:
>
> $$\frac{d}{dx} \left[ \int_{a}^{x} f(t) \, dt \right] = f(x)$$

---

## 3. Completing the Proof of the FTC

Since $A'(x) = f(x)$, $A(x)$ is an **antiderivative** of $f(x)$.

1. Let $F(x)$ be **any** antiderivative of $f(x)$. Since all antiderivatives differ by a constant $C$:

$$F(x) = A(x) + C$$

2. Determine $C$ by evaluating at $x = a$:

$$F(a) = A(a) + C = 0 + C \implies C = F(a)$$

3. Substitute $C$ back into the relation:

$$F(x) = A(x) + F(a) \implies A(x) = F(x) - F(a)$$

4. Evaluate at $x = b$:

$$A(b) = F(b) - F(a)$$

Since $A(b) = \int_{a}^{b} f(t) \, dt$, this completes the proof:

$$\int_{a}^{b} f(t) \, dt = F(b) - F(a)$$

---

## 4. Summary Table

| Concept                     | Symbol                                  | Description                                                                |
| --------------------------- | --------------------------------------- | -------------------------------------------------------------------------- |
| **Area Function**           | $A(x) = \int_{a}^{x} f(t) \, dt$        | Accumulates area under $f(t)$ from lower bound $a$ up to variable $x$.     |
| **Derivative of Area**      | $A'(x) = f(x)$                          | Rate at which area expands at $x$ equals the height of the curve at $x$.   |
| **Antiderivative Relation** | $F(x) = A(x) + C$                       | Connects any algebraic antiderivative $F(x)$ to the area function $A(x)$.  |
| **FTC Formula**             | $\int_{a}^{b} f(x) \, dx = F(b) - F(a)$ | Computes exact continuous sums using endpoint values of an antiderivative. |

---

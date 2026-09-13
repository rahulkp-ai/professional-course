## 1. Mathematical Definitions & Formulations

The **Chain Rule** is used to differentiate composite functions (a function within a function).

### Leibniz's Notation

If $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

- **Intuition:** The differential $du$ in the numerator effectively cancels with $du$ in the denominator as if they were ordinary algebraic fractions.

### Function / Prime Notation

For the composite function $(f \circ g)(x) = f(g(x))$:

$$(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$$

---

## 2. Heuristic Proof Sketch

1. **Difference Quotient:** Let a small change $\Delta x$ induce a change $\Delta u$ in $u$, which in turn induces a change $\Delta y$ in $y$.
2. **Splitting the Fraction:** Assuming $\Delta u \neq 0$:

$$\frac{\Delta y}{\Delta x} = \frac{\Delta y}{\Delta u} \cdot \frac{\Delta u}{\Delta x}$$

3. **Taking Limits:** Applying $\lim_{\Delta x \to 0}$ and noting that $\Delta u \to 0$ as $\Delta x \to 0$:

$$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \left( \lim_{\Delta u \to 0} \frac{\Delta y}{\Delta u} \right) \cdot \left( \lim_{\Delta x \to 0} \frac{\Delta u}{\Delta x} \right)$$

4. **Conclusion:**

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

---

## 3. Worked Examples Analysis

### Example 1: Polynomial Function

Find $\frac{dy}{dx}$ for $y = (-3x + 6)^2$.

- **Direct Method (Expansion):**

$$y = 9x^2 - 36x + 36 \implies \frac{dy}{dx} = 18x - 36 = 18(x - 2)$$

- **Chain Rule Method:**
- Let $u = -3x + 6 \implies \frac{du}{dx} = -3$
- Then $y = u^2 \implies \frac{dy}{du} = 2u$
- Apply rule: $\frac{dy}{dx} = (2u)(-3) = -6u = -6(-3x + 6) = 18(x - 2)$

---

### Example 2: Exponential Functions

- **Derivative of $y = e^{-x}$:**
- Let $u = -x \implies \frac{du}{dx} = -1$ and $y = e^u \implies \frac{dy}{du} = e^u$
- $\frac{dy}{dx} = e^u \cdot (-1) = -e^{-x}$

- **General Rule for $y = e^{kx}$:**

$$\frac{d}{dx}\left(e^{kx}\right) = k e^{kx}$$

---

### Example 3: Order of Composition Matters

Given $f(x) = x^3$ (so $f'(x) = 3x^2$) and $g(x) = x^2 - 1$ (so $g'(x) = 2x$):

1. **Derivative of $(f \circ g)(x)$:**

$$(f \circ g)'(x) = f'(g(x)) \cdot g'(x) = 3(x^2 - 1)^2 \cdot 2x = 6x(x^2 - 1)^2$$

2. **Derivative of $(g \circ f)(x)$:**

$$(g \circ f)'(x) = g'(f(x)) \cdot f'(x) = 2(x^3) \cdot 3x^2 = 6x^5$$

---

## 4. Method Comparison

| Feature           | Direct Expansion                                    | Chain Rule                                                                        |
| ----------------- | --------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Prerequisites** | Polynomial terms easily expandable                  | Works on non-expandable/transcendental functions ($e^{g(x)}$, $\sin(g(x))$, etc.) |
| **Efficiency**    | Becomes tedious for high exponents/nested functions | Direct and minimal algebraic expansion required                                   |
| **Flexibility**   | Limited to simple algebraic forms                   | Handles multi-layered compositions via repeated substitution                      |

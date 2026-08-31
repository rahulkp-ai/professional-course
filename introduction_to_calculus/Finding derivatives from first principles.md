# Repertoire of Derivatives & Differentiation Rules

## Core Concepts & Basic Rules

- **Differentiation:** The process of taking derivatives of functions using the limit definition:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### Basic Rules

1. **Power Rule:** For any exponent $n$:

$$\frac{d}{dx}[x^n] = n x^{n-1}$$

2. **Linear Functions:** A straight line $f(x) = ax + b$ coincides with its tangent line at every point:

$$f'(x) = a$$

- Constant function ($a = 0$): $f(x) = b \implies f'(x) = 0$
- Identity function ($a = 1, b = 0$): $f(x) = x \implies f'(x) = 1$

3. **Additivity (Sum Rule):**

$$\frac{d}{dx}[u(x) + v(x)] = u'(x) + v'(x)$$

4. **Constant Multiple Rule:**

$$\frac{d}{dx}[k \cdot g(x)] = k \cdot g'(x)$$

---

## Differentiating Polynomials

Using linearity, differentiate each power of $x$, multiply by its constant factor, and sum the results.

### Example Walkthrough

For $f(x) = x^4 - 2x^3 + 5x^2 - 3x + 7$:

1. Differentiate $x^4 \to 4x^3$
2. Differentiate $-2x^3 \to -2(3x^2) = -6x^2$
3. Differentiate $5x^2 \to 5(2x) = 10x$
4. Differentiate $-3x \to -3(1) = -3$
5. Differentiate constant $7 \to 0$

$$f'(x) = 4x^3 - 6x^2 + 10x - 3$$

### Order of Differentiation

Differentiating a polynomial reduces its degree by 1. A polynomial of degree $n$ disappears (equals zero) after being differentiated $n+1$ times.

- **Example:** Quadratic ($n=2$)
- $f(x) = 3x^2 - 5x + 2$
- $f'(x) = 6x - 5$ (1st derivative)
- $f''(x) = 6$ (2nd derivative)
- $f'''(x) = 0$ (3rd derivative — degree $2+1=3$)

---

## The Natural Exponential Function $e^x$

### Fundamental Limit Property

Euler's number $e$ is defined such that the tangent line to $y = e^x$ at its y-intercept $(0,1)$ has a slope of $1$:

$$\lim_{h \to 0} \frac{e^h - 1}{h} = 1$$

### Proof: $\frac{d}{dx}[e^x] = e^x$

1. **Limit definition:**

$$f'(x) = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h}$$

2. **Apply exponent rules & factor:**

$$f'(x) = \lim_{h \to 0} \frac{e^x e^h - e^x}{h} = \lim_{h \to 0} \frac{e^x (e^h - 1)}{h}$$

3. **Pull out non-$h$ terms:**

$$f'(x) = e^x \cdot \lim_{h \to 0} \frac{e^h - 1}{h}$$

4. **Evaluate fundamental limit:**

$$f'(x) = e^x \cdot 1 = e^x$$

> $e^x$ is **indestructible** under differentiation — it reproduces itself identically regardless of how many times it is differentiated.

---

## Trigonometric Functions

### Important Trigonometric Limits

1. **Sine at Origin:** Slope of $y = \sin x$ at $x = 0$ is $1$:

$$\lim_{h \to 0} \frac{\sin h}{h} = 1$$

2. **Cosine at Peak:** Slope of $y = \cos x$ at $x = 0$ is $0$:

$$\lim_{h \to 0} \frac{\cos h - 1}{h} = 0$$

### Proof Sketch: $\frac{d}{dx}[\sin x] = \cos x$

1. **Limit definition:**

$$f'(x) = \lim_{h \to 0} \frac{\sin(x+h) - \sin x}{h}$$

2. **Apply sum identity $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$:**

$$f'(x) = \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h}$$

3. **Regroup and separate limits:**

$$f'(x) = \lim_{h \to 0} \left[ \sin x \left(\frac{\cos h - 1}{h}\right) + \cos x \left(\frac{\sin h}{h}\right) \right]$$

4. **Pull out constants relative to $h$ and substitute limit values:**

$$f'(x) = \sin x \cdot (0) + \cos x \cdot (1) = \cos x$$

---

## Summary of Elementary Derivatives & Cycles

| Function $f(x)$ | Derivative $f'(x)$              | Notes / Behavior                            |
| --------------- | ------------------------------- | ------------------------------------------- |
| $x^n$           | $n x^{n-1}$                     | Power Rule                                  |
| $e^x$           | $e^x$                           | Self-reproducing (indestructible)           |
| $\sin x$        | $\cos x$                        | Cyclic                                      |
| $\cos x$        | $-\sin x$                       | Cyclic                                      |
| $\tan x$        | $\frac{1}{\cos^2 x} = \sec^2 x$ | Derived via quotient rule in future lessons |

### 4-Step Trigonometric Higher-Order Derivatives

The circular functions form an endless 4-step derivative cycle:

1. **Position:** $f(x) = \sin x$
2. **Velocity ($f'$):** $\cos x$
3. **Acceleration ($f''$):** $-\sin x$
4. **Jerk ($f'''$):** $-\cos x$
5. **Snap ($f^{(4)}$):** $\sin x$ _(returns to start)_

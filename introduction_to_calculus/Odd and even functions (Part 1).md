# Lecture Notes: Symmetry in Functions — Even and Odd Functions

This topic explores the geometric symmetries and algebraic properties of **even** and **odd** functions, their connections to power series, derivative rules, and integral simplifications.

---

## 1. Geometric vs. Algebraic Symmetries

| Type               | Geometric Symmetry                        | Algebraic Condition | Visual Examples      |
| ------------------ | ----------------------------------------- | ------------------- | -------------------- |
| **Even Functions** | Reflectional symmetry across the $y$-axis | $f(-x) = f(x)$      | Letters: M, T, Y<br> |

<br>Curves: Parabola ($x^2$), Bell curve, Cosine |
| **Odd Functions** | $180^\circ$ rotational symmetry about the origin | $f(-x) = -f(x)$ | Letters: N, S, Z<br>

<br>Curves: Cubic ($x^3$), Sine, Newton's Serpentine |

> **Note**: The circle represents the most symmetrical shape in 2D space, possessing infinitely many axes of reflectional and rotational symmetry.

---

## 2. Classic Function Examples

### The Witch of Agnesi ($g(x) = \frac{1}{x^2 + 1}$) — Even Function

- **Algebraic Test**: $g(-x) = \frac{1}{(-x)^2 + 1} = \frac{1}{x^2 + 1} = g(x)$
- **Geometry**: Perfect reflectional symmetry across the $y$-axis.

### Newton's Serpentine ($h(x) = \frac{x}{x^2 + 1}$) — Odd Function

- **Algebraic Test**: $h(-x) = \frac{-x}{(-x)^2 + 1} = -\frac{x}{x^2 + 1} = -h(x)$
- **Geometry**: $180^\circ$ rotational symmetry around $(0,0)$. Turning points at $\left(1, \frac{1}{2}\right)$ and $\left(-1, -\frac{1}{2}\right)$ rotate directly into one another.

---

## 3. General Rules for Functions & Rational Expressions

1. **Polynomials**:

- Contains **only even powers** of $x$ (including $x^0 = 1$, constants) $\implies$ **Even Function**.
- Contains **only odd powers** of $x$ $\implies$ **Odd Function**.

2. **Rational Functions ($R(x) = \frac{P(x)}{Q(x)}$)**:

- $\frac{\text{Even}}{\text{Even}} = \text{Even}$
- $\frac{\text{Odd}}{\text{Odd}} = \text{Even}$
- $\frac{\text{Even}}{\text{Odd}} = \text{Odd}$
- $\frac{\text{Odd}}{\text{Even}} = \text{Odd}$

---

## 4. Connection to Infinite Series (Taylor / Maclaurin Series)

Circular functions reveal their even and odd nature when expanded into infinite power series:

### Sine Series (Odd Function)

Only contains **odd exponents** of $x$:

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$$

### Cosine Series (Even Function)

Only contains **even exponents** of $x$:

$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$

---

## 5. Differentiation and Integration Properties

### Derivative Rule

Differentiating shifts power exponents by $1$ ($\frac{d}{dx}[x^n] = n x^{n-1}$), changing parity:

- The derivative of an **even function** is always **odd**.
- The derivative of an **odd function** is always **even**.

$$\frac{d}{dx}[\sin(x)] = \cos(x) \quad (\text{Odd} \to \text{Even})$$

$$\frac{d}{dx}[\cos(x)] = -\sin(x) \quad (\text{Even} \to \text{Odd})$$

### Symmetric Definite Integration

When integrating over a symmetric interval $[-a, a]$:

- **Odd Function**: Areas on opposite sides of the $y$-axis cancel out.

$$\int_{-a}^{a} f_{\text{odd}}(x) \, dx = 0$$

- **Even Function**: Area is double the integral over $[0, a]$.

$$\int_{-a}^{a} f_{\text{even}}(x) \, dx = 2 \int_{0}^{a} f_{\text{even}}(x) \, dx$$

---

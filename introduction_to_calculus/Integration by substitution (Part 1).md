# Lecture Notes: Integration by Substitution

Integration by substitution (also known as $u$-substitution) is a core method for finding anti-derivatives and evaluating definite integrals. It acts as the integral calculus equivalent of the **Chain Rule** in differentiation, allowing us to simplify complex integrands through a change of variables.

---

## 1. Overview & Core Terminology

- **Indefinite Integral**: The process of anti-differentiation that yields a **family of functions** (including a constant of integration, $+ C$).
- **Definite Integral**: The process of evaluating an integral over a specific interval $[a, b]$, yielding a **real number** (representing net signed area).
- **Purpose of Substitution**: Reduces the complexity of a target integral by making an appropriate choice of variable substitution, followed by algebraic manipulation of the integrand and differential.

---

## 2. Indefinite Integration by Substitution

### Example 1: Algebraic Substitution

Find $\int 4x(x^2 + 1) \, dx$ using two methods:

#### Method A: Direct Expansion

$$\int 4x(x^2 + 1) \, dx = \int (4x^3 + 4x) \, dx = x^4 + 2x^2 + C$$

#### Method B: Substitution

1. Let $u = x^2 + 1$.
2. Differentiate with respect to $x$: $\frac{du}{dx} = 2x \implies du = 2x \, dx$.
3. Rearrange the original integral:

$$\int 2(x^2 + 1) \cdot (2x \, dx) = \int 2u \, du$$

4. Anti-differentiate with respect to $u$:

$$\int 2u \, du = u^2 + C'$$

5. Substitute $x^2 + 1$ back for $u$:

$$(x^2 + 1)^2 + C' = x^4 + 2x^2 + 1 + C'$$

> **Reconciling the Constants**:
> Although $x^4 + 2x^2 + C$ and $(x^2 + 1)^2 + C'$ look superficially different, expanding the second result shows $x^4 + 2x^2 + (1 + C')$. Letting $C = 1 + C'$ proves both methods produce the exact same family of functions.

---

### Example 2: Trigonometric Functions & "Guess and Check"

Find $\int \cos(2x) \, dx$:

- **Guess and Check Method**:
- _Guess_: $\sin(2x)$.
- _Check derivative_: $\frac{d}{dx}[\sin(2x)] = 2\cos(2x)$ (2 times larger than needed).
- _Adjust_: Divide by $2 \implies \frac{1}{2}\sin(2x) + C$.

- **Systematic Substitution Method**:

1. Let $u = 2x \implies \frac{du}{dx} = 2 \implies dx = \frac{1}{2}du$.
2. Substitute:

$$\int \cos(2x) \, dx = \int \cos(u) \cdot \frac{1}{2}du = \frac{1}{2} \int \cos(u) \, du = \frac{1}{2}\sin(u) + C = \frac{1}{2}\sin(2x) + C$$

---

## 3. General Framework & Formula Derivation

The substitution rule directly stems from the Chain Rule:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

If $y$ is an anti-derivative of $f(u)$ such that $\frac{dy}{du} = f(u)$, then:

$$y = \int f(u) \, du$$

By the Chain Rule:

$$\frac{dy}{dx} = f(u) \cdot \frac{du}{dx}$$

Expressing this as an indefinite integral with respect to $x$:

$$y = \int f(u) \frac{du}{dx} \, dx$$

Equating the two expressions for $y$ yields the **Integration by Substitution Formula**:

$$\int f(u) \frac{du}{dx} \, dx = \int f(u) \, du$$

In function notation where $u = g(x)$ and $\frac{du}{dx} = g'(x)$:

$$\int f(g(x)) g'(x) \, dx = \int f(u) \, du$$

---

## 4. Definite Integration & Changing Limits (Terminals)

When evaluating a definite integral using substitution, the limits of integration ($a$ and $b$) correspond to the original variable $x$ and **must be converted** to match the new variable $u$:

$$\int_{a}^{b} f(g(x)) g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du$$

### Example 3: Area Under $y = \cos\left(\frac{\pi x}{2}\right)$ from $x = -1$ to $x = 1$

#### Method 1: Anti-differentiate First, Then Apply Limits

1. Indefinite Integral: $\int \cos\left(\frac{\pi x}{2}\right) dx = \frac{2}{\pi}\sin\left(\frac{\pi x}{2}\right) + C$
2. Apply Fundamental Theorem of Calculus with original $x$ limits:

$$\left[ \frac{2}{\pi}\sin\left(\frac{\pi x}{2}\right) \right]_{-1}^{1} = \frac{2}{\pi}\sin\left(\frac{\pi}{2}\right) - \frac{2}{\pi}\sin\left(-\frac{\pi}{2}\right) = \frac{2}{\pi}(1) - \frac{2}{\pi}(-1) = \frac{4}{\pi}$$

#### Method 2: Convert Limits during Substitution (Recommended)

1. Let $u = \frac{\pi x}{2} \implies du = \frac{\pi}{2} dx \implies dx = \frac{2}{\pi} du$.
2. Convert limits ($x \to u$):

- Upper limit: $x = 1 \implies u = \frac{\pi(1)}{2} = \frac{\pi}{2}$
- Lower limit: $x = -1 \implies u = \frac{\pi(-1)}{2} = -\frac{\pi}{2}$

3. Evaluate transformed definite integral:

$$\int_{-\pi/2}^{\pi/2} \cos(u) \cdot \frac{2}{\pi} du = \frac{2}{\pi} [\sin(u)]_{-\pi/2}^{\pi/2} = \frac{2}{\pi} \left[ \sin\left(\frac{\pi}{2}\right) - \sin\left(-\frac{\pi}{2}\right) \right] = \frac{2}{\pi} [1 - (-1)] = \frac{4}{\pi}$$

---

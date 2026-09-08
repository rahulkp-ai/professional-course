# Lecture Notes: Definite Integrals of Even and Odd Functions

This topic focuses on evaluating definite integrals over symmetric intervals $[-a, a]$ by leveraging the geometric symmetries of even and odd functions.

---

## 1. General Principles on Symmetric Intervals $[-a, a]$

When the integration bounds are symmetric about the origin ($x \in [-a, a]$):

### Odd Functions ($f(-x) = -f(x)$)

- **Geometric Behavior**: $180^\circ$ rotational symmetry about the origin. Positive areas on one side of the $y$-axis are matched by equal-magnitude negative areas on the other.
- **Integral Value**: Areas cancel completely.

$$\int_{-a}^{a} f_{\text{odd}}(x) \, dx = 0$$

### Even Functions ($f(-x) = f(x)$)

- **Geometric Behavior**: Reflectional symmetry across the $y$-axis. The region to the left of the $y$-axis is an exact mirror image of the region to the right, preserving sign.
- **Integral Value**: Doubles the integral over the positive half-interval $[0, a]$.

$$\int_{-a}^{a} f_{\text{even}}(x) \, dx = 2 \int_{0}^{a} f_{\text{even}}(x) \, dx$$

---

## 2. Standard Examples

### Integrals of Odd Functions

- **Sine Function**:

$$\int_{-\pi/2}^{\pi/2} \sin(x) \, dx = [-\cos(x)]_{-\pi/2}^{\pi/2} = -\cos\left(\frac{\pi}{2}\right) - \left(-\cos\left(-\frac{\pi}{2}\right)\right) = 0 - 0 = 0$$

- **Cubic Function**:

$$\int_{-1}^{1} x^3 \, dx = \left[\frac{x^4}{4}\right]_{-1}^{1} = \frac{1}{4} - \frac{1}{4} = 0$$

- **Newton's Serpentine**:

$$\int_{-1}^{1} \frac{x}{x^2 + 1} \, dx = 0$$

### Integrals of Even Functions

- **Cosine Function**:

$$\int_{-\pi/2}^{\pi/2} \cos(x) \, dx = 2 \int_{0}^{\pi/2} \cos(x) \, dx = 2 [\sin(x)]_{0}^{\pi/2} = 2(1 - 0) = 2$$

- **The Witch of Agnesi**:

$$\int_{-1/\sqrt{3}}^{1/\sqrt{3}} \frac{1}{x^2 + 1} \, dx = 2 \int_{0}^{1/\sqrt{3}} \frac{1}{x^2 + 1} \, dx = 2 \left[ \arctan(x) \right]_{0}^{1/\sqrt{3}} = 2 \left( \frac{\pi}{6} - 0 \right) = \frac{\pi}{3}$$

---

## 3. Advanced Challenge Problem

### Problem Statement

Evaluate the definite integral:

$$I = \int_{-\pi/2}^{\pi/2} \frac{\cos(x)}{1 + e^{-x}} \, dx$$

### Key Concepts & Decomposition

1. **The Logistic / Sigmoid Component**:
   The denominator function $g(x) = \frac{1}{1 + e^{-x}}$ has a point of inflection at $\left(0, \frac{1}{2}\right)$ and possesses $180^\circ$ rotational symmetry about this point.
2. **Shifting to Create Parity**:
   Subtracting $\frac{1}{2}$ lowers the inflection point to the origin $(0,0)$, creating an odd function:

$$o(x) = \frac{1}{1 + e^{-x}} - \frac{1}{2} \quad \implies \quad o(-x) = -o(x)$$

3. **Algebraic Rewrite ("Add and Subtract $\frac{1}{2}$")**:

$$\frac{1}{1 + e^{-x}} = \left( \frac{1}{1 + e^{-x}} - \frac{1}{2} \right) + \frac{1}{2}$$

4. **Splitting the Integral**:

$$I = \int_{-\pi/2}^{\pi/2} \cos(x) \left( \left[ \frac{1}{1 + e^{-x}} - \frac{1}{2} \right] + \frac{1}{2} \right) dx$$

$$I = \underbrace{\int_{-\pi/2}^{\pi/2} \cos(x) \left( \frac{1}{1 + e^{-x}} - \frac{1}{2} \right) dx}_{\text{Part 1}} + \underbrace{\int_{-\pi/2}^{\pi/2} \frac{\cos(x)}{2} \, dx}_{\text{Part 2}}$$

### Evaluating the Parts

- **Part 1**: The integrand is $(\text{Even}) \times (\text{Odd}) = \text{Odd}$. Integrating an odd function over $[-\pi/2, \pi/2]$ yields **$0$**.
- **Part 2**: Using even symmetry for $\cos(x)$:

$$\int_{-\pi/2}^{\pi/2} \frac{\cos(x)}{2} \, dx = \frac{1}{2} \int_{-\pi/2}^{\pi/2} \cos(x) \, dx = \frac{1}{2} (2) = 1$$

$$\text{Final Answer: } I = 0 + 1 = 1$$

---

## 4. Key Takeaways

- **Parity Product Rules**:
- $\text{Even} \times \text{Even} = \text{Even}$
- $\text{Odd} \times \text{Odd} = \text{Even}$
- $\text{Even} \times \text{Odd} = \text{Odd}$

- Integrating over symmetric intervals simplifies hard problems: odd terms eliminate entirely ($= 0$), while even terms can be simplified to half-interval calculations.

---

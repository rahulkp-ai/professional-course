# Optimization Problems

Optimization involves using the derivative to find the maximum or minimum values of a given function by analyzing its turning points and sign diagrams.

---

## 1. Problem 1: Minimizing a Number and Its Reciprocal

### Problem Statement

Find the minimum sum of a positive real number and its reciprocal.

### Mathematical Formulation

Let $x > 0$. We wish to minimize the function:
$$y = f(x) = x + \frac{1}{x} = x + x^{-1}$$

### Differentiation & Critical Points

1. **Find the derivative:**
   $$y' = 1 - x^{-2} = 1 - \frac{1}{x^2} = \frac{x^2 - 1}{x^2}$$
2. **Set $y' = 0$ to find critical points:**
   $$\frac{x^2 - 1}{x^2} = 0 \implies x^2 - 1 = 0 \implies x = \pm 1$$
   _(Note: $y'$ is undefined at $x = 0$, representing a vertical asymptote)._

### Sign Diagram ($x > 0$)

- For $0 < x < 1$: $y' < 0$ (Decreasing $\downarrow$)
- At $x = 1$: $y' = 0$ (Turning point)
- For $x > 1$: $y' > 0$ (Increasing $\uparrow$)

### Conclusion

- A **global minimum** for positive real numbers occurs at $x = 1$.
- **Minimum Value:** $f(1) = 1 + \frac{1}{1} = 2$.
- **Geometric Behavior:** The curve has two branches separated by a vertical asymptote at $x = 0$ and an oblique asymptote at $y = x$.

---

## 2. Problem 2: Maximizing Rectangular Area with Fixed Perimeter

### Problem Statement

Determine the dimensions $x$ and $y$ that maximize the area $A$ of a rectangular enclosure using $100\text{ m}$ of fencing.

### Mathematical Formulation

- **Area equation:** $A = xy$
- **Perimeter constraint:** $2x + 2y = 100 \implies x + y = 50 \implies y = 50 - x$

Substitute $y$ into the Area equation:
$$A(x) = x(50 - x) = 50x - x^2$$

### Differentiation & Critical Points

1. **Find the first derivative:**
   $$\frac{dA}{dx} = 50 - 2x = 2(25 - x)$$
2. **Find the critical point:**
   $$\frac{dA}{dx} = 0 \implies 25 - x = 0 \implies x = 25$$
3. **Check second derivative for concavity:**
   $$\frac{d^2A}{dx^2} = -2 < 0 \implies \text{Concave down (Maximum)}$$

### Sign Diagram for $\frac{dA}{dx}$

- For $x < 25$: $\frac{dA}{dx} > 0$ (Increasing $\uparrow$)
- For $x > 25$: $\frac{dA}{dx} < 0$ (Decreasing $\downarrow$)

### Conclusion

- **Dimensions:** $x = 25\text{ m}$, $y = 50 - 25 = 25\text{ m}$ (A perfect square).
- **Maximum Area:** $A = 25 \times 25 = 625\text{ m}^2$.

---

## 3. Problem 3: Viewing Angle Optimization (Statue of Liberty Problem)

### Problem Statement

A statue of height $h = 46\text{ m}$ stands on a pedestal also of height $h = 46\text{ m}$. Find the horizontal distance $x$ from the base that maximizes the subtended viewing angle $\theta$, and find the maximum angle.

```
   |  Statue (Height = h)
   |   |
   |---|  (Top of pedestal / Bottom of statue)
   |   |  Pedestal (Height = h)
   |___|_______________________
   Base        x          Viewer
```

### Trigonometric Setup

- Let $\phi$ be the angle subtended by the pedestal alone:
  $$\tan(\phi) = \frac{h}{x} \implies \phi = \arctan\left(\frac{h}{x}\right)$$
- Let $\theta + \phi$ be the angle subtended by both statue and pedestal combined (height $2h$):
  $$\tan(\theta + \phi) = \frac{2h}{x} \implies \theta + \phi = \arctan\left(\frac{2h}{x}\right)$$
- Therefore, the viewing angle function $\theta(x)$ is:
  $$\theta(x) = \arctan\left(\frac{2h}{x}\right) - \arctan\left(\frac{h}{x}\right)$$

### Differentiation using Chain Rule

Recall that $\frac{d}{du}[\arctan(u)] = \frac{1}{u^2 + 1}$.

Let $u = \frac{2h}{x} \implies \frac{du}{dx} = -\frac{2h}{x^2}$  
Let $v = \frac{h}{x} \implies \frac{dv}{dx} = -\frac{h}{x^2}$

$$\frac{d\theta}{dx} = \frac{1}{\left(\frac{2h}{x}\right)^2 + 1} \cdot \left(-\frac{2h}{x^2}\right) - \frac{1}{\left(\frac{h}{x}\right)^2 + 1} \cdot \left(-\frac{h}{x^2}\right)$$

### Algebraic Simplification

$$\frac{d\theta}{dx} = \frac{-2h}{x^2 + 4h^2} - \frac{-h}{x^2 + h^2} = \frac{h}{x^2 + h^2} - \frac{2h}{x^2 + 4h^2}$$

Combine over a common denominator:
$$\frac{d\theta}{dx} = \frac{h(x^2 + 4h^2) - 2h(x^2 + h^2)}{(x^2 + h^2)(x^2 + 4h^2)} = \frac{h x^2 + 4h^3 - 2hx^2 - 2h^3}{(x^2 + h^2)(x^2 + 4h^2)}$$

$$\frac{d\theta}{dx} = \frac{h(2h^2 - x^2)}{(x^2 + h^2)(x^2 + 4h^2)}$$

### Maximization Analysis

- The denominator and constant $h$ are strictly positive for $x > 0$.
- The sign of $\frac{d\theta}{dx}$ is determined entirely by the numerator term: $(2h^2 - x^2)$.
- **Critical Point:** $\frac{d\theta}{dx} = 0 \implies 2h^2 - x^2 = 0 \implies x = \sqrt{2}h$.

### Sign Diagram for $\frac{d\theta}{dx}$

- For $0 < x < \sqrt{2}h$: $\frac{d\theta}{dx} > 0$ (Increasing $\uparrow$)
- For $x > \sqrt{2}h$: $\frac{d\theta}{dx} < 0$ (Decreasing $\downarrow$)
- A **local/global maximum** occurs at $x = \sqrt{2}h$.

### Numerical Evaluation ($h = 46\text{ m}$)

1. **Optimal Distance ($x$):**
   $$x = \sqrt{2} \times 46 \approx 65.05\text{ m}$$

2. **Maximum Viewing Angle ($\theta_{\text{max}}$):**
   $$\theta_{\text{max}} = \arctan(\sqrt{2}) - \arctan\left(\frac{1}{\sqrt{2}}\right)$$
   _(Note: $h$ cancels out, making the maximum angle independent of height when statue and pedestal heights are equal)._
   $$\theta_{\text{max}} \approx 0.3398\text{ radians} \approx 19.47^\circ$$

---

## 4. Summary Checklist of Optimization Steps

1. **Model:** Set up the objective function in terms of a single variable (use constraint equations to eliminate extra variables if needed).
2. **Differentiate:** Find the first derivative of the objective function.
3. **Critical Points:** Solve for points where the derivative is zero or undefined.
4. **Test:** Use sign diagrams or second derivative tests to confirm local/global ma

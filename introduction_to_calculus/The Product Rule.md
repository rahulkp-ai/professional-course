# Product Rule in Calculus

## 1. Definition & Notation

The **Product Rule** is used to differentiate a function $y$ that is expressed as the product of two functions, $u(x)$ and $v(x)$:
$$y = u \cdot v$$

### Notations

- **Leibniz Notation:**
  $$\frac{dy}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}$$
- **Prime Notation:**
  $$y' = u v' + v u'$$

---

## 2. Examples

### Example 1: Polynomial Product

Find $y'$ for $y = (x^2 + 3x - 4)(2x - 5)$.

- **Method 1: Direct Expansion (Without Product Rule)**
  1. Expand brackets: $y = 2x^3 + x^2 - 23x + 20$
  2. Differentiate directly: $y' = 6x^2 + 2x - 23$

- **Method 2: Product Rule**
  1. Set $u = x^2 + 3x - 4 \implies u' = 2x + 3$
  2. Set $v = 2x - 5 \implies v' = 2$
  3. Apply $y' = uv' + vu'$:
     $$y' = (x^2 + 3x - 4)(2) + (2x - 5)(2x + 3)$$
  4. Expand and simplify:
     $$y' = 2x^2 + 6x - 8 + 4x^2 - 4x - 15 = 6x^2 + 2x - 23$$

---

### Example 2: Exponential Product

Find $y'$ for $y = (1 + e^{-x})(2 - e^{3x})$.

- **Method 1: Direct Expansion**
  1. Expand: $y = 2 - e^{3x} + 2e^{-x} - e^{2x}$
  2. Differentiate term-by-term using $\frac{d}{dx}[e^{kx}] = k e^{kx}$:
     $$y' = -3e^{3x} - 2e^{-x} - 2e^{2x}$$

- **Method 2: Product Rule**
  1. Set $u = 1 + e^{-x} \implies u' = -e^{-x}$
  2. Set $v = 2 - e^{3x} \implies v' = -3e^{3x}$
  3. Apply $y' = uv' + vu'$:
     $$y' = (1 + e^{-x})(-3e^{3x}) + (2 - e^{3x})(-e^{-x})$$
  4. Expand and simplify:
     $$y' = -3e^{3x} - 3e^{2x} - 2e^{-x} + e^{2x} = -3e^{3x} - 2e^{2x} - 2e^{-x}$$

---

### Example 3: Trigonometric Product

Find $y'$ for $y = x \sin(x)$.

- **Application of Product Rule:**
  1. Set $u = x \implies u' = 1$
  2. Set $v = \sin(x) \implies v' = \cos(x)$
  3. Apply $\frac{dy}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}$:
     $$\frac{dy}{dx} = x \cos(x) + \sin(x) \cdot 1 = x \cos(x) + \sin(x)$$

---

## 3. Proof Sketch (First Principles)

1. **Initial Increment:**
   $$\Delta y = y(x + \Delta x) - y(x) = u(x + \Delta x)v(x + \Delta x) - u(x)v(x)$$

2. **Algebraic Trick (Add and Subtract $u(x + \Delta x)v(x)$):**
   $$\Delta y = u(x + \Delta x)v(x + \Delta x) - u(x + \Delta x)v(x) + u(x + \Delta x)v(x) - u(x)v(x)$$

3. **Factorization:**
   $$\Delta y = u(x + \Delta x)\Big[v(x + \Delta x) - v(x)\Big] + v(x)\Big[u(x + \Delta x) - u(x)\Big]$$
   $$\Delta y = u(x + \Delta x)\Delta v + v(x)\Delta u$$

4. **Divide by $\Delta x$ and Take the Limit ($\Delta x \to 0$):**
   $$\frac{\Delta y}{\Delta x} = u(x + \Delta x)\frac{\Delta v}{\Delta x} + v(x)\frac{\Delta u}{\Delta x}$$

5. **Apply Limits:**
   - As $\Delta x \to 0$, $u(x + \Delta x) \to u(x)$ (assuming continuity).
   - $\frac{\Delta v}{\Delta x} \to \frac{dv}{dx}$ and $\frac{\Delta u}{\Delta x} \to \frac{du}{dx}$.

   $$\frac{dy}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}$$

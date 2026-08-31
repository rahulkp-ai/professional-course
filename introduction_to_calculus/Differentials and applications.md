# Differentials, Linear Approximations & Errors

Differentials treat $\frac{dy}{dx}$ like an ordinary fraction in localized contexts, yielding the fundamental linear approximation formula:

$$\Delta y \approx dy = f'(x) \cdot \Delta x$$

This provides a method for approximating changes, propagation of error, and specific values along a curve using tangent line geometry.

---

## 1. Linear Approximations of Area ($A = x^2$)

For a square of side length $x = 100\text{ m}$, the exact area change is $\Delta A = (x + \Delta x)^2 - x^2 = 2x\Delta x + (\Delta x)^2$. The differential approximation drops the second-order terms $(\Delta x)^2$:

$$dA = 2x\,dx \implies \Delta A \approx 2x\,\Delta x = 200\,\Delta x$$

```
   ┌───────────────────────┬────────┐
   │                       │        │
   │                       │ Beige  │  ← Corner error: (Δx)²
   │                       │ (Error)│
   │     Blue Square       ├────────┤
   │                       │        │
   │      x × x            │ Pink   │  ← Differential estimate:
   │    (10,000 m²)        │ x · Δx │     2x · Δx (Two pink strips)
   │                       │        │
   └───────────────────────┴────────┘
             x                 Δx

```

| Change in Side ($\Delta x$)         | Exact $\Delta A$    | Estimated $\Delta A$ ($200 \cdot \Delta x$) | Error ($(\Delta x)^2$) | Relative Error |
| ----------------------------------- | ------------------- | ------------------------------------------- | ---------------------- | -------------- |
| **$10\text{ m}$**                   | $2,100\text{ m}^2$  | $2,000\text{ m}^2$                          | $100\text{ m}^2$       | $4.76\%$       |
| **$5\text{ m}$**                    | $1,025\text{ m}^2$  | $1,000\text{ m}^2$                          | $25\text{ m}^2$        | $2.44\%$       |
| **$1\text{ m}$**                    | $201\text{ m}^2$    | $200\text{ m}^2$                            | $1\text{ m}^2$         | $0.497\%$      |
| **$0.01\text{ m}$ ($1\text{ cm}$)** | $2.0001\text{ m}^2$ | $2.0000\text{ m}^2$                         | $0.0001\text{ m}^2$    | $0.005\%$      |

As $\Delta x \to 0$, the corner beige square $(\Delta x)^2$ becomes vanishingly small compared to the two linear pink rectangles $2x\Delta x$, causing the proportional error to approach zero.

---

## 2. Error Propagation in Sphere Volume ($V = \frac{4}{3}\pi r^3$)

Differentials allow us to relate percentage errors (relative errors) between input and output measurements without needing the exact absolute size of the object.

### Derivation of Relative Error

1. **Differentiate:**

$$\frac{dV}{dr} = \frac{d}{dr}\left[\frac{4}{3}\pi r^3\right] = 4\pi r^2 \implies dV = 4\pi r^2 dr$$

2. **Form Relative Error Ratio:**

$$\frac{\Delta V}{V} \approx \frac{dV}{V} = \frac{4\pi r^2 dr}{\frac{4}{3}\pi r^3} = 3 \left(\frac{dr}{r}\right)$$

3. **Apply Bound:**
   Given $\left\vert{}\frac{\Delta r}{r}\right\vert{} \le 0.02$ ($2\%$ error in radius):

$$\left\vert{}\frac{\Delta V}{V}\right\vert{} \approx 3\left\vert{}\frac{\Delta r}{r}\right\vert{} \le 3(0.02) = 0.06$$

$$\text{Percentage Error in Volume } \approx 6\%$$

> **Key Takeaway:** For any power relation $y = k \cdot x^n$, the relative error in $y$ is approximately **$n$ times** the relative error in $x$:
>
> $$\frac{dy}{y} = n \frac{dx}{x}$$

---

## 3. Estimating Roots via Linearization ($f(x) = x^{1/3}$)

To estimate $f(x + \Delta x) = (x + \Delta x)^{1/3}$ near a known anchor point $x_0 = 64$ (where $f(64) = 4$):

$$\frac{dy}{dx} = \frac{1}{3}x^{-2/3} \implies dy = \frac{dx}{3x^{2/3}}$$

At $x_0 = 64$:

$$dy = \frac{dx}{3(64)^{2/3}} = \frac{dx}{3(16)} = \frac{dx}{48}$$

### Comparison of Estimates

$$\text{Approximate Value} = 4 + \frac{\Delta x}{48} \quad \left(\text{or coarsened to } 4 + \frac{\Delta x}{50}\right)$$

| Target Value       | $\Delta x$ | Rough Approx. ($/50$)                | Refined Approx. ($/48$)                   | Actual Value  | Refined Accuracy    |
| ------------------ | ---------- | ------------------------------------ | ----------------------------------------- | ------------- | ------------------- |
| **$\sqrt[3]{70}$** | $+6$       | $4 + \frac{6}{50} = \mathbf{4.1200}$ | $4 + \frac{6}{48} = \mathbf{4.1250}$      | $4.121285...$ | $2\text{ decimals}$ |
| **$\sqrt[3]{65}$** | $+1$       | $4 + \frac{1}{50} = \mathbf{4.0200}$ | $4 + \frac{1}{48} = \mathbf{4.020833...}$ | $4.020725...$ | $4\text{ decimals}$ |
| **$\sqrt[3]{63}$** | $-1$       | $4 - \frac{1}{50} = \mathbf{3.9800}$ | $4 - \frac{1}{48} = \mathbf{3.979166...}$ | $3.979057...$ | $4\text{ decimals}$ |

---

## 4. Tangent Line Equivalence

Estimating outputs using differentials is mathematically identical to finding $y$-values on the tangent line $L(x)$ at $x = x_0$.

1. **Point-Slope Form:**

$$y - y_0 = m(x - x_0)$$

2. **Substitute $x_0 = 64$, $y_0 = 4$, and $m = f'(64) = \frac{1}{48}$:**

$$y - 4 = \frac{1}{48}(x - 64)$$

3. **Linearization Equation:**

$$L(x) = \frac{x}{48} + \left(4 - \frac{64}{48}\right) = \frac{x}{48} + \frac{8}{3}$$

Evaluating $L(65)$ gives:

$$L(65) = \frac{65}{48} + \frac{128}{48} = \frac{193}{48} = 4.020833...$$

This yields the exact same formula $\Delta y = \frac{\Delta x}{48}$ derived via differentials.

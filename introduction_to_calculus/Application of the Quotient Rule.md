# Calculus Notes: Analysis of "The Witch of Agnesi" & Derivative of Inverse Tan

## 1. Overview of the Function

The curve defined by:
$$y = \frac{1}{x^2 + 1}$$

is historically known as the **Witch of Maria Agnesi** (named after 18th-century Italian mathematician Maria Agnesi).

### Key Characteristics:

- **Domain:** All real numbers ($\mathbb{R}$), since $x^2 + 1 \ge 1 > 0$ for all real $x$.
- **Y-intercept:** $(0, 1)$
- **X-intercepts:** None (the function is strictly positive, $y > 0$).
- **Horizontal Asymptote:** $y = 0$ as $x \to \pm\infty$ ($\lim_{x \to \pm\infty} \frac{1}{x^2 + 1} = 0$).

---

## 2. First Derivative Analysis (Increasing/Decreasing & Turning Points)

Using the Chain Rule by setting $y = (x^2 + 1)^{-1}$:

$$\frac{dy}{dx} = -1 \cdot (x^2 + 1)^{-2} \cdot \frac{d}{dx}(x^2 + 1) = -\frac{2x}{(x^2 + 1)^2}$$

### Critical Points & Behavior:

- **Critical Point:** Set $y' = 0 \implies -2x = 0 \implies x = 0$.
- **Sign Diagram for $y'$:**
  - For $x < 0$: $y' > 0$ (Function is **increasing**).
  - For $x > 0$: $y' < 0$ (Function is **decreasing**).
- **Global Maximum:** Located at $(0, 1)$.

---

## 3. Second Derivative Analysis (Concavity & Points of Inflection)

Using the **Quotient Rule** on $y' = \frac{-2x}{(x^2 + 1)^2}$:

- Let $u = -2x \implies u' = -2$
- Let $v = (x^2 + 1)^2 \implies v' = 2(x^2 + 1) \cdot 2x = 4x(x^2 + 1)$

Applying $y'' = \frac{v u' - u v'}{v^2}$:

$$y'' = \frac{(x^2 + 1)^2 (-2) - (-2x)(4x(x^2 + 1))}{(x^2 + 1)^4}$$

Factoring out $(x^2 + 1)$ from the numerator and simplifying:

$$y'' = \frac{(x^2 + 1)\left[-2(x^2 + 1) + 8x^2\right]}{(x^2 + 1)^4} = \frac{6x^2 - 2}{(x^2 + 1)^3} = \frac{2(3x^2 - 1)}{(x^2 + 1)^3}$$

### Inflection Points & Concavity:

- Set $y'' = 0 \implies 3x^2 - 1 = 0 \implies x = \pm\frac{1}{\sqrt{3}}$
- **Sign Diagram for $y''$:**
  - $x < -\frac{1}{\sqrt{3}}$: $y'' > 0$ (**Concave Up**)
  - $-\frac{1}{\sqrt{3}} < x < \frac{1}{\sqrt{3}}$: $y'' < 0$ (**Concave Down**)
  - $x > \frac{1}{\sqrt{3}}$: $y'' > 0$ (**Concave Up**)
- **Points of Inflection:** $x = \pm\frac{1}{\sqrt{3}}$

---

## 4. Trigonometric Identity Derivation

Dividing the Pythagorean Identity by $\cos^2(x)$:

$$\sin^2(x) + \cos^2(x) = 1$$
$$\frac{\sin^2(x)}{\cos^2(x)} + \frac{\cos^2(x)}{\cos^2(x)} = \frac{1}{\cos^2(x)}$$
$$\tan^2(x) + 1 = \sec^2(x)$$

---

## 5. Derivative of the Inverse Tangent Function $\arctan(x)$

### Theorem:

$$\frac{d}{dx}\left[\arctan(x)\right] = \frac{1}{x^2 + 1}$$

### Proof via Inverse Function Derivative Rule:

1. Let $y = \tan(x) \implies x = \arctan(y)$.
2. The derivative of $\tan(x)$ is:
   $$\frac{dy}{dx} = \sec^2(x) = \tan^2(x) + 1 = y^2 + 1$$
3. By the reciprocal rule of inverse derivatives ($\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}$):
   $$\frac{dx}{dy} = \frac{d}{dy}\left[\arctan(y)\right] = \frac{1}{y^2 + 1}$$
4. Expressing in standard dummy variable $x$:
   $$\frac{d}{dx}\left[\arctan(x)\right] = \frac{1}{x^2 + 1}$$

---

## Summary of Curve Features

| Feature                   | Function Behavior                                                |
| :------------------------ | :--------------------------------------------------------------- |
| **Max Value**             | Global peak at $(0, 1)$                                          |
| **Symmetry**              | Symmetric about the y-axis (Even function: $f(-x) = f(x)$)       |
| **Shape**                 | Bell-shaped curve (qualitatively similar to Gaussian $e^{-x^2}$) |
| **Derivative Connection** | Represents the rate of change of $\arctan(x)$                    |

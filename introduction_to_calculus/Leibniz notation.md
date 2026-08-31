# Leibniz Notation for Derivatives

## 1. Introduction to Leibniz Notation

- **Notation Origin:** Named after **Gottfried Wilhelm Leibniz** (co-founder of calculus alongside Isaac Newton).
- **Core Concept:** Expresses the derivative as a fraction-like operator involving differentials ($\frac{dy}{dx}$) rather than prime/dash notation ($f'(x)$).
- **Heuristic & Historical Background:**
- Leibniz viewed derivatives as ratios of **infinitesimals** (idealized, infinitely small numbers).
- Formally placed on rigorous foundations in the 1960s via **Nonstandard Analysis** and the **Hyperreal Number System**.

---

## 2. Geometric Interpretation & Limit Definition

1. **Perturbation of Input ($x$):**

- Let $h = \Delta x$ (change or difference in $x$).

2. **Induced Change in Output ($y$):**

- $\Delta y = f(x + \Delta x) - f(x)$ (change or difference in $y$).

3. **Secant Line Slope:**

$$\text{Slope} = \frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x}$$

4. **Tangent Line Slope (Derivative):**

$$\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}$$

- In the limit, the Greek uppercase $\Delta$ becomes the Latin lowercase $d$, yielding the **differentials** $dy$ and $dx$.

---

## 3. Revisiting Examples in Leibniz Notation

- **Constant Function:** $y = k \implies \frac{dy}{dx} = 0$
- **Linear Function:** $y = mx + k \implies \frac{dy}{dx} = m$
- **Quadratic Polynomial:** $y = ax^2 + bx + c$

$$\frac{dy}{dx} = \frac{d}{dx}[ax^2] + \frac{d}{dx}[bx] + \frac{d}{dx}[c] = 2ax + b$$

> **Common Pitfall Warning:** Do **not** confuse power functions with exponential functions.
>
> - **Power Function ($x^n$):** Variable $x$ is the base $\implies \frac{d}{dx}[x^n] = n x^{n-1}$.
> - **Exponential Function ($e^x$):** Variable $x$ is the exponent $\implies \frac{d}{dx}[e^x] = e^x$. Bringing the exponent down ($\cancel{x e^{x-1}}$) is completely incorrect.

---

## 4. Inverting Derivatives & Inverse Functions

Because Leibniz notation places $x$ and $y$ explicitly in the denominator and numerator, reversing input and output roles yields a reciprocal relationship:

$$\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}$$

This identity provides a powerful method for finding derivatives of inverse functions.

### Application 1: Derivative of Natural Logarithm ($\ln x$)

1. Let $y = e^x$, so its inverse is $x = \ln y$.
2. We know $\frac{dy}{dx} = e^x = y$.
3. Apply the inversion rule:

$$\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}} = \frac{1}{y}$$

4. Expressing in terms of $x$ (swapping input notation back to $x$):

$$\frac{d}{dx}[\ln x] = \frac{1}{x}$$

- **Geometric Intuition:** The graphs of $y = e^x$ and $y = \ln x$ are reflections across $y = x$.
- At $x = 0$, $y = e^x$ has slope $1$. Reflected at $x = 1$, $y = \ln x$ retains slope $1 = \frac{1}{1}$.
- At $x = 2$, slope of $\ln x$ is $\frac{1}{2}$; at $x = 3$, slope is $\frac{1}{3}$.

---

### Application 2: Derivative of Square Root ($\sqrt{x}$)

1. Let $y = x^2$ (for $x \ge 0$), so $x = \sqrt{y} = y^{1/2}$.
2. We know $\frac{dy}{dx} = 2x = 2\sqrt{y}$.
3. Invert the derivative:

$$\frac{dx}{dy} = \frac{1}{2\sqrt{y}}$$

4. Reverting to standard input variable $x$:

$$\frac{d}{dx}[\sqrt{x}] = \frac{1}{2\sqrt{x}} = \frac{1}{2}x^{-1/2}$$

_(Matches the Power Rule for $n = \frac{1}{2}$)_

---

### Application 3: Derivative of Cube Root ($\sqrt[3]{x}$)

1. Let $y = x^3$, so $x = \sqrt[3]{y} = y^{1/3}$.
2. We know $\frac{dy}{dx} = 3x^2 = 3(y^{1/3})^2 = 3y^{2/3}$.
3. Invert the derivative:

$$\frac{dx}{dy} = \frac{1}{3y^{2/3}} = \frac{1}{3}y^{-2/3}$$

4. Reverting to standard input variable $x$:

$$\frac{d}{dx}[x^{1/3}] = \frac{1}{3}x^{-2/3}$$

_(Matches the Power Rule for $n = \frac{1}{3}$)_

---

## 5. Summary Table of Inverse Derivatives

| Original Function $y = f(x)$ | Derivative $\frac{dy}{dx}$ | Inverse Function $x = g(y)$ | Inverse Derivative $\frac{dx}{dy} = \frac{1}{dy/dx}$ | Standard Form $\frac{d}{dx}[g(x)]$ |
| ---------------------------- | -------------------------- | --------------------------- | ---------------------------------------------------- | ---------------------------------- |
| $y = e^x$                    | $e^x = y$                  | $x = \ln y$                 | $\frac{1}{y}$                                        | $\frac{1}{x}$                      |
| $y = x^2$                    | $2x = 2\sqrt{y}$           | $x = x^{1/2}$               | $\frac{1}{2\sqrt{y}}$                                | $\frac{1}{2\sqrt{x}}$              |
| $y = x^3$                    | $3x^2 = 3y^{2/3}$          | $x = x^{1/3}$               | $\frac{1}{3y^{2/3}}$                                 | $\frac{1}{3}x^{-2/3}$              |

# Advanced Integration by Substitution & Strategic Techniques

This guide explores advanced integration by substitution techniques, handling trigonometric powers, algebraic restructuring, logarithmic substitutions, and managing constants of integration.

---

## 1. Trigonometric Powers: Odd vs. Even Powers

When integrating combinations of circular functions such as $\int \sin^m(x) \cos^n(x) \, dx$, target the **odd power** to set up the substitution differential.

### Example 1: Evaluating $\int \sin^3(x) \cos^2(x) \, dx$

1. **Identify the problematic term**: The even power $\cos^2(x)$ is difficult to manipulate directly. Use the odd power $\sin^3(x)$ by peeling off a single $\sin(x)$ factor.

$$\sin^3(x) \cos^2(x) = \sin^2(x) \cos^2(x) \cdot \sin(x)$$

2. **Apply the Pythagorean Identity**: Rewrite $\sin^2(x)$ as $1 - \cos^2(x)$:

$$\int (1 - \cos^2(x)) \cos^2(x) \cdot \sin(x) \, dx$$

3. **Substitute**:

- Let $u = \cos(x) \implies \frac{du}{dx} = -\sin(x) \implies -du = \sin(x) \, dx$.

4. **Transform and Integrate**:

$$\begin{aligned}    \int (1 - \cos^2(x)) \cos^2(x) \cdot \sin(x) \, dx &= -\int (1 - u^2) u^2 \, du \\    &= \int (u^4 - u^2) \, du \\    &= \frac{u^5}{5} - \frac{u^3}{3} + C \\    &= \frac{\cos^5(x)}{5} - \frac{\cos^3(x)}{3} + C    \end{aligned}$$

---

## 2. Rational Functions: Completing the Square & Splitting Integrands

For rational functions with a linear numerator and a non-factorable quadratic denominator, complete the square to group the terms.

### Example 2: Evaluating $\int \frac{4x + 7}{x^2 + 2x + 2} \, dx$

1. **Complete the Square in the Denominator**:

$$x^2 + 2x + 2 = (x + 1)^2 + 1$$

2. **Shift the Variable**:

- Let $u = x + 1 \implies dx = du$ and $x = u - 1$.
- Substitute into the numerator: $4x + 7 = 4(u - 1) + 7 = 4u + 3$.

3. **Transform and Split the Integral**:

$$\int \frac{4u + 3}{u^2 + 1} \, du = \int \frac{4u}{u^2 + 1} \, du + 3 \int \frac{1}{u^2 + 1} \, du$$

4. **Solve Each Component Separately**:

- **Part A**: $\int \frac{4u}{u^2 + 1} \, du$
  Let $v = u^2 + 1 \implies dv = 2u \, du \implies 2 \, dv = 4u \, du$.

$$\int \frac{2}{v} \, dv = 2 \ln\vert{}v\vert{} = 2 \ln(u^2 + 1)$$

_(Note: $u^2 + 1 > 0$, so absolute value signs can be dropped)._

- **Part B**: $3 \int \frac{1}{u^2 + 1} \, du$
  Recall that $\frac{d}{du}[\arctan(u)] = \frac{1}{u^2 + 1}$.

$$3 \int \frac{1}{u^2 + 1} \, du = 3 \arctan(u)$$

5. **Recombine and Substitute back to $x$** ($u = x + 1$):

$$\int \frac{4x + 7}{x^2 + 2x + 2} \, dx = 2 \ln((x + 1)^2 + 1) + 3 \arctan(x + 1) + C$$

> **The Witch of Agnesi**: The curve defined by $y = \frac{1}{x^2 + 1}$ gives rise to the inverse tangent integral $\int \frac{1}{x^2 + 1} dx = \arctan(x) + C$.

---

## 3. Advanced Radical Substitutions

When the integrand contains expressions like $\sqrt{x}$ inside a fraction, substitute the entire denominator to eliminate radical complications.

### Example 3: Evaluating $\int \frac{\sqrt{x}}{1 + \sqrt{x}} \, dx$

1. **Set Up the Substitution**:

- Let $u = 1 + \sqrt{x} \implies \sqrt{x} = u - 1 \implies x = (u - 1)^2$.
- Differentiating yields $dx = 2(u - 1) \, du$.

2. **Substitute into the Integral**:

$$\int \frac{\sqrt{x}}{1 + \sqrt{x}} \, dx = \int \frac{u - 1}{u} \cdot 2(u - 1) \, du = 2 \int \frac{(u - 1)^2}{u} \, du$$

3. **Expand and Divide Term-by-Term**:

$$2 \int \frac{u^2 - 2u + 1}{u} \, du = 2 \int \left( u - 2 + \frac{1}{u} \right) \, du$$

4. **Integrate**:

$$2 \left( \frac{u^2}{2} - 2u + \ln\vert{}u\vert{} \right) + C' = u^2 - 4u + 2 \ln\vert{}u\vert{} + C'$$

5. **Back-Substitute $u = 1 + \sqrt{x}$ and Simplify**:

$$\begin{aligned}    &= (1 + \sqrt{x})^2 - 4(1 + \sqrt{x}) + 2 \ln(1 + \sqrt{x}) + C' \\    &= (1 + 2\sqrt{x} + x) - 4 - 4\sqrt{x} + 2 \ln(1 + \sqrt{x}) + C' \\    &= x - 2\sqrt{x} + 2 \ln(1 + \sqrt{x}) + (-3 + C')    \end{aligned}$$

6. **Absorb Constants**:
   Combine the numerical constant $-3$ with $C'$ into a single constant $C$:

$$\int \frac{\sqrt{x}}{1 + \sqrt{x}} \, dx = x - 2\sqrt{x} + 2 \ln(1 + \sqrt{x}) + C$$

---

## 4. Summary of Strategy Selection

| Integrand Pattern                            | Recommended Initial Substitution      | Key Algebraic / Trigonometric Identity                          |
| -------------------------------------------- | ------------------------------------- | --------------------------------------------------------------- |
| $\sin^{\text{odd}}(x) \cos^{\text{even}}(x)$ | $u = \cos(x)$                         | $\sin^2(x) = 1 - \cos^2(x)$                                     |
| $\cos^{\text{odd}}(x) \sin^{\text{even}}(x)$ | $u = \sin(x)$                         | $\cos^2(x) = 1 - \sin^2(x)$                                     |
| $\frac{Ax + B}{ax^2 + bx + c}$               | $u = x + k$ (after completing square) | $\int \frac{1}{u^2+1} du = \arctan(u) + C$                      |
| $\frac{f(\sqrt{x})}{a + b\sqrt{x}}$          | $u = a + b\sqrt{x}$                   | Express $x$ in terms of $u$: $x = \left(\frac{u-a}{b}\right)^2$ |

---

To see a detailed geometric derivation and visual walkthrough of parametric curves related to these substitution methods, watch [The Witch of Maria Agnesi curve derivation](https://www.youtube.com/watch?v=tIWFMCU-KCk). This video breaks down how the $\frac{1}{x^2 + 1}$ form arises geometrically and connects to inverse trigonometric integration.

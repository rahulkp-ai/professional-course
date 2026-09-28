# The Quotient Rule

## 1. Definition of the Quotient Rule

The **Quotient Rule** allows us to differentiate a function that is expressed as the quotient of two functions, $y = \frac{u}{v}$, where both $u$ and $v$ are functions of $x$.

### Formulations

- **Leibniz Notation:**
  $$\frac{dy}{dx} = \frac{v \frac{du}{dx} - u \frac{dv}{dx}}{v^2}$$

- **Prime/Dash Notation:**
  $$y' = \frac{v u' - u v'}{v^2}$$

---

## 2. Derivation using Product and Chain Rules

The quotient rule is derived directly by rewriting the quotient as a product:

$$y = \frac{u}{v} = u \cdot v^{-1}$$

1. **Apply the Product Rule:**
   $$\frac{dy}{dx} = u \cdot \frac{d}{dx}(v^{-1}) + v^{-1} \cdot \frac{du}{dx}$$

2. **Apply the Chain Rule to $\frac{d}{dx}(v^{-1})$:**
   $$\frac{d}{dx}(v^{-1}) = \frac{d}{dv}(v^{-1}) \cdot \frac{dv}{dx} = -1 \cdot v^{-2} \cdot \frac{dv}{dx} = -\frac{1}{v^2} \frac{dv}{dx}$$

3. **Combine & Simplify:**
   $$\frac{dy}{dx} = u \left(-\frac{1}{v^2} \frac{dv}{dx}\right) + \frac{1}{v} \frac{du}{dx}$$
   $$\frac{dy}{dx} = \frac{-u \frac{dv}{dx} + v \frac{du}{dx}}{v^2} = \frac{v \frac{du}{dx} - u \frac{dv}{dx}}{v^2}$$

---

## 3. Practical Examples

### Example 1: Differentiating $y = \frac{x^2 + 1}{x}$

- **Method A: Direct Algebraic Splitting**
  $$y = \frac{x^2}{x} + \frac{1}{x} = x + x^{-1}$$
  $$y' = 1 - x^{-2} = 1 - \frac{1}{x^2} = \frac{x^2 - 1}{x^2}$$

- **Method B: Applying the Quotient Rule**
  Let $u = x^2 + 1 \implies u' = 2x$  
  Let $v = x \implies v' = 1$  
  $$y' = \frac{(x)(2x) - (x^2 + 1)(1)}{x^2} = \frac{2x^2 - x^2 - 1}{x^2} = \frac{x^2 - 1}{x^2}$$

### Example 2: Derivative of $\tan(x)$

Express $\tan(x)$ as $\frac{\sin(x)}{\cos(x)}$:

- $u = \sin(x) \implies u' = \cos(x)$
- $v = \cos(x) \implies v' = -\sin(x)$

Applying the Quotient Rule:
$$\frac{d}{dx}[\tan(x)] = \frac{\cos(x)\cos(x) - \sin(x)(-\sin(x))}{\cos^2(x)} = \frac{\cos^2(x) + \sin^2(x)}{\cos^2(x)}$$

Using the Pythagorean Identity ($\sin^2(x) + \cos^2(x) = 1$):
$$\frac{d}{dx}[\tan(x)] = \frac{1}{\cos^2(x)} = \sec^2(x)$$

---

## 4. Trigonometric Reciprocals Notation Summary

| Function      | Reciprocal Definition                                   | Common Abbreviations | Derivative                           |
| :------------ | :------------------------------------------------------ | :------------------- | :----------------------------------- |
| **Secant**    | $\sec(x) = \frac{1}{\cos(x)}$                           | `sec`                | $\frac{d}{dx}[\tan(x)] = \sec^2(x)$  |
| **Cosecant**  | $\csc(x) = \frac{1}{\sin(x)}$                           | `csc`, `cosec`       | —                                    |
| **Cotangent** | $\cot(x) = \frac{\cos(x)}{\sin(x)} = \frac{1}{\tan(x)}$ | `cot`, `cotan`       | $\frac{d}{dx}[\cot(x)] = -\csc^2(x)$ |

---

## 5. Key Takeaways

- The Quotient Rule makes differentiating complex fractional expressions procedural and mechanical.
- The derived derivative formula allows finding slopes of tangent lines at defined points even if the graph's global shape is unknown.

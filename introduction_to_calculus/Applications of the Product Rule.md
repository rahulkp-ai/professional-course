# Applications of the Product Rule & Power Rule Proofs

## 1. Curve Sketching: Gaussian Curve ($y = e^{-x^2}$)

### Baseline Properties (from First Derivative Analysis)

- **$y$-intercept:** $(0, 1)$
- **$x$-intercepts:** None
- **Asymptote:** $y = 0$ (Horizontal asymptote as $x \to \pm\infty$)
- **Critical Point:** Local maximum at $x = 0$
- **First Derivative:**
  $$y' = -2x e^{-x^2}$$

---

### Finding the Second Derivative ($y''$)

Using the **Product Rule** on $y' = u \cdot v$:

- Let $u = -2x \implies u' = -2$
- Let $v = e^{-x^2} \implies v' = y' = -2x e^{-x^2}$

Applying $y'' = u v' + v u'$:
$$y'' = (-2x)(-2x e^{-x^2}) + (e^{-x^2})(-2)$$
$$y'' = 4x^2 e^{-x^2} - 2 e^{-x^2}$$
$$y'' = 2(2x^2 - 1) e^{-x^2}$$

---

### Concavity and Inflection Points

Since $e^{-x^2} > 0$ for all real $x$, $y'' = 0$ occurs when:
$$2x^2 - 1 = 0 \implies x = \pm\frac{1}{\sqrt{2}}$$

#### Concavity Sign Diagram:

- **$x < -\frac{1}{\sqrt{2}}$:** $y'' > 0 \implies$ **Concave Up**
- **$-\frac{1}{\sqrt{2}} < x < \frac{1}{\sqrt{2}}$:** $y'' < 0 \implies$ **Concave Down**
- **$x > \frac{1}{\sqrt{2}}$:** $y'' > 0 \implies$ **Concave Up**

> **Inflection Points:** Occur at $x = \pm\frac{1}{\sqrt{2}}$, confirming the bell curve shape.

---

## 2. Proof of Power Rule for Positive Integers ($n \in \mathbb{Z}^+$)

**Claim ($\star$):**
$$\frac{d}{dx}[x^n] = n x^{n-1} \quad \text{for all } n \in \mathbb{Z}^+$$

### Proof by Mathematical Induction

#### Base Case ($n = 1$)

$$\frac{d}{dx}[x^1] = 1 \cdot x^0 = 1 \quad \text{(Verified true)}$$

#### Inductive Hypothesis ($\star$)

Assume statement $(\star)$ holds for a specific integer $n$:
$$\frac{d}{dx}[x^n] = n x^{n-1}$$

#### Inductive Step ($\star \implies \star\star$)

Show statement $(\star\star)$ holds for $n+1$:
$$\frac{d}{dx}[x^{n+1}] = (n+1) x^n$$

1. Express $x^{n+1}$ as a product: $x^{n+1} = x^n \cdot x$
2. Apply the **Product Rule**:
   $$\frac{d}{dx}[x^{n+1}] = x^n \cdot \frac{d}{dx}[x] + x \cdot \frac{d}{dx}[x^n]$$
3. Substitute base derivative $\frac{d}{dx}[x]=1$ and inductive hypothesis $(\star)$:
   $$\frac{d}{dx}[x^{n+1}] = x^n (1) + x \left(n x^{n-1}\right)$$
4. Simplify:
   $$\frac{d}{dx}[x^{n+1}] = x^n + n x^n = (n + 1) x^n$$

By mathematical induction, $\frac{d}{dx}[x^n] = n x^{n-1}$ is true for all positive integers $n$.

---

## 3. Generalization to Real Exponents ($x^\alpha$ where $\alpha \in \mathbb{R}, x > 0$)

**Claim:**
$$\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}$$

### Proof Using the Chain Rule and Logarithms

1. Rewrite $x^\alpha$ using base $e$:
   $$y = x^\alpha = e^{\ln(x^\alpha)} = e^{\alpha \ln(x)}$$

2. Set $u = \alpha \ln(x) \implies \frac{du}{dx} = \frac{\alpha}{x}$

3. Apply the **Chain Rule** ($\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$):
   $$\frac{d}{dx}[e^u] = e^u \cdot \frac{du}{dx}$$
   $$\frac{d}{dx}[x^\alpha] = e^{\alpha \ln(x)} \cdot \left(\frac{\alpha}{x}\right)$$

4. Simplify using original variable substitution:
   $$\frac{d}{dx}[x^\alpha] = x^\alpha \cdot \alpha \cdot x^{-1} = \alpha x^{\alpha - 1}$$

# Derivation of the Rule of 70 (and 69 / 72)

The **Rule of 70** is a financial rule of thumb that estimates the number of years $x$ required to double an investment at an annual compounding interest rate $i\%$:

$$\text{Years to double } (x) \approx \frac{70}{i}$$

---

## 1. Mathematical Basis: Linear Approximation of $\ln(1 + \Delta)$

The calculus foundation relies on the tangent line approximation of the natural logarithm near $x = 1$.

1. **Tangent Line to $y = \ln(x)$ at $x = 1$:**

- $f(x) = \ln(x) \implies f'(x) = \frac{1}{x} \implies f'(1) = 1$
- Point of tangency: $(1, \ln(1)) = (1, 0)$
- Tangent line equation: $y - 0 = 1(x - 1) \implies y = x - 1$

2. **Linear Approximation:**
   For $x$ close to $1$:

$$\ln(x) \approx x - 1$$

3. **Substituting $x = 1 + \Delta$ (where $\Delta$ is small):**

$$\ln(1 + \Delta) \approx (1 + \Delta) - 1 = \Delta$$

$$\ln(1 + \Delta) \approx \Delta \quad (\text{for small } \Delta)$$

---

## 2. Deriving the Doubling Time Formula

1. **Compound Interest Formula:**
   Let $P$ be the initial principal, $i$ be the interest rate in percentage points, and $x$ be the number of years:

$$y(x) = P \left(1 + \frac{i}{100}\right)^x$$

2. **Set Target to Double Principal ($y(x) = 2P$):**

$$2P = P \left(1 + \frac{i}{100}\right)^x$$

3. **Divide by $P$ and Take Natural Logarithms:**

$$2 = \left(1 + \frac{i}{100}\right)^x$$

$$\ln(2) = \ln\left[\left(1 + \frac{i}{100}\right)^x\right] = x \ln\left(1 + \frac{i}{100}\right)$$

4. **Solve for $x$:**

$$x = \frac{\ln(2)}{\ln\left(1 + \frac{i}{100}\right)}$$

---

## 3. Applying Linear Approximation

Using $\ln(1 + \Delta) \approx \Delta$ with $\Delta = \frac{i}{100}$ (since realistic interest rates make $\frac{i}{100}$ small):

$$\ln\left(1 + \frac{i}{100}\right) \approx \frac{i}{100}$$

Substituting this approximation back into the doubling time equation:

$$x \approx \frac{\ln(2)}{\frac{i}{100}} = \frac{100 \cdot \ln(2)}{i}$$

Since $\ln(2) \approx 0.693147$:

$$100 \cdot \ln(2) \approx 69.31$$

$$x \approx \frac{69.31}{i}$$

---

## 4. Comparing Rules of Thumb

| Rule           | Numerator Formula | Ideal Use Case                                 | Pros & Cons                                                                                                                                      |
| -------------- | ----------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Rule of 69** | $\frac{69}{i}$    | Continuous compounding / Exact linear estimate | **Most mathematically accurate** for small continuous/annual rates, but $69$ has few divisors.                                                   |
| **Rule of 70** | $\frac{70}{i}$    | Standard financial rule of thumb               | Rounding $69.31 \to 70$ makes mental math easier while maintaining high accuracy.                                                                |
| **Rule of 72** | $\frac{72}{i}$    | Practical mental math                          | Highly composite number ($72$ is divisible by $1, 2, 3, 4, 6, 8, 9, 12$), making quick calculations trivial (e.g., at $6\%$, $72/6 = 12$ years). |

---

## 5. Numerical Example Comparison ($i = 6\%$)

$$\text{Exact Value: } x = \frac{\ln(2)}{\ln(1.06)} = \frac{0.693147}{0.058269} \approx 11.896 \text{ years}$$

- **Rule of 69:** $\frac{69}{6} = 11.50 \text{ years}$
- **Rule of 70:** $\frac{70}{6} = 11.67 \text{ years}$
- **Rule of 72:** $\frac{72}{6} = 12.00 \text{ years}$ _(Closest mental integer)_

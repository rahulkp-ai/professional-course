# Error Propagation Using Differentials

When calculating a quantity $y = f(x)$ or $y = f(u, v)$ from measured inputs, small uncertainties (errors) in those inputs propagate into the calculated result. Using differentials, we relate **absolute error** ($\Delta y \approx dy$), **relative error** ($\frac{dy}{y}$), and **percentage error** ($\frac{dy}{y} \times 100\%$).

---

## General Rules for Relative Error Propagation

For functions of a single variable $y = k x^n$:

$$\frac{dy}{y} = n \left(\frac{dx}{x}\right)$$

When multiple independent variables are involved, we use **multivariable differentials**:

$$dy = \frac{\partial y}{\partial u} du + \frac{\partial y}{\partial v} dv$$

To find the worst-case maximum error bound, we sum the absolute magnitudes of the individual error contributions:

$$\vert{}dy\vert{} \le \left\vert{}\frac{\partial y}{\partial u}\right\vert{} \vert{}du\vert{} + \left\vert{}\frac{\partial y}{\partial v}\right\vert{} \vert{}dv\vert{}$$

---

## Example 1: Electrical Power Dissipation ($P = I^2 R$)

The power $P$ dissipated in a resistor depends on the current $I$ and resistance $R$.

### Problem

Suppose current $I$ is measured with a maximum percentage error of **$\pm 3\%$**, and resistance $R$ is measured with a maximum percentage error of **$\pm 1.5\%$**. Estimate the maximum percentage error in the calculated power $P$.

### Derivation

1. **Take the natural logarithm of both sides:**

$$\ln P = \ln(I^2 R) = 2 \ln I + \ln R$$

2. **Differentiate implicitly (take differentials):**

$$\frac{dP}{P} = 2 \frac{dI}{I} + \frac{dR}{R}$$

3. **Apply maximum error bounds using absolute values:**

$$\left\vert{}\frac{dP}{P}\right\vert{} \le 2 \left\vert{}\frac{dI}{I}\right\vert{} + \left\vert{}\frac{dR}{R}\right\vert{}$$

4. **Substitute the given percentage errors:**

$$\left\vert{}\frac{dP}{P}\right\vert{} \le 2(3\%) + 1.5\% = 6\% + 1.5\% = 7.5\%$$

$$\text{Maximum Percentage Error in Power } (P) \approx 7.5\%$$

> **Insight:** Because current $I$ is squared in the power formula, its error contribution is **doubled**. A $3\%$ error in current contributes $6\%$ to the total error in power.

---

## Example 2: Period of a Simple Pendulum ($T = 2\pi \sqrt{\frac{L}{g}}$)

The period $T$ of a simple pendulum depends on its length $L$ and local gravitational acceleration $g$.

### Problem

A student uses a pendulum to measure $g$. The length $L$ is measured with a **$1\%$ error**, and the period $T$ is measured with a **$0.5\%$ error**. Estimate the percentage error in the calculated value of $g$.

### Derivation

1. **Solve for $g$ in terms of $L$ and $T$:**

$$T^2 = 4\pi^2 \frac{L}{g} \implies g = 4\pi^2 L T^{-2}$$

2. **Take the natural logarithm:**

$$\ln g = \ln(4\pi^2) + \ln L - 2 \ln T$$

3. **Take differentials:**

$$\frac{dg}{g} = \frac{dL}{L} - 2 \frac{dT}{T}$$

4. **Apply maximum bound for total error:**

$$\left\vert{}\frac{dg}{g}\right\vert{} \le \left\vert{}\frac{dL}{L}\right\vert{} + 2 \left\vert{}\frac{dT}{T}\right\vert{}$$

5. **Substitute the percentage errors:**

$$\left\vert{}\frac{dg}{g}\right\vert{} \le 1\% + 2(0.5\%) = 1\% + 1\% = 2\%$$

$$\text{Maximum Percentage Error in } g \approx 2\%$$

---

## Example 3: Ideal Gas Law Pressure ($P = \frac{nRT}{V}$)

For $n$ moles of an ideal gas, pressure depends on temperature $T$ and volume $V$.

### Problem

If temperature $T$ increases by **$2\%$** and volume $V$ increases by **$3\%$** (with $n$ and $R$ constant), estimate the percentage change in pressure $P$.

### Derivation

1. **Take differentials:**

$$\ln P = \ln(nR) + \ln T - \ln V \implies \frac{dP}{P} = \frac{dT}{T} - \frac{dV}{V}$$

2. **Substitute relative changes ($\frac{dT}{T} = +0.02$, $\frac{dV}{V} = +0.03$):**

$$\frac{dP}{P} \approx +0.02 - 0.03 = -0.01$$

$$\text{Pressure decreases by approximately } 1\%$$

---

## Summary of Common Power-Law Error Formulas

| Physical Quantity / Formula                                      | Logarithmic Differential Expression                 | Relative Error Relation                                              |
| ---------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------- |
| **Kinetic Energy:** $K = \frac{1}{2}m v^2$                       | $\frac{dK}{K} = \frac{dm}{m} + 2\frac{dv}{v}$       | $\% \text{Error}_K \le \% \text{Error}_m + 2(\% \text{Error}_v)$     |
| **Focal Length:** $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$      | $\frac{df}{f^2} = \frac{du}{u^2} + \frac{dv}{v^2}$  | $df = \left(\frac{f}{u}\right)^2 du + \left(\frac{f}{v}\right)^2 dv$ |
| **Density:** $\rho = \frac{m}{V} = \frac{m}{\frac{4}{3}\pi r^3}$ | $\frac{d\rho}{\rho} = \frac{dm}{m} - 3\frac{dr}{r}$ | $\% \text{Error}_\rho \le \% \text{Error}_m + 3(\% \text{Error}_r)$  |

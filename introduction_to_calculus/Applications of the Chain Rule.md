## 1. Application 1: Analysis of the Gaussian Curve ($y = e^{-x^2}$)

The Gaussian curve (or standard normal probability density function) is a fundamental bell-shaped curve in science and statistics.

### **Key Curve Sketching Features**

1. **$y$-intercept:** $f(0) = e^{-(0)^2} = 1 \implies (0, 1)$.
2. **$x$-intercepts:** None, because $e^{-x^2} > 0$ for all real $x$.
3. **Asymptotic Behavior:**

$$\lim_{x \to \pm\infty} e^{-x^2} = \lim_{x \to \pm\infty} \frac{1}{e^{x^2}} = 0$$

The $x$-axis ($y = 0$) is a **horizontal asymptote** at both ends. 4. **Symmetry:** $f(-x) = e^{-(-x)^2} = e^{-x^2} = f(x)$. It is an **even function**, symmetric across the $y$-axis.

---

### **First Derivative & Critical Points (Chain Rule Application)**

- Let $y = e^u$ where $u = -x^2$.
- $\frac{dy}{du} = e^u$ and $\frac{du}{dx} = -2x$.
- Applying the Chain Rule:

$$y' = \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = e^{-x^2} \cdot (-2x) = -2x e^{-x^2}$$

- **Sign Diagram of $y'$:**
- Since $e^{-x^2} > 0$ always, $y' = 0$ only at $x = 0$.
- $y' > 0$ for $x < 0$ (Increasing)
- $y' < 0$ for $x > 0$ (Decreasing)
- **Local / Global Maximum** at $(0, 1)$.

> **Note on Second Derivative ($y''$):** Finding $y''$ requires differentiating $y' = -2x e^{-x^2}$, which involves a product of two terms ($-2x$ and $e^{-x^2}$). This requires the **Product Rule**, which is covered in the next lecture.

---

## 2. Application 2: Mathematical Modeling of a Melting Ice Cube

### **Problem Setup & Variables**

- Let $t =$ time in hours.
- Let $x(t) =$ side length of the ice cube.
- **Volume:** $V(t) = x^3$
- **Surface Area:** $A(t) = 6x^2$ (6 square faces)

---

### **Physical Assumption & Differential Equation**

The rate of volume loss is directly proportional to the surface area exposed to warm air:

$$\frac{dV}{dt} = k \cdot A(t) = 6k x^2 \quad \text{(where $k < 0$ is a constant)}$$

From basic differentiation of $V = x^3$:

$$\frac{dV}{dx} = 3x^2$$

---

### **Connecting Rates via the Chain Rule**

Using the Chain Rule to solve for $\frac{dx}{dt}$ (rate of change of side length):

$$\frac{dV}{dt} = \frac{dV}{dx} \cdot \frac{dx}{dt}$$

Substitute known terms:

$$6k x^2 = 3x^2 \cdot \frac{dx}{dt}$$

Divide both sides by $3x^2$:

$$\frac{dx}{dt} = 2k \quad \text{(a constant)}$$

---

### **Linear Model Deduction**

Because the rate of change of $x$ with respect to time $t$ is constant ($\frac{dx}{dt} = 2k$), the side length $x(t)$ **must be a linear function of time**:

$$x(t) = 2kt + C \quad \text{(where $C$ is a constant equal to initial side length $x(0)$)}$$

---

### **Solving for Total Melting Time**

#### **1. Boundary Conditions**

- Initial volume at $t = 0$: $V(0) = C^3$
- After 3 hours ($t = 3$), $10\%$ has melted $\implies 90\%$ volume remains:

$$V(3) = 0.9 \cdot V(0) \implies [x(3)]^3 = 0.9 \cdot C^3$$

#### **2. Relation Between $C$ and $k$**

Substitute $x(3) = 6k + C$:

$$(6k + C)^3 = 0.9 C^3$$

Take the cube root of both sides:

$$6k + C = \sqrt[3]{0.9} \cdot C$$

$$6k = (\sqrt[3]{0.9} - 1) C \implies C = \frac{6k}{\sqrt[3]{0.9} - 1}$$

#### **3. Calculating Time to Complete Disappearance ($x(t) = 0$)**

Set $x(t) = 0$:

$$2kt + C = 0 \implies 2kt = -C \implies t = \frac{-C}{2k}$$

Substitute $C$:

$$t = \frac{-1}{2k} \cdot \frac{6k}{\sqrt[3]{0.9} - 1} = \frac{3}{1 - \sqrt[3]{0.9}}$$

#### **4. Numerical Evaluation**

$$t = \frac{3}{1 - 0.96549} \approx \frac{3}{0.03451} \approx 86.9 \text{ hours}$$

---

## 3. Comparison of Mathematical Decay Models

| Model Type            | Governing Equation              | Behavior as $t \to \infty$                           | Reaches Zero?                                |
| --------------------- | ------------------------------- | ---------------------------------------------------- | -------------------------------------------- |
| **Melting Ice Cube**  | $x(t) = 2kt + C$ (Linear width) | Hits zero at finite time $t \approx 86.9\text{ hrs}$ | **Yes**, object completely disappears.       |
| **Exponential Decay** | $y(t) = y_0 e^{-kt}$            | Asymptotic to $0$ as $t \to \infty$                  | **No**, only approaches zero asymptotically. |

# Lecture Notes: Geometric Applications of Area Functions & Integration

This lesson explores geometric applications of area functions, proving why derivative relationships exist between 2D and 3D measurements, and using integral calculus to derive the volume and surface area formulas for a sphere.

---

## 1. Circle Area and Perimeter via Geometric Squeezing

To explain why differentiating the area of a circle $A(r) = \pi r^2$ yields its perimeter $P(r) = 2\pi r$, consider a small radial expansion $\Delta r > 0$:

```
                       +-------------------+
                       | Outer Radius: r+Δr|
                       | Perimeter: P(r+Δr)|
                       +---------+---------+
                                 |
                     Path Area ΔA = A(r+Δr) - A(r)
                                 |
                       +---------+---------+
                       | Inner Radius: r   |
                       | Perimeter: P(r)   |
                       +-------------------+

```

### Derivation Steps

1. **Enclose the Path Area ($\Delta A$)**:
   The area of the added concentric pathway lies between the inner boundary and outer boundary rectangular estimates:

$$P(r) \cdot \Delta r \le \Delta A \le P(r + \Delta r) \cdot \Delta r$$

2. **Form the Difference Quotient**:
   Divide through by $\Delta r > 0$:

$$P(r) \le \frac{\Delta A}{\Delta r} \le P(r + \Delta r)$$

3. **Apply the Limit $\Delta r \to 0$**:

- As $\Delta r \to 0$, $P(r + \Delta r) \to P(r)$ by continuity.
- $\lim_{\Delta r \to 0} \frac{\Delta A}{\Delta r} = \frac{dA}{dr}$
- By the **Squeeze Law**:

$$\frac{dA}{dr} = P(r)$$

---

## 2. Sphere Volume and Surface Area Relationship

Applying the same geometric logic to a 3D sphere of radius $r$, volume $V(r)$, and surface area $S(r)$:

1. **Volume of the Outer Layer (Crust)**:
   Adding a thin layer of thickness $\Delta r$ creates a volume increment $\Delta V = V(r + \Delta r) - V(r)$.
2. **Bounding the Crust Volume**:

- **Inner Bound**: Base area $S(r) \times \text{thickness } \Delta r$
- **Outer Bound**: Base area $S(r + \Delta r) \times \text{thickness } \Delta r$

$$S(r) \cdot \Delta r \le \Delta V \le S(r + \Delta r) \cdot \Delta r$$

3. **Taking the Limit**:
   Dividing by $\Delta r$ and taking $\Delta r \to 0$ yields:

$$S(r) \le \frac{\Delta V}{\Delta r} \le S(r + \Delta r) \implies \frac{dV}{dr} = S(r)$$

> **Key Takeaway**: The surface area of a sphere is the rate of change of its volume with respect to its radius.

---

## 3. Deriving Sphere Volume Using the Disk Method

To calculate $V(r)$ directly, set up the sphere as a **volume of revolution** formed by rotating $x^2 + y^2 = r^2$ around the $x$-axis.

```
                  y ^
                    |     * * *
                    |   *  |  *  <- Vertical Circular Slice
                    |  *   |   *    Radius: y = √(r² - x²)
              ------+------|------+------> x
                   -r      x      +r

```

1. **Cross-Sectional Area**:
   At any point $x \in [-r, r]$, the circular slice has radius $y = \sqrt{r^2 - x^2}$.

$$\text{Area}(x) = \pi y^2 = \pi (r^2 - x^2)$$

2. **Set up the Integral**:
   Sum all thin slices from $x = -r$ to $x = r$:

$$V = \int_{-r}^{r} \pi (r^2 - x^2) \, dx = \pi \int_{-r}^{r} (r^2 - x^2) \, dx$$

3. **Evaluate via Fundamental Theorem of Calculus**:
   Since $r^2$ is constant with respect to $x$:

$$\text{Antiderivative } F(x) = r^2 x - \frac{x^3}{3}$$

$$V = \pi \left[ r^2 x - \frac{x^3}{3} \right]_{-r}^{r}$$

$$V = \pi \left( \left( r^3 - \frac{r^3}{3} \right) - \left( -r^3 - \frac{-r^3}{3} \right) \right) = \pi \left( \frac{2r^3}{3} - \left(-\frac{2r^3}{3}\right) \right) = \frac{4}{3}\pi r^3$$

---

## 4. Finding Surface Area via Differentiation

Using the relationship $\frac{dV}{dr} = S(r)$:

$$S(r) = \frac{d}{dr} \left( \frac{4}{3}\pi r^3 \right) = \frac{4}{3}\pi (3r^2) = 4\pi r^2$$

---

## Geometric Derivative Summary Table

| Shape      | Primary Measure                    | Variable Derivative | Resulting Measure              |
| ---------- | ---------------------------------- | ------------------- | ------------------------------ |
| **Circle** | Area $A(r) = \pi r^2$              | $\frac{dA}{dr}$     | Perimeter $P(r) = 2\pi r$      |
| **Sphere** | Volume $V(r) = \frac{4}{3}\pi r^3$ | $\frac{dV}{dr}$     | Surface Area $S(r) = 4\pi r^2$ |

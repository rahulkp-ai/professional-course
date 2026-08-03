---
title: Pearson Correlation and Correlation Heat Maps in Python
course: Data Analysis with Python
platform: Coursera
module: Exploratory Data Analysis (EDA)
tags:
  - python
  - pandas
  - scipy
  - seaborn
  - exploratory-data-analysis
  - pearson-correlation
  - statistics
  - heatmap
created: 2026-07-05
---

# Pearson Correlation and Correlation Heat Maps in Python

## Overview

After visually inspecting relationships using scatter plots and regression plots, the next step is to **quantitatively measure** the strength of the relationship between variables.

One of the most widely used statistical methods for this purpose is the **Pearson Correlation Coefficient**.

Pearson Correlation provides:

1. **Correlation Coefficient (r)** – Measures the strength and direction of the relationship.
2. **P-value** – Measures the statistical significance (confidence) of the observed correlation.

Together, these values help determine whether two variables are meaningfully related.

---

# What is Pearson Correlation?

**Pearson Correlation** is a statistical method used to measure the **linear relationship** between two continuous numerical variables.

It answers the question:

> **How strongly are two variables linearly related?**

---

# Pearson Correlation Output

The Pearson Correlation test returns **two values**:

1. Correlation Coefficient (**r**)
2. P-value

---

# 1. Correlation Coefficient (r)

The **correlation coefficient**, denoted by **r**, measures both:

- **Direction** of the relationship.
- **Strength** of the relationship.

Its value always lies between:

\[
-1 \le r \le +1
\]

---

## Interpretation of Correlation Coefficient

| Correlation Coefficient (r) | Interpretation                |
| --------------------------: | ----------------------------- |
|                          +1 | Perfect positive correlation  |
|                  0.8 to 1.0 | Strong positive correlation   |
|                  0.5 to 0.8 | Moderate positive correlation |
|                         0.0 | No linear correlation         |
|                -0.5 to -0.8 | Moderate negative correlation |
|                -0.8 to -1.0 | Strong negative correlation   |
|                          -1 | Perfect negative correlation  |

---

## Positive Correlation

As one variable increases:

- The other also increases.

Example:

```text
Engine Size ↑
Price ↑
```

The correlation coefficient is close to **+1**.

---

## Negative Correlation

As one variable increases:

- The other decreases.

Example:

```text
Fuel Efficiency ↑
Price ↓
```

The correlation coefficient is close to **-1**.

---

## No Correlation

No consistent linear relationship exists.

Example:

```text
Peak RPM
      ↕
Price
```

The correlation coefficient is close to **0**.

---

# 2. P-value

The **P-value** measures how confident we are that the observed correlation is statistically significant and not due to random chance.

A **smaller P-value** indicates greater confidence in the calculated correlation.

---

## Interpretation of P-value

| P-value      | Interpretation           |
| ------------ | ------------------------ |
| < 0.001      | Strong certainty         |
| 0.001 – 0.05 | Moderate certainty       |
| 0.05 – 0.10  | Weak certainty           |
| > 0.10       | No statistical certainty |

---

# Strong Correlation

A relationship is considered **strong** when:

- Correlation coefficient is close to **+1** or **-1**
- P-value is **less than 0.001**

Example:

```
r = 0.82
p = 0.000001
```

Interpretation:

- Strong positive relationship.
- Very high statistical confidence.

---

# Example: Horsepower vs Price

The lecture examines the relationship between:

- Horsepower
- Car Price

The computed Pearson Correlation is approximately:

```
r ≈ 0.8
```

Since:

- r is close to **1**
- P-value is much smaller than **0.001**

We conclude:

- Horsepower and price have a **strong positive correlation**.
- We are highly confident that this relationship is statistically significant.

---

# Calculating Pearson Correlation in Python

The **SciPy** library provides the `pearsonr()` function.

---

## Import

```python
from scipy import stats
```

---

## Syntax

```python
stats.pearsonr(x, y)
```

---

## Example

```python
from scipy import stats

r, p = stats.pearsonr(
    df["horsepower"],
    df["price"]
)

print(r)
print(p)
```

Output:

```text
r = 0.80
p = 0.00000001
```

---

# Interpreting Results

Suppose:

```
r = 0.80
p = 0.000001
```

Interpretation:

- Strong positive relationship.
- High statistical significance.
- Horsepower is a good predictor of price.

---

Suppose:

```
r = -0.82
p = 0.0004
```

Interpretation:

- Strong negative relationship.
- High confidence.
- As one variable increases, the other decreases.

---

Suppose:

```
r = 0.06
p = 0.52
```

Interpretation:

- Almost no linear relationship.
- Not statistically significant.

---

# Correlation Matrix

Instead of computing Pearson Correlation for only one pair of variables, we can compute it for **all numerical variables**.

This produces a **Correlation Matrix**.

Example:

|             | Price | Horsepower | Engine Size | Width |
| ----------- | ----: | ---------: | ----------: | ----: |
| Price       |  1.00 |       0.81 |        0.88 |  0.76 |
| Horsepower  |  0.81 |       1.00 |        0.84 |  0.63 |
| Engine Size |  0.88 |       0.84 |        1.00 |  0.71 |
| Width       |  0.76 |       0.63 |        0.71 |  1.00 |

Notice:

- Every variable has a correlation of **1** with itself.

---

# Correlation Heat Map

A **Correlation Heat Map** visualizes the correlation matrix using colors.

Each cell represents the Pearson Correlation coefficient between two variables.

---

## Example

```text
            Price  HP  Engine  Width

Price        ██   ██    ███     ██

HP           ██   ███   ██      ██

Engine       ███  ██    ███     ██

Width        ██   ██    ██      ███
```

Color intensity indicates the strength of the relationship.

---

# Why is the Diagonal Always 1?

Every variable is perfectly correlated with itself.

Therefore:

```
Price vs Price = 1

Horsepower vs Horsepower = 1

Engine Size vs Engine Size = 1
```

This creates a dark diagonal line in the heat map.

---

# Creating a Correlation Matrix in Pandas

```python
corr_matrix = df.corr()
```

---

# Visualizing with Seaborn

```python
import seaborn as sns

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)
```

Where:

- `annot=True` displays correlation values.
- `cmap` specifies the color scheme.

---

# Workflow

```text
Numerical Variables
          │
          ▼
Calculate Pearson Correlation
          │
          ▼
Obtain
r-value
&
P-value
          │
          ▼
Interpret Strength
and Significance
          │
          ▼
Create Correlation Matrix
          │
          ▼
Visualize Using Heat Map
```

---

# Advantages of Pearson Correlation

- Measures the strength of linear relationships.
- Indicates the direction of the relationship.
- Helps identify useful predictor variables.
- Supports feature selection.
- Easy to interpret.
- Widely used in statistics and machine learning.

---

# Limitations

- Detects only **linear relationships**.
- Sensitive to outliers.
- Does not imply causation.
- Requires numerical variables.

---

# Best Practices

- Use Pearson Correlation only with continuous numerical variables.
- Always consider both the correlation coefficient and the P-value.
- Remember that a strong correlation does not prove cause-and-effect.
- Visualize the correlation matrix with a heat map for easier interpretation.
- Use correlation analysis before selecting features for machine learning models.

---

# Summary

Pearson Correlation is a statistical technique used to measure the strength and direction of a linear relationship between two numerical variables.

The Pearson test returns:

- **Correlation Coefficient (r)** – Indicates the strength and direction of the relationship.
- **P-value** – Indicates the statistical significance of that relationship.

A **Correlation Matrix** summarizes pairwise correlations among all numerical variables, while a **Heat Map** provides a visual representation of these relationships using color intensity.

These tools are fundamental components of **Exploratory Data Analysis (EDA)** and feature selection.

---

# Interview Questions

## Basic

1. What is Pearson Correlation?
2. What are the two outputs of the Pearson Correlation test?
3. What does the correlation coefficient measure?
4. What does the P-value indicate?

## Intermediate

5. How do you interpret:
   - r = 0.95
   - r = -0.90
   - r = 0
6. Why is a small P-value important?
7. Why is the diagonal of a correlation matrix always equal to 1?
8. Why does correlation not imply causation?

## Python

9. Which SciPy function calculates Pearson Correlation?
10. How do you compute a correlation matrix in Pandas?
11. Which Seaborn function is commonly used to visualize a correlation matrix?
12. Write the Python code to compute Pearson Correlation between two variables.

---

# Key Takeaways

- **Pearson Correlation** measures the **strength** and **direction** of a linear relationship between two continuous numerical variables.
- The **correlation coefficient (r)** ranges from **-1 to +1**.
- The **P-value** measures the statistical significance of the observed correlation.
- A strong relationship typically has **|r| close to 1** and **P-value < 0.001**.
- **Correlation matrices** summarize relationships between all numerical variables.
- **Heat maps** provide an intuitive visualization of correlation strengths.
- Correlation is invaluable for **feature selection**, **EDA**, and understanding relationships in machine learning datasets.

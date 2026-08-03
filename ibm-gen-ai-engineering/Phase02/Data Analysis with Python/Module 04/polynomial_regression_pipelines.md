# Polynomial Regression and Pipelines

> **Polynomial Regression** extends linear regression to model **nonlinear (curvilinear)** relationships by transforming the input features into polynomial terms. **Pipelines** automate preprocessing and model training, making machine learning workflows cleaner, more maintainable, and less error-prone.

---

# Learning Objectives

After studying this note, you should be able to:

- Understand why Polynomial Regression is needed.
- Explain curvilinear relationships.
- Differentiate between linear and polynomial regression.
- Build polynomial regression models in Python.
- Generate polynomial features using Scikit-learn.
- Standardize features before training.
- Understand and implement Machine Learning Pipelines.

---

# Why Polynomial Regression?

Linear Regression assumes a **straight-line relationship** between the independent variable \(X\) and dependent variable \(Y\).

Example:

```
Y
↑
|
|      *
|    *
|  *
|*
+----------------------→ X
```

However, many real-world datasets do **not** follow a straight line.

Example:

- House Price vs Age
- Salary vs Experience
- Fuel Consumption vs Engine Size
- Temperature vs Electricity Usage

These relationships are often **curved**.

---

# Curvilinear Relationship

A **curvilinear relationship** occurs when the relationship between variables follows a **curve instead of a straight line**.

Example

```
Y
↑
|
|           *
|        *
|     *
|   *
| *
+----------------------→ X
```

A linear model cannot accurately capture this pattern.

Polynomial Regression solves this problem by transforming the input feature.

---

# What is Polynomial Regression?

Polynomial Regression transforms the original feature into higher-degree polynomial terms and then applies **Linear Regression** on the transformed features.

Instead of fitting

\[
Y = b_0 + b_1X
\]

it fits

\[
Y=b_0+b_1X+b_2X^2+b_3X^3+\cdots+b_nX^n
\]

Although the graph becomes nonlinear, the model remains **linear with respect to the coefficients**.

---

# General Polynomial Equation

\[
Y=b_0+b_1X+b_2X^2+b_3X^3+\cdots+b_nX^n
\]

Where

- \(b_0\) = Intercept
- \(b_1,b_2,\ldots,b_n\) = Model coefficients
- \(n\) = Degree of the polynomial

---

# Polynomial Degrees

## First Degree (Linear)

Equation

\[
Y=b_0+b_1X
\]

Graph

```
/
```

---

## Second Degree (Quadratic)

Equation

\[
Y=b_0+b_1X+b_2X^2
\]

Graph

```
   ∩
```

or

```
   ∪
```

Useful for simple curved relationships.

---

## Third Degree (Cubic)

Equation

\[
Y=b_0+b_1X+b_2X^2+b_3X^3
\]

Graph

```
S-shaped curve
```

Can model more complex relationships.

---

## Higher Degree

Examples

- Degree 4
- Degree 5
- Degree 6

Higher degrees provide greater flexibility but increase the risk of **overfitting**.

---

# Effect of Polynomial Degree

| Degree | Model Complexity | Typical Shape  |
| ------ | ---------------- | -------------- |
| 1      | Low              | Straight Line  |
| 2      | Moderate         | Parabola       |
| 3      | High             | S-Curve        |
| 4+     | Very High        | Complex Curves |

Increasing the degree increases flexibility but may reduce generalization.

---

# Polynomial Regression Example

Suppose the fitted model is

\[
Y=-1.557X^3+204.8X^2+8965X+1.37\times10^5
\]

Interpretation:

- Cubic term models complex curvature.
- Quadratic term adjusts the bend.
- Linear term captures the overall trend.
- Constant term shifts the curve vertically.

---

# Polynomial Regression in NumPy

NumPy provides the `polyfit()` function for **single-variable polynomial regression**.

```python
import numpy as np

model = np.polyfit(x, y, 3)
print(model)
```

### Parameters

| Parameter | Description          |
| --------- | -------------------- |
| `x`       | Independent variable |
| `y`       | Target variable      |
| `3`       | Degree of polynomial |

---

# Polynomial Function

Convert coefficients into a callable function.

```python
poly = np.poly1d(model)

predictions = poly(x)
```

---

# Limitation of NumPy `polyfit()`

`polyfit()` only supports **one independent variable**.

Example:

```
Price = f(Horsepower)
```

It **cannot** directly model:

```
Price = f(Horsepower, Engine Size)
```

For multiple features, Scikit-learn is required.

---

# Polynomial Features in Scikit-learn

Scikit-learn's `PolynomialFeatures` transforms multiple input features into polynomial features.

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
```

---

## Transform Features

```python
X_poly = poly.fit_transform(X)
```

Original features

| X₁  | X₂  |
| --- | --- |
| 2   | 3   |

After transformation (Degree = 2)

| 1   | X₁  | X₂  | X₁² | X₁X₂ | X₂² |
| --- | --- | --- | --- | ---- | --- |
| 1   | 2   | 3   | 4   | 6    | 9   |

The dataset now includes interaction and squared terms.

---

# Why Transform Features?

Suppose

Original feature

```
Horsepower
```

After polynomial transformation

```
Horsepower
Horsepower²
Horsepower³
```

The model can now capture nonlinear relationships while still using Linear Regression.

---

# Feature Scaling

Polynomial features often have vastly different ranges.

Example

```
Horsepower = 200

Horsepower² = 40,000

Horsepower³ = 8,000,000
```

Without scaling, optimization becomes inefficient.

---

# Standardization

Standardization transforms features to have:

- Mean = 0
- Standard Deviation = 1

Formula

\[
z=\frac{x-\mu}{\sigma}
\]

Where

- \(x\) = Original value
- \(\mu\) = Mean
- \(\sigma\) = Standard deviation

---

# StandardScaler Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

# Benefits of Standardization

- Faster convergence
- Improved numerical stability
- Equal importance for all features
- Better optimization performance

---

# Machine Learning Pipeline

Training a model usually involves multiple sequential steps:

```
Raw Data
      │
      ▼
Feature Scaling
      │
      ▼
Polynomial Features
      │
      ▼
Linear Regression
      │
      ▼
Prediction
```

Writing these steps manually becomes repetitive.

---

# What is a Pipeline?

A **Pipeline** combines multiple preprocessing and modeling steps into a single reusable workflow.

Instead of calling each transformation manually, the pipeline executes them automatically.

---

# Pipeline Workflow

```
Input Data
     │
     ▼
StandardScaler
     │
     ▼
PolynomialFeatures
     │
     ▼
LinearRegression
     │
     ▼
Prediction
```

---

# Creating a Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
```

---

## Build Pipeline

```python
pipe = Pipeline([
    ("scale", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", LinearRegression())
])
```

Each tuple contains:

- Step name
- Model or transformer

---

# Train Pipeline

```python
pipe.fit(X_train, y_train)
```

The pipeline automatically:

1. Scales the features.
2. Generates polynomial features.
3. Fits the Linear Regression model.

---

# Make Predictions

```python
predictions = pipe.predict(X_test)
```

Prediction automatically applies:

- Feature scaling
- Polynomial transformation
- Regression model

No manual preprocessing is required.

---

# Advantages of Pipelines

- Cleaner code
- Fewer preprocessing mistakes
- Easier maintenance
- Reusable workflows
- Better reproducibility
- Simplifies experimentation with different models

---

# Complete Workflow

```
Dataset
   │
   ▼
Split Train/Test
   │
   ▼
StandardScaler
   │
   ▼
PolynomialFeatures
   │
   ▼
LinearRegression
   │
   ▼
Prediction
   │
   ▼
Evaluation
```

---

# Polynomial Regression vs Linear Regression

| Feature               | Linear Regression | Polynomial Regression        |
| --------------------- | ----------------- | ---------------------------- |
| Relationship          | Linear            | Curved                       |
| Equation              | \(Y=b_0+b_1X\)    | \(Y=b_0+b_1X+b_2X^2+\cdots\) |
| Flexibility           | Low               | High                         |
| Captures Nonlinearity | ❌ No             | ✅ Yes                       |
| Risk of Overfitting   | Low               | Higher for large degrees     |

---

# NumPy vs Scikit-learn

| Feature           | NumPy `polyfit()` | Scikit-learn `PolynomialFeatures` |
| ----------------- | ----------------- | --------------------------------- |
| Single Feature    | ✅ Yes            | ✅ Yes                            |
| Multiple Features | ❌ No             | ✅ Yes                            |
| Feature Expansion | Limited           | Automatic                         |
| Pipeline Support  | ❌ No             | ✅ Yes                            |

---

# Best Practices

- Start with **Linear Regression**.
- Use **Polynomial Regression** only when residual plots indicate nonlinearity.
- Begin with **degree 2** or **degree 3**.
- Avoid unnecessarily high polynomial degrees to reduce overfitting.
- Standardize features before polynomial transformation when feature scales differ.
- Use **Pipelines** to automate preprocessing and model training.

---

# Key Takeaways

- 📈 **Polynomial Regression** models nonlinear relationships by adding higher-order terms while remaining linear in its coefficients.
- 📐 A **curvilinear relationship** is one that follows a curve rather than a straight line.
- 🔢 Increasing the polynomial degree increases model flexibility but also the risk of overfitting.
- 🧩 `numpy.polyfit()` is suitable for **single-variable** polynomial regression.
- 🚀 `PolynomialFeatures` in **Scikit-learn** enables polynomial regression for **multiple features**.
- ⚖️ `StandardScaler` standardizes features, improving optimization and numerical stability.
- 🔄 **Pipelines** chain preprocessing and modeling steps into a single, reusable workflow, making machine learning code cleaner and easier to maintain.

```

```

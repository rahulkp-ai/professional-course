# Simple Linear Regression (SLR) & Multiple Linear Regression (MLR)

## Overview

Regression is a supervised machine learning technique used to predict a **continuous numerical value** (e.g., car price).

There are two common types:

- **Simple Linear Regression (SLR)** → Uses **one** predictor (feature).
- **Multiple Linear Regression (MLR)** → Uses **two or more** predictors.

---

# 1. Simple Linear Regression (SLR)

## Definition

Simple Linear Regression models the relationship between:

- **Predictor (Independent Variable)** → \(x\)
- **Target (Dependent Variable)** → \(y\)

The goal is to fit the **best straight line** through the data.

### Mathematical Equation

\[
\hat{y} = b_0 + b_1x
\]

Where:

- \(\hat{y}\) = Predicted value
- \(b_0\) = Intercept
- \(b_1\) = Slope (Coefficient)
- \(x\) = Predictor variable

---

## Understanding the Parameters

### Intercept (\(b_0\))

The value of \(y\) when \(x = 0\).

---

### Slope (\(b_1\))

Indicates how much the prediction changes for every one-unit increase in \(x\).

- Positive slope → Increasing relationship
- Negative slope → Decreasing relationship

---

## Training the Model

Training means finding the values of:

- Intercept (\(b_0\))
- Slope (\(b_1\))

that produce the best-fitting line for the training data.

```
Training Data
      │
      ▼
 Fit Linear Regression
      │
      ▼
Learn b₀ and b₁
      │
      ▼
Prediction Model
```

---

# Example: Predicting Car Price

Suppose:

Feature:

- Highway Miles Per Gallon (Highway MPG)

Target:

- Price

If a car has:

```
Highway MPG = 20
```

The trained model predicts:

```
Predicted Price = $22,000
```

---

# Training Data Representation

Machine learning data is typically stored as:

## X (Features)

Contains predictor variables.

Example:

| Highway MPG |
| ----------- |
| 18          |
| 20          |
| 25          |
| 30          |

---

## y (Target)

Contains values we want to predict.

| Price ($) |
| --------- |
| 26,000    |
| 22,000    |
| 19,000    |
| 16,000    |

Each row in **X** corresponds to the same row in **y**.

---

# Noise in Regression

Real-world data is never perfectly linear.

Many hidden factors affect price, including:

- Brand
- Vehicle Age
- Condition
- Color
- Market Demand

These unknown influences are represented as **noise**.

### Characteristics of Noise

- Usually small positive values
- Usually small negative values
- Large deviations are rare
- Most noise is centered around zero

```
Actual Price
      ▲
      │
      ●
      │
------Regression Line------
      │
      ▼
Predicted Price
```

The vertical distance between the point and the regression line is partly due to noise.

---

# Prediction Process

```
Training Data
      │
      ▼
Fit Model
      │
      ▼
Learn Parameters
      │
      ▼
Regression Equation
      │
      ▼
Predict New Values
```

The predicted value is written as:

\[
\hat{y}
\]

("y hat"), indicating it is an **estimate**, not the actual value.

---

# Prediction Error

Predictions are rarely perfect.

```
Actual Price ≠ Predicted Price
```

Reasons include:

- Noise
- Missing features
- Incorrect assumption of linearity
- Measurement errors

Prediction error is expected in real-world datasets.

---

# Implementing SLR in Python

## Step 1: Import

```python
from sklearn.linear_model import LinearRegression
```

---

## Step 2: Create Model

```python
lm = LinearRegression()
```

---

## Step 3: Train Model

```python
lm.fit(X, y)
```

- **X** → Predictor(s)
- **y** → Target

The model learns:

- Intercept (\(b_0\))
- Slope (\(b_1\))

---

## Step 4: Predict

```python
predictions = lm.predict(X)
```

Returns:

```
NumPy Array
```

The output contains one prediction for every input sample.

---

## Accessing Model Parameters

### Intercept

```python
lm.intercept_
```

---

### Slope (Coefficient)

```python
lm.coef_
```

---

# Example Regression Equation

After training, the model may produce:

\[
\text{Price}
=
38423.31

- 821.73
  \times
  (\text{Highway MPG})
  \]

Interpretation:

- Base price = **$38,423.31**
- Every additional Highway MPG decreases the predicted price by **$821.73**

---

# 2. Multiple Linear Regression (MLR)

## Definition

Multiple Linear Regression predicts one target using **multiple predictor variables**.

Instead of one feature, it uses many.

---

## Mathematical Equation

\[
\hat{y}
=
b_0

- b_1x_1
- b_2x_2
- \cdots
- b_nx_n
  \]

Where:

- \(b_0\) = Intercept
- \(b_1\) = Coefficient of feature \(x_1\)
- \(b_2\) = Coefficient of feature \(x_2\)
- ...
- \(b_n\) = Coefficient of feature \(x_n\)

---

## Example Features

Predict car price using:

- Engine Size
- Horsepower
- Curb Weight
- Highway MPG

The model becomes:

```
Price

=

b₀
+
b₁(Engine Size)
+
b₂(Horsepower)
+
b₃(Curb Weight)
+
b₄(Highway MPG)
```

---

# Visualizing Multiple Linear Regression

With two predictors:

```
X₁ → Horizontal Axis
X₂ → Depth Axis
ŷ  → Vertical Axis
```

Instead of fitting a line, Multiple Linear Regression fits a **plane**.

```
        ŷ
        ▲
       /|
      / |
     /  |
----/---|------ X₁
   /
  /
 X₂
```

With more than two predictors, visualization is no longer practical, but the mathematical concept remains the same.

---

# Implementing MLR in Python

## Select Multiple Features

```python
Z = df[['horsepower',
        'curb-weight',
        'engine-size',
        'highway-mpg']]
```

---

## Train Model

```python
lm.fit(Z, y)
```

---

## Predict

```python
predictions = lm.predict(Z)
```

Input:

- DataFrame or NumPy array
- One column per feature

Output:

- NumPy array
- One prediction per sample

---

## Model Parameters

### Intercept

```python
lm.intercept_
```

---

### Coefficients

```python
lm.coef_
```

Returns one coefficient for each feature.

Example:

```
[
 b₁,
 b₂,
 b₃,
 b₄
]
```

---

# SLR vs MLR

| Feature              | Simple Linear Regression | Multiple Linear Regression                    |
| -------------------- | ------------------------ | --------------------------------------------- |
| Number of Predictors | 1                        | 2 or More                                     |
| Equation             | Straight Line            | Plane / Hyperplane                            |
| Complexity           | Simple                   | Higher                                        |
| Prediction Accuracy  | Lower (usually)          | Better (if relevant features are used)        |
| Example              | Price vs Highway MPG     | Price vs Engine Size, Horsepower, Weight, MPG |

---

# Key Takeaways

- Regression predicts **continuous numerical values**.
- **Simple Linear Regression (SLR)** uses one predictor.
- **Multiple Linear Regression (MLR)** uses multiple predictors.
- The regression equation contains:
  - Intercept (\(b_0\))
  - Coefficients (\(b_1, b_2, ...\))
- Training learns these parameters from data.
- Predictions are estimates (\(\hat{y}\)) and may differ from actual values due to noise.
- In **scikit-learn**, the primary workflow is:
  - `LinearRegression()`
  - `fit()`
  - `predict()`
  - `intercept_`
  - `coef_`

---

# Summary

Linear Regression models the relationship between features and a continuous target variable. **Simple Linear Regression** fits a straight line using one feature, while **Multiple Linear Regression** extends this concept by incorporating several predictors, generally leading to more accurate predictions when the selected features are relevant. Python's **scikit-learn** library provides a straightforward implementation through the `LinearRegression` class, making it easy to train models, inspect learned parameters, and generate predictions.

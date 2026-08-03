# In-Sample Evaluation Metrics for Regression

## Overview

After training a regression model, we need a way to determine **how well it fits the data**. While visualization (scatter plots, regression plots, residual plots) provides a visual understanding, numerical evaluation gives objective measurements.

The two most common evaluation metrics are:

1. **Mean Squared Error (MSE)**
2. **Coefficient of Determination (R² Score)**

---

# 1. Mean Squared Error (MSE)

## Definition

Mean Squared Error (MSE) measures the **average squared difference** between the actual values and the predicted values.

It tells us **how far the predictions are from the actual values**.

> **Lower MSE = Better model**

---

## Formula

\[
MSE=\frac{1}{n}\sum\_{i=1}^{n}(y_i-\hat y_i)^2
\]

Where:

- \(y_i\) = Actual value
- \(\hat y_i\) = Predicted value
- \(n\) = Number of samples

---

## Step-by-Step Example

Suppose:

Actual value:

```
150
```

Predicted value:

```
50
```

### Step 1: Find the error

```
Error = Actual − Predicted
      = 150 − 50
      = 100
```

### Step 2: Square the error

```
100² = 10,000
```

Repeat this process for every data point.

### Step 3: Find the average

```
MSE = Sum of all squared errors / Number of samples
```

---

## Interpretation

| MSE Value | Meaning                                |
| --------- | -------------------------------------- |
| Small     | Predictions are close to actual values |
| Large     | Predictions are far from actual values |

---

## Advantages

- Easy to compute
- Penalizes large errors heavily
- Commonly used in machine learning

---

## Disadvantages

Because errors are squared:

- Large mistakes receive much larger penalties.
- Units become squared (e.g., dollars²).

---

# Computing MSE in Python

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_actual, y_pred)

print(mse)
```

Parameters:

- `y_actual` → Actual target values
- `y_pred` → Predicted target values

---

# 2. Coefficient of Determination (R² Score)

## Definition

R² (R-Squared) measures **how well the regression model explains the variation in the target variable**.

It answers the question:

> **"How much of the variation in the data is explained by the model?"**

It is also called:

- Coefficient of Determination

---

## Idea Behind R²

Imagine two models:

### Model A

Uses only the **average** of all target values.

Prediction:

```
Every prediction = Mean(y)
```

---

### Model B

Uses regression.

Prediction:

```
ŷ = mx + c
```

If Model B performs much better than simply predicting the average, then the R² value will be high.

---

## Formula

\[
R^2 = 1-\frac{MSE*{Regression}}{MSE*{Mean}}
\]

Where:

- Numerator = Error from regression model
- Denominator = Error from predicting the average

---

# Understanding R² Visually

## Good Regression Model

```
Regression Line

Actual points
      •
    •
  •
 •
-------------------------
```

Characteristics:

- Small prediction errors
- Small MSE
- R² close to **1**

---

## Poor Regression Model

```
Average Line

•      •
    •
        •
```

Characteristics:

- Regression performs almost the same as predicting the average
- Large errors
- R² close to **0**

---

# Interpretation of R²

| R² Value | Meaning                               |
| -------- | ------------------------------------- |
| 1.0      | Perfect prediction                    |
| 0.9      | Excellent fit                         |
| 0.8      | Very good fit                         |
| 0.6      | Moderate fit                          |
| 0.5      | Explains about 50% of variation       |
| 0.0      | No better than predicting the average |
| Negative | Worse than predicting the average     |

---

## Example

Suppose:

```
R² = 0.49659
```

Interpretation:

> Approximately **49.659%** of the variation in the target variable (e.g., house price) is explained by the regression model.

The remaining:

```
100 − 49.659
= 50.341%
```

is due to:

- Other variables
- Random noise
- Model limitations

---

# Computing R² in Python

Using Scikit-Learn:

```python
r2 = model.score(X, y)

print(r2)
```

or

```python
from sklearn.metrics import r2_score

score = r2_score(y_actual, y_pred)

print(score)
```

---

# Negative R²

Although R² usually lies between **0 and 1**, it can sometimes become negative.

A negative R² means:

- The regression model performs **worse than simply predicting the average**.
- It may indicate:
  - Overfitting
  - Poor model choice
  - Incorrect features
  - Very noisy data

---

# MSE vs R²

| Feature          | MSE                              | R²                               |
| ---------------- | -------------------------------- | -------------------------------- |
| Full Name        | Mean Squared Error               | Coefficient of Determination     |
| Measures         | Prediction error                 | Goodness of fit                  |
| Ideal Value      | 0                                | 1                                |
| Lower or Higher? | Lower is better                  | Higher is better                 |
| Units            | Squared units                    | Unitless                         |
| Interpretation   | Average squared prediction error | Percentage of variance explained |

---

# Python Example

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Mean Squared Error
mse = mean_squared_error(y, y_pred)

# R² Score
r2 = model.score(X, y)

print("MSE:", mse)
print("R²:", r2)
```

---

# Key Points

- MSE measures the **average squared prediction error**.
- Smaller MSE indicates better model performance.
- R² measures how well the model explains the variation in the data.
- R² ranges from **0 to 1** in most cases.
- R² close to **1** indicates an excellent fit.
- R² close to **0** means the model is no better than predicting the average.
- A negative R² indicates a poor model that performs worse than the baseline average predictor.
- In Scikit-Learn:
  - `mean_squared_error()` computes MSE.
  - `model.score()` or `r2_score()` computes the R² score.

---

# Interview Questions

### 1. What does Mean Squared Error (MSE) measure?

**Answer:**  
MSE measures the average squared difference between actual and predicted values. A smaller MSE indicates a better-fitting regression model.

---

### 2. Why are errors squared in MSE?

**Answer:**  
Squaring ensures that negative and positive errors do not cancel each other out and gives more weight to larger errors.

---

### 3. What does an R² value of 0.85 mean?

**Answer:**  
It means the model explains **85% of the variation** in the target variable.

---

### 4. Which is better: lower MSE or higher MSE?

**Answer:**  
A **lower MSE** is better because it indicates smaller prediction errors.

---

### 5. What does a negative R² indicate?

**Answer:**  
A negative R² means the regression model performs worse than simply predicting the average of the target values.

---

### 6. Which Scikit-Learn functions are used to calculate MSE and R²?

**Answer:**

- `mean_squared_error(y_true, y_pred)` → Computes MSE
- `model.score(X, y)` or `r2_score(y_true, y_pred)` → Computes the R² score

# Model Evaluation Using Visualization

> Visualization is one of the most effective ways to evaluate how well a regression model performs. It helps identify relationships, errors, assumptions, and potential problems in the model.

---

# Learning Objectives

After studying this note, you should be able to:

- Understand Regression Plots
- Interpret Residual Plots
- Understand Distribution Plots
- Evaluate regression model performance visually
- Detect linear and nonlinear relationships

---

# Why Use Visualization for Model Evaluation?

Numerical metrics such as:

- MAE
- MSE
- RMSE
- R² Score

provide quantitative performance.

Visualization provides **qualitative insights** that numbers alone cannot show.

It helps answer questions like:

- Is the relationship linear?
- Are predictions biased?
- Are errors random?
- Does variance change?
- Should another model be used?

---

# 1. Regression Plot

A **Regression Plot** visualizes:

- Relationship between variables
- Direction of relationship
- Strength of correlation
- Regression line (predictions)

---

## Structure

```
                Dependent Variable (Y)

                       ●
                  ●
             ●
        ●
    ●

-------------------------------> Independent Variable (X)
```

Where

- Horizontal axis → Independent Variable (Feature)
- Vertical axis → Dependent Variable (Target)
- Points → Actual observations
- Line → Regression model prediction

---

## What Can We Learn?

Regression plots show:

### Relationship

How one variable changes with another.

Example:

```
Horsepower ↑
Price ↑
```

---

### Correlation Strength

Strong correlation

```
●
 ●
  ●
   ●
    ●
```

Weak correlation

```
●      ●

      ●

  ●

         ●
```

---

### Direction

Positive relationship

```
X ↑
Y ↑
```

Negative relationship

```
X ↑
Y ↓
```

---

# Creating Regression Plot using Seaborn

```python
import seaborn as sns

sns.regplot(
    x="horsepower",
    y="price",
    data=df
)
```

---

## Parameters

| Parameter | Description          |
| --------- | -------------------- |
| x         | Independent variable |
| y         | Dependent variable   |
| data      | DataFrame            |

---

## Output

The plot contains:

- Scatter points (actual data)
- Best-fit regression line

---

# 2. Residual Plot

Residual plots visualize prediction errors.

---

## What is a Residual?

Residual is the difference between:

```
Residual = Actual Value − Predicted Value
```

or sometimes

```
Residual = Predicted − Actual
```

Depending on implementation.

---

## Example

| Actual | Predicted | Residual |
| ------ | --------- | -------- |
| 100    | 95        | 5        |
| 80     | 84        | -4       |
| 60     | 59        | 1        |

---

# Residual Plot Structure

```
Residual

 5 |      ●
 3 |
 1 | ●
 0 |----------------------------
-1 |
-3 |           ●

     ----------------------------> X
```

- X-axis → Feature
- Y-axis → Residual

---

# Ideal Residual Plot

A good regression model produces residuals that are:

- Randomly scattered
- Centered around zero
- Constant variance
- No visible pattern

Example:

```
     ●    ●

 ●

------0------------------------

      ●

   ●       ●
```

Characteristics:

- Mean ≈ 0
- Constant spread
- No trend
- No curve

This suggests that a **linear model is appropriate**.

---

# Bad Residual Plot (Curvature)

Example

```
      ●

   ●

--------------------

        ●

             ●
```

Notice the curved pattern.

This means:

- Errors depend on X
- Residuals are not random
- Linear assumption is violated

This suggests:

> A nonlinear model may fit the data better.

---

# Increasing Variance (Heteroscedasticity)

Example

```
  ●

     ●

         ●

             ●

                   ●
```

Residual spread increases with X.

This indicates:

- Non-constant variance
- Poor model assumptions
- Possible need for data transformation or a different model

---

# Creating Residual Plot in Seaborn

```python
import seaborn as sns

sns.residplot(
    x=df["horsepower"],
    y=df["price"]
)
```

---

## Parameters

| Parameter | Description          |
| --------- | -------------------- |
| x         | Independent variable |
| y         | Target variable      |

---

# Interpreting Residual Plots

| Pattern        | Interpretation                    |
| -------------- | --------------------------------- |
| Random scatter | Good linear model                 |
| Curved pattern | Nonlinear relationship            |
| Funnel shape   | Heteroscedasticity                |
| Clusters       | Missing variables or model issues |
| Large outliers | Possible anomalous data           |

---

# 3. Distribution Plot

Distribution plots compare:

- Actual target values
- Predicted values

Instead of showing individual points, they compare the overall distributions.

---

## Why Use Distribution Plots?

Especially useful for:

- Multiple Linear Regression
- Models with many independent variables
- Comparing prediction quality

---

## Concept

Suppose predicted values are:

```
1
1
2
2
3
3
3
```

Actual values are:

```
2
2
2
2
2
```

Distribution plots compare how these values are spread.

---

# Histogram vs Distribution Plot

Histogram

```
██████
████
██
```

Distribution Plot

```
      /\
     /  \
 ___/    \____
```

Histograms are for discrete bins.

Continuous predictions are converted into smooth probability distributions.

The total area under the curve equals **1**.

---

# Distribution Plot Interpretation

Example

```
Actual Values  → Red

Predicted      → Blue
```

If curves overlap:

✅ Good predictions

If curves differ significantly:

❌ Poor predictions

---

## Example Observation

Predicted prices:

```
40,000–50,000
```

Large deviation from actual values.

Prediction quality is poor.

---

Predicted prices:

```
10,000–20,000
```

Very close to actual values.

Prediction quality is good.

---

# Multiple Linear Regression

Distribution plots become even more valuable when models use multiple features.

Example:

```
Price =
f(
Horsepower,
Engine Size,
Mileage,
Curb Weight,
Length
)
```

Instead of checking one feature at a time, compare:

- Actual price distribution
- Predicted price distribution

Closer overlap indicates better model performance.

---

# Creating Distribution Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(
    y_actual,
    color="red",
    label="Actual Values"
)

sns.kdeplot(
    y_pred,
    color="blue",
    label="Predicted Values"
)

plt.legend()
plt.show()
```

---

# Summary of Visualization Techniques

| Visualization     | Purpose                                   | Good Model Looks Like           |
| ----------------- | ----------------------------------------- | ------------------------------- |
| Regression Plot   | Relationship between X and Y              | Points close to regression line |
| Residual Plot     | Analyze prediction errors                 | Random scatter around zero      |
| Distribution Plot | Compare actual vs predicted distributions | High overlap between curves     |

---

# Comparison

| Regression Plot                     | Residual Plot                 | Distribution Plot            |
| ----------------------------------- | ----------------------------- | ---------------------------- |
| Shows regression line               | Shows prediction errors       | Compares distributions       |
| Best for single-variable regression | Detects assumption violations | Best for multiple regression |
| Evaluates relationship              | Evaluates residual behavior   | Evaluates prediction quality |

---

# Common Problems Detected

| Visualization     | Detects                                    |
| ----------------- | ------------------------------------------ |
| Regression Plot   | Weak/strong relationships                  |
| Residual Plot     | Nonlinearity, heteroscedasticity, outliers |
| Distribution Plot | Prediction bias and distribution mismatch  |

---

# Best Practices

- Use **Regression Plots** to inspect the relationship between variables.
- Always examine a **Residual Plot** after fitting a regression model.
- Residuals should be randomly scattered around zero with constant variance.
- Use **Distribution Plots** to compare actual and predicted values, especially in multiple linear regression.
- Combine visual evaluation with numerical metrics (MAE, RMSE, R²) for a comprehensive assessment.

---

# Key Takeaways

- 📈 **Regression Plot** shows the relationship between features and the target, along with the fitted regression line.
- 📉 **Residual Plot** visualizes prediction errors and helps verify regression assumptions.
- 📊 **Distribution Plot** compares the overall distributions of actual and predicted values.
- ✅ Random residuals around zero indicate that a linear model is appropriate.
- ⚠️ Curvature or increasing variance in residuals suggests the need for a different model or data transformation.
- 🎯 Visualization complements evaluation metrics and provides deeper insight into model performance.

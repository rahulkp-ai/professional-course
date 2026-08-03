---
title: Data Normalization in Python
course: Data Analysis with Python
platform: Coursera
module: Data Preprocessing
tags:
  - python
  - pandas
  - data-analysis
  - data-preprocessing
  - normalization
  - feature-scaling
  - machine-learning
created: 2026-07-05
---

# Data Normalization in Python

## Overview

**Data normalization** is a preprocessing technique used to scale numerical features so that they have comparable ranges.

In real-world datasets, different features often have vastly different scales. These differences can negatively affect statistical analysis and machine learning algorithms.

Normalization transforms the values into a common scale without changing the relationships between the data points.

---

# Why is Normalization Important?

Consider a used-car dataset.

| Feature | Typical Range |
| ------- | ------------: |
| Length  |     150 – 250 |
| Width   |      50 – 100 |
| Height  |      50 – 100 |

Although these features describe the same object (a car), their numerical ranges are very different.

Without normalization:

- Larger-valued features dominate computations.
- Comparisons between features become unfair.
- Some machine learning algorithms produce biased results.

Normalization ensures that every feature contributes more equally to the analysis.

---

# Example: Age vs Income

Suppose a dataset contains two features.

| Feature |            Range |
| ------- | ---------------: |
| Age     |          0 – 100 |
| Income  | 20,000 – 500,000 |

Income values are thousands of times larger than age values.

During algorithms such as **Linear Regression**, the model may assign greater importance to **Income** simply because its values are numerically larger—not because it is actually a better predictor.

This creates an unintended bias.

After normalization, both features are placed on similar scales, allowing the model to evaluate them more fairly.

---

# Benefits of Normalization

- Makes features comparable.
- Prevents large-scale variables from dominating.
- Improves numerical stability.
- Speeds up optimization algorithms.
- Improves the performance of many machine learning models.

---

# Common Normalization Techniques

This module introduces three widely used normalization methods.

1. Simple Feature Scaling
2. Min-Max Normalization
3. Z-Score Standardization

---

# 1. Simple Feature Scaling

## Formula

\[
x*{new}=\frac{x}{x*{max}}
\]

Each value is divided by the maximum value of the feature.

---

## Example

Original values

| Length |
| -----: |
|    150 |
|    180 |
|    200 |
|    250 |

Maximum value

```
250
```

Normalized values

| Length |
| -----: |
|   0.60 |
|   0.72 |
|   0.80 |
|   1.00 |

The resulting values lie between **0 and 1**.

---

## Pandas Implementation

```python
df["length"] = df["length"] / df["length"].max()
```

---

# 2. Min-Max Normalization

## Formula

\[
x*{new}=\frac{x-x*{min}}{x*{max}-x*{min}}
\]

This method:

1. Subtracts the minimum value.
2. Divides by the feature's range.

---

## Example

Original values

| Length |
| -----: |
|    150 |
|    180 |
|    200 |
|    250 |

Minimum = **150**

Maximum = **250**

Range = **100**

Normalized values

| Length |
| -----: |
|   0.00 |
|   0.30 |
|   0.50 |
|   1.00 |

Again, every value falls between **0 and 1**.

---

## Pandas Implementation

```python
df["length"] = (
    df["length"] - df["length"].min()
) / (
    df["length"].max() - df["length"].min()
)
```

---

# 3. Z-Score Standardization

Also called **Standard Score**.

Unlike the previous methods, Z-score does **not** scale values between 0 and 1.

Instead, it centers the data around its mean.

---

## Formula

\[
z=\frac{x-\mu}{\sigma}
\]

Where:

- **x** = Original value
- **μ (mu)** = Mean of the feature
- **σ (sigma)** = Standard deviation

---

## Characteristics

- Mean becomes **0**
- Standard deviation becomes **1**
- Most values lie between **-3 and +3**
- Extreme values may fall outside this range

---

## Example

Suppose

Mean = **180**

Standard Deviation = **20**

For

```
Length = 200
```

The Z-score is

\[
\frac{200-180}{20}=1
\]

This means the value is **one standard deviation above the mean**.

---

## Pandas Implementation

```python
df["length"] = (
    df["length"] - df["length"].mean()
) / df["length"].std()
```

---

# Comparing the Three Methods

| Method                  | Formula               | Output Range    | Best Use                                    |
| ----------------------- | --------------------- | --------------- | ------------------------------------------- |
| Simple Feature Scaling  | \(x/x\_{max}\)        | 0 to 1          | Quick scaling                               |
| Min-Max Normalization   | \((x-min)/(max-min)\) | 0 to 1          | General machine learning preprocessing      |
| Z-Score Standardization | \((x-\mu)/\sigma\)    | Around -3 to +3 | Statistical analysis and many ML algorithms |

---

# Useful Pandas Methods

| Method   | Purpose                        |
| -------- | ------------------------------ |
| `max()`  | Returns the maximum value      |
| `min()`  | Returns the minimum value      |
| `mean()` | Returns the average value      |
| `std()`  | Returns the standard deviation |

---

# Choosing a Normalization Method

### Use Simple Feature Scaling

- When only maximum scaling is required.
- Easy and computationally inexpensive.

---

### Use Min-Max Normalization

- When features should be within **0–1**.
- Commonly used in machine learning.
- Suitable when minimum and maximum values are meaningful.

---

### Use Z-Score Standardization

- When data approximately follows a normal distribution.
- Useful for statistical analysis.
- Preferred by many algorithms that assume centered data.

---

# Workflow

```text
Raw Numerical Features
        │
        ▼
Inspect Feature Ranges
        │
        ▼
Choose Normalization Method
        │
        ├── Simple Feature Scaling
        ├── Min-Max Normalization
        └── Z-Score Standardization
        │
        ▼
Normalized Dataset
        │
        ▼
Statistical Analysis / Machine Learning
```

---

# Best Practices

- Normalize numerical features before training many machine learning models.
- Apply the same normalization method to both training and testing datasets.
- Do not normalize categorical variables.
- Choose the normalization technique based on the requirements of the algorithm.
- Always inspect feature ranges before deciding whether normalization is necessary.

---

# Summary

Normalization transforms numerical features into comparable scales.

The three normalization methods introduced are:

1. **Simple Feature Scaling**
   - Divide by the maximum value.

2. **Min-Max Normalization**
   - Scale values between **0 and 1**.

3. **Z-Score Standardization**
   - Center data around the mean with a standard deviation of one.

Normalization prevents large-valued features from dominating the analysis and improves the performance and stability of many machine learning algorithms.

---

# Interview Questions

## Basic

1. What is data normalization?
2. Why is normalization important?
3. What problems occur if features have different ranges?

## Intermediate

4. Explain Simple Feature Scaling.
5. Explain Min-Max Normalization.
6. Explain Z-Score Standardization.
7. Why can large numerical values bias machine learning algorithms?

## Pandas

8. Which Pandas method returns the maximum value?
9. How do you calculate the mean of a column?
10. How do you calculate the standard deviation of a column?
11. Write the Pandas code for Min-Max normalization.
12. Write the Pandas code for Z-score normalization.

---

# Key Takeaways

- Normalization scales numerical features to comparable ranges.
- It prevents large-valued features from dominating computations.
- **Simple Feature Scaling** divides by the maximum value.
- **Min-Max Normalization** rescales values between **0 and 1**.
- **Z-Score Standardization** centers data around a mean of **0** with a standard deviation of **1**.
- Pandas provides built-in methods such as `max()`, `min()`, `mean()`, and `std()` to perform normalization efficiently.

---
title: Handling Missing Values in Python
course: Data Analysis with Python
platform: Coursera
module: Data Preprocessing
tags:
  - python
  - pandas
  - data-analysis
  - missing-values
  - data-cleaning
  - machine-learning
created: 2026-07-05
---

# Handling Missing Values in Python

## Overview

Missing values are one of the most common problems encountered in real-world datasets. Before performing data analysis or training machine learning models, these missing values must be identified and handled appropriately.

Python's **Pandas** library provides powerful tools for detecting, removing, and replacing missing values.

---

# What are Missing Values?

A **missing value** occurs when no data is stored for a feature (column) of a particular observation (row).

Common representations of missing values include:

- `NaN` (Not a Number)
- `?`
- `N/A`
- `0` (in some datasets)
- Blank or empty cells

### Example

| Car    | Normalized Losses |
| ------ | ----------------: |
| Honda  |              2500 |
| Toyota |               NaN |
| Ford   |              4100 |

In this example, the Toyota entry contains a missing value.

---

# Why are Missing Values a Problem?

Missing values can:

- Reduce the quality of analysis.
- Cause errors in machine learning algorithms.
- Produce misleading statistical results.
- Reduce prediction accuracy.

Therefore, handling missing values is an essential preprocessing step.

---

# Strategies for Handling Missing Values

There is **no single best method**. The appropriate technique depends on the dataset and the problem being solved.

The common strategies are:

1. Obtain the missing value.
2. Remove the missing data.
3. Replace (impute) the missing value.
4. Estimate using domain knowledge.
5. Leave the value as missing.

---

# Strategy 1: Obtain the Original Value

If possible, contact the person or organization that collected the data and retrieve the correct value.

### Advantages

- Most accurate solution.
- No estimation required.

### Disadvantages

- Often impossible.
- Time-consuming.

---

# Strategy 2: Remove Missing Data

Instead of estimating the missing value, remove it from the dataset.

There are two approaches.

## Remove Rows

Delete only the observations containing missing values.

Example:

| Car    | Price |
| ------ | ----: |
| Honda  | 12000 |
| Toyota |   NaN |
| Ford   | 15000 |

After removing the row:

| Car   | Price |
| ----- | ----: |
| Honda | 12000 |
| Ford  | 15000 |

### Best When

- Only a few observations are missing.
- The missing rows represent a very small percentage of the dataset.

---

## Remove Columns

Delete the entire feature (column).

### Best When

- Most values in the column are missing.
- The feature is not important.

### Disadvantage

Important information may be permanently lost.

---

# Strategy 3: Replace Missing Values (Imputation)

Instead of removing data, estimate the missing values.

This keeps all observations in the dataset.

---

## Mean Imputation

For numerical variables, replace missing values with the **mean** of the column.

Example:

Normalized Losses

| Value |
| ----: |
|  3000 |
|  4500 |
|   NaN |
|  6000 |

Mean

```
(3000 + 4500 + 6000) / 3

= 4500
```

After replacement

| Value |
| ----: |
|  3000 |
|  4500 |
|  4500 |
|  6000 |

### Advantages

- Easy to implement.
- No observations are lost.

### Disadvantages

- Reduces data variability.
- Introduces estimated values instead of real observations.

---

## Mode Imputation

Mean cannot be calculated for categorical variables.

Example:

| Fuel Type |
| --------- |
| Gasoline  |
| Diesel    |
| Gasoline  |
| NaN       |

Most common value (Mode)

```
Gasoline
```

Replace missing value with:

```
Gasoline
```

This technique is commonly used for categorical features.

---

## Domain Knowledge Imputation

Sometimes an expert can estimate missing values based on additional information.

Example

Suppose:

- Missing cars are known to be old vehicles.
- Older vehicles generally have higher normalized losses.

Instead of using the overall average, a more accurate estimate may be obtained by considering only older vehicles.

This often produces better results than simple mean replacement.

---

# Strategy 4: Leave Missing Values

Sometimes it is preferable to leave missing values unchanged.

Reasons include:

- The missing value itself may carry useful information.
- Future analysis may use algorithms capable of handling missing values.
- Estimation could introduce bias.

---

# Handling Missing Values in Pandas

Pandas provides built-in functions for managing missing values efficiently.

---

# Removing Missing Values with `dropna()`

The `dropna()` method removes rows or columns containing missing values.

## Remove Rows

```python
df.dropna(axis=0)
```

`axis=0` removes rows containing missing values.

---

## Remove Columns

```python
df.dropna(axis=1)
```

`axis=1` removes columns containing missing values.

---

## Modify the Original DataFrame

```python
df.dropna(axis=0, inplace=True)
```

`inplace=True` updates the original DataFrame directly.

Equivalent without `inplace=True`:

```python
df = df.dropna(axis=0)
```

---

# Example: Removing Cars Without Price

Suppose the dataset contains:

| Car    | Price |
| ------ | ----: |
| Honda  | 12000 |
| Toyota |   NaN |
| Ford   | 17000 |

Since **Price** is the target variable to predict, rows without a price cannot be used.

Remove them using:

```python
df.dropna(subset=["price"], axis=0, inplace=True)
```

---

# Replacing Missing Values with `replace()`

Pandas provides the `replace()` method to substitute missing values.

---

## Step 1: Calculate the Mean

```python
mean = df["normalized-losses"].mean()
```

---

## Step 2: Replace Missing Values

```python
df["normalized-losses"].replace(np.nan, mean)
```

This replaces every `NaN` with the calculated mean.

---

# Other Imputation Techniques

Besides replacing with the overall mean, other approaches include:

- Group mean replacement
- Median replacement
- Mode replacement
- Forward fill
- Backward fill
- Machine learning–based imputation

The choice depends on the dataset and the application.

---

# Important Notes

- Always inspect the dataset before removing data.
- Removing too many observations may reduce model performance.
- Replacing values introduces estimates, not actual observations.
- Read the official Pandas documentation when learning new methods.
- Domain knowledge often improves imputation quality.

---

# Key Pandas Functions

| Function       | Purpose                                |
| -------------- | -------------------------------------- |
| `dropna()`     | Remove missing rows or columns         |
| `replace()`    | Replace specific values                |
| `mean()`       | Calculate average                      |
| `mode()`       | Find the most frequent value           |
| `inplace=True` | Modify the original DataFrame directly |

---

# Comparison of Missing Value Strategies

| Strategy                | Best Used When              | Advantage                   | Disadvantage                      |
| ----------------------- | --------------------------- | --------------------------- | --------------------------------- |
| Retrieve Original Value | Original data is accessible | Most accurate               | Often impossible                  |
| Remove Rows             | Few missing observations    | Simple                      | Data loss                         |
| Remove Columns          | Feature is mostly missing   | Removes problematic feature | Information loss                  |
| Mean Replacement        | Numerical data              | Keeps all observations      | Less accurate                     |
| Mode Replacement        | Categorical data            | Simple                      | May introduce bias                |
| Domain Knowledge        | Expert knowledge available  | More realistic estimates    | Requires expertise                |
| Leave Missing           | Missingness is informative  | Preserves original data     | Some algorithms cannot handle NaN |

---

# Summary

Handling missing values is one of the first and most important preprocessing tasks.

Common approaches include:

1. Retrieve the original value.
2. Remove rows containing missing values.
3. Remove columns with excessive missing data.
4. Replace numerical values using the mean.
5. Replace categorical values using the mode.
6. Estimate values using domain knowledge.
7. Leave missing values unchanged when appropriate.

Pandas simplifies these tasks with methods such as `dropna()` and `replace()`.

---

# Interview Questions

### Basic

1. What is a missing value?
2. Why are missing values problematic?
3. What are the common representations of missing values?

### Intermediate

4. When should rows be removed instead of columns?
5. Why is mean imputation unsuitable for categorical data?
6. What is mode imputation?
7. Explain domain knowledge imputation.

### Pandas

8. What does `dropna()` do?
9. What is the difference between `axis=0` and `axis=1`?
10. What is the purpose of `inplace=True`?
11. How does the `replace()` method work?
12. How would you replace missing values with the mean of a column?

---

# Key Takeaways

- Missing values are common in real-world datasets.
- There is no universally best method for handling them.
- Mean is commonly used for numerical data.
- Mode is commonly used for categorical data.
- Removing data should minimize information loss.
- Domain knowledge can significantly improve imputation.
- Pandas provides efficient methods like `dropna()` and `replace()` to manage missing values.

```

```

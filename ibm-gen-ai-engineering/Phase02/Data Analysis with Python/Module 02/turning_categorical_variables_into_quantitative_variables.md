---
title: Turning Categorical Variables into Quantitative Variables in Python
course: Data Analysis with Python
platform: Coursera
module: Data Preprocessing
tags:
  - python
  - pandas
  - data-analysis
  - data-preprocessing
  - categorical-data
  - one-hot-encoding
  - feature-engineering
  - machine-learning
created: 2026-07-05
---

# Turning Categorical Variables into Quantitative Variables in Python

## Overview

Many real-world datasets contain **categorical variables**, such as names, colors, cities, or fuel types.

While these values are meaningful to humans, **most statistical models and machine learning algorithms require numerical input**. Therefore, categorical data must be converted into numerical form before model training.

One of the most common techniques for this conversion is **One-Hot Encoding**.

---

# What are Categorical Variables?

A **categorical variable** stores values that represent categories rather than numerical quantities.

Examples include:

| Feature      | Values                  |
| ------------ | ----------------------- |
| Fuel Type    | Gas, Diesel             |
| Color        | Red, Blue, Black        |
| Transmission | Manual, Automatic       |
| City         | New York, London, Tokyo |

These values are stored as **strings (objects)** in Pandas.

---

# Why Convert Categorical Variables?

Most machine learning algorithms perform mathematical operations such as:

- Addition
- Multiplication
- Distance calculations
- Gradient optimization

These operations cannot be performed directly on text values.

For example:

```
Gas + Diesel
```

has no mathematical meaning.

Therefore, categorical values must first be converted into numbers.

---

# Example Dataset

Consider the following **Fuel Type** column.

| Car | Fuel Type |
| --- | --------- |
| A   | Gas       |
| B   | Diesel    |
| C   | Gas       |
| D   | Gas       |

This column contains two unique categories:

- Gas
- Diesel

---

# One-Hot Encoding

**One-Hot Encoding** creates a separate binary (0 or 1) column for each unique category.

Instead of one categorical column:

| Fuel Type |
| --------- |
| Gas       |
| Diesel    |

We create two numerical columns.

| Gas | Diesel |
| --: | -----: |
|   1 |      0 |
|   0 |      1 |
|   1 |      0 |
|   1 |      0 |

Each row contains:

- **1** if the category is present.
- **0** otherwise.

---

# Example

### Car B

Original:

| Fuel Type |
| --------- |
| Diesel    |

After encoding:

| Gas | Diesel |
| --: | -----: |
|   0 |      1 |

---

### Car D

Original:

| Fuel Type |
| --------- |
| Gas       |

After encoding:

| Gas | Diesel |
| --: | -----: |
|   1 |      0 |

Only the corresponding category receives a value of **1**.

---

# Why is it Called "One-Hot"?

Each observation has exactly **one active (hot)** category.

Example:

```
Gas      Diesel

1          0

0          1

1          0
```

Only one value is **1**, while all others are **0**.

---

# One-Hot Encoding in Pandas

Pandas provides the `get_dummies()` function to automatically perform One-Hot Encoding.

---

## Syntax

```python
pd.get_dummies(data)
```

---

## Example

Suppose the DataFrame contains:

```python
df["fuel-type"]
```

Perform One-Hot Encoding:

```python
dummy_variable_one = pd.get_dummies(df["fuel-type"])
```

The resulting DataFrame becomes:

| Gas | Diesel |
| --: | -----: |
|   1 |      0 |
|   0 |      1 |
|   1 |      0 |
|   1 |      0 |

Pandas automatically:

- Detects all unique categories.
- Creates new columns.
- Assigns binary values (0 or 1).

No manual coding is required.

---

# Adding Dummy Variables to the Dataset

After creating the dummy variables, they are usually merged with the original DataFrame.

Example:

```python
dummy_variable_one = pd.get_dummies(df["fuel-type"])

df = pd.concat(
    [df, dummy_variable_one],
    axis=1
)
```

Optionally, remove the original categorical column:

```python
df.drop("fuel-type", axis=1, inplace=True)
```

The dataset now contains only numerical features.

---

# Workflow

```text
Categorical Variable
        │
        ▼
Find Unique Categories
        │
        ▼
Create One Column
for Each Category
        │
        ▼
Assign
1 = Category Present
0 = Category Absent
        │
        ▼
Numerical Dataset
Ready for Machine Learning
```

---

# Advantages of One-Hot Encoding

- Converts categorical data into numerical form.
- Required by many machine learning algorithms.
- Prevents assigning artificial numerical order to categories.
- Simple and easy to interpret.
- Automatically handled by Pandas.

---

# Limitations

- Increases the number of columns.
- High-cardinality features (many unique categories) can create a very large dataset.
- May increase memory usage.

---

# Pandas Function

| Function           | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| `pd.get_dummies()` | Converts categorical variables into dummy (binary) variables |

---

# Example

Original dataset:

| Car | Fuel Type |
| --- | --------- |
| A   | Gas       |
| B   | Diesel    |
| C   | Gas       |

After encoding:

| Car | Gas | Diesel |
| --- | --: | -----: |
| A   |   1 |      0 |
| B   |   0 |      1 |
| C   |   1 |      0 |

This transformed dataset is now suitable for statistical analysis and machine learning.

---

# Best Practices

- Apply One-Hot Encoding to **nominal categorical variables** (categories without any natural order).
- Remove the original categorical column after encoding if it is no longer needed.
- Be cautious when encoding features with a large number of unique categories.
- Use Pandas' built-in functions instead of manually creating binary columns.

---

# Summary

Categorical variables contain text values that cannot be directly processed by most machine learning algorithms.

**One-Hot Encoding** converts each category into a separate binary feature, making the dataset fully numerical.

Pandas simplifies this process with the `pd.get_dummies()` function, which automatically detects unique categories and creates the corresponding dummy variables.

---

# Interview Questions

## Basic

1. What is a categorical variable?
2. Why can't machine learning algorithms use string values directly?
3. What is One-Hot Encoding?

## Intermediate

4. Why is One-Hot Encoding preferred over assigning arbitrary numbers to categories?
5. What are dummy variables?
6. What are the limitations of One-Hot Encoding?

## Python

7. What does `pd.get_dummies()` do?
8. How do you convert a categorical column into dummy variables?
9. How do you merge dummy variables with the original DataFrame?
10. Why is the original categorical column often removed after encoding?

---

# Key Takeaways

- Categorical variables store labels rather than numerical values.
- Most statistical and machine learning models require numerical input.
- **One-Hot Encoding** converts each category into a binary (0/1) feature.
- Each observation has exactly one active category represented by **1**.
- `pd.get_dummies()` automatically performs One-Hot Encoding in Pandas.
- One-Hot Encoding is a fundamental feature engineering technique used in data preprocessing for machine learning.

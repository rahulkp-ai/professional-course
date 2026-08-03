---
title: Chi-Square Test for Categorical Variables
course: Data Analysis with Python
platform: Coursera (IBM)
module: Exploratory Data Analysis (EDA)
tags:
  - python
  - scipy
  - pandas
  - statistics
  - chi-square
  - categorical-data
  - hypothesis-testing
  - exploratory-data-analysis
created: 2026-07-05
---

# Chi-Square Test for Categorical Variables

## Overview

The **Chi-Square (χ²) Test** is a statistical hypothesis test used to determine whether there is a significant relationship between **two categorical variables**.

Unlike **Pearson Correlation**, which measures relationships between **continuous numerical variables**, the Chi-Square Test is specifically designed for **categorical (qualitative) data**.

Examples:

- Gender vs Car Purchase
- Fuel Type vs Vehicle Transmission
- Body Style vs Drive Wheels

---

# Why Use the Chi-Square Test?

Suppose we want to answer questions such as:

- Does fuel type depend on transmission type?
- Is body style related to drive-wheel type?
- Is customer gender associated with product preference?

Since these variables are **categorical**, Pearson correlation cannot be used.

Instead, we use the **Chi-Square Test of Independence**.

---

# What is a Categorical Variable?

Categorical variables contain labels or categories rather than numerical measurements.

Examples:

| Variable     | Categories            |
| ------------ | --------------------- |
| Gender       | Male, Female          |
| Fuel Type    | Gas, Diesel           |
| Drive Wheels | FWD, RWD, 4WD         |
| Body Style   | Sedan, Hatchback, SUV |

---

# What Does the Chi-Square Test Measure?

The Chi-Square Test determines whether:

- The variables are **independent**, or
- The variables are **associated**.

It compares:

- **Observed frequencies**
- **Expected frequencies**

If the observed values differ greatly from the expected values, there is evidence of an association.

---

# Hypotheses

## Null Hypothesis (H₀)

The two categorical variables are **independent**.

There is **no relationship** between them.

---

## Alternative Hypothesis (H₁)

The two categorical variables are **associated**.

There **is** a relationship between them.

---

# Observed Frequencies

Observed frequencies are the actual counts collected from the dataset.

Example:

| Fuel Type | Automatic | Manual |
| --------- | --------: | -----: |
| Gas       |       120 |     60 |
| Diesel    |        40 |     80 |

These values come directly from the data.

---

# Expected Frequencies

Expected frequencies are the counts we would expect if the variables were completely independent.

The Chi-Square Test compares these expected values with the observed values.

Large differences indicate a possible relationship.

---

# Chi-Square Statistic

The Chi-Square statistic measures how different the observed frequencies are from the expected frequencies.

Large values indicate stronger evidence against the null hypothesis.

---

# Interpretation Using P-value

After calculating the Chi-Square statistic, a **P-value** is obtained.

---

## Decision Rule

| P-value  | Interpretation                                |
| -------- | --------------------------------------------- |
| P < 0.05 | Reject H₀ (Variables are associated)          |
| P ≥ 0.05 | Fail to reject H₀ (Variables are independent) |

---

# Example

Suppose we test the relationship between:

- Fuel Type
- Drive Wheels

Results:

```
Chi-Square Statistic = 16.72

P-value = 0.002
```

Interpretation:

- P-value < 0.05
- Reject the null hypothesis.
- Fuel Type and Drive Wheels are statistically associated.

---

# Another Example

Results:

```
Chi-Square Statistic = 1.08

P-value = 0.71
```

Interpretation:

- P-value > 0.05
- Fail to reject the null hypothesis.
- No evidence of an association.

---

# Chi-Square Test in Python

SciPy provides the `chi2_contingency()` function.

---

## Import

```python
from scipy.stats import chi2_contingency
```

---

## Step 1: Create a Contingency Table

```python
contingency_table = pd.crosstab(
    df["fuel-type"],
    df["drive-wheels"]
)
```

Example output:

| Fuel Type | FWD | RWD | 4WD |
| --------- | --: | --: | --: |
| Gas       |  80 |  45 |  12 |
| Diesel    |  25 |  38 |  20 |

---

## Step 2: Perform Chi-Square Test

```python
from scipy.stats import chi2_contingency

chi2,
p,
dof,
expected = chi2_contingency(
    contingency_table
)
```

---

# Returned Values

```python
chi2
```

Chi-Square statistic

---

```python
p
```

P-value

---

```python
dof
```

Degrees of freedom

---

```python
expected
```

Expected frequencies

---

# Example Output

```text
Chi-Square Statistic : 18.63

P-value : 0.0014

Degrees of Freedom : 2
```

Interpretation:

- Strong evidence of association.
- Variables are not independent.

---

# Contingency Table

A contingency table summarizes the frequency of observations for two categorical variables.

Example:

|     | Sedan | Hatchback | Wagon |
| --- | ----: | --------: | ----: |
| FWD |    60 |        50 |    10 |
| RWD |    40 |        15 |     8 |
| 4WD |    20 |         8 |    30 |

This table is the input to the Chi-Square Test.

---

# Workflow

```text
Categorical Variables
          │
          ▼
Create Contingency Table
          │
          ▼
Compute Expected Frequencies
          │
          ▼
Calculate χ² Statistic
          │
          ▼
Obtain P-value
          │
          ▼
Interpret Relationship
```

---

# Difference Between Pearson Correlation and Chi-Square

| Pearson Correlation                      | Chi-Square Test                      |
| ---------------------------------------- | ------------------------------------ |
| Numerical variables                      | Categorical variables                |
| Measures strength of linear relationship | Tests association between categories |
| Returns r-value and P-value              | Returns χ² statistic and P-value     |
| Range: -1 to +1                          | χ² ≥ 0                               |

---

# When to Use the Chi-Square Test

Use Chi-Square when:

- Both variables are categorical.
- Data are frequency counts.
- You want to determine whether two variables are associated.

Examples:

- Gender vs Product Choice
- Fuel Type vs Transmission
- Education Level vs Employment Status
- Drive Wheels vs Body Style

---

# Advantages

- Simple to interpret.
- Works well with categorical data.
- Widely used in research.
- Supports feature selection.
- Useful in Exploratory Data Analysis.

---

# Limitations

- Works only with categorical variables.
- Does not indicate the strength or direction of the relationship.
- Does not imply causation.
- Requires sufficiently large expected frequencies.

---

# Best Practices

- Use contingency tables before performing the test.
- Always interpret the P-value.
- Reject the null hypothesis only when P-value < 0.05.
- Remember that statistical significance does not imply practical significance.

---

# Summary

The **Chi-Square Test of Independence** determines whether two categorical variables are associated.

The test compares **observed frequencies** with **expected frequencies** under the assumption of independence.

Python's **SciPy** library provides the `chi2_contingency()` function to perform the test efficiently.

A small P-value indicates that the variables are likely associated, while a large P-value suggests they are independent.

---

# Interview Questions

## Basic

1. What is the Chi-Square Test?
2. When should the Chi-Square Test be used?
3. What type of variables are required?

## Intermediate

4. What is the difference between observed and expected frequencies?
5. Explain the null and alternative hypotheses.
6. How do you interpret the P-value?
7. Why can't Pearson Correlation be used for categorical variables?

## Python

8. Which SciPy function performs the Chi-Square Test?
9. How do you create a contingency table in Pandas?
10. What are the outputs of `chi2_contingency()`?

---

# Key Takeaways

- The **Chi-Square Test** measures the association between two categorical variables.
- It compares **observed** and **expected** frequencies.
- A **P-value < 0.05** generally indicates a statistically significant association.
- `pd.crosstab()` is commonly used to create contingency tables.
- `scipy.stats.chi2_contingency()` performs the Chi-Square Test in Python.
- Chi-Square is one of the most important statistical tests used during **Exploratory Data Analysis (EDA)** and feature selection for categorical data.

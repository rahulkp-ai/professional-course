---
title: Correlation Between Variables in Python
course: Data Analysis with Python
platform: Coursera
module: Exploratory Data Analysis (EDA)
tags:
  - python
  - pandas
  - seaborn
  - exploratory-data-analysis
  - correlation
  - regression
  - scatter-plot
created: 2026-07-05
---

# Correlation Between Variables in Python

## Overview

One of the primary objectives of **Exploratory Data Analysis (EDA)** is to determine whether variables are related to one another.

A common statistical measure used for this purpose is **correlation**.

Correlation measures the **strength** and **direction** of the relationship between two variables. Understanding these relationships helps identify which features are useful predictors for machine learning and statistical modeling.

---

# What is Correlation?

**Correlation** is a statistical metric that measures the degree to which two variables change together.

In simple terms:

> If one variable changes, does another variable also change?

Correlation helps answer questions such as:

- Does engine size affect car price?
- Does fuel efficiency influence vehicle cost?
- Is age related to income?

---

# Real-World Examples

### Example 1: Smoking and Lung Cancer

People who smoke have a higher probability of developing lung cancer.

This indicates a **positive correlation** between smoking and lung cancer risk.

---

### Example 2: Rain and Umbrellas

When rainfall increases:

- More people carry umbrellas.

When there is no rain:

- Few people carry umbrellas.

These variables are strongly correlated.

---

# Correlation Does NOT Mean Causation

One of the most important concepts in statistics is:

> **Correlation does not imply causation.**

Just because two variables are related does **not** mean one causes the other.

### Example

Rain and umbrella usage are correlated.

However:

- Umbrellas do **not** cause rain.
- Rain does **not** occur because people carry umbrellas.

Instead:

- Rain causes people to use umbrellas.

Therefore, a correlation simply indicates an association between variables—not a cause-and-effect relationship.

---

# Types of Correlation

There are three common types of correlation.

1. Positive Correlation
2. Negative Correlation
3. Weak (or No) Correlation

---

# 1. Positive Correlation

A **positive correlation** means:

- As one variable increases, the other also increases.
- As one decreases, the other decreases.

### Example

Engine Size vs Price

| Engine Size |  Price |
| ----------: | -----: |
|       Small |    Low |
|      Medium | Medium |
|       Large |   High |

Larger engines generally have higher prices.

---

## Scatter Plot

```text
Price
 ^
 |
 |                  •
 |              •
 |          •
 |      •
 |  •
 +---------------------------->
      Engine Size
```

The regression line has a **positive slope**.

This indicates a **positive linear relationship**.

---

# Example in Python

```python
import seaborn as sns

sns.regplot(
    x="engine-size",
    y="price",
    data=df
)
```

If the regression line slopes upward, the variables have a positive correlation.

---

# 2. Negative Correlation

A **negative correlation** means:

- As one variable increases, the other decreases.

### Example

Highway Miles per Gallon (Fuel Efficiency) vs Price

| Highway MPG |  Price |
| ----------: | -----: |
|        High |    Low |
|      Medium | Medium |
|         Low |   High |

Cars with better fuel efficiency often have lower prices compared to high-performance vehicles.

---

## Scatter Plot

```text
Price
 ^
 | •
 |    •
 |        •
 |             •
 |                  •
 +---------------------------->
      Highway MPG
```

The regression line slopes downward.

This represents a **negative correlation**.

---

## Important Observation

Even though the relationship is negative, a **steep regression line** still indicates a strong relationship.

Therefore, **Highway MPG** can still be an effective predictor of vehicle price.

---

# Example in Python

```python
sns.regplot(
    x="highway-mpg",
    y="price",
    data=df
)
```

---

# 3. Weak (or No) Correlation

A **weak correlation** means there is little or no consistent relationship between the variables.

Knowing one variable provides little information about the other.

### Example

Peak RPM vs Price

Both low and high RPM values may correspond to:

- Low prices
- Medium prices
- High prices

No clear pattern exists.

---

## Scatter Plot

```text
Price
 ^
 |     •     •
 | •       •
 |      •
 |   •      •
 |       •
 +---------------------------->
         Peak RPM
```

The regression line is nearly horizontal.

This indicates **weak or no linear relationship**.

Peak RPM is therefore **not a good predictor** of vehicle price.

---

# Regression Line

A **Regression Line** (Best-Fit Line) summarizes the overall trend in the data.

It helps determine:

- Direction of the relationship
- Strength of the relationship
- Predictive usefulness of a variable

---

# Interpreting Regression Lines

| Slope             | Interpretation         |
| ----------------- | ---------------------- |
| Positive          | Positive correlation   |
| Negative          | Negative correlation   |
| Nearly Horizontal | Weak or no correlation |

---

# Correlation Strength

| Correlation Type | Relationship                            |
| ---------------- | --------------------------------------- |
| Strong Positive  | Variables increase together             |
| Weak Positive    | Slight upward trend                     |
| No Correlation   | No clear trend                          |
| Weak Negative    | Slight downward trend                   |
| Strong Negative  | One increases while the other decreases |

---

# Why Correlation is Important

Correlation helps data scientists:

- Identify useful predictor variables.
- Remove irrelevant features.
- Understand relationships in data.
- Improve predictive models.
- Support feature selection.

---

# Visualizing Correlation

The lecture uses **Seaborn's `regplot()`**.

A regression plot combines:

- Scatter Plot
- Regression Line
- Confidence Interval (optional)

This provides both the raw observations and the overall linear trend.

---

# Syntax

```python
sns.regplot(
    x="feature",
    y="target",
    data=df
)
```

---

# Workflow

```text
Select Two Numerical Variables
            │
            ▼
Create Scatter Plot
            │
            ▼
Fit Regression Line
            │
            ▼
Observe Line Direction
            │
            ├── Positive Slope
            ├── Negative Slope
            └── Nearly Flat
            │
            ▼
Interpret Correlation
```

---

# Best Practices

- Always visualize relationships using scatter plots before interpreting correlation.
- Remember that correlation only measures association, not causation.
- A strong negative correlation can be just as useful as a strong positive correlation.
- Weakly correlated variables are often poor predictors.
- Use correlation analysis during feature selection before building machine learning models.

---

# Summary

Correlation measures the relationship between two variables.

The lecture discusses three types of relationships:

1. **Positive Correlation**
   - Both variables increase together.
   - Example: Engine Size vs Price.

2. **Negative Correlation**
   - One variable increases while the other decreases.
   - Example: Highway MPG vs Price.

3. **Weak Correlation**
   - No consistent relationship exists.
   - Example: Peak RPM vs Price.

Seaborn's `regplot()` provides an effective way to visualize these relationships using scatter plots with regression lines.

---

# Interview Questions

## Basic

1. What is correlation?
2. What does a positive correlation indicate?
3. What does a negative correlation indicate?
4. What is a weak correlation?

## Intermediate

5. Explain the statement **"Correlation does not imply causation."**
6. Why is correlation useful in Exploratory Data Analysis?
7. Can a strong negative correlation still be useful for prediction? Why?
8. Why is Peak RPM considered a poor predictor of price in the example?

## Python

9. Which Seaborn function is used to visualize correlation?
10. What information does a regression line provide?
11. How do you create a regression plot in Seaborn?

---

# Key Takeaways

- Correlation measures how strongly two variables are related.
- A **positive correlation** means both variables move in the same direction.
- A **negative correlation** means the variables move in opposite directions.
- A **weak correlation** indicates little or no linear relationship.
- **Correlation does not imply causation**—association alone does not prove cause and effect.
- Regression plots (`sns.regplot()`) are commonly used to visualize correlations.
- Correlation analysis is an essential step in Exploratory Data Analysis (EDA) and feature selection for machine learning.

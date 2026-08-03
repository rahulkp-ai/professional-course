---
title: Data Visualization Commands in Python
course: Data Analysis with Python
platform: Coursera (IBM)
module: Exploratory Data Analysis (EDA)
tags:
  - python
  - matplotlib
  - seaborn
  - data-visualization
  - exploratory-data-analysis
  - plotting
created: 2026-07-05
---

# Data Visualization Commands in Python

## Overview

Data visualization is an essential part of **Exploratory Data Analysis (EDA)**. It enables analysts to understand patterns, relationships, trends, distributions, and outliers within data before applying statistical or machine learning models.

Python provides two major visualization libraries:

- **Matplotlib** – The fundamental plotting library for Python.
- **Seaborn** – A high-level visualization library built on top of Matplotlib that produces more attractive and statistically informative plots.

---

# Why Data Visualization?

Visualization helps to:

- Understand data distributions.
- Detect outliers.
- Identify trends.
- Discover relationships between variables.
- Compare categories.
- Validate assumptions before modeling.
- Communicate insights effectively.

---

# Visualization Libraries

## 1. Matplotlib

Matplotlib is the most widely used plotting library in Python.

### Import

```python
from matplotlib import pyplot as plt
```

or

```python
import matplotlib.pyplot as plt
```

---

### Displaying Plots in Jupyter Notebook

```python
%matplotlib inline
```

This magic command displays plots directly inside the notebook.

---

## 2. Seaborn

Seaborn provides attractive statistical graphics and simplifies many visualization tasks.

### Import

```python
import seaborn as sns
```

---

# Matplotlib Plots

---

# 1. Line Plot

## Purpose

A **Line Plot** shows how one variable changes with respect to another.

It is commonly used for:

- Trends over time
- Continuous data
- Time-series analysis

---

## Syntax

```python
plt.plot(x, y)
```

Where:

- `x` → Independent variable
- `y` → Dependent variable

---

## Example

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")
plt.show()
```

---

## Applications

- Stock prices
- Temperature changes
- Sales growth
- Sensor readings

---

# 2. Scatter Plot

## Purpose

A **Scatter Plot** shows the relationship between two numerical variables.

Each point represents one observation.

---

## Syntax

```python
plt.scatter(x, y)
```

---

## Example

```python
plt.scatter(age, income)
```

---

## Applications

- Correlation analysis
- Detecting clusters
- Identifying outliers
- Regression analysis

---

# 3. Histogram

## Purpose

A **Histogram** displays the frequency distribution of numerical data.

Values are grouped into **bins**.

---

## Syntax

```python
plt.hist(x, bins)
```

---

## Example

```python
plt.hist(
    prices,
    bins=10,
    edgecolor="black"
)
```

---

## Interpretation

- X-axis → Data intervals (bins)
- Y-axis → Number of observations

---

## Applications

- Data distribution
- Normality checking
- Frequency analysis

---

# 4. Bar Plot

## Purpose

A **Bar Plot** compares values across categories.

---

## Syntax

```python
plt.bar(x, height)
```

Where:

- `x` → Categories
- `height` → Values

---

## Example

```python
cars = ["Sedan","SUV","Truck"]
sales = [50,80,30]

plt.bar(cars, sales)
```

---

## Applications

- Category comparison
- Sales reports
- Population comparison
- Survey analysis

---

# 5. Pseudo Color Plot (Heat Map)

## Purpose

A **Pseudo Color Plot (`pcolor`)** visualizes matrix data using colors.

Each cell is assigned a color based on its numerical value.

---

## Syntax

```python
plt.pcolor(C)
```

Optional:

```python
plt.pcolor(
    C,
    cmap="RdBu"
)
```

---

## Applications

- Pivot table visualization
- Correlation matrices
- Feature comparison
- Average values across two categorical variables

---

## Example

```python
plt.pcolor(
    pivot_table,
    cmap="RdBu"
)
```

---

# Seaborn Plots

---

# 1. Regression Plot

## Purpose

A **Regression Plot** combines:

- Scatter Plot
- Regression Line
- 95% Confidence Interval

It helps determine whether two variables have a linear relationship.

---

## Syntax

```python
sns.regplot(
    x="feature1",
    y="feature2",
    data=df
)
```

---

## Example

```python
sns.regplot(
    x="engine-size",
    y="price",
    data=df
)
```

---

## Applications

- Correlation analysis
- Linear regression
- Trend identification

---

# 2. Box and Whisker Plot

## Purpose

A **Box Plot** summarizes the distribution of numerical data.

It displays:

- Minimum
- First Quartile (Q1)
- Median
- Third Quartile (Q3)
- Maximum
- Outliers

---

## Components

```text
Minimum
    │
    ├───────┐
            │
         Q1 │
   ┌────────┴────────┐
   │     Median      │
   └────────┬────────┘
         Q3 │
            │
    └───────┤
            │
        Maximum
```

---

## Important Terms

### Quartiles

- Q1 = 25%
- Median = 50%
- Q3 = 75%

---

### Interquartile Range (IQR)

\[
IQR = Q3 - Q1
\]

---

### Outliers

A value is generally considered an outlier if it lies beyond:

\[
1.5 \times IQR
\]

---

## Syntax

```python
sns.boxplot(
    x="category",
    y="value",
    data=df
)
```

---

## Applications

- Detecting outliers
- Comparing distributions
- Understanding spread
- Comparing multiple categories

---

# 3. Residual Plot

## Purpose

Residual plots evaluate the quality of a regression model.

Residual:

\[
Residual = Actual - Predicted
\]

A good regression model produces residuals randomly scattered around zero.

---

## Syntax

```python
sns.residplot(
    x="feature",
    y="target",
    data=df
)
```

or

```python
sns.residplot(
    x=df["feature"],
    y=df["target"]
)
```

---

## Applications

- Regression diagnostics
- Model validation
- Detecting non-linearity
- Checking regression assumptions

---

# 4. KDE Plot (Kernel Density Estimate)

## Purpose

A **KDE Plot** estimates the probability density of continuous data.

Instead of bars, it displays a smooth probability curve.

---

## Syntax

```python
sns.kdeplot(X)
```

---

## Applications

- Distribution analysis
- Comparing datasets
- Probability estimation

---

# 5. Distribution Plot

## Purpose

A Distribution Plot combines:

- Histogram
- KDE Curve

It provides both frequency and density information.

---

## Syntax

```python
sns.distplot(
    X,
    hist=False
)
```

If:

```python
hist=True
```

both histogram and KDE curve are displayed.

> **Note:** `sns.distplot()` has been deprecated in recent Seaborn versions. Modern code should use `sns.histplot()` or `sns.displot()` together with `sns.kdeplot()`.

---

# Comparison of Visualization Techniques

| Plot              | Data Type              | Purpose                           |
| ----------------- | ---------------------- | --------------------------------- |
| Line Plot         | Continuous             | Show trends over time or sequence |
| Scatter Plot      | Numerical vs Numerical | Relationship between variables    |
| Histogram         | Numerical              | Frequency distribution            |
| Bar Plot          | Categorical            | Compare categories                |
| Pseudo Color Plot | Matrix                 | Heat map visualization            |
| Regression Plot   | Numerical              | Relationship + regression line    |
| Box Plot          | Numerical              | Distribution and outliers         |
| Residual Plot     | Numerical              | Regression diagnostics            |
| KDE Plot          | Numerical              | Probability density estimation    |
| Distribution Plot | Numerical              | Histogram + KDE                   |

---

# Choosing the Right Plot

| Goal                                | Recommended Plot    |
| ----------------------------------- | ------------------- |
| Trend over time                     | Line Plot           |
| Relationship between variables      | Scatter Plot        |
| Check data distribution             | Histogram           |
| Compare categories                  | Bar Plot            |
| Visualize grouped averages          | Heat Map (`pcolor`) |
| Study linear relationship           | Regression Plot     |
| Detect outliers                     | Box Plot            |
| Evaluate regression model           | Residual Plot       |
| Estimate probability density        | KDE Plot            |
| Show histogram and density together | Distribution Plot   |

---

# Best Practices

- Choose a plot based on the type of data.
- Label axes clearly.
- Add meaningful titles.
- Use color maps consistently.
- Avoid cluttering visualizations.
- Use Seaborn for statistical graphics and Matplotlib for flexibility.
- Prefer modern Seaborn functions (`histplot`, `displot`) over deprecated `distplot()`.

---

# Summary

Python provides powerful visualization tools through **Matplotlib** and **Seaborn**.

### Matplotlib

- Line Plot
- Scatter Plot
- Histogram
- Bar Plot
- Pseudo Color Plot

### Seaborn

- Regression Plot
- Box Plot
- Residual Plot
- KDE Plot
- Distribution Plot

Selecting the appropriate visualization technique allows analysts to better understand data distributions, relationships, trends, and anomalies, forming a crucial step in Exploratory Data Analysis (EDA).

---

# Interview Questions

## Basic

1. Why is data visualization important?
2. What is the difference between Matplotlib and Seaborn?
3. What is a histogram?

## Intermediate

4. When should a scatter plot be used?
5. What is a regression plot?
6. Explain the components of a box plot.
7. What is the purpose of a residual plot?
8. What information does a KDE plot provide?

## Python

9. How do you import Matplotlib?
10. How do you import Seaborn?
11. What does `%matplotlib inline` do?
12. Write the syntax for creating:
    - Line Plot
    - Scatter Plot
    - Histogram
    - Bar Plot
    - Regression Plot
    - Box Plot

---

# Key Takeaways

- **Matplotlib** is the foundational plotting library for Python.
- **Seaborn** builds upon Matplotlib to create more informative statistical visualizations.
- Different plot types serve different analytical purposes.
- Histograms and KDE plots help analyze distributions.
- Scatter and regression plots reveal relationships between variables.
- Box plots identify spread and outliers.
- Residual plots evaluate regression models.
- Heat maps (`pcolor`) visualize matrix or pivot table data effectively.
- Effective visualization is a cornerstone of Exploratory Data Analysis (EDA).

---

# References

- [Creating Different Types of Plots in Python](https://www.coursera.org/learn/data-analysis-with-python/supplement/IG1nj/creating-different-types-of-plots-in-python)

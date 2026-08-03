---
title: Data Binning in Python
course: Data Analysis with Python
platform: Coursera
module: Data Preprocessing
tags:
  - python
  - pandas
  - numpy
  - data-analysis
  - data-preprocessing
  - data-binning
  - histogram
  - feature-engineering
created: 2026-07-05
---

# Data Binning in Python

## Overview

**Data binning** (also called **bucketing**) is a preprocessing technique that groups continuous numerical values into a smaller number of intervals called **bins**.

Instead of working with every unique numerical value, similar values are grouped together into categories.

Binning can:

- Simplify data analysis.
- Improve data visualization.
- Reduce the effect of small fluctuations.
- Sometimes improve the performance of predictive models.

---

# What is Data Binning?

Data binning converts continuous numerical data into discrete categories.

### Example

Instead of storing every age separately:

| Original Age |
| -----------: |
|            2 |
|            4 |
|            7 |
|           12 |
|           15 |

We can group them into ranges:

| Age | Bin   |
| --: | ----- |
|   2 | 0–5   |
|   4 | 0–5   |
|   7 | 6–10  |
|  12 | 11–15 |
|  15 | 11–15 |

This makes the data easier to understand and analyze.

---

# Why Use Data Binning?

Binning provides several advantages.

- Reduces the number of unique values.
- Simplifies complex datasets.
- Makes patterns easier to identify.
- Improves visualization.
- Helps compare groups instead of individual values.
- May improve the accuracy of some predictive models.

---

# Example: Car Price Dataset

Suppose a used-car dataset contains the following prices.

| Car Price (₹) |
| ------------: |
|         5,188 |
|         8,500 |
|        12,000 |
|        20,500 |
|        35,000 |
|        45,400 |

Instead of analyzing hundreds of different prices, we group them into categories.

| Price Range | Category        |
| ----------- | --------------- |
| Low         | Affordable cars |
| Medium      | Mid-range cars  |
| High        | Premium cars    |

This makes the dataset much easier to interpret.

---

# Real Dataset Example

In the used-car dataset:

- Price ranges from **5,188** to **45,400**.
- There are **201 unique price values**.

Rather than working with all 201 unique values, we can group them into three categories:

- Low Price
- Medium Price
- High Price

---

# Equal Width Binning

The lecture uses **Equal Width Binning**.

The entire range is divided into intervals of equal size.

Suppose the range is:

```
5,188 ─────────────────────────── 45,400
```

Divide it into three equal-width bins.

```
Low          Medium          High
│────────────│──────────────│────────────│
```

To create **3 bins**, we need **4 boundary values**.

---

# Creating Bin Boundaries with NumPy

NumPy provides the `linspace()` function.

It generates evenly spaced numbers over a specified interval.

### Syntax

```python
np.linspace(start, stop, number_of_points)
```

---

## Example

```python
import numpy as np

bins = np.linspace(
    df["price"].min(),
    df["price"].max(),
    4
)
```

Explanation:

- Start = Minimum price
- Stop = Maximum price
- 4 points create 3 equal-width bins

Example output:

```text
[5188, 18659, 32129, 45400]
```

These values become the bin boundaries.

---

# Naming the Bins

Create labels for each category.

```python
group_names = [
    "Low",
    "Medium",
    "High"
]
```

These labels make the categories easy to understand.

---

# Creating Bins with `pd.cut()`

Pandas provides the `cut()` function to place each value into the correct bin.

### Syntax

```python
pd.cut(
    data,
    bins,
    labels=group_names
)
```

---

## Example

```python
df["price-binned"] = pd.cut(
    df["price"],
    bins,
    labels=group_names,
    include_lowest=True
)
```

### Result

| Price | Category |
| ----: | -------- |
|  6000 | Low      |
| 15000 | Low      |
| 22000 | Medium   |
| 33000 | High     |

A new categorical column is created.

---

# Visualizing Binned Data

After binning, the distribution can be visualized using a **histogram**.

A histogram displays:

- Number of observations
- Frequency of each bin
- Overall data distribution

Example:

```text
Frequency

█████████████████  Low

████████           Medium

██                 High
```

From the histogram, we can quickly observe:

- Most cars belong to the **Low Price** category.
- Fewer cars belong to the **Medium Price** category.
- Very few cars belong to the **High Price** category.

---

# Workflow

```text
Continuous Numerical Data
            │
            ▼
Find Minimum & Maximum
            │
            ▼
Generate Bin Boundaries
(using NumPy linspace)
            │
            ▼
Assign Labels
            │
            ▼
Create Bins
(using Pandas cut)
            │
            ▼
Visualize with Histogram
            │
            ▼
Analyze Distribution
```

---

# Key Functions

## NumPy

| Function     | Purpose                              |
| ------------ | ------------------------------------ |
| `linspace()` | Creates evenly spaced bin boundaries |

---

## Pandas

| Function | Purpose                |
| -------- | ---------------------- |
| `cut()`  | Assigns values to bins |

---

# Equal Width Binning Example

Suppose prices range from **10,000** to **40,000**.

Three equal-width bins:

| Price Range   | Category |
| ------------- | -------- |
| 10,000–20,000 | Low      |
| 20,000–30,000 | Medium   |
| 30,000–40,000 | High     |

Price examples:

|  Price | Bin    |
| -----: | ------ |
| 12,000 | Low    |
| 19,500 | Low    |
| 24,000 | Medium |
| 28,000 | Medium |
| 36,000 | High   |

---

# Advantages

- Simplifies numerical data.
- Makes visualization easier.
- Helps identify data distribution.
- Useful for feature engineering.
- Can improve some predictive models.
- Easier for humans to interpret.

---

# Limitations

- Some information is lost because exact values are replaced by categories.
- Different bin sizes may produce different analytical results.
- Choosing the number of bins requires careful consideration.

---

# Best Practices

- Use binning only when grouping improves interpretation.
- Choose an appropriate number of bins.
- Label bins with meaningful names.
- Visualize the results using histograms.
- Preserve the original numerical feature if precise values may be needed later.

---

# Summary

Data binning groups continuous numerical values into discrete categories.

In this lecture:

- Car prices were grouped into **Low**, **Medium**, and **High** categories.
- NumPy's `linspace()` created equal-width bin boundaries.
- Pandas' `cut()` assigned values to the appropriate bins.
- Histograms were used to visualize the resulting distribution.

Binning simplifies data exploration and is a useful preprocessing and feature engineering technique.

---

# Interview Questions

## Basic

1. What is data binning?
2. Why is data binning used?
3. What is a bin?

## Intermediate

4. What is Equal Width Binning?
5. Why are four boundary values required to create three bins?
6. What information is lost during binning?
7. How can binning improve predictive models?

## Python

8. What does `np.linspace()` do?
9. What is the purpose of `pd.cut()`?
10. How do you assign labels to bins?
11. How can you visualize binned data?

---

# Key Takeaways

- Data binning converts continuous numerical values into categories.
- It simplifies analysis and improves interpretability.
- Equal Width Binning divides the data range into intervals of equal size.
- `numpy.linspace()` generates evenly spaced bin boundaries.
- `pandas.cut()` assigns observations to bins.
- Histograms are commonly used to visualize the distribution of binned data.
- Binning is an important preprocessing and feature engineering technique in data analysis and machine learning.

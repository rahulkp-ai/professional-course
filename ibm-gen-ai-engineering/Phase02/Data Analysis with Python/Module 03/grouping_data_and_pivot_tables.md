---
title: Grouping Data and Pivot Tables in Python
course: Data Analysis with Python
platform: Coursera
module: Exploratory Data Analysis (EDA)
tags:
  - python
  - pandas
  - data-analysis
  - exploratory-data-analysis
  - groupby
  - pivot-table
  - heatmap
  - visualization
created: 2026-07-05
---

# Grouping Data and Pivot Tables in Python

## Overview

When analyzing a dataset, it is often useful to **group observations into categories** and calculate summary statistics such as the mean, count, or sum.

Grouping helps answer questions like:

- Which category has the highest average value?
- How do different groups compare?
- Is there a relationship between categorical variables and a target variable?

Pandas provides the powerful **`groupby()`** method for this purpose.

---

# Why Group Data?

Suppose we have a used-car dataset and want to answer the question:

> **Does the type of drive system affect the price of a vehicle?**

The dataset contains three drive wheel types:

- Front-Wheel Drive (FWD)
- Rear-Wheel Drive (RWD)
- Four-Wheel Drive (4WD)

Instead of examining hundreds of individual records, we can group cars by their drive system and calculate the **average price** for each category.

---

# What is Grouping?

**Grouping** divides a dataset into subsets based on one or more categorical variables.

Each group can then be analyzed independently.

Example:

| Car | Drive Wheels |  Price |
| --- | ------------ | -----: |
| A   | FWD          | 12,000 |
| B   | RWD          | 22,000 |
| C   | FWD          | 15,000 |
| D   | 4WD          | 18,000 |

After grouping by **Drive Wheels**:

| Drive Wheels | Average Price |
| ------------ | ------------: |
| FWD          |        13,500 |
| RWD          |        22,000 |
| 4WD          |        18,000 |

Grouping summarizes large datasets into meaningful statistics.

---

# The `groupby()` Method

Pandas provides the **`groupby()`** method to group data by one or more categorical variables.

### Syntax

```python
df.groupby("column")
```

---

# Grouping by One Variable

Example:

```python
df.groupby("drive-wheels")
```

This creates groups for:

- FWD
- RWD
- 4WD

You can then compute statistics such as:

- Mean
- Count
- Maximum
- Minimum
- Sum

---

# Grouping by Multiple Variables

Pandas also allows grouping using multiple columns.

Example:

```python
df.groupby(
    ["drive-wheels", "body-style"]
)
```

This creates groups such as:

- FWD Sedan
- FWD Hatchback
- RWD Convertible
- RWD Hardtop
- 4WD Wagon

Each combination becomes its own group.

---

# Example: Average Vehicle Price

Suppose we want to analyze:

- Drive Wheels
- Body Style
- Price

First, select only the required columns.

```python
df_group = df[
    ["drive-wheels",
     "body-style",
     "price"]
]
```

Next, group the data.

```python
grouped = df_group.groupby(
    ["drive-wheels", "body-style"]
).mean()
```

The resulting table contains the **average price** for every combination of drive system and body style.

---

# Example Output

| Drive Wheels | Body Style  | Average Price |
| ------------ | ----------- | ------------: |
| FWD          | Sedan       |        13,000 |
| FWD          | Hatchback   |        11,000 |
| RWD          | Convertible |        34,000 |
| RWD          | Hardtop     |        36,000 |
| 4WD          | Hatchback   |        10,500 |

From this analysis:

- **Rear-wheel drive convertibles and hardtops** have the highest average prices.
- **Four-wheel drive hatchbacks** have the lowest average prices.

---

# Why Use a Pivot Table?

The grouped table is informative but difficult to read and visualize because multiple grouping variables are stored in the index.

A **Pivot Table** reorganizes the grouped data into a matrix.

This makes comparisons much easier.

---

# What is a Pivot Table?

A pivot table displays:

- One variable along the **rows**
- Another variable along the **columns**
- Summary values inside the table

Example:

| Drive Wheels | Convertible | Hardtop | Hatchback |  Sedan |
| ------------ | ----------: | ------: | --------: | -----: |
| FWD          |           — |       — |    11,000 | 13,000 |
| RWD          |      34,000 |  36,000 |    17,000 | 24,000 |
| 4WD          |           — |       — |    10,500 | 18,000 |

This layout is much easier to interpret than the grouped table.

---

# Creating a Pivot Table

Pandas provides the `pivot()` (or `pivot_table()`) method.

Example:

```python
pivot_table = grouped.pivot(
    index="drive-wheels",
    columns="body-style"
)
```

Result:

- Rows → Drive Wheels
- Columns → Body Style
- Values → Average Price

---

# Why Pivot Tables Are Useful

Pivot tables:

- Improve readability.
- Organize summary statistics.
- Simplify comparisons.
- Prepare data for visualization.
- Work similarly to Pivot Tables in Microsoft Excel.

---

# Visualizing a Pivot Table with a Heat Map

Instead of reading numbers directly, we can represent the pivot table graphically using a **Heat Map**.

A heat map uses **color intensity** to represent numerical values.

Higher values are shown with stronger colors, while lower values are shown with lighter colors.

---

# Example Heat Map

```text
                 Body Style

           Sedan  Hatch  Hardtop  Convertible

FWD          ▓▓      ▓       ░         ░

RWD         ███     ██      ███       ████

4WD         ██      ░        ░         ░
```

The darker the color, the higher the average vehicle price.

From the heat map we can immediately observe:

- Rear-wheel drive vehicles generally have higher prices.
- Four-wheel drive hatchbacks tend to have lower prices.

---

# Creating a Heat Map

The lecture uses **Matplotlib's** `pcolor()` function.

Example:

```python
plt.pcolor(
    pivot_table,
    cmap="RdBu"
)
```

Where:

- `pivot_table` contains the summarized data.
- `RdBu` specifies the **Red–Blue** color scheme.

The resulting graph includes:

- X-axis → Body Style
- Y-axis → Drive Wheels
- Color → Average Price

---

# Workflow

```text
Raw Dataset
      │
      ▼
Select Relevant Columns
      │
      ▼
Group Data
(groupby)
      │
      ▼
Calculate Summary Statistics
(mean)
      │
      ▼
Create Pivot Table
      │
      ▼
Generate Heat Map
      │
      ▼
Identify Patterns
```

---

# Key Pandas Functions

| Function        | Purpose                                                         |
| --------------- | --------------------------------------------------------------- |
| `groupby()`     | Groups data by one or more categorical variables                |
| `mean()`        | Calculates the average of each group                            |
| `pivot()`       | Converts grouped data into a matrix layout                      |
| `pivot_table()` | Creates a summarized pivot table (more flexible than `pivot()`) |

---

# Matplotlib Function

| Function       | Purpose                                |
| -------------- | -------------------------------------- |
| `plt.pcolor()` | Creates a heat map from numerical data |

---

# Advantages

- Simplifies large datasets.
- Makes category comparisons easy.
- Reveals hidden relationships.
- Improves visualization.
- Useful for Exploratory Data Analysis (EDA).
- Helps identify trends before building machine learning models.

---

# Best Practices

- Use `groupby()` for categorical variables.
- Compute summary statistics such as mean, count, or sum.
- Convert grouped data into a pivot table for better readability.
- Use heat maps to visualize relationships between variables.
- Interpret both numerical values and visual patterns together.

---

# Summary

Grouping organizes data into meaningful categories for analysis.

In this lecture:

- **`groupby()`** grouped vehicles by **Drive Wheels** and **Body Style**.
- **`mean()`** calculated the average vehicle price for each group.
- **Pivot tables** reorganized the grouped data into a readable matrix.
- **Heat maps** visualized the average prices using color intensity.

These techniques are fundamental tools in **Exploratory Data Analysis (EDA)** and help uncover relationships between categorical variables and target variables.

---

# Interview Questions

## Basic

1. What is data grouping?
2. Why is grouping useful in data analysis?
3. What does the `groupby()` method do?

## Intermediate

4. What is the difference between grouping by one variable and multiple variables?
5. Why are pivot tables easier to interpret than grouped tables?
6. What information does a heat map convey?
7. Why are summary statistics calculated after grouping?

## Python

8. How do you group a DataFrame by a categorical variable?
9. How do you calculate the average value for each group?
10. How do you create a pivot table in Pandas?
11. Which Matplotlib function can be used to create a heat map?

---

# Key Takeaways

- **Grouping** divides data into subsets based on categorical variables.
- `groupby()` is the primary Pandas method for grouping data.
- Summary statistics such as **mean** help compare different groups.
- **Pivot tables** reorganize grouped data into a matrix for easier interpretation.
- **Heat maps** visualize numerical values using color intensity, making patterns and relationships easier to identify.
- Grouping, pivot tables, and heat maps are essential techniques in **Exploratory Data Analysis (EDA)**.

# Descriptive Statistics

## Introduction

Before building complex machine learning models, explore and understand
your dataset using **descriptive statistics**.

**Purpose** - Summarize the dataset. - Understand data distribution. -
Identify patterns, outliers, and relationships.

## 1. Descriptive Statistics using `describe()`

In **Pandas**, the `describe()` function automatically computes
statistics for numerical columns.

It includes: - Count (number of observations) - Mean - Standard
Deviation - Minimum value - 25th Percentile (Q1) - 50th Percentile
(Median) - 75th Percentile (Q3) - Maximum value

**Note:** Missing (`NaN`) values are ignored automatically.

---

## 2. Categorical Data

Categorical variables contain discrete groups.

**Example** - Drive-wheel - Front-wheel drive (FWD) - Rear-wheel drive
(RWD) - Four-wheel drive (4WD)

### `value_counts()`

Use `value_counts()` to count the frequency of each category.

Example results: - FWD: 118 cars - RWD: 75 cars - 4WD: 8 cars

---

## 3. Box Plot

A **Box Plot** visualizes the distribution of numerical data.

### Components

- **Median (Q2):** Middle value.
- **Lower Quartile (Q1):** 25th percentile.
- **Upper Quartile (Q3):** 75th percentile.
- **Interquartile Range (IQR):** Q3 − Q1.
- **Whiskers:** Extend up to **1.5 × IQR** above Q3 and below Q1.
- **Outliers:** Values outside the whiskers.

### Advantages

- Detects outliers.
- Shows skewness.
- Compares distributions across groups.

**Example:** Comparing car prices across drive-wheel categories shows
RWD prices differ noticeably, while FWD and 4WD appear similar.

---

## 4. Continuous Variables

Continuous variables can take any value within a range.

**Examples** - Price - Engine Size

---

## 5. Scatter Plot

A **Scatter Plot** shows the relationship between two continuous
variables.

### Variables

- **Predictor (Independent Variable):** Engine Size (X-axis)
- **Target (Dependent Variable):** Price (Y-axis)

Always include: - Axis labels - Plot title

### Interpretation

The scatter plot indicates a **positive linear relationship**: - As
**engine size increases**, **car price tends to increase**.

---

## Key Takeaways

- Use `describe()` for numerical summaries.
- Use `value_counts()` for categorical summaries.
- Use box plots to visualize distributions and detect outliers.
- Use scatter plots to study relationships between continuous
  variables.
- Engine size appears to be a useful predictor of car price.

## Keywords

EDA, Descriptive Statistics, Pandas, describe(), value_counts(), Box
Plot, Quartiles, IQR, Outliers, Scatter Plot, Predictor Variable, Target
Variable, Positive Linear Relationship

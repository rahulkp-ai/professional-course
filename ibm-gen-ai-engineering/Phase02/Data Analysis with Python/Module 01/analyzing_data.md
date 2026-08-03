# Introduction

Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making.

Python is one of the most popular languages for data analysis because of its powerful libraries:

- NumPy
- Pandas
- Matplotlib
- SciPy
- Scikit-learn

The first step in any data analysis project is understanding and exploring the dataset. :contentReference[oaicite:0]{index=0}

---

# Data Analysis Workflow

A typical data analysis process follows these stages:

```text
Data Collection
       ↓
Data Import
       ↓
Data Cleaning
       ↓
Data Exploration
       ↓
Data Visualization
       ↓
Model Building
       ↓
Decision Making
```

---

# Understanding the Dataset

Before performing analysis, answer the following questions:

### 1. What is the problem?

Example:

- Predict car prices
- Predict house prices
- Recommend products

### 2. What type of data do we have?

Examples:

| Type        | Example              |
| ----------- | -------------------- |
| Numerical   | Age, Salary, Price   |
| Categorical | Gender, Color, Brand |
| Date-Time   | Timestamp            |
| Text        | Reviews, Comments    |

### 3. What are the target variables?

Target Variable:

The variable we want to predict.

Example:

```python
price
```

---

# Loading Data into Python

The most common library used is Pandas.

### Import Pandas

```python
import pandas as pd
```

### Read CSV File

```python
df = pd.read_csv("filename.csv")
```

### Display First Rows

```python
df.head()
```

Output:

```text
Shows first 5 rows
```

### Display Last Rows

```python
df.tail()
```

---

# Understanding the DataFrame

A DataFrame is a two-dimensional table structure.

Example:

| Brand | Price | Mileage |
| ----- | ----- | ------- |
| BMW   | 25000 | 30000   |
| Audi  | 28000 | 25000   |

```python
type(df)
```

Output:

```python
pandas.core.frame.DataFrame
```

---

# Basic Dataset Exploration

## View Dataset Dimensions

```python
df.shape
```

Example Output:

```python
(205, 26)
```

Meaning:

- 205 rows
- 26 columns

---

## View Column Names

```python
df.columns
```

---

## Data Types of Columns

```python
df.dtypes
```

Example:

```text
price          int64
horsepower     float64
make           object
```

---

# Statistical Summary

Use:

```python
df.describe()
```

Provides:

- Count
- Mean
- Standard Deviation
- Minimum
- Maximum
- Quartiles

Example:

```text
count
mean
std
min
25%
50%
75%
max
```

Useful for identifying unusual values.

---

# Viewing Dataset Information

```python
df.info()
```

Provides:

- Number of rows
- Number of columns
- Data types
- Missing values

Example:

```text
205 entries
26 columns
```

---

# Accessing Columns

## Single Column

```python
df["price"]
```

or

```python
df.price
```

---

## Multiple Columns

```python
df[["price","horsepower"]]
```

---

# Accessing Rows

### Using Index

```python
df.iloc[0]
```

First row.

### Multiple Rows

```python
df.iloc[0:5]
```

Rows 0 to 4.

---

# Finding Missing Values

Missing values are common in real-world datasets.

Check:

```python
df.isnull()
```

Count missing values:

```python
df.isnull().sum()
```

Example:

```text
price         0
horsepower    2
stroke        4
```

Missing values must be handled before modeling.

---

# Why Data Exploration Matters

Data exploration helps us:

- Understand the dataset
- Detect missing values
- Detect outliers
- Verify data types
- Identify important variables
- Find patterns

Without exploration, later analysis may produce incorrect results.

---

# Common Pandas Commands

| Command             | Purpose              |
| ------------------- | -------------------- |
| `df.head()`         | First 5 rows         |
| `df.tail()`         | Last 5 rows          |
| `df.shape`          | Rows and columns     |
| `df.columns`        | Column names         |
| `df.dtypes`         | Data types           |
| `df.describe()`     | Statistical summary  |
| `df.info()`         | Dataset information  |
| `df.isnull().sum()` | Missing values count |
| `df["column"]`      | Select column        |
| `df.iloc[]`         | Select rows          |

---

# Example Dataset Exploration

```python
import pandas as pd

df = pd.read_csv("automobile.csv")

print(df.head())

print(df.shape)

print(df.dtypes)

print(df.describe())

print(df.isnull().sum())
```

This simple workflow provides a quick understanding of any dataset before deeper analysis.

---

# Key Takeaways

✅ Data analysis starts with understanding the dataset.

✅ Pandas DataFrames are the primary structure used for analysis.

✅ Always inspect:

- Shape
- Columns
- Data types
- Missing values
- Statistical summaries

✅ Important functions:

- `head()`
- `tail()`
- `shape`
- `describe()`
- `info()`
- `isnull()`

✅ Proper data exploration is the foundation of successful data analysis and machine learning projects. :contentReference[oaicite:1]{index=1}

---

# Exam Quick Revision

```python
import pandas as pd

df = pd.read_csv("data.csv")

df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.describe()
df.info()
df.isnull().sum()

df["column"]
df.iloc[0]
```

Remember:

Data Analysis = Understand Data → Explore Data → Clean Data → Analyze Data → Model Data.

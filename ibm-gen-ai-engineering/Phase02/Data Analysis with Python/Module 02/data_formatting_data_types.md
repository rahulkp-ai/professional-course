---
title: Data Formatting and Data Types in Python
course: Data Analysis with Python
platform: Coursera
module: Data Preprocessing
tags:
  - python
  - pandas
  - data-analysis
  - data-preprocessing
  - data-formatting
  - data-types
  - data-cleaning
created: 2026-07-05
---

# Data Formatting and Data Types in Python

## Overview

Data collected from different sources is rarely stored in a consistent format. Before performing analysis, data should be standardized so that values, units, and data types are consistent throughout the dataset.

Python's **Pandas** library provides several methods to standardize data formats and convert data types.

---

# What is Data Formatting?

**Data formatting** is the process of converting data into a common and consistent format.

The goal is to make data:

- Consistent
- Easy to understand
- Ready for statistical analysis
- Suitable for machine learning

It is an important step in **data cleaning** and **data preprocessing**.

---

# Why is Data Formatting Important?

Data may come from:

- Different organizations
- Different countries
- Different software systems
- Different people

Each source may use different:

- Naming conventions
- Measurement units
- Date formats
- Data types

Without standardization, meaningful analysis becomes difficult.

---

# Example: Different Naming Conventions

The same city may be represented in multiple ways.

| Original Values |
| --------------- |
| New York        |
| NY              |
| N.Y.            |
| Ny              |

Although all refer to the same city, a computer treats them as different values.

After formatting:

| Standard Value |
| -------------- |
| New York       |
| New York       |
| New York       |
| New York       |

This improves consistency throughout the dataset.

---

# When Should Data NOT Be Standardized?

Sometimes inconsistencies are actually useful.

Examples include:

- **Fraud Detection**
  - Unusual spellings may indicate suspicious activity.

- **Behavior Analysis**
  - Different writing styles may reveal user behavior.

In such cases, preserving the original formatting can provide valuable information.

---

# Unit Conversion

Datasets collected in different countries often use different measurement systems.

### Example

A used-car dataset contains fuel efficiency measured as:

```
City Miles per Gallon (MPG)
```

However, many countries use:

```
Liters per 100 Kilometers (L/100 km)
```

To standardize the dataset, convert all values into the desired unit.

---

# MPG to L/100 km Conversion

The conversion formula is:

\[
\text{L/100 km} = \frac{235}{\text{MPG}}
\]

---

## Pandas Implementation

```python
df["city-mpg"] = 235 / df["city-mpg"]
```

Each value in the column is automatically converted.

Example:

| MPG | L/100 km |
| --: | -------: |
|  20 |    11.75 |
|  25 |     9.40 |
|  30 |     7.83 |

---

# Renaming Columns

After converting units, rename the column to reflect the new measurement.

### Before

```
city-mpg
```

### After

```
city-L/100km
```

---

## Pandas Implementation

```python
df.rename(
    columns={"city-mpg": "city-L/100km"},
    inplace=True
)
```

Renaming columns improves readability and avoids confusion.

---

# Data Types

Every column in a Pandas DataFrame has an associated **data type**.

The data type determines:

- How values are stored
- What operations can be performed
- Memory usage
- Computational efficiency

---

# Common Pandas Data Types

| Data Type    | Description     | Example         |
| ------------ | --------------- | --------------- |
| `object`     | Text or strings | `"Toyota"`      |
| `int64`      | Integer numbers | `15000`         |
| `float64`    | Decimal numbers | `15.75`         |
| `bool`       | Boolean values  | `True`, `False` |
| `datetime64` | Dates and times | `2026-07-05`    |

---

# Why Correct Data Types Matter

Sometimes imported datasets assign incorrect data types.

Example:

| Column | Actual Data | Stored As |
| ------ | ----------- | --------- |
| Price  | 12000       | object    |

Although the values are numerical, Pandas treats them as text.

This can cause:

- Incorrect calculations
- Sorting issues
- Machine learning errors
- Valid values being interpreted as missing data

Therefore, verifying data types is an essential preprocessing step.

---

# Checking Data Types

Pandas provides the `dtypes` attribute to inspect the data type of every column.

```python
df.dtypes
```

Example output:

```
price          object
horsepower     int64
city-mpg     float64
fuel-type      object
```

This allows you to identify columns with incorrect types.

---

# Converting Data Types with `astype()`

The `astype()` method converts a column from one data type to another.

### Syntax

```python
df["column"] = df["column"].astype("datatype")
```

---

## Example: Convert Price to Integer

Suppose the `price` column is stored as an object.

Before:

```
price → object
```

Convert it to an integer.

```python
df["price"] = df["price"].astype("int")
```

After:

```
price → int64
```

---

## Other Examples

Convert to float:

```python
df["price"] = df["price"].astype("float")
```

Convert to string:

```python
df["price"] = df["price"].astype("str")
```

Convert to Boolean:

```python
df["is_new"] = df["is_new"].astype("bool")
```

---

# Workflow for Data Formatting

```text
Raw Dataset
      │
      ▼
Inspect Values
      │
      ▼
Standardize Names
      │
      ▼
Convert Units
      │
      ▼
Check Data Types
      │
      ▼
Correct Data Types
      │
      ▼
Clean and Consistent Dataset
```

---

# Key Pandas Functions

| Function              | Purpose                              |
| --------------------- | ------------------------------------ |
| `df.dtypes`           | Display the data type of each column |
| `astype()`            | Convert one data type to another     |
| `rename()`            | Rename columns                       |
| Arithmetic operations | Convert measurement units            |

---

# Best Practices

- Standardize naming conventions before analysis.
- Convert all measurements into the same unit.
- Always inspect data types after importing a dataset.
- Rename columns after unit conversion.
- Convert numerical values stored as text into numeric types.
- Verify conversions before performing statistical analysis or machine learning.

---

# Summary

Data formatting ensures consistency across the dataset by standardizing names, measurement units, and data types.

Pandas makes these tasks straightforward through:

- Arithmetic operations for unit conversion
- `rename()` for changing column names
- `dtypes` for inspecting data types
- `astype()` for converting between data types

Proper data formatting improves data quality and ensures reliable statistical analysis and machine learning.

---

# Interview Questions

## Basic

1. What is data formatting?
2. Why is data formatting important?
3. Give examples of inconsistent data formats.

## Intermediate

4. Why should units be standardized?
5. Why might incorrect data types cause problems?
6. Explain the difference between `object`, `int64`, and `float64`.
7. Why should columns be renamed after unit conversion?

## Pandas

8. How do you check the data type of every column?
9. What does the `astype()` method do?
10. How do you rename a column in Pandas?
11. How would you convert MPG to L/100 km using Pandas?

---

# Key Takeaways

- Data formatting standardizes values for consistency.
- The same information may appear in multiple formats and should often be unified.
- Unit conversion ensures meaningful comparisons across datasets.
- Every column has a data type that determines how it is processed.
- Incorrect data types can lead to inaccurate analysis.
- Use `dtypes` to inspect data types.
- Use `astype()` to convert columns to the correct type.
- Rename columns after transforming their values or units.

```

```

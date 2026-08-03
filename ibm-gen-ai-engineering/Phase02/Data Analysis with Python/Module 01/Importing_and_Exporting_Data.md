# Importing and Exporting Data in Python

## Learning Objectives

After completing this lecture, you should be able to:

- Import datasets from various file formats.
- Export processed data to external files.
- Understand common file formats used in Data Science.
- Use Pandas functions for reading and writing data.

---

# Why Import and Export Data?

Data rarely exists directly inside a Python program.

Data scientists usually:

1. Import data from external sources.
2. Analyze and transform the data.
3. Export the cleaned data for further use.

```text
External File
      ↓
Import into Python
      ↓
Data Analysis
      ↓
Export Results
```

---

# Common Data Formats

## 1. CSV (Comma Separated Values)

Most commonly used format.

Example:

```csv
Name,Age,Salary
John,25,50000
Alice,30,65000
```

Advantages:

- Lightweight
- Easy to read
- Supported everywhere

---

## 2. Excel Files

Extensions:

```text
.xls
.xlsx
```

Widely used in business environments.

---

## 3. JSON Files

JavaScript Object Notation.

Example:

```json
{
  "name": "John",
  "age": 25
}
```

Often used in APIs and web applications.

---

## 4. SQL Databases

Data may be stored in relational databases.

Examples:

- MySQL
- PostgreSQL
- SQLite
- SQL Server

---

# Importing Data with Pandas

Pandas provides powerful functions for reading datasets.

---

## Reading CSV Files

```python
import pandas as pd

df = pd.read_csv("cars.csv")
```

---

### Reading CSV from URL

```python
url = "https://example.com/data.csv"

df = pd.read_csv(url)
```

Useful when datasets are hosted online.

---

# Understanding File Paths

## Relative Path

```python
df = pd.read_csv("data.csv")
```

Python searches in the current working directory.

---

## Absolute Path

Windows:

```python
df = pd.read_csv(
    "C:/Users/User/Documents/data.csv"
)
```

Linux/Mac:

```python
df = pd.read_csv(
    "/Users/user/Documents/data.csv"
)
```

---

# Viewing Imported Data

## Display First Rows

```python
df.head()
```

Default:

```python
df.head(5)
```

---

## Display Last Rows

```python
df.tail()
```

Example:

```python
df.tail(10)
```

---

# Exporting Data

After cleaning or analyzing data, save the results.

---

## Export to CSV

```python
df.to_csv("output.csv")
```

Creates a CSV file.

---

## Remove Index Column

```python
df.to_csv(
    "output.csv",
    index=False
)
```

Recommended for most projects.

---

# Export to Excel

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

---

# Complete Example

## Step 1: Import Dataset

```python
import pandas as pd

df = pd.read_csv("automobile.csv")
```

---

## Step 2: Analyze Data

```python
print(df.head())
```

---

## Step 3: Save Processed Data

```python
df.to_csv(
    "cleaned_automobile.csv",
    index=False
)
```

---

# Typical Data Science Workflow

```text
Raw Dataset
     ↓
Import Data
     ↓
Inspect Data
     ↓
Clean Data
     ↓
Analyze Data
     ↓
Export Results
```

---

# Important Pandas Functions

| Function        | Purpose         |
| --------------- | --------------- |
| pd.read_csv()   | Read CSV file   |
| pd.read_excel() | Read Excel file |
| df.head()       | View first rows |
| df.tail()       | View last rows  |
| df.to_csv()     | Save as CSV     |
| df.to_excel()   | Save as Excel   |

---

# Interview Questions

## Q1. What is the purpose of importing data?

To load external datasets into Python for analysis.

---

## Q2. Which function imports CSV files?

```python
pd.read_csv()
```

---

## Q3. Which function exports a DataFrame to CSV?

```python
df.to_csv()
```

---

## Q4. What does `index=False` do?

Prevents Pandas from saving row index values into the output file.

---

## Q5. What is the difference between absolute and relative paths?

| Relative Path                 | Absolute Path      |
| ----------------------------- | ------------------ |
| Relative to current directory | Full file location |
| Shorter                       | Complete path      |
| More portable                 | Less portable      |

---

# Key Takeaways

- Data is typically imported from external files.
- CSV is the most common format in Data Science.
- Use `pd.read_csv()` to import CSV files.
- Use `df.head()` and `df.tail()` to inspect data.
- Use `df.to_csv()` and `df.to_excel()` to export results.
- Always use `index=False` when exporting clean datasets.
- Understanding file paths is essential for loading datasets correctly.

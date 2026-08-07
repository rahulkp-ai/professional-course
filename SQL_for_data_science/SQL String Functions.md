# SQL String Functions

## Overview

When working with data from multiple sources, strings (text data) often have different formats. SQL provides several **string functions** that help clean, transform, and standardize text before analysis. These functions are especially useful for **data cleaning, preprocessing, and feature engineering**.

---

# Learning Objectives

After studying this topic, you should be able to:

- Concatenate (combine) text strings.
- Remove unwanted spaces using trimming functions.
- Extract part of a string using `SUBSTR()`.
- Convert text to uppercase or lowercase.
- Understand common real-world applications of string manipulation. :contentReference[oaicite:1]{index=1}

---

# Why String Functions Matter

String functions help:

- Clean messy text data.
- Standardize names and categories.
- Create unique identifiers.
- Prepare data before analysis.
- Reduce processing in client applications by handling transformations directly in SQL. :contentReference[oaicite:2]{index=2}

---

# Common SQL String Functions

| Function   | Purpose                      |
| ---------- | ---------------------------- |
| `CONCAT()` | Combine strings              |
| `TRIM()`   | Remove spaces from both ends |
| `LTRIM()`  | Remove spaces from the left  |
| `RTRIM()`  | Remove spaces from the right |
| `SUBSTR()` | Extract part of a string     |
| `UPPER()`  | Convert to uppercase         |
| `LOWER()`  | Convert to lowercase         |

# 1. Concatenation

## What is Concatenation?

Concatenation means **joining two or more strings into a single string**.

Example:

```
"John" + "Smith"

↓

"JohnSmith"
```

In many SQL databases (such as SQLite), concatenation is performed using the **pipe operator (`||`)**. Some database systems (such as SQL Server) use the **`+` operator** instead. :contentReference[oaicite:3]{index=3}

---

## Syntax (SQLite)

```sql
SELECT CompanyName || ContactName
FROM Customers;
```

Example:

| CompanyName | ContactName | Result        |
| ----------- | ----------- | ------------- |
| Microsoft   | John        | MicrosoftJohn |
| Google      | Alice       | GoogleAlice   |

---

## Real-World Uses

- Creating usernames
- Generating unique IDs
- Combining first and last names
- Creating labels

Example:

```sql
SELECT FirstName || LastName AS FullName
FROM Employees;
```

---

# 2. TRIM()

## Purpose

Removes **leading and trailing spaces** from text.

Before:

```
"   Hello World   "
```

After:

```
"Hello World"
```

---

## Syntax

```sql
SELECT TRIM(column_name)
FROM table_name;
```

Example:

```sql
SELECT TRIM('   You the best   ');
```

Output:

```
You the best
```

---

# LTRIM()

Removes spaces only from the **left**.

```sql
SELECT LTRIM('    Rahul');
```

Result:

```
Rahul
```

---

# RTRIM()

Removes spaces only from the **right**.

```sql
SELECT RTRIM('Rahul     ');
```

Result:

```
Rahul
```

---

# Why Use TRIM?

Useful for:

- Cleaning imported data.
- Removing accidental spaces.
- Improving comparisons.
- Avoiding duplicate values caused by whitespace.

---

# 3. SUBSTR()

## Purpose

Extracts a portion of a string.

Imagine:

```
Andrew

Position:

A n d r e w
1 2 3 4 5 6
```

If we start at position **3** and extract **4** characters:

```
drew
```

---

## Syntax

```sql
SUBSTR(string, start_position, length)
```

Parameters:

- **string** → Source text
- **start_position** → Starting character
- **length** → Number of characters to return

---

## Example

```sql
SELECT SUBSTR(FirstName, 3, 4)
FROM Employees;
```

Results:

| Name   | Output |
| ------ | ------ |
| Nancy  | ncy    |
| Andrew | drew   |
| Ann    | n      |

If the string is shorter than the requested length, SQL returns only the available characters. :contentReference[oaicite:5]{index=5}

---

## More Examples

First three characters:

```sql
SELECT SUBSTR(FirstName,1,3)
FROM Employees;
```

Result:

| Name   | Output |
| ------ | ------ |
| Rahul  | Rah    |
| Andrew | And    |

---

# Uses of SUBSTR()

- Create employee IDs
- Extract country codes
- Shorten long names
- Parse product codes
- Generate abbreviations

---

# 4. Changing Text Case

Different users may enter text inconsistently:

```
RAHUL
Rahul
rahul
RaHuL
```

This makes searching and comparing difficult.

Convert everything to one standard case before analysis. :contentReference[oaicite:6]{index=6}

---

# UPPER()

Converts text to uppercase.

```sql
SELECT UPPER(FirstName)
FROM Employees;
```

Result:

```
RAHUL
```

Some databases also support:

```sql
UCASE()
```

---

# LOWER()

Converts text to lowercase.

```sql
SELECT LOWER(FirstName)
FROM Employees;
```

Result:

```
rahul
```

---

# Practical Example

Before:

```
Rahul
RAHUL
rahul
RaHuL
```

After:

```sql
SELECT UPPER(Name)
```

Result:

```
RAHUL
RAHUL
RAHUL
RAHUL
```

---

# Real-World Applications

## Data Cleaning

```sql
SELECT TRIM(Name)
FROM Customers;
```

---

## Standardizing Names

```sql
SELECT UPPER(Name)
FROM Employees;
```

---

## Creating User IDs

```sql
SELECT SUBSTR(FirstName,1,2) ||
       SUBSTR(LastName,1,2)
FROM Employees;
```

Example:

```
Rahul Kurup

↓

RaKu
```

---

## Creating Full Names

```sql
SELECT FirstName || ' ' || LastName
FROM Employees;
```

Output:

```
Rahul Kurup
```

---

# Summary Table

| Function   | Description                  | Example            |
| ---------- | ---------------------------- | ------------------ | --------------- | ---------- | --- | --------- |
| `          |                              | `                  | Combine strings | `FirstName |     | LastName` |
| `TRIM()`   | Remove spaces from both ends | `TRIM(Name)`       |
| `LTRIM()`  | Remove left spaces           | `LTRIM(Name)`      |
| `RTRIM()`  | Remove right spaces          | `RTRIM(Name)`      |
| `SUBSTR()` | Extract part of a string     | `SUBSTR(Name,1,3)` |
| `UPPER()`  | Convert to uppercase         | `UPPER(Name)`      |
| `LOWER()`  | Convert to lowercase         | `LOWER(Name)`      |

---

# Interview Questions

### Q1. What is concatenation?

**Answer:**  
Concatenation combines two or more strings into a single string using operators such as `||` (SQLite/PostgreSQL) or `+` (SQL Server).

---

### Q2. What does `TRIM()` do?

**Answer:**  
It removes leading and trailing spaces from a string.

---

### Q3. Difference between `TRIM()`, `LTRIM()`, and `RTRIM()`?

| Function  | Removes                    |
| --------- | -------------------------- |
| `TRIM()`  | Both left and right spaces |
| `LTRIM()` | Left spaces only           |
| `RTRIM()` | Right spaces only          |

---

### Q4. What is `SUBSTR()`?

**Answer:**  
`SUBSTR()` extracts a specified portion of a string using a starting position and length.

---

### Q5. What is the purpose of `UPPER()` and `LOWER()`?

**Answer:**  
They standardize text by converting strings to uppercase or lowercase, making comparisons and data cleaning easier.

---

# Key Takeaways

- String functions are essential for **data cleaning and preprocessing**.
- Use **concatenation (`||`)** to combine strings.
- Use **`TRIM()`, `LTRIM()`, and `RTRIM()`** to remove unwanted spaces.
- Use **`SUBSTR()`** to extract part of a string.
- Use **`UPPER()` and `LOWER()`** to standardize text case.
- Different database systems may use different syntax for concatenation, so always check your DBMS documentation. :contentReference[oaicite:7]{index=7}

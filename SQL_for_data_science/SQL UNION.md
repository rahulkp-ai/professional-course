# SQL UNION

## Overview

`UNION` is an SQL operator used to **combine the results of two or more `SELECT` statements into a single result set**.

Unlike **JOIN**, which combines **columns** from multiple tables, **UNION combines rows** by stacking one query's results on top of another.

> Think of UNION as stacking two tables vertically.

---

# Learning Objectives

After studying this topic, you should be able to:

- Explain what a `UNION` does.
- Understand the rules required to use `UNION`.
- Write correct `UNION` syntax.
- Identify situations where `UNION` is useful.

---

# What is UNION?

A `UNION` merges the output of multiple `SELECT` queries into **one result table**.

Each query executes independently, and the resulting rows are combined.

```
Query 1 Result
--------------
A
B
C

UNION

Query 2 Result
--------------
D
E
F

↓

Final Result
------------
A
B
C
D
E
F
```

---

# UNION vs JOIN

| JOIN                                           | UNION                             |
| ---------------------------------------------- | --------------------------------- |
| Combines **columns**                           | Combines **rows**                 |
| Matches related records                        | Stacks result sets                |
| Uses ON clause                                 | No ON clause                      |
| Usually works across tables with relationships | Works on compatible query results |

---

# Rules for Using UNION

To successfully use `UNION`, all queries must satisfy these conditions.

## 1. Same Number of Columns

Both queries must return the **same number of columns**.

Correct

```sql
SELECT City, Country
FROM Customers

UNION

SELECT City, Country
FROM Suppliers;
```

Incorrect

```sql
SELECT City, Country
FROM Customers

UNION

SELECT City
FROM Suppliers;
```

The second query returns fewer columns.

---

## 2. Compatible Data Types

Corresponding columns must have compatible data types.

Example:

| Query 1 | Query 2 | Valid? |
| ------- | ------- | ------ |
| VARCHAR | VARCHAR | Yes    |
| INTEGER | INTEGER | Yes    |
| DATE    | DATE    | Yes    |
| INTEGER | VARCHAR | No     |

---

## 3. Same Column Order

Columns must appear in the **same order**.

Correct:

```sql
SELECT City, Country
FROM Customers

UNION

SELECT City, Country
FROM Suppliers;
```

Incorrect:

```sql
SELECT City, Country
FROM Customers

UNION

SELECT Country, City
FROM Suppliers;
```

Even though the names match, the order is different.

---

# Syntax

```sql
SELECT column1, column2
FROM table1

UNION

SELECT column1, column2
FROM table2;
```

---

# Example

Find all cities in Germany where the company has either customers or suppliers.

```sql
SELECT City, Country
FROM Customers
WHERE Country = 'Germany'

UNION

SELECT City, Country
FROM Suppliers
WHERE Country = 'Germany'

ORDER BY City;
```

---

# Explanation

### First Query

Gets German customer locations.

```sql
SELECT City, Country
FROM Customers
WHERE Country = 'Germany'
```

Example:

| City   | Country |
| ------ | ------- |
| Berlin | Germany |
| Munich | Germany |

---

### Second Query

Gets German supplier locations.

```sql
SELECT City, Country
FROM Suppliers
WHERE Country = 'Germany'
```

Example:

| City    | Country |
| ------- | ------- |
| Hamburg | Germany |
| Munich  | Germany |

---

### Final Result

```
Berlin
Hamburg
Munich
```

Now you have every German city where your business has a presence.

---

# Real-World Use Cases

## 1. Customer + Supplier Locations

Find every city where the business operates.

```sql
SELECT City FROM Customers

UNION

SELECT City FROM Suppliers;
```

---

## 2. Employee Lists

Combine employees from multiple branches.

```sql
SELECT Name
FROM BranchA

UNION

SELECT Name
FROM BranchB;
```

---

## 3. Product Catalog

Combine products from multiple warehouses.

```sql
SELECT ProductName
FROM Warehouse1

UNION

SELECT ProductName
FROM Warehouse2;
```

---

## 4. Reporting

Merge data from archived and current tables.

```sql
SELECT *
FROM Orders2025

UNION

SELECT *
FROM Orders2026;
```

---

# UNION vs UNION ALL

## UNION

- Removes duplicate rows.
- Performs duplicate checking.
- Slightly slower.

```sql
SELECT City FROM Customers

UNION

SELECT City FROM Suppliers;
```

Result:

```
Berlin
Munich
Hamburg
```

Only one `Munich` appears.

---

## UNION ALL

- Keeps duplicates.
- Faster because no duplicate removal.

```sql
SELECT City FROM Customers

UNION ALL

SELECT City FROM Suppliers;
```

Result:

```
Berlin
Munich
Hamburg
Munich
```

`Munich` appears twice.

---

# Visual Representation

```
Customers

Berlin
Munich

        UNION

Suppliers

Hamburg
Munich

        ↓

Final Result

Berlin
Hamburg
Munich
```

---

# Key Differences

| Feature                   | UNION | JOIN        |
| ------------------------- | ----- | ----------- |
| Combines                  | Rows  | Columns     |
| Requires matching columns | Yes   | No          |
| Requires related tables   | No    | Usually Yes |
| Uses ON clause            | No    | Yes         |
| Removes duplicates        | Yes   | No          |

---

# Advantages

- Combines multiple query results into one.
- Simplifies reporting across multiple tables.
- Easy to read and write.
- Eliminates duplicates automatically.
- Useful for merging similar datasets.

---

# Limitations

- Requires the same number of columns.
- Data types must be compatible.
- Column order must match.
- Cannot merge unrelated column structures.

---

# Interview Questions

### Q1. What is UNION?

**Answer:**  
`UNION` combines the results of two or more `SELECT` statements into a single result set by stacking rows vertically.

---

### Q2. What is the difference between UNION and JOIN?

**Answer:**

- `UNION` combines **rows**.
- `JOIN` combines **columns** based on relationships.

---

### Q3. What conditions must be met to use UNION?

- Same number of columns.
- Compatible data types.
- Same column order.

---

### Q4. What is the difference between UNION and UNION ALL?

| UNION              | UNION ALL                       |
| ------------------ | ------------------------------- |
| Removes duplicates | Keeps duplicates                |
| Slightly slower    | Faster                          |
| Most commonly used | Used when duplicates are needed |

---

### Q5. When should UNION be used?

Use `UNION` when you want to merge the results of multiple similar queries into one result set, such as combining customers and suppliers, employees from multiple branches, or historical and current records.

---

# Summary

- `UNION` combines the **rows** of multiple `SELECT` queries.
- It **stacks result sets vertically**.
- Every query must return:
  - The **same number of columns**.
  - **Compatible data types**.
  - The **same column order**.
- `UNION` removes duplicates by default.
- Use `UNION ALL` to keep duplicates and improve performance.
- Unlike `JOIN`, `UNION` combines **rows**, not **columns**.

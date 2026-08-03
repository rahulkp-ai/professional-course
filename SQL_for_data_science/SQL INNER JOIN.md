# SQL INNER JOIN

## Learning Objectives

After completing this lesson, you should be able to:

- Define an **INNER JOIN**.
- Explain when an INNER JOIN is used.
- Write the SQL syntax for an INNER JOIN.
- Understand the purpose of the `ON` clause.
- Use **table aliases** and **qualified column names**.
- Join multiple tables efficiently.

---

# What is an INNER JOIN?

An **INNER JOIN** returns **only the rows that have matching values in both tables**.

Unlike a CROSS JOIN, an INNER JOIN only returns related records based on a matching key.

---

# Visualization

```
Table A               Table B

A                     A
B                     B
C                     D
```

INNER JOIN Result

```
A
B
```

Only the matching rows are returned.

---

# How INNER JOIN Works

Suppose we have two tables.

### Suppliers

| SupplierID | CompanyName |
| ---------- | ----------- |
| 1          | ABC Ltd     |
| 2          | XYZ Ltd     |

### Products

| ProductName | SupplierID |
| ----------- | ---------- |
| Laptop      | 1          |
| Mouse       | 1          |
| Keyboard    | 3          |

Using an INNER JOIN:

| CompanyName | ProductName |
| ----------- | ----------- |
| ABC Ltd     | Laptop      |
| ABC Ltd     | Mouse       |

Notice:

- Supplier **1** exists in both tables
- Supplier **3** has no matching supplier
- Supplier **2** has no products

Only matching records are returned.

---

# Why Are Keys Important?

INNER JOIN depends on **keys**.

Example:

```
Suppliers.SupplierID

=

Products.SupplierID
```

SQL compares these values.

If they match,

the rows are combined.

---

# SQL Syntax

```sql
SELECT
    CompanyName,
    ProductName,
    UnitPrice
FROM Suppliers
INNER JOIN Products
ON Suppliers.SupplierID = Products.SupplierID;
```

---

# Syntax Breakdown

### SELECT

Choose the columns you want.

```sql
SELECT
    CompanyName,
    ProductName,
    UnitPrice
```

---

### FROM

Choose the first table.

```sql
FROM Suppliers
```

---

### INNER JOIN

Specify the second table.

```sql
INNER JOIN Products
```

---

### ON

Defines **how the tables are connected**.

```sql
ON Suppliers.SupplierID = Products.SupplierID
```

This tells SQL which rows should be matched.

---

# CROSS JOIN vs INNER JOIN

| CROSS JOIN               | INNER JOIN            |
| ------------------------ | --------------------- |
| Every row with every row | Only matching rows    |
| No key required          | Matching key required |
| No `ON` clause           | Requires `ON` clause  |
| Result = X × Y           | Only matching records |
| Rarely used              | Most commonly used    |

---

# Qualified Column Names

Sometimes multiple tables contain columns with the same name.

Example:

```
CompanyName
```

exists in both:

- Suppliers
- Products

SQL won't know which one to use.

Instead, qualify the column.

```sql
Suppliers.CompanyName
```

or

```sql
Products.CompanyName
```

This removes ambiguity.

---

# Table Aliases

Typing long table names repeatedly is tedious.

Instead, use aliases.

Example:

```sql
FROM Orders AS o
```

or simply

```sql
FROM Orders o
```

Now instead of:

```sql
Orders.OrderID
```

write

```sql
o.OrderID
```

Much cleaner.

---

# Common Alias Style

| Table     | Alias |
| --------- | ----- |
| Orders    | o     |
| Customers | c     |
| Employees | e     |
| Products  | p     |
| Suppliers | s     |

Aliases improve readability and reduce typing.

---

# Example Using Aliases

```sql
SELECT
    s.CompanyName,
    p.ProductName,
    p.UnitPrice
FROM Suppliers s
INNER JOIN Products p
ON s.SupplierID = p.SupplierID;
```

Much easier to read.

---

# Joining Multiple Tables

INNER JOIN is **not limited to two tables**.

Example:

```
Orders

↓

Customers

↓

Employees
```

SQL:

```sql
SELECT
    o.OrderID,
    c.CompanyName,
    e.LastName
FROM Orders o
INNER JOIN Customers c
ON o.CustomerID = c.CustomerID
INNER JOIN Employees e
ON o.EmployeeID = e.EmployeeID;
```

---

# How This Query Works

Step 1:

```
Orders

JOIN

Customers
```

using

```
CustomerID
```

Now we know:

- Order
- Customer

---

Step 2:

Join the result with Employees.

```
Orders

JOIN

Employees
```

using

```
EmployeeID
```

Now we know:

- Order
- Customer
- Employee

---

# Multiple JOIN Visualization

```
Orders
   |
CustomerID
   |
Customers
   |
EmployeeID
   |
Employees
```

Each JOIN connects tables using matching keys.

---

# Best Practices

## 1. Always Qualify Column Names

Instead of:

```sql
SELECT CompanyName
```

write

```sql
SELECT c.CompanyName
```

This avoids ambiguity.

---

## 2. Use Table Aliases

Instead of:

```sql
Orders.CustomerID
```

write

```sql
o.CustomerID
```

Cleaner and easier to maintain.

---

## 3. Join Only When Necessary

Each JOIN increases query complexity.

More JOINs mean:

- More computation
- More memory usage
- Slower execution

Avoid unnecessary joins.

---

## 4. Verify Your Join

A query may execute successfully but still return incorrect data.

Always check:

- Are you joining on the correct key?
- Is the number of returned rows reasonable?
- Does the result make business sense?

---

# Advantages of INNER JOIN

Returns only relevant matching records

Efficient for relational databases

Combines data from multiple tables

Supports multiple table joins

Most commonly used SQL JOIN

---

# Limitations

- Excludes unmatched rows.
- Requires matching key values.
- Incorrect join conditions lead to incorrect results.
- Too many joins can reduce performance.

---

# INNER JOIN Summary

- Returns **only matching records** from both tables.
- Uses **keys** to connect related tables.
- Requires an **ON** clause.
- Supports joining multiple tables.
- Table aliases improve readability.
- Qualified column names avoid ambiguity.
- Only join tables when necessary.

---

# Quick Comparison

| Feature           | CROSS JOIN        | INNER JOIN         |
| ----------------- | ----------------- | ------------------ |
| Matching required | No                | Yes                |
| Uses key          | No                | Yes                |
| Uses `ON`         | No                | Yes                |
| Result            | Every combination | Only matching rows |
| Common usage      | Rare              | Very common        |

---

# Key Takeaways

- **INNER JOIN** is the most commonly used SQL join.
- Returns only rows with matching values in both tables.
- Uses the `ON` clause to define the relationship.
- Keys (e.g., `CustomerID`, `SupplierID`) connect related tables.
- Table aliases (`o`, `c`, `e`) simplify queries.
- Qualify column names to avoid ambiguity.
- INNER JOIN can connect multiple tables in a single query.
- Always verify your join conditions and returned data.

---

# Quick Revision

### Q1. What does an INNER JOIN return?

Only rows that have matching values in both tables.

---

### Q2. Which clause defines how tables are matched?

```sql
ON
```

---

### Q3. Why are keys important?

They link related records between tables.

---

### Q4. What is the purpose of table aliases?

To shorten table names and improve readability.

Example:

```sql
Orders → o
Customers → c
Employees → e
```

---

### Q5. Can an INNER JOIN combine more than two tables?

Yes.

You can chain multiple `INNER JOIN` statements together.

---

### Q6. Why should you avoid unnecessary joins?

Because they increase:

- Query complexity
- CPU usage
- Memory consumption
- Execution time

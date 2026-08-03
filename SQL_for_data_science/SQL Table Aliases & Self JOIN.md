# SQL Table Aliases & Self JOIN

## Learning Objectives

After completing this lesson, you should be able to:

- Define a **table alias**.
- Create aliases for tables in SQL queries.
- Explain why aliases improve readability.
- Understand common alias naming conventions.
- Define and use a **SELF JOIN**.
- Explain why aliases are essential in SELF JOINs.

---

# What is a Table Alias?

A **table alias** is a temporary name assigned to a table during the execution of a SQL query.

It makes queries:

- Easier to read
- Easier to write
- Easier to maintain

> **Important:** A table alias **does not rename the actual table**. It exists only for the duration of the query.

---

# Why Use Table Aliases?

Without aliases, long table names make SQL queries difficult to read.

Example (without aliases):

```sql
SELECT
    Vendors.VendorName,
    Products.ProductName,
    Products.Price
FROM Vendors
INNER JOIN Products
ON Vendors.VendorID = Products.VendorID;
```

Notice how `Vendors` and `Products` are repeated many times.

---

# Using Table Aliases

Assign short names to tables.

```sql
SELECT
    v.VendorName,
    p.ProductName,
    p.Price
FROM Vendors AS v
INNER JOIN Products AS p
ON v.VendorID = p.VendorID;
```

Much cleaner and easier to read.

---

# Alias Syntax

Using `AS`:

```sql
FROM Vendors AS v
```

Without `AS` (also valid):

```sql
FROM Vendors v
```

Both produce the same result.

---

# How Aliases Work

```
Vendors

↓

Alias

↓

v
```

Instead of writing:

```sql
Vendors.VendorName
```

write:

```sql
v.VendorName
```

---

# Benefits of Table Aliases

- Less typing

- Cleaner SQL

- Easier to read

- Easier to maintain

- Essential when joining multiple tables

---

# Common Alias Naming Conventions

There is no fixed rule.

Common styles include:

| Table     | Alias |
| --------- | ----- |
| Vendors   | v     |
| Products  | p     |
| Customers | c     |
| Orders    | o     |
| Employees | e     |

---

Some developers prefer:

```
A
B
C
D
```

Others use abbreviations:

```
VEN
PROD
EMP
CUST
```

Choose a style that is:

- Consistent
- Easy to remember
- Meaningful

---

# Best Practice

Use logical aliases.

Example:

```
Orders

↓

o
```

instead of

```
Orders

↓

a
```

Meaningful aliases improve readability.

---

# Aliases in JOIN Conditions

Without aliases:

```sql
ON Vendors.VendorID = Products.VendorID
```

With aliases:

```sql
ON v.VendorID = p.VendorID
```

The query becomes much shorter.

---

# Aliases in SELECT

Instead of:

```sql
SELECT
Products.Price
```

write:

```sql
SELECT
p.Price
```

---

# What is a SELF JOIN?

A **SELF JOIN** is a join where **a table is joined with itself**.

Although only one table exists, SQL treats it as two separate copies using aliases.

---

# Why Would We Join a Table to Itself?

Sometimes a table stores relationships between its own rows.

Example:

### Employees Table

| EmployeeID | Name    | ReportsTo |
| ---------- | ------- | --------- |
| 1          | CEO     | NULL      |
| 2          | Alice   | 1         |
| 3          | Bob     | 1         |
| 4          | Charlie | 2         |

Notice:

- Charlie reports to Alice.
- Alice reports to the CEO.

Both employees and managers are stored in the **same table**.

---

# Why Aliases Are Required

Without aliases:

```sql
Employees.EmployeeID
=
Employees.EmployeeID
```

SQL cannot distinguish between:

- Employee
- Manager

Aliases solve this problem.

---

# SELF JOIN Example

```sql
SELECT
    e1.FirstName AS Employee,
    e2.FirstName AS Manager
FROM Employees e1
LEFT JOIN Employees e2
ON e1.ReportsTo = e2.EmployeeID;
```

---

# How This Query Works

### First Copy

```sql
Employees e1
```

Represents:

```
Employees
```

---

### Second Copy

```sql
Employees e2
```

Represents:

```
Managers
```

Although both are the same table.

---

### JOIN Condition

```sql
e1.ReportsTo = e2.EmployeeID
```

Meaning:

Find the employee whose manager's ID matches another employee's ID.

---

# Visualization

```
Employees Table

EmployeeID   Name      ReportsTo

1            CEO       NULL
2            Alice     1
3            Bob       1
4            Charlie   2
```

SELF JOIN Result

| Employee | Manager |
| -------- | ------- |
| CEO      | NULL    |
| Alice    | CEO     |
| Bob      | CEO     |
| Charlie  | Alice   |

---

# Why LEFT JOIN Is Used

Notice:

The CEO has no manager.

If we use:

```sql
LEFT JOIN
```

The CEO still appears in the result with:

```
Manager = NULL
```

If an INNER JOIN were used, the CEO would be excluded because there is no matching manager.

---

# Real-World Uses of SELF JOIN

### Organizational Charts

Find employees and managers.

---

### Reporting Hierarchies

Who reports to whom?

---

### Family Trees

Find parent-child relationships.

---

### Product Categories

Parent category → Child category.

---

### Folder Structures

Parent folder → Subfolder.

---

### Employee Management Systems

Determine reporting structures inside a company.

---

# Why Table Aliases Are Essential

For a normal JOIN:

```
Customers

JOIN

Orders
```

Two different tables already exist.

---

For a SELF JOIN:

```
Employees

JOIN

Employees
```

SQL cannot distinguish between the two copies.

Aliases create separate identities.

Example:

```
Employees

↓

e1
```

```
Employees

↓

e2
```

Now SQL knows which instance is being referenced.

---

# Best Practices

- Use meaningful aliases.

- Keep aliases short.

- Always qualify column names.

- Use aliases whenever multiple tables are involved.

- SELF JOINs always require aliases.

---

# Key Takeaways

- A **table alias** is a temporary name assigned to a table.
- Aliases simplify SQL queries and improve readability.
- Aliases exist only during query execution.
- Use logical aliases like `o`, `c`, `e`, `p`, `v`.
- A **SELF JOIN** joins a table with itself.
- SELF JOINs require **different aliases** for each instance of the table.
- SELF JOINs are commonly used to model hierarchical relationships, such as employees and managers.

---

# Quick Revision

### Q1. What is a table alias?

A temporary name given to a table within a SQL query.

---

### Q2. Does an alias rename the actual table?

No.

It exists only during query execution.

---

### Q3. Why use table aliases?

- Shorter queries
- Better readability
- Easier maintenance
- Required for SELF JOINs

---

### Q4. What is a SELF JOIN?

A JOIN where a table is joined with itself.

---

### Q5. Why are aliases mandatory in a SELF JOIN?

Because SQL must distinguish between the two instances of the same table.

---

### Q6. Give a common real-world use of a SELF JOIN.

Finding employees and their managers using an employee hierarchy.

# SQL Joins - Introduction

## Learning Objectives

After completing this lesson, you should be able to:

- Explain the benefits of relational database systems.
- Understand what a **JOIN** is.
- Use **JOIN** to combine data from multiple tables.
- Explain how **keys** connect related tables.

---

# Why Do We Need JOIN?

Previously, we used **subqueries** to combine information from multiple tables.

Although subqueries are useful, they have limitations:

- Can become difficult to read.
- May be less efficient.
- Not always the best solution.

**JOIN** is the standard and more powerful method for combining related data stored in different tables.

---

# Why Is Data Stored in Multiple Tables?

Relational databases intentionally split data into multiple tables.

Instead of storing everything in one giant table:

| CustomerID | Name | City | OrderID | Product | Price |
| ---------- | ---- | ---- | ------- | ------- | ----- |

the database separates information:

### Customers

| CustomerID | Name  | City  |
| ---------- | ----- | ----- |
| 101        | Rahul | Kochi |

### Orders

| OrderID | CustomerID | Product |
| ------- | ---------- | ------- |
| 1       | 101        | Laptop  |

---

## Benefits of Multiple Tables

### 1. Efficient Storage

Avoids duplicate data.

Instead of storing customer information with every order:

```
Rahul | Kochi | Laptop
Rahul | Kochi | Mouse
Rahul | Kochi | Keyboard
```

Store customer information only once.

---

### 2. Easier Updates

If Rahul moves from Kochi to Calicut:

Without normalization:

Update hundreds of rows.

With separate tables:

Update **only one row** in the Customers table.

---

### 3. Better Data Management

Breaking data into logical tables makes it:

- Easier to organize
- Easier to maintain
- Easier to scale

---

### 4. Better Database Design

Tables are usually designed around business processes.

Examples:

- Customers
- Orders
- Products
- Employees
- Payments

Each table has a specific responsibility.

---

# What Is a JOIN?

A **JOIN** combines related rows from two or more tables into a single result.

It allows SQL to retrieve information spread across multiple tables **using one query**.

---

## Simple Example

### Customers

| CustomerID | Name  |
| ---------- | ----- |
| 101        | Rahul |

### Orders

| OrderID | CustomerID | Product |
| ------- | ---------- | ------- |
| 1       | 101        | Laptop  |

JOIN combines them:

| Name  | Product |
| ----- | ------- |
| Rahul | Laptop  |

---

# How Does JOIN Work?

JOIN works by matching **key values** between tables.

Example:

```
Customers.CustomerID
          =
Orders.CustomerID
```

If the values match,

SQL combines those rows into one result.

---

# Keys

A **Key** is a column that links related tables.

Example:

Customers table

```
CustomerID
```

Orders table

```
CustomerID
```

This common field allows SQL to identify which customer placed which order.

---

## Keys Are the Bridge

```
Customers
+------------+
| CustomerID |
+------------+
       |
       |
       |
Orders
+------------+
| CustomerID |
+------------+
```

The key acts as the connection between tables.

---

# Why JOIN Is Better Than Subqueries

| Subqueries                        | JOIN                            |
| --------------------------------- | ------------------------------- |
| Can be complex                    | Easier to read                  |
| Sometimes slower                  | Usually more efficient          |
| Limited for combining many tables | Easily combines multiple tables |
| Harder to maintain                | Cleaner SQL                     |

---

# Important Characteristics of JOIN

- Combines data from multiple tables.
- Uses matching key values.
- Executes in a single SQL query.
- Does **not** permanently merge tables.
- Exists only while the query is running.

---

# Temporary Nature of JOIN

A JOIN **does not create a new table**.

It only creates a temporary result set during query execution.

After the query finishes,

the joined data disappears.

---

# Real-World Example

Imagine an online shopping system.

### Customers

| CustomerID | Name  |
| ---------- | ----- |
| 101        | Rahul |

### Orders

| OrderID | CustomerID | Product |
| ------- | ---------- | ------- |
| 1       | 101        | Laptop  |
| 2       | 101        | Mouse   |

Using JOIN:

| Name  | Product |
| ----- | ------- |
| Rahul | Laptop  |
| Rahul | Mouse   |

Notice that customer information is stored only once but can be retrieved with every order.

---

# Key Takeaways

- Relational databases store data in multiple related tables.
- Multiple tables reduce redundancy and improve efficiency.
- JOIN combines information from multiple tables.
- Keys link related records across tables.
- JOIN retrieves data in a single query.
- JOIN is temporary—it does not modify the database.
- JOIN is generally preferred over subqueries for combining related data.

---

# What's Next?

In the next lesson, you'll learn the different types of SQL JOINs, including:

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- CROSS JOIN

These joins determine **which rows are returned** when combining tables.

---

# Quick Revision

**Q1. Why are databases split into multiple tables?**

- Efficient storage
- Avoid duplicate data
- Easier updates
- Better scalability

---

**Q2. What is a JOIN?**

A SQL operation that combines rows from multiple related tables.

---

**Q3. What connects two tables?**

A **Key** (such as `CustomerID`).

---

**Q4. Does JOIN create a permanent table?**

No.

It only exists during query execution.

---

**Q5. Why is JOIN preferred over subqueries?**

- Cleaner
- Faster
- Easier to maintain
- Better for combining multiple tables

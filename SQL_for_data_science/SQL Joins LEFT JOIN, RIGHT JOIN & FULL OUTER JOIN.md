# SQL Joins : LEFT JOIN, RIGHT JOIN & FULL OUTER JOIN

## Learning Objectives

After completing this topic, you should be able to:

- Explain how **LEFT JOIN**, **RIGHT JOIN**, and **FULL OUTER JOIN** work.
- Identify when each join should be used.
- Write SQL queries using these joins.
- Understand SQLite limitations regarding joins.

---

# SQLite Support

| Join Type       | SQLite Support |
| --------------- | -------------- |
| INNER JOIN      | Yes            |
| LEFT JOIN       | Yes            |
| RIGHT JOIN      | No             |
| FULL OUTER JOIN | No             |

> **Important:** SQLite only supports **LEFT JOIN**.  
> RIGHT JOIN can be simulated by swapping table order and using LEFT JOIN.  
> FULL OUTER JOIN is not supported.

---

# 1. LEFT JOIN

## Definition

A **LEFT JOIN** returns:

- All rows from the **left table**
- Matching rows from the right table
- NULL values if no matching record exists in the right table

### Visualization

```
LEFT TABLE          RIGHT TABLE

      ●────────●
    ●────────────●

Returned Area:
Entire Left Table + Matching Right Rows
```

---

## Example

### Customers Table

| CustomerID | Company |
| ---------- | ------- |
| 1          | ABC Ltd |
| 2          | XYZ Ltd |
| 3          | Google  |

### Orders Table

| OrderID | CustomerID |
| ------- | ---------- |
| 101     | 1          |
| 102     | 2          |

Customer **3** has no order.

### LEFT JOIN Result

| Company | OrderID |
| ------- | ------- |
| ABC Ltd | 101     |
| XYZ Ltd | 102     |
| Google  | NULL    |

Notice:

- Every customer appears.
- Customers without orders still appear.
- Missing order information becomes **NULL**.

---

## Syntax

```sql
SELECT
    C.CompanyName,
    O.OrderID
FROM Customers AS C
LEFT JOIN Orders AS O
ON C.CustomerID = O.CustomerID;
```

---

## When to Use LEFT JOIN

Use LEFT JOIN when:

- You want **all records from the first table**
- Missing matches should still be displayed
- Finding missing relationships

Examples:

- Customers without orders
- Students without grades
- Employees without departments

---

# 2. RIGHT JOIN

## Definition

A **RIGHT JOIN** returns:

- All rows from the **right table**
- Matching rows from the left table
- NULL values for unmatched left records

---

### Visualization

```
LEFT TABLE          RIGHT TABLE

      ●────────●
         ●────────────●

Returned Area:
Entire Right Table + Matching Left Rows
```

---

## Example

Suppose:

Left Table → Customers

Right Table → Orders

Result:

| Company | OrderID |
| ------- | ------- |
| ABC Ltd | 101     |
| XYZ Ltd | 102     |
| NULL    | 103     |

Order **103** exists even though no customer record matches.

---

## Syntax

```sql
SELECT
    Orders.OrderID,
    Employees.LastName,
    Employees.FirstName
FROM Orders
RIGHT JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID;
```

---

## SQLite Alternative

SQLite **does not support RIGHT JOIN**.

Instead:

Swap the table order and use **LEFT JOIN**.

Instead of:

```sql
Orders
RIGHT JOIN Employees
```

Write:

```sql
Employees
LEFT JOIN Orders
```

Both produce the same result.

---

## When to Use RIGHT JOIN

Use when:

- Every row from the **right table** is required.
- Matching rows from the left table are optional.

Since SQLite lacks RIGHT JOIN:

> Simply reverse table order and use LEFT JOIN.

---

# 3. FULL OUTER JOIN

## Definition

A **FULL OUTER JOIN** returns:

- All rows from the left table
- All rows from the right table
- Matching rows where possible
- NULL where no match exists

---

### Visualization

```
LEFT TABLE        RIGHT TABLE

     ●────────●
   ●────────────●

Returned Area:
Everything
```

---

## Example

Customers

| ID  | Company |
| --- | ------- |
| 1   | ABC     |
| 2   | XYZ     |

Orders

| OrderID | CustomerID |
| ------- | ---------- |
| 101     | 1          |
| 102     | 3          |

FULL OUTER JOIN Result

| Company | OrderID |
| ------- | ------- |
| ABC     | 101     |
| XYZ     | NULL    |
| NULL    | 102     |

Notice:

- Customer 2 has no order.
- Order 102 has no customer.
- Both still appear.

---

## Syntax

```sql
SELECT
    C.CompanyName,
    O.OrderID
FROM Customers AS C
FULL OUTER JOIN Orders AS O
ON C.CustomerID = O.CustomerID;
```

---

## SQLite Support

SQLite **does not support FULL OUTER JOIN**.

Other database systems that support it include:

- PostgreSQL
- SQL Server
- Oracle

---

## When to Use FULL OUTER JOIN

Useful when you need:

- Every record from both tables
- Complete comparison of two datasets
- Detect missing records on either side

Examples:

- Inventory comparison
- Customer vs Order audit
- Data migration validation

---

# Comparison

| Feature                           | LEFT JOIN | RIGHT JOIN | FULL OUTER JOIN |
| --------------------------------- | --------- | ---------- | --------------- |
| Returns all rows from left table  | Yes       | No         | Yes             |
| Returns all rows from right table | No        | Yes        | No              |
| Returns matching rows             | Yes       | Yes        | Yes             |
| SQLite Supported                  | Yes       | No         | No              |

---

# Quick Memory Trick

```
LEFT JOIN
← Keep everything on the LEFT

RIGHT JOIN
Keep everything on the RIGHT →

FULL OUTER JOIN
Keep EVERYTHING
```

---

# Key Notes

- LEFT JOIN keeps all rows from the first (left) table.
- RIGHT JOIN keeps all rows from the second (right) table.
- FULL OUTER JOIN keeps all rows from both tables.
- Missing matches are filled with **NULL**.
- SQLite supports **LEFT JOIN only**.
- RIGHT JOIN can be replaced by swapping table order and using LEFT JOIN.
- FULL OUTER JOIN is unavailable in SQLite.

---

# Exam Tips

LEFT JOIN → All left rows + matching right rows

RIGHT JOIN → All right rows + matching left rows

FULL OUTER JOIN → All rows from both tables

SQLite:

- LEFT JOIN → Supported
- RIGHT JOIN → Not Supported
- FULL OUTER JOIN → Not Supported

---

# Summary

| Join            | Keeps                       |
| --------------- | --------------------------- |
| INNER JOIN      | Only matching rows          |
| LEFT JOIN       | All left rows + matches     |
| RIGHT JOIN      | All right rows + matches    |
| FULL OUTER JOIN | Everything from both tables |

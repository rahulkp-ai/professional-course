# SQL Views

## 1. Overview

A **View** in SQL is essentially a **stored query** that can be used like a table.

Views are useful when:

- Queries become complex
- Multiple tables need to be joined repeatedly
- Calculations involve complicated logic
- A query needs to be broken into multiple steps
- You want to simplify future queries
- You want to avoid creating a new physical table

### Core idea

```text
Complex Query
     ↓
   VIEW
     ↓
Acts like a table
     ↓
Simpler queries
```

A view creates the **illusion of a table** without creating a new physical table containing duplicated data.

---

# 2. What Is a View?

A view is a **stored SQL query** that can be queried like a table.

For example:

```sql
CREATE VIEW my_view AS
SELECT
    EmployeeId,
    FirstName,
    LastName
FROM Employees;
```

You can then query it:

```sql
SELECT *
FROM my_view;
```

Conceptually:

```text
Employees Table
       │
       │ SELECT ...
       ▼
    my_view
       │
       │ SELECT *
       ▼
    Result
```

---

# 3. Why Use Views?

Views help **encapsulate complexity**.

Instead of repeatedly writing:

```sql
SELECT ...
FROM TableA
JOIN TableB
    ON ...
JOIN TableC
    ON ...
WHERE ...
GROUP BY ...;
```

you can store that logic inside a view:

```sql
CREATE VIEW my_view AS
SELECT ...
FROM TableA
JOIN TableB
    ON ...
JOIN TableC
    ON ...
WHERE ...;
```

Then future queries can simply use:

```sql
SELECT *
FROM my_view;
```

---

# 4. Basic Syntax

General syntax:

```sql
CREATE VIEW view_name AS
SELECT
    column1,
    column2,
    ...
FROM table_name
WHERE condition;
```

### With `IF NOT EXISTS`

Some SQL systems support:

```sql
CREATE VIEW IF NOT EXISTS view_name AS
SELECT ...
FROM table_name;
```

This prevents an error when the view already exists.

> **Note:** Exact `CREATE VIEW` syntax and support for `IF NOT EXISTS` vary between database systems.

---

# 5. The `AS` Keyword

In a view definition, `AS` introduces the query that defines the view.

```sql
CREATE VIEW my_view AS
SELECT *
FROM Employees;
```

Think of it as:

```text
CREATE VIEW my_view
        ↓
      AS
        ↓
"What should this view contain?"
        ↓
   SELECT statement
```

### Important distinction

`AS` is also commonly used for aliases:

```sql
SELECT Salary AS EmployeeSalary
FROM Employees;
```

But in:

```sql
CREATE VIEW my_view AS
SELECT ...
```

`AS` introduces the **query definition of the view**.

---

# 6. Creating a View from Multiple Tables

One of the biggest advantages of views is that the underlying query can contain joins.

Example:

```sql
CREATE VIEW employee_territories AS
SELECT
    e.EmployeeId,
    e.FirstName,
    e.LastName,
    t.TerritoryId,
    t.TerritoryDescription
FROM Employees e
JOIN EmployeeTerritories et
    ON e.EmployeeId = et.EmployeeId
JOIN Territories t
    ON et.TerritoryId = t.TerritoryId;
```

The view hides the complexity of joining multiple tables.

Now we can simply write:

```sql
SELECT *
FROM employee_territories;
```

---

# 7. Querying a View

Creating the view does not necessarily display its data.

To retrieve the data:

```sql
SELECT *
FROM employee_territories;
```

You can also select specific columns:

```sql
SELECT
    FirstName,
    LastName,
    TerritoryDescription
FROM employee_territories;
```

You can treat the view similarly to a table in many queries.

---

# 8. Performing Further Queries on a View

One of the most useful features is that you can build another query **on top of a view**.

For example:

```sql
SELECT
    LastName,
    FirstName,
    COUNT(*) AS TerritoryCount
FROM employee_territories
GROUP BY
    LastName,
    FirstName;
```

The workflow becomes:

```text
Multiple Tables
      ↓
Complex JOIN
      ↓
    VIEW
      ↓
GROUP BY
      ↓
COUNT()
      ↓
Final Result
```

This makes complicated analysis much easier to manage.

---

# 9. Views as Query Building Blocks

Views can act as **stepping stones** for multi-level queries.

For example:

### Step 1 — Create a view containing sales

```sql
CREATE VIEW sales_by_person AS
SELECT
    SalesPerson,
    COUNT(*) AS SalesCount
FROM Sales
GROUP BY SalesPerson;
```

### Step 2 — Group salespeople

```sql
SELECT
    CASE
        WHEN SalesCount >= 100 THEN 'High'
        WHEN SalesCount >= 50 THEN 'Medium'
        ELSE 'Low'
    END AS SalesGroup,
    COUNT(*) AS NumberOfSalespeople
FROM sales_by_person
GROUP BY
    CASE
        WHEN SalesCount >= 100 THEN 'High'
        WHEN SalesCount >= 50 THEN 'Medium'
        ELSE 'Low'
    END;
```

The view acts as an intermediate layer.

---

# 10. Views and ETL

A view can reduce the need to create intermediate physical tables for transformations.

Instead of:

```text
Source Tables
     ↓
   ETL
     ↓
Intermediate Table
     ↓
Analysis
```

you can sometimes use:

```text
Source Tables
     ↓
    VIEW
     ↓
Analysis
```

This is useful because the view stores the **query logic**, rather than requiring a separate table populated through an ETL process.

---

# 11. Views vs Tables

| Feature                          | Table           | View       |
| -------------------------------- | --------------- | ---------- |
| Stores data physically           | Usually yes     | Usually no |
| Stores SQL query                 | No              | Yes        |
| Can be queried with `SELECT`     | ✅              | ✅         |
| Can combine multiple tables      | Through queries | Yes        |
| Requires ETL to populate         | Sometimes       | Usually no |
| Can simplify complex queries     | —               | ✅         |
| Acts like a table                | ✅              | ✅         |
| Contains its own persistent data | ✅              | ❌ Usually |
| Can be dropped                   | ✅              | ✅         |

> **Important:** A normal view is generally **virtual**. A **materialized view**, supported by some database systems, is different because it stores the query result physically.

---

# 12. Temporary vs Persistent Views

The transcript emphasizes **temporary/session-based views**.

However, the exact behavior depends on the database system.

### Session/temporary view

A temporary view may exist only for the current database session.

Conceptually:

```text
Session 1
   ↓
CREATE TEMP VIEW
   ↓
Use View
   ↓
Session Ends
   ↓
View Disappears
```

If you start another session, you may need to create the temporary view again.

### Persistent view

A regular:

```sql
CREATE VIEW ...
```

is normally stored in the database schema until explicitly dropped.

Therefore:

> **Do not assume every `CREATE VIEW` is temporary.** The persistence behavior depends on the database system and whether you create a temporary view.

---

# 13. Dropping a View

If a view is no longer required:

```sql
DROP VIEW my_view;
```

Some systems support:

```sql
DROP VIEW IF EXISTS my_view;
```

This removes the view definition.

It does **not** normally delete the underlying source-table data.

---

# 14. Views and Data Security

Views can also be useful for controlling what users can access.

Suppose a table contains:

```text
EmployeeID
Name
Department
Salary
Address
Phone
```

Instead of giving a user access to the entire table, you could create a view exposing only selected columns:

```sql
CREATE VIEW employee_public AS
SELECT
    EmployeeID,
    Name,
    Department
FROM Employees;
```

Users can then query:

```sql
SELECT *
FROM employee_public;
```

without necessarily being given direct access to sensitive columns such as:

```text
Salary
Address
Phone
```

This makes views useful for **data abstraction and access control**.

> Actual security depends on the database's permission model. Creating a view alone does not automatically make the underlying data inaccessible.

---

# 15. Views and Write Operations

A view can sometimes support operations such as:

```sql
INSERT
UPDATE
DELETE
```

but this depends on:

- Database system
- View definition
- Joins
- Aggregations
- Expressions
- Database-specific rules

Complex views are often **not directly updatable**.

Therefore, views are commonly used primarily for:

```text
SELECT
Filtering
Joining
Transformation
Aggregation
Abstraction
```

---

# 16. When Are Views Most Useful?

Views are particularly helpful when:

### 1. Joining multiple tables

```sql
Table A
   +
Table B
   +
Table C
   ↓
 VIEW
```

### 2. Complex calculations

Especially when the calculation depends on several steps or complicated ordering of operations.

### 3. Reusing a query

If the same complex query is needed repeatedly, put it into a view.

### 4. Multi-level analysis

A view can become an intermediate layer for another query.

### 5. Data abstraction

Expose only the columns or rows required by a particular user or application.

### 6. Simplifying SQL

Instead of repeatedly writing a long query, query the view.

---

# 17. Example: Complete Workflow

Suppose we need to count territories per employee.

### Step 1 — Create the view

```sql
CREATE VIEW employee_territories AS
SELECT
    e.EmployeeId,
    e.FirstName,
    e.LastName,
    t.TerritoryDescription
FROM Employees e
JOIN EmployeeTerritories et
    ON e.EmployeeId = et.EmployeeId
JOIN Territories t
    ON et.TerritoryId = t.TerritoryId;
```

### Step 2 — Query the view

```sql
SELECT *
FROM employee_territories;
```

### Step 3 — Calculate territory count

```sql
SELECT
    LastName,
    FirstName,
    COUNT(*) AS TerritoryCount
FROM employee_territories
GROUP BY
    LastName,
    FirstName;
```

### Step 4 — Remove the view if no longer required

```sql
DROP VIEW employee_territories;
```

---

# 18. Advantages of Views

### ✅ Simplifies complex queries

Complex joins and calculations can be hidden behind a simple view name.

### ✅ Improves query readability

Instead of repeating a long query:

```sql
SELECT *
FROM complex_query;
```

### ✅ Encourages query reuse

The same logic can be reused by multiple queries.

### ✅ Provides abstraction

Users don't need to know the underlying database structure.

### ✅ Can support security

Expose only selected rows/columns through a view and grant access appropriately.

### ✅ Useful for multi-step analysis

Views can act as intermediate layers.

### ✅ Avoids unnecessary intermediate tables

For many use cases, you can encapsulate transformations without materializing another table.

---

# 19. Limitations of Views

### ❌ Normal views don't usually store their own data

The underlying query is evaluated when the view is queried.

### ❌ Complex views can be slow

If the underlying query contains many joins, aggregations, or calculations, querying the view can still be expensive.

### ❌ Some views are not updatable

Complex views may not support `INSERT`, `UPDATE`, or `DELETE`.

### ❌ Dependency management

If underlying tables or columns change, the view may break.

### ❌ Temporary views have limited lifetime

If using a temporary/session view, it may disappear when the session ends.

### ❌ Database-specific behavior

Syntax and capabilities vary between PostgreSQL, MySQL, SQL Server, SQLite, Oracle, etc.

---

# 20. View vs Subquery

Both can encapsulate complex SQL, but they serve different purposes.

### Subquery

Used directly inside another query:

```sql
SELECT *
FROM (
    SELECT *
    FROM Employees
) AS employee_data;
```

Usually useful for **one query**.

### View

Stored and reusable:

```sql
CREATE VIEW employee_data AS
SELECT *
FROM Employees;
```

Then:

```sql
SELECT *
FROM employee_data;
```

### Comparison

| Feature                    | Subquery | View |
| -------------------------- | -------- | ---- |
| Stored separately          | ❌       | ✅   |
| Reusable across queries    | Limited  | ✅   |
| Simplifies repeated logic  | ❌       | ✅   |
| Defined with `CREATE VIEW` | ❌       | ✅   |
| Good for one-off logic     | ✅       | ✅   |
| Good for reusable logic    | ❌       | ✅   |

---

# 21. View vs Materialized View

These concepts should not be confused.

### View

```text
Query Definition
       ↓
     VIEW
       ↓
Query executed when accessed
```

### Materialized View

```text
Query
  ↓
Result stored physically
  ↓
Materialized View
  ↓
Read stored result
```

Materialized views can improve performance for expensive queries, but their stored results need to be **refreshed** to reflect changes in the underlying data.

---

# 22. Important Syntax

### Create

```sql
CREATE VIEW view_name AS
SELECT ...
FROM ...;
```

### Query

```sql
SELECT *
FROM view_name;
```

### Drop

```sql
DROP VIEW view_name;
```

### Conditional creation

```sql
CREATE VIEW IF NOT EXISTS view_name AS
SELECT ...;
```

> Support for `IF NOT EXISTS` varies by database system.

---

# 23. Key Takeaways

> **A SQL view is a stored query that can be queried like a table.**

Remember:

```text
CREATE VIEW
      ↓
     AS
      ↓
SELECT ...
      ↓
    VIEW
      ↓
SELECT FROM VIEW
```

### The most important points

- A view encapsulates a SQL query.
- A view can be queried like a table.
- Views can contain joins, filters, calculations, and aggregations.
- Views simplify complex SQL.
- Views can be reused by multiple queries.
- Views can act as intermediate layers in multi-step analysis.
- Views can help with data abstraction and access control.
- A normal view generally does not physically store its result.
- Temporary views may exist only for a session.
- A regular view is usually persistent until dropped.
- `DROP VIEW` removes the view definition, not the underlying source data.
- Complex views may not be directly updatable.
- Database-specific behavior should always be checked.

---

# 24. Quick Revision

```text
VIEW
│
├── Stored SQL query
├── Acts like a table
├── Simplifies complex queries
├── Can combine multiple tables
├── Supports query reuse
├── Useful for multi-level analysis
├── Can provide data abstraction
├── Can support access control
│
├── CREATE VIEW
├── SELECT FROM VIEW
└── DROP VIEW
```

### Core syntax

```sql
CREATE VIEW view_name AS
SELECT
    ...
FROM
    ...
WHERE
    ...;
```

Then:

```sql
SELECT *
FROM view_name;
```

Finally:

```sql
DROP VIEW view_name;
```

---

# 25. One-Line Summary

**A SQL view is a reusable, virtual representation of a query that helps encapsulate complex joins, transformations, calculations, and filtering so that subsequent SQL queries become simpler and more maintainable.**

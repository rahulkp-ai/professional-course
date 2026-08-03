# SQL CROSS JOIN (Cartesian JOIN)

## Learning Objectives

After completing this lesson, you should be able to:

- Define a **Cartesian (CROSS) JOIN**.
- Explain how a CROSS JOIN works.
- Write the SQL syntax for a CROSS JOIN.
- Identify when a CROSS JOIN is useful.
- Understand its performance implications.

---

# What is a CROSS JOIN?

A **CROSS JOIN** (also called a **Cartesian JOIN**) combines **every row from the first table with every row from the second table**.

Unlike other joins:

- No matching condition
- No key required
- Every row is paired with every other row

---

# How CROSS JOIN Works

Suppose:

### Table A

| ID  |
| --- |
| A   |
| B   |

### Table B

| Number |
| ------ |
| 1      |
| 2      |
| 3      |

Result of CROSS JOIN:

| ID  | Number |
| --- | ------ |
| A   | 1      |
| A   | 2      |
| A   | 3      |
| B   | 1      |
| B   | 2      |
| B   | 3      |

Notice:

Each row in Table A is combined with **every row** in Table B.

---

# Formula

If:

- First table contains **X** rows
- Second table contains **Y** rows

Then:

```
Total Rows = X × Y
```

Example:

```
Customers = 10 rows
Products = 10 rows

Result = 10 × 10
       = 100 rows
```

---

# Larger Example

```
Suppliers = 29 rows
Products  = 77 rows
```

Result:

```
29 × 77 = 2233 rows
```

A relatively small increase in table size quickly produces thousands of rows.

---

# SQL Syntax

```sql
SELECT
    ProductName,
    UnitPrice,
    CompanyName
FROM Suppliers
CROSS JOIN Products;
```

---

## Explanation

```sql
SELECT
    ProductName,
    UnitPrice,
    CompanyName
```

Choose the columns you want.

---

```sql
FROM Suppliers
```

First table.

---

```sql
CROSS JOIN Products
```

Second table.

SQL combines **every supplier** with **every product**.

---

# Important Point

Unlike INNER JOIN or LEFT JOIN,

there is:

- No `ON` clause
- No matching key
- No relationship required

Example:

```sql
FROM Suppliers
CROSS JOIN Products
```

No condition is necessary.

---

# Why?

Because SQL is **not matching** rows.

It is simply generating **every possible combination**.

---

# Visualization

```
Table A

A
B

Table B

1
2
3
```

CROSS JOIN

```
A 1
A 2
A 3
B 1
B 2
B 3
```

Every row meets every other row.

---

# When Is CROSS JOIN Useful?

Although not frequently used, CROSS JOIN is helpful when generating all possible combinations.

Examples:

### Product Variations

Products

```
T-Shirt
Shoes
```

Colors

```
Red
Blue
Black
```

Result:

```
T-Shirt  Red
T-Shirt  Blue
T-Shirt  Black
Shoes    Red
Shoes    Blue
Shoes    Black
```

---

### Scheduling

Employees

```
Alice
Bob
```

Work Days

```
Monday
Tuesday
Wednesday
```

Generate every employee-day combination.

---

### Testing

Generate sample datasets by combining multiple tables.

---

### Matrix Generation

Create all combinations of:

- Categories
- Sizes
- Colors
- Regions
- Dates

---

# Advantages

- Very simple syntax

- No keys required

- Useful for generating every possible combination

- Helpful for testing and simulations

---

# Disadvantages

## 1. Computationally Expensive

The number of rows grows rapidly.

Example:

```
1000 × 1000

=

1,000,000 rows
```

Large databases can become slow.

---

## 2. High Memory Usage

More rows mean:

- More RAM
- More CPU
- Longer execution time

---

## 3. Can Produce Incorrect Results

Since nothing is matched,

many combinations may be meaningless.

Example:

```
Customer A
paired with
every product
```

This does **not** mean the customer actually purchased every product.

---

# CROSS JOIN vs INNER JOIN

| CROSS JOIN               | INNER JOIN                         |
| ------------------------ | ---------------------------------- |
| No matching condition    | Matches related rows               |
| No key required          | Uses keys                          |
| Every row with every row | Only matching rows                 |
| Result = X × Y           | Result depends on matching records |
| Rarely used              | Most commonly used                 |

---

# Key Characteristics

- Combines every row with every other row.
- Also called a **Cartesian Product**.
- Requires no relationship between tables.
- Does not use `ON`.
- Can generate extremely large result sets.
- Should be used carefully.

---

# Real-World Example

### Products

| Product |
| ------- |
| Laptop  |
| Mouse   |

### Colors

| Color  |
| ------ |
| Black  |
| Silver |

Result:

| Product | Color  |
| ------- | ------ |
| Laptop  | Black  |
| Laptop  | Silver |
| Mouse   | Black  |
| Mouse   | Silver |

Useful when generating all available product variants.

---

# Key Takeaways

- **CROSS JOIN** is also known as a **Cartesian JOIN**.
- Every row from the first table is combined with every row from the second table.
- Result size is **X × Y**.
- No keys or matching conditions are required.
- CROSS JOIN uses **no `ON` clause**.
- Mainly used for generating all possible combinations.
- Can become computationally expensive for large tables.
- Use CROSS JOIN only when every possible combination is required.

---

# Quick Revision

### Q1. What is another name for CROSS JOIN?

**Cartesian JOIN**

---

### Q2. Does CROSS JOIN require a key?

No

---

### Q3. Does CROSS JOIN use an `ON` clause?

No

---

### Q4. If Table A has 15 rows and Table B has 8 rows, how many rows are returned?

```
15 × 8 = 120 rows
```

---

### Q5. Why should CROSS JOIN be used carefully?

- Produces very large result sets.
- Computationally expensive.
- Can generate meaningless combinations if used incorrectly.

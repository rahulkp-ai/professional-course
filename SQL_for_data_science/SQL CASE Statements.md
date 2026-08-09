# SQL CASE Statements

## 1. Overview

A **`CASE` statement** in SQL is used to perform conditional logic, similar to an **`if-then-else`** statement in programming languages.

It is especially useful in **data manipulation and data analysis** because it allows us to:

- Transform variables
- Recode data
- Create new categorical or binary variables
- Group or **bin** numerical data
- Apply conditional calculations
- Prepare data for analysis and predictive modeling

`CASE` statements can be used with:

- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

---

## 2. Why Use CASE Statements?

Data scientists frequently need to transform raw data into a form that is easier to analyze.

Common use cases include:

### Variable transformation

Convert existing values into new categories.

Example:

```sql
Calgary → Calgary
Other cities → Other
```

### Binary variables

Convert a categorical variable into `0` and `1`.

Example:

```text
Calgary → 1
Other   → 0
```

This can be useful for machine-learning algorithms that cannot directly work with categorical variables.

### Binning

Convert continuous numerical values into groups.

Example:

```text
< 300,000       → Small
300,001–500,000 → Medium
≥ 500,001       → Large
```

---

# 3. CASE Statement Syntax

The general structure is:

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

### Components

| Component | Purpose                                         |
| --------- | ----------------------------------------------- |
| `CASE`    | Starts the conditional expression               |
| `WHEN`    | Specifies a condition                           |
| `THEN`    | Specifies the result when the condition is true |
| `ELSE`    | Specifies the result when no condition matches  |
| `END`     | Ends the `CASE` expression                      |

`ELSE` is optional.

If `ELSE` is omitted and no condition matches, SQL generally returns `NULL`.

---

# 4. Simple CASE Expression

A simple `CASE` compares a column against specific values.

### Syntax

```sql
CASE column_name
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE result3
END
```

---

## 5. Example: Reclassifying Cities

Suppose we want to classify employees based on their city.

We want:

```text
Calgary → Calgary
Everything else → Other
```

### Query

```sql
SELECT
    FirstName,
    LastName,
    EmployeeId,
    City,
    CASE City
        WHEN 'Calgary' THEN 'Calgary'
        ELSE 'Other'
    END AS Calgary
FROM Employee;
```

### Result

| City       | Calgary |
| ---------- | ------- |
| Calgary    | Calgary |
| Lethbridge | Other   |
| Calgary    | Calgary |
| Edmonton   | Other   |

The `CASE` expression creates a **new calculated column** called `Calgary`.

---

# 6. Creating a Binary Variable

The same technique can be used to create a binary variable.

Instead of:

```text
Calgary → Calgary
Other   → Other
```

we can create:

```text
Calgary → 1
Other   → 0
```

### Example

```sql
SELECT
    City,
    CASE City
        WHEN 'Calgary' THEN 1
        ELSE 0
    END AS IsCalgary
FROM Employee;
```

### Result

| City       | IsCalgary |
| ---------- | --------: |
| Calgary    |         1 |
| Lethbridge |         0 |
| Calgary    |         1 |
| Edmonton   |         0 |

This is useful when preparing categorical data for **machine-learning algorithms**.

> **Note:** Converting categories into multiple binary columns is related to **one-hot encoding**. In a real ML pipeline, the encoding is often handled by preprocessing tools rather than manually with SQL.

---

# 7. Searched CASE Expression

A `CASE` statement can also evaluate conditions such as:

- `<`
- `>`
- `<=`
- `>=`
- `=`
- `BETWEEN`
- Other Boolean expressions

### Syntax

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

This is called a **searched CASE expression**.

---

# 8. Example: Binning Track Sizes

Suppose a database contains tracks and their size in bytes.

We want to categorize tracks into:

- Small
- Medium
- Large
- Other

### Query

```sql
SELECT
    TrackId,
    Name,
    Bytes,
    CASE
        WHEN Bytes < 300000 THEN 'Small'
        WHEN Bytes >= 300001 AND Bytes < 500000 THEN 'Medium'
        WHEN Bytes >= 500001 THEN 'Large'
        ELSE 'Other'
    END AS TrackSize
FROM Track;
```

### Conceptual result

|  Bytes | TrackSize |
| -----: | --------- |
| 250000 | Small     |
| 350000 | Medium    |
| 450000 | Medium    |
| 600000 | Large     |

This technique is called **binning** or **bucketing**.

---

# 9. Binning / Categorizing Data

Binning converts numerical values into meaningful groups.

For example:

```text
Numerical value
       ↓
    CASE
       ↓
Categorical group
```

Example:

```text
0–299,999       → Small
300,000–499,999 → Medium
500,000+        → Large
```

Binning can be useful in:

- Exploratory Data Analysis
- Reporting
- Segmentation
- Forecasting
- Predictive modeling
- Customer classification

---

# 10. Using CASE with Calculated Fields

The `THEN` expression does **not** have to be a fixed word or number.

It can also reference another column.

For example:

```sql
CASE
    WHEN Period BETWEEN 1 AND 5 THEN NetSales
    ELSE 0
END
```

Here:

- If `Period` is between `1` and `5`, return `NetSales`.
- Otherwise, return `0`.

This allows `CASE` to perform **conditional calculations**.

---

# 11. CASE with Aggregation

`CASE` becomes particularly powerful when combined with aggregate functions such as:

- `SUM()`
- `COUNT()`
- `AVG()`
- `MIN()`
- `MAX()`

### Example

```sql
SELECT
    SUM(
        CASE
            WHEN Period BETWEEN 1 AND 5 THEN NetSales
            ELSE 0
        END
    ) AS Sales_Period_1_5
FROM Sales;
```

This calculates the total sales only for records where the period is between `1` and `5`.

This pattern is commonly used for **conditional aggregation**.

---

# 12. ELSE and NULL

`ELSE` is optional.

### With ELSE

```sql
CASE
    WHEN condition THEN 'Yes'
    ELSE 'No'
END
```

If nothing matches, SQL returns `'No'`.

### Without ELSE

```sql
CASE
    WHEN condition THEN 'Yes'
END
```

If nothing matches, the result is generally:

```text
NULL
```

Using `ELSE` can therefore make the output more predictable.

---

# 13. Simple vs Searched CASE

There are two important forms of `CASE`.

### Simple CASE

Compares one expression against values.

```sql
CASE City
    WHEN 'Calgary' THEN 'Calgary'
    WHEN 'Toronto' THEN 'Toronto'
    ELSE 'Other'
END
```

### Searched CASE

Evaluates independent Boolean conditions.

```sql
CASE
    WHEN Bytes < 300000 THEN 'Small'
    WHEN Bytes < 500000 THEN 'Medium'
    ELSE 'Large'
END
```

### Key Difference

| Type          | Logic                                       |
| ------------- | ------------------------------------------- |
| Simple CASE   | Compare one expression with specific values |
| Searched CASE | Evaluate conditions/Boolean expressions     |

---

# 14. Important Syntax Rules

### Rule 1 — Start with `CASE`

```sql
CASE
```

### Rule 2 — Add one or more `WHEN` conditions

```sql
WHEN condition
```

### Rule 3 — Define the result with `THEN`

```sql
THEN result
```

### Rule 4 — Optionally handle unmatched rows with `ELSE`

```sql
ELSE result
```

### Rule 5 — Always finish with `END`

```sql
END
```

### Rule 6 — Use an alias when creating a calculated column

```sql
END AS Category
```

---

# 15. CASE Statement Mental Model

Think of a `CASE` expression as:

```text
                CASE
                  │
                  ▼
             Is condition 1?
              /         \
            YES          NO
             │            │
             ▼            ▼
         Result 1    Is condition 2?
                         /      \
                       YES       NO
                        │         │
                        ▼         ▼
                    Result 2    ELSE
                                  │
                                  ▼
                               Result
```

The conditions are evaluated in order.

Once a matching `WHEN` condition is found, its corresponding `THEN` result is returned.

---

# 16. Common Data-Science Applications

`CASE` statements are especially useful for:

### 1. Feature Engineering

Creating new variables from existing data.

```sql
CASE
    WHEN Age >= 18 THEN 1
    ELSE 0
END AS IsAdult
```

### 2. Binning

```sql
CASE
    WHEN Income < 30000 THEN 'Low'
    WHEN Income < 70000 THEN 'Medium'
    ELSE 'High'
END AS IncomeGroup
```

### 3. Data Cleaning

```sql
CASE
    WHEN Gender IS NULL THEN 'Unknown'
    ELSE Gender
END AS CleanGender
```

### 4. Conditional Aggregation

```sql
SUM(
    CASE
        WHEN Status = 'Completed' THEN Amount
        ELSE 0
    END
)
```

### 5. Business Rules

```sql
CASE
    WHEN OrderAmount >= 10000 THEN 'Premium'
    WHEN OrderAmount >= 5000 THEN 'Standard'
    ELSE 'Basic'
END AS CustomerType
```

---

# 17. Key Takeaways

> **`CASE` is SQL's conditional logic mechanism, similar to `if-then-else` in programming.**

Remember the core structure:

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

### What CASE can do

- Transform values
- Recode categorical variables
- Create binary variables
- Create categories
- Bin numerical data
- Perform conditional calculations
- Support feature engineering
- Work with aggregate functions
- Be used in `SELECT`, `INSERT`, `UPDATE`, and `DELETE`

### Most important concepts

```text
CASE
 ↓
WHEN → condition
 ↓
THEN → result
 ↓
WHEN → another condition
 ↓
THEN → another result
 ↓
ELSE → fallback result
 ↓
END
```

---

# 18. Practice Examples

## Example 1 — Age Classification

```sql
SELECT
    Name,
    Age,
    CASE
        WHEN Age < 18 THEN 'Minor'
        WHEN Age < 60 THEN 'Adult'
        ELSE 'Senior'
    END AS AgeGroup
FROM Customers;
```

## Example 2 — Salary Classification

```sql
SELECT
    EmployeeName,
    Salary,
    CASE
        WHEN Salary < 30000 THEN 'Low'
        WHEN Salary < 70000 THEN 'Medium'
        ELSE 'High'
    END AS SalaryGroup
FROM Employees;
```

## Example 3 — Pass/Fail

```sql
SELECT
    StudentName,
    Marks,
    CASE
        WHEN Marks >= 40 THEN 'Pass'
        ELSE 'Fail'
    END AS Result
FROM Students;
```

## Example 4 — Conditional Revenue

```sql
SELECT
    SUM(
        CASE
            WHEN Status = 'Completed' THEN Revenue
            ELSE 0
        END
    ) AS CompletedRevenue
FROM Orders;
```

---

# 19. One-Line Summary

**SQL `CASE` statements allow you to apply conditional logic to transform, classify, categorize, bin, and calculate data directly inside SQL queries.**

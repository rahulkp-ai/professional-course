# SQL Data Profiling, Query Building, Testing & Troubleshooting

## Overview

After understanding the problem, business requirements, and data, the next step is to **profile the data and systematically build the SQL query**.

A strong SQL workflow is not:

```text
Write huge query
      ↓
Run it
      ↓
Hope the result is correct
```

Instead:

```text
Understand Problem
      ↓
Understand Data
      ↓
Profile Data
      ↓
Map Required Data Elements
      ↓
Build Query Incrementally
      ↓
Test Along the Way
      ↓
Troubleshoot
      ↓
Format & Document
      ↓
Review & Maintain
```

> **Core principle:** Start small, test frequently, and build complexity gradually.

---

# 1. Data Profiling

## What Is Data Profiling?

**Data profiling** is the process of examining a dataset to understand its characteristics, distributions, completeness, and quality.

It commonly includes:

- Descriptive statistics
- Missing-value analysis
- Data type inspection
- Value distributions
- Duplicate detection
- Range checks
- Outlier detection
- Category inspection
- Relationship validation

Data profiling should happen **before finalizing the data extraction used for analysis or modeling**.

---

# Why Profile Your Data?

Profiling helps you identify **data quality problems** before they affect your analysis.

For example:

```text
Column: customer_age

NULL values:       12%
Minimum:           -5
Maximum:           214
Average:           38.7
```

This immediately tells you that the column may contain:

- Missing values
- Invalid values
- Potential data-entry errors

Without profiling, these problems could silently enter your analysis or machine learning model.

---

# 2. Descriptive Statistics

Descriptive statistics help you understand the basic characteristics of numerical data.

Common statistics include:

```text
COUNT
MIN
MAX
AVG
SUM
```

Example:

```sql
SELECT
    COUNT(*) AS total_records,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price,
    AVG(price) AS average_price,
    SUM(price) AS total_sales
FROM sales;
```

This gives you a basic understanding of the `price` field.

---

# 3. Profiling Categorical Data

For categorical columns, inspect the possible values and their frequencies.

Example:

```sql
SELECT
    gender,
    COUNT(*) AS count
FROM customers
GROUP BY gender
ORDER BY count DESC;
```

This can reveal unexpected values such as:

```text
Male
Female
M
F
male
female
Unknown
NULL
```

These inconsistencies may need to be handled before analysis.

---

# 4. Profiling NULL Values

Always investigate missing values.

Example:

```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(customer_id) AS non_null_customer_ids,
    COUNT(*) - COUNT(customer_id) AS null_customer_ids
FROM customers;
```

You can also inspect a specific column:

```sql
SELECT
    COUNT(*) AS total_rows,
    SUM(
        CASE
            WHEN email IS NULL THEN 1
            ELSE 0
        END
    ) AS null_emails
FROM customers;
```

Understanding the amount and distribution of missing data is essential before using the data for analysis.

---

# 5. Map the Required Data Elements

Before writing a complex query, determine **exactly what data you need**.

Start with the question:

> What information is required to answer the problem?

Then identify:

- Required tables
- Required columns
- Relationships
- Joins
- Filters
- Calculations
- Aggregations

---

# Creating a Data Map

A useful approach is to create a simple diagram of the required data sources.

Example:

```text
customers
    |
    | customer_id
    ↓
orders
    |
    | order_id
    ↓
order_items
    |
    | product_id
    ↓
products
```

Then identify the fields required from each table:

```text
customers
├── customer_id
├── age
└── location

orders
├── order_id
├── customer_id
└── order_date

order_items
├── order_id
├── product_id
└── quantity

products
├── product_id
├── product_name
└── price
```

This creates a mental model of the query before you write it.

---

# 6. Start With SELECT and FROM

For data extraction, SQL queries generally begin with:

```sql
SELECT
FROM
```

Start by identifying:

```text
SELECT → What data do I need?
FROM   → Where does the data come from?
```

Example:

```sql
SELECT
    customer_id,
    name,
    email
FROM customers;
```

Then gradually introduce additional complexity.

---

# 7. Start Simple

One of the most important SQL development strategies is:

> **Start small.**

Instead of immediately writing:

```text
SELECT
FROM
JOIN
JOIN
JOIN
WHERE
CASE
GROUP BY
HAVING
ORDER BY
Subqueries
Window functions
```

start with one table.

### Step 1 — One Table

```sql
SELECT
    customer_id,
    name
FROM customers;
```

### Step 2 — Add Another Table

```sql
SELECT
    c.customer_id,
    c.name,
    o.order_id
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;
```

### Step 3 — Add Filters

```sql
SELECT
    c.customer_id,
    c.name,
    o.order_id
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_date >= '2026-01-01';
```

### Step 4 — Add Calculations

```sql
SELECT
    c.customer_id,
    c.name,
    SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    c.customer_id,
    c.name;
```

Build complexity **one step at a time**.

---

# 8. Subqueries: Start From the Inside

When using nested queries, build the **innermost query first**.

Example:

```sql
SELECT *
FROM (
    SELECT
        customer_id,
        AVG(amount) AS avg_purchase
    FROM orders
    GROUP BY customer_id
) AS customer_stats;
```

Build it in this order:

```text
1. Inner SELECT
       ↓
2. Verify its result
       ↓
3. Add outer query
       ↓
4. Verify again
```

This makes complex SQL much easier to understand and troubleshoot.

---

# 9. Test Along the Way

Do not wait until the entire query is finished before testing it.

Think of a complex query as a collection of **small building blocks**.

```text
Block 1
  ↓
Test
  ↓
Block 2
  ↓
Test
  ↓
Block 3
  ↓
Test
  ↓
Final Query
```

---

## Example

Suppose you need to calculate average selling price.

Start with:

```sql
SELECT
    AVG(selling_price) AS avg_selling_price
FROM sales;
```

Check:

- Does the result make sense?
- How many records are involved?
- Are there `NULL` values?
- Is the value within a reasonable range?

Then build on it.

---

# 10. Validate Intermediate Results

For every major step, ask:

### Row Count

```sql
SELECT COUNT(*)
FROM customers;
```

### Distinct Values

```sql
SELECT COUNT(DISTINCT customer_id)
FROM orders;
```

### Sample Records

```sql
SELECT *
FROM orders
LIMIT 10;
```

### Distribution

```sql
SELECT
    status,
    COUNT(*) AS count
FROM orders
GROUP BY status;
```

These checks help confirm that each stage is producing expected results.

---

# 11. Correct Results vs. Expected Results

A query can execute successfully without producing the correct result.

This is a critical distinction:

```text
SQL Syntax Correct
        ≠
Analysis Correct
```

For example, this query may execute perfectly:

```sql
SELECT COUNT(*)
FROM orders;
```

But if the business question requires counting **completed orders only**, the query may be logically incorrect.

The correct version might be:

```sql
SELECT COUNT(*)
FROM orders
WHERE status = 'completed';
```

> **The database checking your syntax does not mean the analysis is correct.**

---

# 12. SQL Troubleshooting

When a query does not produce the expected result, **do not immediately rewrite the entire query**.

Instead:

> **Start small and rebuild the query gradually.**

---

## Troubleshooting Strategy

### Step 1 — Test the Base Table

```sql
SELECT *
FROM customers
LIMIT 10;
```

Confirm that the expected data exists.

---

### Step 2 — Test the Required Columns

```sql
SELECT
    customer_id,
    name
FROM customers
LIMIT 10;
```

---

### Step 3 — Test the Join

```sql
SELECT
    c.customer_id,
    o.order_id
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
LIMIT 10;
```

Check whether the relationship behaves as expected.

---

### Step 4 — Add Filters

```sql
SELECT
    c.customer_id,
    o.order_id
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.status = 'completed';
```

Check the result again.

---

### Step 5 — Add Calculations

Only after the previous stages work correctly should you add:

- Aggregations
- `CASE`
- Subqueries
- Window functions
- Additional joins
- Complex filters

---

# 13. Common SQL Troubleshooting Checklist

When results look wrong, investigate:

### Data

- Does the required data actually exist?
- Are there `NULL` values?
- Are there duplicates?
- Are the values correct?
- Are the data types correct?

### JOINs

- Is the join key correct?
- Is the relationship correct?
- Is the join type appropriate?
- Is the join creating duplicate rows?
- Are records being unintentionally removed?

### WHERE

- Is the filter too restrictive?
- Is the filter excluding valid records?
- Are `NULL` values affecting the condition?

### GROUP BY

- Are you grouping at the correct level?
- Are you accidentally aggregating multiple records together?

### Calculations

- Are you using the correct columns?
- Is the formula correct?
- Are `NULL` values affecting the calculation?

### Dates

- Is the date range correct?
- Are timestamps involved?
- Are boundary dates handled correctly?

---

# 14. Keep SQL Code Clean

Once the query works, make sure it is **readable and maintainable**.

Good SQL formatting communicates professionalism and makes future debugging easier.

Instead of:

```sql
SELECT c.customer_id,c.name,o.order_id FROM customers c JOIN orders o ON c.customer_id=o.customer_id WHERE o.status='completed';
```

prefer:

```sql
SELECT
    c.customer_id,
    c.name,
    o.order_id
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.status = 'completed';
```

---

# 15. Use Meaningful Formatting

Good formatting includes:

- One selected column per line
- Consistent indentation
- Clear aliases
- Proper spacing
- Logical clause ordering
- Readable joins
- Strategic comments

Example:

```sql
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.status = 'completed'
GROUP BY
    c.customer_id,
    c.name
ORDER BY
    total_spent DESC;
```

---

# 16. Comment Strategically

Comments should explain **why** something is being done when the reason is not obvious.

Good:

```sql
-- Exclude test accounts from customer analysis
WHERE c.account_type != 'test'
```

Less useful:

```sql
-- Select customer ID
SELECT customer_id
```

The SQL itself already explains what the second comment says.

> **Comments should provide context, not repeat the code.**

---

# 17. Query Maintenance

A query that worked previously may not remain correct forever.

Business requirements and data can change.

When reusing an old query, ask:

### Has the data changed?

- New tables?
- Changed schema?
- New columns?
- Changed data types?
- New categories?

### Have the business rules changed?

- New inclusion criteria?
- New exclusions?
- Changed definitions?

### Have the dates changed?

- Analysis period?
- Reporting period?
- Prediction window?

### Has the meaning of the data changed?

A column may still exist but have a different interpretation.

---

# 18. Be Careful With Old Queries

Never blindly reuse an old SQL query.

Before using it, verify:

```text
Schema
Data
Business Rules
Filters
Dates
Joins
Calculations
Expected Output
```

A query that was correct six months ago may produce incorrect results today.

---

# 19. End-to-End SQL Problem-Solving Framework

The complete workflow can now be summarized as:

```text
┌──────────────────────────────┐
│ 1. Understand the Problem    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 2. Understand the Business   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 3. Understand the Data       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 4. Profile the Data          │
│    • NULLs                   │
│    • Duplicates              │
│    • Distributions           │
│    • Data Quality            │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 5. Map Data Elements         │
│    • Tables                  │
│    • Columns                 │
│    • Relationships            │
│    • Joins                   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 6. Start With Simple SQL     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 7. Test Along the Way        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 8. Add Complexity Gradually  │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 9. Troubleshoot              │
│    • Start Small              │
│    • Rebuild Incrementally    │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 10. Format & Document        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 11. Review & Validate        │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ 12. Maintain Over Time        │
└──────────────────────────────┘
```

---

# Key Takeaways

1. **Profile your data before finalizing your extraction.**
2. Use descriptive statistics to understand the data.
3. Check for `NULL` values, duplicates, unexpected values, and data-quality issues.
4. Map the required tables, columns, relationships, and joins before writing complex SQL.
5. Start with `SELECT` and `FROM`.
6. **Start simple and gradually add complexity.**
7. Build subqueries from the innermost query outward.
8. **Test every major step instead of waiting until the end.**
9. A query that runs successfully is not necessarily logically correct.
10. When troubleshooting, start with the simplest working query and rebuild it incrementally.
11. Keep SQL formatted, readable, and strategically commented.
12. Review old queries before reusing them.
13. Always verify whether the **data, schema, business rules, and date requirements have changed**.

---

# Golden Rules

```text
Understand → Profile → Map → Build → Test → Troubleshoot → Clean → Review
```

### The most important habits:

> **Start small.**

> **Test along the way.**

> **Never confuse successful execution with correct analysis.**

> **Clean code is maintainable code.**

> **Understand the data before trusting the result.**

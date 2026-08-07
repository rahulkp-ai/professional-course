# SQL Date and Time Functions (SQLite)

## Overview

Dates and times are among the most commonly used data types in SQL. They are essential for reporting, filtering, time-series analysis, clustering, and trend analysis. However, they are also one of the most challenging data types because they can be stored in many different formats.

SQLite provides several built-in functions to manipulate date and time values efficiently.

---

# Learning Objectives

After studying this topic, you should be able to:

- Understand why date and time data is difficult to work with.
- Recognize different date and time formats.
- Explain the five built-in SQLite date and time functions.
- Understand the role of **time strings** and **modifiers**.
- Extract and manipulate date and time information.

---

# Why Date and Time Are Important

Date and time values are used for:

- Sales analysis
- Time-series forecasting
- Customer behavior analysis
- Clustering data by time
- Trend analysis
- Reporting
- Scheduling

Since dates can appear in different formats, they often require cleaning and transformation before analysis.

---

# Challenges of Working with Dates

Dates can be stored in many formats, such as:

```
2024-08-01
08/01/2024
1 Aug 2024
August 1, 2024
Thu, Aug 1, 2024
2024-08-01 14:30:45
2024-08-01T14:30:45Z
Julian Day Number
```

Because every database system supports different date formats, you should always understand how your database stores dates before writing queries.

---

# SQLite Date Storage

SQLite does **not** have a dedicated DATE data type.

Instead, dates can be stored as:

- TEXT
- INTEGER (Unix Timestamp)
- REAL (Julian Day Number)

SQLite converts these internally using its built-in date functions.

---

# Date Only vs Date-Time

## Date Only

```
2024-08-01
```

Simple to query:

```sql
WHERE PurchaseDate = '2024-08-01'
```

---

## Date with Time

```
2024-08-01 14:25:36
```

This query **will not match**:

```sql
WHERE PurchaseDate = '2024-08-01'
```

because the stored value contains hours, minutes, and seconds.

Instead, you must extract the date portion.

---

# SQLite Date and Time Functions

SQLite provides **five** built-in date and time functions.

| Function      | Purpose                                   |
| ------------- | ----------------------------------------- |
| `DATE()`      | Returns only the date                     |
| `TIME()`      | Returns only the time                     |
| `DATETIME()`  | Returns date and time together            |
| `JULIANDAY()` | Returns the Julian day number             |
| `STRFTIME()`  | Formats dates and extracts specific parts |

---

# 1. DATE()

Returns only the date.

## Syntax

```sql
DATE(time_string, modifier)
```

Example

```sql
SELECT DATE('2024-08-01 15:30:45');
```

Output

```
2024-08-01
```

---

# 2. TIME()

Returns only the time.

Example

```sql
SELECT TIME('2024-08-01 15:30:45');
```

Output

```
15:30:45
```

---

# 3. DATETIME()

Returns both date and time.

Example

```sql
SELECT DATETIME('2024-08-01');
```

Output

```
2024-08-01 00:00:00
```

---

# 4. JULIANDAY()

Returns the Julian Day Number.

A Julian Day represents the number of days since a fixed historical reference date.

Example

```sql
SELECT JULIANDAY('2024-08-01');
```

Output

```
2460523.5
```

Useful for:

- Calculating date differences
- Scientific calculations
- Astronomy

---

# 5. STRFTIME()

The most flexible date function.

It formats dates and extracts individual components.

## Syntax

```sql
STRFTIME(format, time_string, modifier)
```

Example

```sql
SELECT STRFTIME('%Y', '2024-08-01');
```

Output

```
2024
```

---

# Common STRFTIME Format Codes

| Code | Meaning        | Example |
| ---- | -------------- | ------- |
| `%Y` | Year           | 2024    |
| `%m` | Month          | 08      |
| `%d` | Day            | 01      |
| `%H` | Hour (24-hour) | 15      |
| `%M` | Minute         | 30      |
| `%S` | Second         | 45      |
| `%w` | Day of week    | 0–6     |
| `%j` | Day of year    | 001–366 |

---

# Time Strings

Every SQLite date function accepts a **time string**.

Examples:

```
2024-08-01

2024-08-01 15:30

2024-08-01 15:30:45

now

2451545.0
```

The time string specifies the date or time you want to manipulate.

---

# Modifiers

A modifier changes the original date or time.

Example

```sql
SELECT DATE('2024-08-01','+7 days');
```

Output

```
2024-08-08
```

---

## Common Modifiers

| Modifier         | Description                |
| ---------------- | -------------------------- |
| `+1 day`         | Add one day                |
| `-1 day`         | Subtract one day           |
| `+7 days`        | Add seven days             |
| `+1 month`       | Add one month              |
| `+1 year`        | Add one year               |
| `start of month` | Move to first day of month |
| `start of year`  | Move to first day of year  |
| `weekday N`      | Move to next weekday       |

---

# Multiple Modifiers

You can chain multiple modifiers.

```sql
SELECT DATE(
    '2024-08-01',
    '+1 month',
    '-5 days'
);
```

SQLite applies modifiers **from left to right**.

Order matters.

Example:

```
Original Date

↓

+1 Month

↓

-5 Days

↓

Final Result
```

---

# Extracting Date Components

Extract only the year

```sql
SELECT STRFTIME('%Y', OrderDate)
FROM Orders;
```

---

Extract month

```sql
SELECT STRFTIME('%m', OrderDate)
FROM Orders;
```

---

Extract day

```sql
SELECT STRFTIME('%d', OrderDate)
FROM Orders;
```

---

Extract hour

```sql
SELECT STRFTIME('%H', OrderDate)
FROM Orders;
```

---

# Real-World Examples

## Find today's orders

```sql
SELECT *
FROM Orders
WHERE DATE(OrderDate) = DATE('now');
```

---

## Orders this year

```sql
SELECT *
FROM Orders
WHERE STRFTIME('%Y', OrderDate) = '2026';
```

---

## Calculate tomorrow's date

```sql
SELECT DATE('now', '+1 day');
```

---

## Last seven days

```sql
SELECT DATE('now', '-7 days');
```

---

## First day of current month

```sql
SELECT DATE('now', 'start of month');
```

---

# Why Date-Time Queries Sometimes Fail

Suppose the database stores:

```
2024-08-01 13:45:26
```

This query:

```sql
WHERE PurchaseDate = '2024-08-01'
```

returns **no rows** because the stored value includes the time.

Correct approach:

```sql
WHERE DATE(PurchaseDate) = '2024-08-01'
```

---

# Best Practices

- Always understand how dates are stored.
- Convert timestamps to dates when only the date matters.
- Use `STRFTIME()` to extract components.
- Use modifiers for date arithmetic.
- Be careful with modifier order.

---

# Summary Table

| Function      | Purpose                                |
| ------------- | -------------------------------------- |
| `DATE()`      | Extract date                           |
| `TIME()`      | Extract time                           |
| `DATETIME()`  | Date and time                          |
| `JULIANDAY()` | Julian day number                      |
| `STRFTIME()`  | Format or extract date/time components |

---

# Interview Questions

### Q1. Why are date and time values difficult to work with?

**Answer:**  
Because they can be stored in many different formats and may include optional time, timezone, or timestamp information.

---

### Q2. Name the five SQLite date and time functions.

- `DATE()`
- `TIME()`
- `DATETIME()`
- `JULIANDAY()`
- `STRFTIME()`

---

### Q3. What is a time string?

**Answer:**  
A time string is the input date or time value passed to SQLite date functions.

---

### Q4. What is a modifier?

**Answer:**  
A modifier transforms a date or time value by adding, subtracting, or adjusting it (for example, `+7 days` or `start of month`).

---

### Q5. Why does the order of modifiers matter?

**Answer:**  
SQLite applies modifiers from **left to right**, so changing the order can produce different results.

---

### Q6. Which SQLite function is the most flexible?

**Answer:**  
`STRFTIME()` because it can format dates and extract specific components such as year, month, day, hour, minute, and second.

---

# Key Takeaways

- Date and time data are essential but often complex due to multiple storage formats.
- SQLite provides **five built-in functions** for handling dates and times.
- Always understand the format of your stored date before querying it.
- Use **time strings** as input and **modifiers** to transform dates.
- SQLite applies modifiers **from left to right**.
- `STRFTIME()` is the most powerful function for formatting and extracting date/time components.
- When comparing timestamps, extract the **date portion** if the time component is not important.

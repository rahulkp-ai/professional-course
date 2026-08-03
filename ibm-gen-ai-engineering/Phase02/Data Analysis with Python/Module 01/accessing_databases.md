# Accessing Databases with Python

---

# Introduction

Databases are used to store, organize, and manage large amounts of data efficiently.

Python can connect to databases, execute SQL queries, retrieve results, and perform data analysis on the retrieved data. This allows analysts and data scientists to combine SQL's data retrieval capabilities with Python's analytical power. :contentReference[oaicite:0]{index=0}

---

# Why Use Databases?

Advantages:

- Store large datasets efficiently
- Fast querying and retrieval
- Data consistency
- Multi-user access
- Security and backup support

Examples:

- Customer databases
- Banking systems
- E-commerce platforms
- Healthcare systems
- Recommendation systems

---

# Python and Databases

Python communicates with databases through database APIs (Application Programming Interfaces).

Common databases:

| Database   | Python Library         |
| ---------- | ---------------------- |
| SQLite     | sqlite3                |
| MySQL      | mysql-connector-python |
| PostgreSQL | psycopg2               |
| IBM Db2    | ibm_db                 |
| SQL Server | pyodbc                 |

---

# DB-API (Database API)

DB-API is a standard interface that Python uses to communicate with relational databases. :contentReference[oaicite:1]{index=1}

General workflow:

```text
Connect
   ↓
Create Cursor
   ↓
Execute SQL Query
   ↓
Fetch Results
   ↓
Close Connection
```

---

# Connecting to SQLite Database

SQLite comes built into Python.

Import Library:

```python
import sqlite3
```

Create Connection:

```python
conn = sqlite3.connect("example.db")
```

This creates:

```text
example.db
```

if it does not already exist.

---

# Creating a Cursor

A cursor allows Python to execute SQL statements.

```python
cursor = conn.cursor()
```

Think of the cursor as a bridge between Python and the database.

---

# Creating a Table

SQL command:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    AGE INTEGER
)
""")
```

Commit changes:

```python
conn.commit()
```

---

# Inserting Data

Insert a record:

```python
cursor.execute("""
INSERT INTO STUDENTS
VALUES (1,'John',21)
""")
```

Save changes:

```python
conn.commit()
```

---

# Querying Data

Retrieve data:

```python
cursor.execute("SELECT * FROM STUDENTS")
```

Fetch all rows:

```python
rows = cursor.fetchall()

print(rows)
```

Output:

```python
[(1,'John',21)]
```

---

# Fetch Methods

### fetchone()

Returns one row.

```python
cursor.fetchone()
```

Example:

```python
(1,'John',21)
```

---

### fetchmany()

Returns multiple rows.

```python
cursor.fetchmany(5)
```

---

### fetchall()

Returns all rows.

```python
cursor.fetchall()
```

---

# Closing Database Connection

Always close the connection after work is complete.

```python
conn.close()
```

Good practice:

```python
cursor.close()
conn.close()
```

---

# Complete SQLite Example

```python
import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
ID INTEGER,
NAME TEXT,
AGE INTEGER
)
""")

cursor.execute("""
INSERT INTO STUDENTS
VALUES(1,'John',21)
""")

conn.commit()

cursor.execute("SELECT * FROM STUDENTS")

rows = cursor.fetchall()

print(rows)

conn.close()
```

---

# Using Pandas with Databases

Pandas can directly read SQL query results.

Import libraries:

```python
import pandas as pd
import sqlite3
```

Connect:

```python
conn = sqlite3.connect("students.db")
```

Read SQL:

```python
df = pd.read_sql_query(
    "SELECT * FROM STUDENTS",
    conn
)
```

Display Data:

```python
print(df)
```

Output:

```text
ID  NAME   AGE
1   John   21
```

This is extremely useful for data analysis workflows. :contentReference[oaicite:2]{index=2}

---

# SQL Magic in Jupyter Notebook

SQL Magic allows SQL queries to be executed directly inside Jupyter notebooks. It is covered in the IBM course module on database access with Python.

Load Extension:

```python
%load_ext sql
```

Connect Database:

```python
%sql sqlite:///students.db
```

Run Query:

```sql
%%sql

SELECT *
FROM STUDENTS
```

Benefits:

- Easier SQL testing
- Interactive querying
- Better notebook workflow

---

# IBM Db2 Connection

IBM Db2 uses the `ibm_db` package.

Import:

```python
import ibm_db
```

Connection Example:

```python
conn = ibm_db.connect(
    database,
    username,
    password
)
```

Used in enterprise environments and cloud database systems. :contentReference[oaicite:4]{index=4}

---

# Data Analysis Workflow with Databases

```text
Database
    ↓
SQL Query
    ↓
Python Connection
    ↓
Pandas DataFrame
    ↓
Data Cleaning
    ↓
Visualization
    ↓
Machine Learning
```

Example:

```python
query = """
SELECT price,
       horsepower
FROM cars
"""

df = pd.read_sql_query(query, conn)
```

Now:

```python
df.describe()
df.head()
df.plot()
```

can be performed directly.

---

# Advantages of Using Databases with Python

### Scalability

Handles millions of records.

### Automation

Automate repetitive SQL operations.

### Data Analysis

Combine SQL with Pandas.

### Machine Learning

Feed database data directly into ML models.

### Visualization

Use Matplotlib and Seaborn on queried data.

---

# Important Concepts

| Concept    | Description                       |
| ---------- | --------------------------------- |
| Connection | Link to database                  |
| Cursor     | Executes SQL commands             |
| Execute    | Runs SQL statement                |
| Commit     | Saves changes                     |
| Fetch      | Retrieves query results           |
| Close      | Terminates connection             |
| SQL Magic  | Run SQL inside Jupyter            |
| Pandas SQL | Load query results into DataFrame |

---

# Typical Interview Questions

### What is DB-API?

A standard Python interface for interacting with databases.

### What is a Cursor?

An object used to execute SQL commands.

### Difference between fetchone() and fetchall()?

| Method     | Purpose          |
| ---------- | ---------------- |
| fetchone() | Returns one row  |
| fetchall() | Returns all rows |

### Why use Pandas with SQL?

To convert SQL query results into DataFrames for analysis.

---

# Key Takeaways

✅ Python connects to databases using DB-API.

✅ SQLite is built into Python via `sqlite3`.

✅ Main steps:

```text
Connect
→ Cursor
→ Execute
→ Fetch
→ Close
```

✅ Important methods:

```python
connect()
cursor()
execute()
commit()
fetchone()
fetchall()
close()
```

✅ Pandas can directly read SQL query results.

✅ SQL Magic enables SQL execution inside Jupyter notebooks.

✅ Databases + Python + Pandas form a core workflow for data analysts, data engineers, and AI/ML engineers. :contentReference[oaicite:5]{index=5}

---

# Exam Quick Revision

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("db.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM table")

rows = cursor.fetchall()

df = pd.read_sql_query(
    "SELECT * FROM table",
    conn
)

conn.close()
```

Remember:

```text
Database
    ↓
SQL Query
    ↓
Python
    ↓
Pandas DataFrame
    ↓
Analysis
```

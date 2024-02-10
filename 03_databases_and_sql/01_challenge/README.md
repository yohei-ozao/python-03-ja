# Challenge 1: **SQL & Python**

## **Background & Objectives**

This challenge aims to integrate SQL querying within Python code, enhancing your skills in database interaction through programming.

## **Data**

We'll use the **`chinook.db`** database for this challenge. 

We'll utilize Python's built-in library **`sqlite3`** to connect and interact with the **`chinook.db`** database.

To connect to the **`chinook.db`** database from IPython or a Python script, run the following code in your challenge directory:

```python
import sqlite3

conn = sqlite3.connect('data/chinook.db')
db = conn.cursor()
db.execute("YOUR SQL QUERY")
rows = db.fetchall()
print(rows)  # => list (rows) of tuples (columns)
```

First, use DBeaver to connect to the **`data/chinook.db`** database and build/test your SQL queries. Then, integrate these queries into your Python code.

Each function in your **`queries.py`** file should take a **`db`** cursor connected to the database. Here's a template for your functions:

```python
def your_function(db):
    query = ""
    db.execute(query)
    results = db.fetchall()
    print(results)  # Inspect the results
    return ?
```

When required, don’t forget to call items from a list, tuple or other structure in order to correctly returned the desired data. If an integer is expected, don’t return a different data type!

### **Number of Artists**

How many artists are in the database?

### **List of Artists**

What is the list of all artist names sorted alphabetically? Return a list of names (strings).

### **List of Albums About “Love”**

Which albums have the word “love” in their title, sorted alphabetically? Return a list of album titles.

### **Number of Tracks Longer Than…**

How many tracks are longer than a duration specified by the user?

### **List of Genres with Most Tracks**

Which genres have the most tracks? Return a list of genre names sorted by the number of tracks, descending.

## **Tips**

👉 Use parameter substitution to safeguard your SQL queries against SQL injection.

👉 For long SQL queries, use triple quotes in Python for multi-line strings:

```python
query = """
    SELECT name
    FROM artists
    WHERE name LIKE "%love%"
    ORDER BY name
"""
rows = db.execute(query)
# [...]
```
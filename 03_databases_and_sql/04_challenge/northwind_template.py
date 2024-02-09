# SQL & Python with Northwind Database

import sqlite3

# Connect to the northwind.db database
conn = sqlite3.connect('../data/northwind.db')
db = conn.cursor()

# List of Suppliers
def list_of_suppliers(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Small Orders
def count_small_orders(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    result = db.fetchone()
    return result[0] if result else 0

# First Ten Products
def first_ten_products(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Products with a Keyword
def products_with_keyword(db, keyword):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Top 5 Categories by Product Count
def top_five_categories_by_product_count(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Example function calls (comment these out before distributing)
# print("List of Suppliers:")
# print(list_of_suppliers(db))

# print("\nFirst Ten Products:")
# print(first_ten_products(db))

# print("\nProducts with a Keyword 'Chai':")
# print(products_with_keyword(db, 'Chai'))

# print("\nTop 5 Categories by Product Count:")
# print(top_five_categories_by_product_count(db))

# Don't forget to close the database connection at the end of your script
conn.close()
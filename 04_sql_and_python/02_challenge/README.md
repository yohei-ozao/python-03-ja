We will work with the northwind.db database, which you should have set up in your environment.

Specs
Open the file queries.py to answer the following questions. You can explore the database using tools like DBeaver to better understand its structure.

There are three methods to implement, focusing on the Orders, OrderDetails, and Products tables:

Implement query_orders to retrieve all orders sorted by OrderID in ascending order.

Implement get_orders_range to fetch all orders placed within a specific date range, sorted by OrderDate in ascending order. This method should take two dates as parameters (date_from and date_to) and include orders on date_to but exclude those on date_from.

Implement get_order_details to obtain details of each order, including the product name and quantity ordered. The results should be sorted by OrderID in ascending order.

👉 Reminder: Each method accepts a db argument, a database connection, where you can use the execute method. This connection is provided by the test framework, so you don't need to establish it yourself. Your methods should follow this structure:

def the_method(db):
    results = db.execute("YOUR SQL QUERY")
    results = results.fetchall()
    # results are in a list of rows, each row is a list of column values
    print(results) # Always inspect the results to ensure correctness!
    # Then return the appropriate value
    return ?

Hint: You can use F-strings to insert arguments into strings. This may help you insert your data arguments into your SQL query. 
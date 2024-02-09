# queries.py

import sqlite3

def query_orders(db):
    """
    Implement this method to retrieve all orders from the Orders table,
    sorted by OrderID in ascending order.
    
    Args:
        db: Database connection object.

    Returns:
        List of tuples representing the orders.
    """
    query = ""  # TODO: Write SQL query here
    results = db.execute(query)
    results = results.fetchall()
    return results


def get_orders_range(db, date_from, date_to):
    """
    Implement this method to get all orders placed between date_from and date_to,
    sorted by OrderDate in ascending order. Include orders on date_to, but exclude
    those on date_from.
    
    Args:
        db: Database connection object.
        date_from: Starting date (exclusive).
        date_to: Ending date (inclusive).

    Returns:
        List of tuples representing the orders.
    """
    query = ""  # TODO: Write SQL query here
    results = db.execute(query)
    results = results.fetchall()
    return results


def get_order_details(db):
    """
    Implement this method to obtain details of each order, including the product name
    and quantity ordered, sorted by OrderID in ascending order.
    
    Args:
        db: Database connection object.

    Returns:
        List of tuples representing the order details.
    """
    query = ""  # TODO: Write SQL query here
    results = db.execute(query)
    results = results.fetchall()
    return results

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('northwind.db')

    # Test the query_orders function
    print("All Orders:")
    # TODO: Adjust the print format as needed
    for order in query_orders(conn):
        print(order)

    # Test the get_orders_range function
    print("\nOrders in a specified date range:")
    # TODO: Replace with actual dates from the database
    for order in get_orders_range(conn, '1996-07-04', '1996-07-10'):
        print(order)

    # Test the get_order_details function
    print("\nOrder Details:")
    # TODO: Adjust the print format as needed
    for detail in get_order_details(conn):
        print(detail)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()

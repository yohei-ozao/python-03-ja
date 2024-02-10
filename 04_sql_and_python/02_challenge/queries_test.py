import unittest
import sqlite3
from queries import query_orders, get_orders_range, get_order_details

class TestDatabaseQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Establish a database connection for all tests
        cls.conn = sqlite3.connect('../data/northwind.db')

    @classmethod
    def tearDownClass(cls):
        # Close the database connection after all tests
        cls.conn.close()

    def test_query_orders(self):
        # Test query_orders function
        results = query_orders(self.conn)
        self.assertIsNotNone(results, "Result should not be None")
        self.assertTrue(len(results) > 0, "Result set should not be empty")

    def test_get_orders_range(self):
        # Test get_orders_range function
        date_from = '1996-07-04'
        date_to = '1996-07-10'
        results = get_orders_range(self.conn, date_from, date_to)
        self.assertIsNotNone(results, "Result should not be None")
        self.assertTrue(len(results) > 0, "Result set should not be empty")
        for order in results:
            self.assertTrue(date_from < order[3] and order[3] <= date_to, "OrderDate should be within the specified range")

    def test_get_order_details(self):
        # Test get_order_details function
        results = get_order_details(self.conn)
        self.assertIsNotNone(results, "Result should not be None")
        self.assertTrue(len(results) > 0, "Result set should not be empty")
        # Check for 3 columns (OrderID, ProductName, Quantity)
        self.assertTrue(all(len(detail) == 3 for detail in results), "Each detail should have 3 columns")
        # Check if Quantity is an integer
        for detail in results:
            self.assertIsInstance(detail[2], int, "Quantity should be an integer")


if __name__ == '__main__':
    unittest.main()

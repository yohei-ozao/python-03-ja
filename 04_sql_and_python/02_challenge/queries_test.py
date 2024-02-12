import unittest
import sqlite3
from queries import query_orders, get_orders_range, get_order_details

class TestDatabaseQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # すべてのテスト用にデータベースに接続する
        cls.conn = sqlite3.connect('../data/northwind.db')

    @classmethod
    def tearDownClass(cls):
        # すべてのテストが完了した後、データベース接続を閉じる
        cls.conn.close()

    def test_query_orders(self):
        # query_orders関数のテスト
        results = query_orders(self.conn)
        self.assertIsNotNone(results, "Result should not be None")
        self.assertTrue(len(results) > 0, "Result set should not be empty")

    def test_get_orders_range(self):
        # get_orders_range関数のテスト
        date_from = '1996-07-04'
        date_to = '1996-07-10'
        results = get_orders_range(self.conn, date_from, date_to)
        self.assertIsNotNone(results, "Result should not be None")
        self.assertTrue(len(results) > 0, "Result set should not be empty")
        for order in results:
            self.assertTrue(date_from < order[3] and order[3] <= date_to, "OrderDate should be within the specified range")

    def test_get_order_details(self):
        # get_order_details関数のテスト
        results = get_order_details(self.conn)
        self.assertIsNotNone(results, "Result should not be None")
        self.assertTrue(len(results) > 0, "Result set should not be empty")
        # 3つの列 (OrderID、ProductName、Quantity) を確認
        self.assertTrue(all(len(detail) == 3 for detail in results), "Each detail should have 3 columns")
        # Quantityが整数であることを確認
        for detail in results:
            self.assertIsInstance(detail[2], int, "Quantity should be an integer")


if __name__ == '__main__':
    unittest.main()

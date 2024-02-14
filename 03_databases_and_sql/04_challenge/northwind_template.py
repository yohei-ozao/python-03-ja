# SQLとPython＋Northwindデータベース

import sqlite3

# northwind.dbデータベースに接続
conn = sqlite3.connect('../data/northwind.db')
db = conn.cursor()

# サプライヤーのリスト
def list_of_suppliers(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 少量の注文
def count_small_orders(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    result = db.fetchone()
    return result[0] if result else 0

# 最初の10商品
def first_ten_products(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# キーワードを含む商品
def products_with_keyword(db, keyword):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 商品数が多いトップ5のカテゴリー
def top_five_categories_by_product_count(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 関数呼び出しの例 (提出する前にこれらをコメントアウトしてください)
# print("List of Suppliers:")
# print(list_of_suppliers(db))

# print("\nFirst Ten Products:")
# print(first_ten_products(db))

# print("\nProducts with a Keyword 'Chai':")
# print(products_with_keyword(db, 'Chai'))

# print("\nTop 5 Categories by Product Count:")
# print(top_five_categories_by_product_count(db))

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()

# SQLとPython＋Chinookデータベース: 楽曲の再生時間に応じたバケット分類

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# 楽曲の再生時間に応じたバケット
def track_length_buckets(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()


# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# アーティストの数
def number_of_artists(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# アーティストのリスト
def list_of_artists(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()

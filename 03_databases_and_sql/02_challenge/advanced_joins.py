
# SQLとPython＋Chinookデータベース: 高度な結合

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# 楽曲の詳細
def detailed_tracks(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# 未購入の楽曲
def tracks_not_bought(db):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# ジャンルの統計情報
def genre_stats(db, genre_name):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# ジャンル別のトップ5アーティスト
def top_five_artists_by_genre(db, genre_name):
    query = ""  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    return results

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()


# SQLとPython＋Chinookデータベース

import sqlite3

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# アーティストの数
def number_of_artists(db):
    query = "SELECT COUNT(*) FROM artists"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    results = results[0][0]
    print(results)
    return results

# アーティストのリスト
def list_of_artists(db):
    query = "SELECT * FROM artists"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    results = list(results[0])
    return results

# 「愛」をテーマにしたアルバムのリスト
def albums_about_love(db):
    query = "SELECT Title FROM albums WHERE LOWER(Title) LIKE '%love%'"  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    results = [row[0] for row in results]
    print(results)
    return results

# 指定された再生時間よりも長い楽曲数
def tracks_longer_than(db, duration):
    query = "SELECT COUNT(*) FROM tracks WHERE Milliseconds > ?"  # ここにSQLクエリを書いてください
    db.execute(query, (duration,))
    results = db.fetchall()
    results = results[0][0]
    return results

# 最も楽曲数が多いジャンルのリスト
def genres_with_most_tracks(db):
    query = """
    SELECT genres.Name, COUNT(tracks.TrackId) as TrackCount
    FROM genres
    JOIN tracks ON genres.GenreId = tracks.GenreId
    GROUP BY genres.Name
    ORDER BY TrackCount DESC
    LIMIT 1
    """  # ここにSQLクエリを書いてください
    db.execute(query)
    results = db.fetchall()
    results = [(row[0], int(row[1])) for row in results]
    return results

number_of_artists(db)
albums_about_love(db)

# スクリプトの最後で必ずデータベース接続を閉じる
conn.close()

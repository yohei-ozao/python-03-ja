
import sqlite3
from chinook_buckets import *

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# track_length_bucketsのテスト
def test_track_length_buckets():
    buckets = track_length_buckets(db)
    assert isinstance(buckets, list), "Should return a list."
    assert len(buckets) > 0, "The list of buckets should not be empty."
    for bucket in buckets:
        assert isinstance(bucket, tuple) and len(bucket) == 2, "Each bucket should be a tuple with 2 elements."

# テストを実行
test_track_length_buckets()

print("All tests passed for Chinook challenges!")

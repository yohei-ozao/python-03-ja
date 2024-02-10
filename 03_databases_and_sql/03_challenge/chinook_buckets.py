
# SQL & Python with Chinook Database: Track Length Challenges

import sqlite3

# Connect to the chinook.db database
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# Track Length Buckets
def track_length_buckets(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Don't forget to close the database connection at the end of your script
conn.close()

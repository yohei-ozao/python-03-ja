
# SQL & Python with Chinook Database: Advanced Joins

import sqlite3

# Connect to the chinook.db database
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# Detailed Tracks
def detailed_tracks(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Tracks Not Bought
def tracks_not_bought(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Genre Statistics
def genre_stats(db, genre_name):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Top 5 Artists by Genre
def top_five_artists_by_genre(db, genre_name):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Don't forget to close the database connection at the end of your script
conn.close()

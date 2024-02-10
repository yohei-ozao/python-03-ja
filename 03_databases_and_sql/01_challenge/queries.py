
# SQL & Python with Chinook Database

import sqlite3

# Connect to the chinook.db database
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# Number of Artists
def number_of_artists(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# List of Artists
def list_of_artists(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# List of Albums About “Love”
def albums_about_love(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Number of Tracks Longer Than a Given Duration
def tracks_longer_than(db, duration):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# List of Genres with Most Tracks
def genres_with_most_tracks(db):
    query = ""  # Your SQL query goes here
    db.execute(query)
    results = db.fetchall()
    return results

# Don't forget to close the database connection at the end of your script
conn.close()

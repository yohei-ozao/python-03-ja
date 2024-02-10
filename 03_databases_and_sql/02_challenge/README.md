# Challenge 2:  **Advanced Joins**

## **Background & Objectives**

This challenge focuses on mastering SQL joins in Python. Understanding different types of joins is crucial for fetching data from multiple tables. For a quick primer on SQL joins, [this Stack Overflow post](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) offers a helpful overview.

We will continue using the **`chinook.db`** database. Ensure you have the database file in the **`data`** directory of this challenge.

You must complete the functions in **`advanced_joins.py`**. Each function will use a **`db`** cursor, provided as an argument, to execute SQL queries. This is a continuation of the previous exercise but with a focus on join operations.

### **Detailed Tracks**

- Implement **`detailed_tracks`** to retrieve all track names with their corresponding album titles and artist names.
- The function should return a list of tuples like (**`track_name`**, **`album_title`**, **`artist_name`**).

### **Tracks Not Bought**

- Implement **`tracks_not_bought`** to find tracks that have never been purchased.
- This function should return a list of track **`titles`**.

### **Genre Statistics**

- Implement **`genre_stats`** to get statistics for a given genre: the number of tracks and the average track length (in seconds).
- The function should return a dictionary like:

```python
results = genre_stats(db, "Rock")
print(results)
=> {
    'genre': 'Rock',
    'number_of_tracks': 1297,
    'avg_track_length': 283.9
}
```

## **Top 5 Artists by Genre**

- Implement **`top_five_artists_by_genre`** to get the top 5 artists with the most tracks in a given genre.
- The function should return a list of tuples like (**`artist_name`**, **`number_of_tracks`**).
- Sort ties alphabetically by artist name.

```python
results = top_five_artists_by_genre(db, "Jazz")
print(results[0])
=> [
    ('Miles Davis', 37),
    ('Gene Krupa', 22),
    ('Spyro Gyra', 21),
    ('Antônio Carlos Jobim', 14),
    ('Icognito', 13)
]
```
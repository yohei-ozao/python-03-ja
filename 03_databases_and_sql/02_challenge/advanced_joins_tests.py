import sqlite3
from advanced_joins import *

# Connect to the chinook.db database
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# Test for Detailed Tracks
def test_detailed_tracks():
    tracks = detailed_tracks(db)
    assert isinstance(tracks, list), "Should return a list."
    assert len(tracks) > 0, "The list of tracks should not be empty."
    for track in tracks:
        assert len(track) == 3, "Each tuple should contain 3 elements (track_name, album_title, artist_name)."

# Test for Tracks Not Bought
def test_tracks_not_bought():
    tracks = tracks_not_bought(db)
    assert isinstance(tracks, list), "Should return a list."
    # This test assumes there are tracks not bought in the sample database

# Test for Genre Statistics
def test_genre_stats():
    stats = genre_stats(db, "Rock")
    assert isinstance(stats, dict), "Should return a dictionary."
    assert 'genre' in stats and 'number_of_tracks' in stats and 'avg_track_length' in stats, "Dictionary keys missing."

# Test for Top 5 Artists by Genre
def test_top_five_artists_by_genre():
    artists = top_five_artists_by_genre(db, "Rock")
    assert isinstance(artists, list), "Should return a list."
    assert len(artists) <= 5, "Should not return more than 5 artists."
    if len(artists) > 1:
        # Check if sorted by number of tracks and then alphabetically by name
        max_tracks = artists[0][1]
        for artist in artists:
            assert artist[1] <= max_tracks, "Artists should be sorted by number of tracks."
            max_tracks = artist[1]

# Running the tests
test_detailed_tracks()
test_tracks_not_bought()
test_genre_stats()
test_top_five_artists_by_genre()

print("All tests passed for advanced joins!")

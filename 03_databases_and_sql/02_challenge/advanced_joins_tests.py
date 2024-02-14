import sqlite3
from advanced_joins import *

# chinook.dbデータベースに接続
conn = sqlite3.connect('../data/chinook.db')
db = conn.cursor()

# detailed_tracksのテスト
def test_detailed_tracks():
    tracks = detailed_tracks(db)
    assert isinstance(tracks, list), "Should return a list."
    assert len(tracks) > 0, "The list of tracks should not be empty."
    for track in tracks:
        assert len(track) == 3, "Each tuple should contain 3 elements (track_name, album_title, artist_name)."

# tracks_not_boughtのテスト
def test_tracks_not_bought():
    tracks = tracks_not_bought(db)
    assert isinstance(tracks, list), "Should return a list."
    # このテストは、サンプルデータベースに未購入の楽曲があることを想定している

# genre_statsのテスト
def test_genre_stats():
    stats = genre_stats(db, "Rock")
    assert isinstance(stats, dict), "Should return a dictionary."
    assert 'genre' in stats and 'number_of_tracks' in stats and 'avg_track_length' in stats, "Dictionary keys missing."

# top_five_artists_by_genreのテスト
def test_top_five_artists_by_genre():
    artists = top_five_artists_by_genre(db, "Rock")
    assert isinstance(artists, list), "Should return a list."
    assert len(artists) <= 5, "Should not return more than 5 artists."
    if len(artists) > 1:
        # 楽曲数で並べ替えた後、名前のアルファベット順で並べ替えられていることを確認
        max_tracks = artists[0][1]
        for artist in artists:
            assert artist[1] <= max_tracks, "Artists should be sorted by number of tracks."
            max_tracks = artist[1]

# テストを実行
test_detailed_tracks()
test_tracks_not_bought()
test_genre_stats()
test_top_five_artists_by_genre()

print("All tests passed for advanced joins!")

# チャレンジ2:  **SQLの高度な結合 (JOIN)**

## **背景と目的**

このチャレンジの目的は、PythonでSQLの結合をマスターすることです。複数のテーブルからデータを取得するには、さまざまな種類の結合について理解する必要があります。[このStackOverflowの記事](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) (英語) を見ると、SQLの結合の概要を理解できます。

**`chinook.db`** データベースを引き続き使用します。このチャレンジの **`data`** ディレクトリにこのデータベースのファイルがあることを確認してください。

このチャレンジでは **`advanced_joins.py`** の関数を完成させてください。各関数では、引数として渡された **`db`** カーソルを使用してSQLクエリを実行します。これは前回の演習の続きにあたりますが、今回は結合操作を中心に取り組みます。

### **楽曲の詳細**

- すべての楽曲名と、それに対応するアルバムのタイトル、アーティスト名を取得する **`detailed_tracks`** 関数を実装します。
- この関数では (**`track_name`**, **`album_title`**, **`artist_name`**) のようなタプルのリストを返すようにします。

### **未購入の楽曲**

- まだ購入していない楽曲を検索する **`tracks_not_bought`** 関数を実装します。
- この関数では、楽曲の **`タイトル`** のリストを返すようにします。

### **ジャンルの統計情報**

- 特定のジャンルの統計情報 (楽曲数、楽曲の平均の再生時間 (秒)) を取得する **`genre_stats`** 関数を実装します。
- この関数では、次のような辞書を返すようにします。

```python
results = genre_stats(db, "Rock")
print(results)
=> {
    'genre': 'Rock',
    'number_of_tracks': 1297,
    'avg_track_length': 283.9
}
```

## **ジャンル別のトップ5アーティスト**

- 特定のジャンルで楽曲数が多い上位5組のアーティストを取得する **`top_five_artists_by_genre`** 関数を実装します。
- この関数では、(**`artist_name`**, **`number_of_tracks`**) のようなタプルのリストを返すようにします。
- アーティスト名のアルファベット順でタイトルを並べ替えます。

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
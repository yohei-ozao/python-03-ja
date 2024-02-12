演習3で確認したOpenWeatherMap APIを使用して、天気の**[CLI](https://en.wikipedia.org/wiki/Command-line_interface)**を作成しましょう。ユーザーの操作の流れは次のようになります (擬似コード)。

1. コマンド **`python weather.py`** でアプリを起動します。
2. ユーザーに都市名を入力するよう促します。
3. 入力された都市名をAPIが認識できない場合、エラーメッセージを表示してステップ2に戻ります。
4. 今後5日間の天気予報 (日付、天気、最高気温 (°C)) を取得して表示します。
5. ステップ2に戻ります (ユーザーに新しい都市名を入力するよう促し、この処理を繰り返します)。
6. ユーザーが **`Ctrl+C`** キーを押したら、随時プログラムを終了します。

実行結果は次のようになります。

```python
> python weather.py
City?
> london
Here's the weather in London
2020-09-30: Heavy Rain 16.4°C
2020-10-01: Light Rain 15.1°C
2020-10-02: Heavy Rain 13.4°C
2020-10-03: Heavy Rain 14.3°C
2020-10-04: Heavy Rain 14.6°C
City?
> 
```

ファイル **`weather.py`** を作り、次の3つの関数を作成します。

- **`search_city(query)`**
- **`weather_forecast(lat, lon)`**
- **`main()`**

これらの関数を**以下に指定した順序**で実装します。CLIでプログラムを実行 (**`python weather.py`** を実行) し、関数の機能を確認してください。

1. はじめに **`search_city`** 関数を作成します。この関数では、都市に関するさまざまな情報 (**`lat`** (緯度) や **`lon`** (経度) など) を含む **`辞書`** を返します。
2. 次に **`weather_forecast`** 関数を作成します。この関数では、都市の **`lat`** と **`lon`** を引数として受け取り、今後5日間の天気予報を返します (関数で辞書の **`リスト`** を返すようにします)。OpenWeatherMapは3時間ごとの予報を提供するため、各日の予報 (1日につき1予報) を表示するように結果を調整する必要があります。
3. **`main`** 関数をコーディングしてチャレンジを完了します。ターミナルから **`weather.py`** ファイルを実行すると **`main`** 関数が実行されます。**`main`** で呼び出す関数とその適切な順序を決定します。

**都市のリスト**

**`ステップ3`** の後でユーザーの入力が曖昧な場合 (検索した結果、複数の都市が返された場合など) は、次のようにオプションを表示して番号を1つ選択するようユーザーに促します。

```
City?
> Pari
1.Paris,FR
2.Paris,FR
3.Paris,FR
4.Pari,IT
5.Puri,IN
Multiple matches found, which city did you mean?
> 1
2022-09-26: Clouds (12°C)
2022-09-27: Clouds (10°C)
2022-09-28: Rain (12°C)
2022-09-29: Clouds (11°C)
2022-09-30: Clear (10°C)
```

💡 **ヒント1**: 組み込みの **[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)** 関数が役立ちます。

💡 **ヒント2**: デフォルトでは、APIは特定のクエリ **`q`** に対して複数のオプションを返すことはありません。指定した数のオプションをAPIが返すようにするには、URLに **`limit=`** パラメータを追加します (例: **`https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&limit=5&appid=XXXXXXXXXXX`** とすると、バルセロナに関する5つのオプションを返します)。
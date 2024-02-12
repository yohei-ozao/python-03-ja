環境内にセットアップされているnorthwind.dbデータベースを使用します。

詳細
queries.pyを開き、次の問題に答えてください。DBeaverなどのツールでデータベースを調査すると、構造を深く理解できます。

Orders、OrderDetails、Productsの各テーブルを参照し、3つのメソッドを実装します。

query_ordersの実装: すべての注文を取得し、OrderIDの昇順で並べ替えてください。

get_orders_rangeの実装: 特定の期間に発生したすべての注文を取得し、OrderDateの昇順で並べ替えてください。このメソッドでは2つの日付 (date_fromとdate_to) を引数に取り、date_toの日付の注文は含めますがdate_fromの日付の注文は除外します。

get_order_detailsの実装: 各注文の詳細情報 (商品名や注文数など) を取得し、OrderIDの昇順で並べ替えてください。

👉 注意: 各メソッドはdb (データベース接続) を引数に取ります。この引数にはexecuteメソッドを使用できます。この接続はテストのフレームワークで提供されるため、自分で接続する必要はありません。各メソッドを次の構成で書いてください。

def the_method(db):
    results = db.execute("YOUR SQL QUERY")
    results = results.fetchall()
    # 結果は行のリストであり、各行は列の値のリストです。
    print(results) # 結果が正しいかどうか常に確認してください。
    # 適切な値を返します。
    return ?

ヒント: f文字列を使用すると、文字列に引数を挿入できます。SQLクエリにデータ引数を挿入する場合にも役立ちます。 
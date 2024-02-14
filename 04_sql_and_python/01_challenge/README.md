チャレンジ1: データ形式の変換

目的: 
カスタム関数を作成して、northwind.dbデータベースのOrdersテーブルにあるOrderDate列の日付形式を変換します。

具体的なタスク: 
データ形式を変換する関数の作成

transform_date_formatという名前の関数を作成します。
この関数はYYYY-MM-DD形式の日付文字列を受け取り、DD/MM/YYYY形式に変換します。

入力が有効な日付でない場合は、元の入力を返します。

関数の適用

OrdersテーブルのOrderDate列にtransform_date_formatを適用するapply_date_transformation関数を実装します。
この関数はSQLiteデータベースに接続し、指定された列を変換した後、変更したDataFrameを返します。

想定される出力

- DataFrameのOrderDate列をDD/MM/YYYY形式の日付にして返します。
- その他の列や行は変更しないでください。

説明

変換ロジックを実装するためのテンプレートファイル (date_transformation.py) を用意してあります。
transform_date_format関数を記述し、これをapply_date_transformation関数で使用してOrdersテーブルのOrderDate列を変更します。

用意されているテストファイル (date_transformation_test.py) を使用して、関数が想定どおりに動作することを確認してください。
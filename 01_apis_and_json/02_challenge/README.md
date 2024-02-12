https://jsonplaceholder.typicode.com/posts APIを使用して、ブログ投稿を管理するためのシンプルなツールをPythonスクリプトで作成します。このCLIでは、ブログ投稿の一覧表示、作成、更新、削除の操作に対応する必要があります。HTTP要求とエラー処理の演習で作成した関数を自由に使用してください。

1. 各操作の関数 (list_posts、create_post、update_post、delete_post) を定義します。
2. requestsライブラリを使用して、各関数でAPIにHTTP要求を送信します。
3. CLIで入力と出力を処理します (例: ユーザーに入力を促す、処理結果 (正常終了/エラー) のメッセージを出力する)。
4. ループ処理を使用してCLIを実行状態で維持します (ユーザーが終了するまで)。
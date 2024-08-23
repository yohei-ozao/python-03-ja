import os
import pathlib
from collections import defaultdict

# ディレクトリの設定
base_dir = pathlib.Path(__file__).parent
data_dir = base_dir / 'data'
text_files_dir = data_dir / 'text_files'
library_dir = data_dir / 'library'

# 書籍のファイルを辞書にインポートし、1つのテキストファイルに保存する
books_dict = defaultdict(str)

for file in text_files_dir.iterdir():
    if file.is_file() and not file.name.startswith('Chapter_') and file.suffix == '.txt':
        with file.open('r', encoding='utf-8') as f:
            books_dict[file.stem] = f.read()

output_file = data_dir / 'books_combined.txt'
with output_file.open('w', encoding='utf-8') as f:
    for book_name, content in books_dict.items():
        f.write(f"=== {book_name} ===\n")
        f.write(content + "\n\n")

# library ディレクトリを作成
library_dir.mkdir(exist_ok=True)

# Chapter_x.txt ファイルを library ディレクトリに移動
for file in text_files_dir.iterdir():
    if file.is_file() and file.name.startswith('Chapter_') and file.suffix == '.txt':
        target_path = library_dir / file.name
        file.rename(target_path)

# pathlib を使用して library ディレクトリに移動し、すべてのファイルとサイズを一覧表示
print(f"Files in {library_dir}:")
for file in library_dir.iterdir():
    if file.is_file():
        print(f"{file.name}: {file.stat().st_size} bytes")
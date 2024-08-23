import csv
import json
import os
import logging

# ログ設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv(file_path):
    """CSVファイルを読み取り、その内容を辞書のリストとして返す"""
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        logging.info(f'CSVファイルを読み取りました: {file_path}')
        return data
    except Exception as e:
        logging.error(f'CSVファイルの読み取り中にエラーが発生しました: {file_path} - {e}')
        raise

def csv_to_json(csv_data):
    """CSVデータ (辞書のリスト) を受け取り、JSON形式 (文字列) に変換する"""
    try:
        json_data = json.dumps(csv_data, ensure_ascii=False, indent=4)
        logging.info('CSVデータをJSON形式に変換しました')
        return json_data
    except Exception as e:
        logging.error(f'CSVデータのJSON形式への変換中にエラーが発生しました: {e}')
        raise

def write_json(json_data, file_path):
    """JSONデータをファイルに書き込む"""
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            file.write(json_data)
        logging.info(f'JSONデータをファイルに書き込みました: {file_path}')
    except Exception as e:
        logging.error(f'JSONデータのファイルへの書き込み中にエラーが発生しました: {file_path} - {e}')
        raise

def read_json(file_path):
    """JSONファイルを読み取り、その内容をデータ (一般には辞書型のリスト) として返す"""
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f'JSONファイルを読み取りました: {file_path}')
        return data
    except Exception as e:
        logging.error(f'JSONファイルの読み取り中にエラーが発生しました: {file_path} - {e}')
        raise

def json_to_csv(json_data):
    """JSONデータ (一般には辞書のリスト) を受け取り、CSV形式 (文字列) に変換する"""
    try:
        if not json_data:
            raise ValueError('空のJSONデータ')

        keys = json_data[0].keys()
        output = []
        output.append(','.join(keys))  # ヘッダー行

        for item in json_data:
            output.append(','.join(str(item[key]) for key in keys))  # データ行

        csv_data = '\n'.join(output)
        logging.info('JSONデータをCSV形式に変換しました')
        return csv_data
    except Exception as e:
        logging.error(f'JSONデータのCSV形式への変換中にエラーが発生しました: {e}')
        raise

def write_csv(csv_data, file_path):
    """CSVデータをファイルに書き込む"""
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            file.write(csv_data)
        logging.info(f'CSVデータをファイルに書き込みました: {file_path}')
    except Exception as e:
        logging.error(f'CSVデータのファイルへの書き込み中にエラーが発生しました: {file_path} - {e}')
        raise

def validate_data(data, data_type):
    """データの整合性をチェックする (例: CSVの列数が一貫している)"""
    try:
        if data_type == 'CSV':
            keys = data[0].keys()
            for entry in data:
                if entry.keys() != keys:
                    raise ValueError('CSVデータの列が一貫していません')
        elif data_type == 'JSON':
            pass  # JSONについて特別なバリデーションを追加する
        logging.info(f'{data_type}データの整合性を確認しました')
        return True
    except Exception as e:
        logging.error(f'{data_type}データの整合性の確認中にエラーが発生しました: {e}')
        raise

def process_directory(directory_path):
    """特定のディレクトリ内のすべてのCSVファイルとJSONファイルを識別し、適切に変換する"""
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if filename.endswith('.csv'):
                csv_data = read_csv(file_path)
                validate_data(csv_data, 'CSV')
                json_data = csv_to_json(csv_data)
                write_json(json_data, file_path.replace('.csv', '.json'))
            elif filename.endswith('.json'):
                json_data = read_json(file_path)
                validate_data(json_data, 'JSON')
                csv_data = json_to_csv(json_data)
                write_csv(csv_data, file_path.replace('.json', '.csv'))
        logging.info('ディレクトリ内のファイル処理を完了しました')
    except Exception as e:
        logging.error(f'ディレクトリ内のファイル処理中にエラーが発生しました: {directory_path} - {e}')
        raise

# テスト用のファイルパス
csv_file_path = 'sample.csv'
json_file_path = 'sample.json'
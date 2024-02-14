import unittest
from date_transformation import transform_date_format, apply_date_transformation

class TestDateFormatTransformation(unittest.TestCase):

    def test_transform_date_format(self):
        # 日付形式の変換をテスト
        self.assertEqual(transform_date_format('2023-01-15'), '15/01/2023')
        # 無効な日付入力をテスト
        self.assertEqual(transform_date_format('InvalidDate'), 'InvalidDate')

    def test_apply_date_transformation(self):
        db_path = '../data/northwind.db'
        transformed_df = apply_date_transformation(db_path, 'Orders', 'OrderDate')
        
        # 日付形式が適切に変換されているかテスト
        # テスト用に変換後のDataFrameからサンプルの日付を取得
        sample_date = transformed_df['OrderDate'].iloc[0]
        # サンプルの日付が想定されている形式か確認
        self.assertRegex(sample_date, r'\d{2}/\d{2}/\d{4}')

if __name__ == '__main__':
    unittest.main()

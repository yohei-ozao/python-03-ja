import unittest
from date_transformation import transform_date_format, apply_date_transformation

class TestDateFormatTransformation(unittest.TestCase):

    def test_transform_date_format(self):
        # Testing date format conversion
        self.assertEqual(transform_date_format('2023-01-15'), '15/01/2023')
        # Testing with invalid date input
        self.assertEqual(transform_date_format('InvalidDate'), 'InvalidDate')

    def test_apply_date_transformation(self):
        db_path = '../data/northwind.db'
        transformed_df = apply_date_transformation(db_path, 'Orders', 'OrderDate')
        
        # Test if the date format is transformed correctly
        # Extract a sample date from the transformed DataFrame for testing
        sample_date = transformed_df['OrderDate'].iloc[0]
        # Check if the sample date is in the expected format
        self.assertRegex(sample_date, r'\d{2}/\d{2}/\d{4}')

if __name__ == '__main__':
    unittest.main()

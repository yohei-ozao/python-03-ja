Challenge 1: Date Format Transformation

Objective:
Develop a custom function to transform the date format in the OrderDate column of the Orders table in the northwind.db database.

Specific Task for Learners:
Transformation Function:

Create a function named transform_date_format.
The function should take a date string in the format YYYY-MM-DD and convert it to the format DD/MM/YYYY.

If the input is not a valid date, the function should return the original input.

Application of Function:

Implement the function apply_date_transformation to apply transform_date_format to the OrderDate column of the Orders table.
This function must connect to the SQLite database, transform the specified column, and return the modified DataFrame.

Expected Outcome:

- The OrderDate column in the returned DataFrame should have dates in the DD/MM/YYYY format.
- Other columns and rows should remain unchanged.

Instructions for Learners:

You are provided with a template file (date_transformation.py) where you can implement your transformation logic.
Your task is to write the transform_date_format function and use it in the apply_date_transformation function to modify the OrderDate column in the Orders table.

Use the provided test file (date_transformation_test.py) to ensure your function behaves as expected.
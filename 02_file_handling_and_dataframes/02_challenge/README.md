## Challenge 2: **Data Transformation Toolkit**

**Objective:** Develop a Python module that provides functionalities to convert data between CSV and JSON formats, ensuring data integrity and automating file processing in a directory. Please use the provided “sample.csv” and “sample.json” files as the tests will rely on these.

### **Tasks:**

1. **Read CSV:**
    - Function: **`read_csv(file_path)`**
    - Description: Reads a CSV file and returns its contents as a list of dictionaries.
2. **CSV to JSON Conversion:**
    - Function: **`csv_to_json(csv_data)`**
    - Description: Takes CSV data (list of dictionaries) and converts it to JSON format (string).
3. **Write JSON:**
    - Function: **`write_json(json_data, file_path)`**
    - Description: Writes JSON data to a file.
4. **Read JSON:**
    - Function: **`read_json(file_path)`**
    - Description: Reads a JSON file and returns its contents as data (typically a list of dictionaries).
5. **JSON to CSV Conversion:**
    - Function: **`json_to_csv(json_data)`**
    - Description: Takes JSON data (typically a list of dictionaries) and converts it to CSV format (string).
6. **Write CSV:**
    - Function: **`write_csv(csv_data, file_path)`**
    - Description: Writes CSV data to a file.
7. **Data Validation:**
    - Function: **`validate_data(data, data_type)`**
    - Description: Checks data integrity (e.g., consistent number of columns in CSV). **`data_type`** can be 'CSV' or 'JSON'.
8. **Automate File Processing:**
    - Function: **`process_directory(directory_path)`**
    - Description: Identifies all CSV and JSON files in a given directory and performs appropriate conversions.
9. **Logging and Error Handling:**
    - Implement logging for tracking the process flow and error handling to manage exceptions.
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from extract import extract_excel, extract_csv, extract_sql

# Excel
df_excel = extract_excel()
print("Excel:")
print(df_excel.head())

# CSV
df_csv = extract_csv()
print("\nCSV:")
print(df_csv.head())

# SQL
df_customer = extract_sql("customer")
print("\nCustomer (SQL):")
print(df_customer.head())
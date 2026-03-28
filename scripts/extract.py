import pandas as pd
from db_connection import create_source_connection

# 🔹 Extract dari Excel
def extract_excel():
    df = pd.read_excel("data/transaction_excel.xlsx")
    return df

# 🔹 Extract dari CSV
def extract_csv():
    df = pd.read_csv("data/transaction_csv.csv")
    return df

# 🔹 Extract dari SQL Server
def extract_sql(table_name):
    conn = create_source_connection()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
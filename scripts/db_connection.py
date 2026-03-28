import pyodbc

# 🔹 Source DB (sample)
def create_source_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=sample;"
        "Trusted_Connection=yes;"
    )
    return conn

# 🔹 DWH DB
def create_dwh_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=DWH;"
        "Trusted_Connection=yes;"
    )
    return conn
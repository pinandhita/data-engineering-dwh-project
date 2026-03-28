from db_connection import create_dwh_connection

def insert_dataframe(df, table_name):
    conn = create_dwh_connection()
    cursor = conn.cursor()

    cols = ",".join(df.columns)
    placeholders = ",".join(["?"] * len(df.columns))

    query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

    for row in df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    conn.commit()
    conn.close()

def truncate_table(table_name):
    conn = create_dwh_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()
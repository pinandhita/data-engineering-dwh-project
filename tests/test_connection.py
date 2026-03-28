import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from db_connection import create_connection

conn = create_connection()
cursor = conn.cursor()

query = "SELECT TOP 5 * FROM customer"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
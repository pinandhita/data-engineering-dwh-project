import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from extract import extract_excel, extract_csv, extract_sql
from transform import (
    transform_dim_customer,
    transform_dim_account,
    transform_dim_branch,
    transform_fact_transaction
)

# Extract
df_customer = extract_sql("customer")
df_city = extract_sql("city")
df_state = extract_sql("state")
df_account = extract_sql("account")
df_branch = extract_sql("branch")
df_transaction_db = extract_sql("transaction_db")

df_excel = extract_excel()
df_csv = extract_csv()

# Transform
dim_customer = transform_dim_customer(df_customer, df_city, df_state)
dim_account = transform_dim_account(df_account)
dim_branch = transform_dim_branch(df_branch)
fact_transaction = transform_fact_transaction(df_excel, df_csv, df_transaction_db)

# Print hasil
print(dim_customer.to_string())
print(fact_transaction.to_string())
import pandas as pd

def transform_dim_customer(df_customer, df_city, df_state):
    # Join customer + city
    df = df_customer.merge(df_city, on="city_id", how="left")
    
    # Join + state
    df = df.merge(df_state, on="state_id", how="left")

    # Rename kolom (PascalCase)
    df = df.rename(columns={
        "customer_id": "CustomerID",
        "customer_name": "CustomerName",
        "address": "Address",
        "city_name": "CityName",
        "state_name": "StateName",
        "age": "Age",
        "gender": "Gender",
        "email": "Email"
    })

    # Select kolom
    df = df[[
        "CustomerID", "CustomerName", "Address",
        "CityName", "StateName", "Age",
        "Gender", "Email"
    ]]

    # Uppercase (kecuali ID, Age, Email)
    for col in ["CustomerName", "Address", "CityName", "StateName", "Gender"]:
        df[col] = df[col].str.upper()

    return df

def transform_dim_account(df_account):
    df = df_account.rename(columns={
        "account_id": "AccountID",
        "customer_id": "CustomerID",
        "account_type": "AccountType",
        "balance": "Balance",
        "date_opened": "DateOpened",
        "status": "Status"
    })

    return df

def transform_dim_branch(df_branch):
    df = df_branch.rename(columns={
        "branch_id": "BranchID",
        "branch_name": "BranchName",
        "branch_location": "BranchLocation"
    })

    return df

def transform_fact_transaction(df_excel, df_csv, df_sql):
    import pandas as pd

    # Gabung semua
    df = pd.concat([df_excel, df_csv, df_sql], ignore_index=True)

    # Hapus duplicate
    df = df.drop_duplicates(subset=["transaction_id"])

    # Convert ke DateTime
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

    # Hapus data yang gagal convert
    df = df.dropna(subset=["transaction_date"])

    # Rename kolom
    df = df.rename(columns={
        "transaction_id": "TransactionID",
        "account_id": "AccountID",
        "transaction_date": "TransactionDate",
        "amount": "Amount",
        "transaction_type": "TransactionType",
        "branch_id": "BranchID"
    })

    return df


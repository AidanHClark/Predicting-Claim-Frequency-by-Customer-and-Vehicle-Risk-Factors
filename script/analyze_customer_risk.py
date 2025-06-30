import sqlite3
import pandas as pd

connection = sqlite3.connect("insurance_data.db")

query = "SELECT customer_age, claim_status FROM insurance_claims"
df = pd.read_sql(query,connection)

df_grouped = (
    df.groupby("customer_age")
    .agg(
        total_policies=("claim_status", "count"),
        total_claims=("claim_status", "sum")
    )
    .reset_index()
)

df_grouped["claim_frequency"] = df_grouped["total_claims"] / df_grouped["total_policies"]

print(df_grouped)
connection.close()
df_customer_risk = df_grouped
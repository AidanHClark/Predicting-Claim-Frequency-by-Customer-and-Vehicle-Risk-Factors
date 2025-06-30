import pandas as pd
import sqlite3


conn = sqlite3.connect("insurance_data.db")


df = pd.read_sql("""
    SELECT ncap_rating, claim_status
    FROM insurance_claims
    WHERE ncap_rating IS NOT NULL
""", conn)
conn.close()


df_analysis = (
    df.groupby("ncap_rating")
      .agg(total_policies=("claim_status", "count"),
           total_claims=("claim_status", "sum"))
      .reset_index()
)


df_analysis["claim_frequency"] = df_analysis["total_claims"] / df_analysis["total_policies"]

print(df_analysis)

import pandas as pd
import sqlite3

connection = sqlite3.connect("insurance_data.db")
df = pd.read_sql("SELECT * FROM insurance_claims",connection)
print(df.head())
connection.close()

print("Unique vehicle ages:")
print(df["vehicle_age"].unique())
print()

print("Unique claim status values:")
print(df["claim_status"].unique())
print()

# Step 6: Count occurrences of each category
print("Vehicle age value counts:")
print(df["vehicle_age"].value_counts())
print()

print("Claim status value counts:")
print(df["claim_status"].value_counts())
print()
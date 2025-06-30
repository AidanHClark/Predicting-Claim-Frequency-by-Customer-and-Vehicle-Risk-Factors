import pandas as pd
import sqlite3
from clean_data import convert_yes_no_to_binary


pd.set_option('display.max_columns', None)


data_frame = pd.read_csv("data/Insurance_claims.csv")


data_frame, converted = convert_yes_no_to_binary(data_frame)
print("Columns converted to binary:", converted)

print("\nPreview of cleaned dataset:")
print(data_frame.head(10))  


connection = sqlite3.connect("insurance_data.db")
data_frame.to_sql("insurance_claims", connection, if_exists="replace", index=False)
connection.commit()


result = pd.read_sql("SELECT customer_age FROM insurance_claims LIMIT 5", connection)
print("\nTest SQL result:")
print(result)

connection.close()

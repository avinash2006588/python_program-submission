#3.	WAP to to read CSV and JSON files. 
import pandas as pd

# Read CSV file
csv_data = pd.read_csv("data.csv")

print("CSV File Data:")
print(csv_data)

# Read JSON file
json_data = pd.read_json("data.json")

print("\nJSON File Data:")
print(json_data)
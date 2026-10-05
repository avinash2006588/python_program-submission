# Wap to create and manipulate dataframe using pandas
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'London', 'Tokyo']}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Manipulate the DataFrame
print("\nFirst Row:")
print(df.iloc[0])
print("\nSpecific Column:")
print(df['Name'])
print("\nSpecific Cell:")
print(df.loc[0, 'Age'])
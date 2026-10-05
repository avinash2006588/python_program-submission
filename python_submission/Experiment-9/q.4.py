#4.	WAP to calculate the correlation between columns in a data frame. 
import pandas as pd

# Create a DataFrame
data = {
    "Maths": [80, 85, 90, 75, 95],
    "Science": [75, 80, 88, 70, 92],
    "English": [70, 78, 85, 72, 90]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Calculate correlation
print("\nCorrelation Matrix:")
print(df.corr())
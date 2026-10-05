# WAP to create and work with a Pandas Series. 
import pandas as pd

# Create a Pandas Series
series = pd.Series([1, 2, 3, 4, 5])
print("Pandas Series:")
print(series)

# Work with the Series
print("\nFirst Element:", series[0])
print("Third Element:", series[2])
print("Sum:", series.sum())
print("Mean:", series.mean())
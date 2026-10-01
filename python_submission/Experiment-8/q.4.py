#wap for statistical opeartions and broadcasting on arrays
import numpy as np
# Creating a NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:")
print(arr)
# Statistical Operations
print("\nStatistical Operations:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
# Broadcasting
print("\nBroadcasting Operations:")
# Adding a scalar to every element
print("Array + 5:", arr + 5)
# Multiplying every element by a scalar
print("Array * 2:", arr * 2)
# Subtracting a scalar
print("Array - 3:", arr - 3)
# Dividing every element
print("Array / 10:", arr / 10)
# Broadcasting between two arrays
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("\nArray A:", a)
print("Array B:", b)
print("A + B:", a + b)
print("A * B:", a * b)

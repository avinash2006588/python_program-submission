#wap  for numpy array properties and functions
import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Array:")
print(arr)
# NumPy Array Properties
print("\nArray Properties:")
print("Number of dimensions (ndim):", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type (dtype):", arr.dtype)
print("Item size:", arr.itemsize)
# NumPy Array Functions
print("\nArray Functions:")
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Square root:", np.sqrt(arr))
# Reshape function
print("\nReshaped Array:")
print(arr.reshape(3, 2))

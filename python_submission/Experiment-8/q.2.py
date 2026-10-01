#write a program for Datatypes and structures in numpy
import numpy as np
a = np.array([10, 20, 30])
b = np.array([1.5, 2.5, 3.5])
c = np.array([True, False, True])
print("Integer Datatype:", a.dtype)
print("Float Datatype:", b.dtype)
print("BOOLEAN Datatype:", c.dtype)
arr1 = np.array([1, 2, 3, 4, 5])
print("\n1-D Array:", arr1)
print("\nDimensions of 2-D array:", arr1.ndim)
print("Shape of 2-D array:", arr1.shape)
print("Size of 2-D array:", arr1.size)
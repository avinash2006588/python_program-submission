#WAP for ndarray object,indexing and slicing
import numpy as np 
arr=np.ndarray([10,20,30,40,50])
#Indexing the arrays
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])
#Slicing the array
print("Elements from index 1 to 3:", arr[1:4])
print("First three elements:", arr[:3])
print("Elements from index 2:", arr[2:])
print("Every second element:", arr[::2])
print("Reverse array:", arr[::-1])
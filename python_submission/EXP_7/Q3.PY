# 3. WAP to create a list containing the power of said number in bases raised to the corresponding number in the index using python map

from math import *
x=list(eval(input("Enter the power list:")))
y=list(eval(input("enter the number list:")))
def power(x,y):
     z=int(pow(y,x)) 
     return z
l=list(map(power,x,y))
print("The resultant list:",l)
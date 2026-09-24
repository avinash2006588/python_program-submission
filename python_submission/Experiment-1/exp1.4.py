import math
a=int(input("enter the 1st  coefficient="))
b=int(input("enter the 2nd  coefficient="))
c=int(input("enter the 3rd  coefficient="))
d=math.sqrt((b**2)-4*a*c)
r1=(-b+d)/(2*a)
r2=(-b-d)/(2*a)
print("roots=",r1,r2)

n=int(input("enter the number="))
f=1
if n>=0:
    for i in range(1,n+1):
        f=f*i
    print("Factorial :",f)
else:
    print("factorial:not defined for negative value")

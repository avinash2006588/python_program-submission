def facto(n):
    if n==0:
        return 1
    else:
        return n*facto(n-1)
n=int(input("enter the number="))
if n<0:
    print("Invalid:factorial is not possible for negative value")
else:
    print("factorial of ",n,"=",facto(n))

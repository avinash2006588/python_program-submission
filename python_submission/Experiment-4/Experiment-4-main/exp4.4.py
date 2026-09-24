def fibbo(n):
    a=0
    b=1
    print("fibbbonaci series=")
    for i in range(n):
        c=a+b
        print(a,end=" ")
        a,b=b,c
n=int(input("enter the number of terms="))
fibbo(n)

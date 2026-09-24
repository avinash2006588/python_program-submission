a=int(input("enter a number="))
sum1=0
for i in range(1,a):
    if a%i==0:
        sum1+=i
if sum1==a:
    print(a,"is perfect number")
else:
    print(a,"is not perfect number")

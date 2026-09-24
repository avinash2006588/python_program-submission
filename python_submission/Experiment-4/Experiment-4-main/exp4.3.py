b=[]
print("enter 20 integers")
for i in range(20):
    n1=int(input("enter element {i+1} ="))
    b.append(n1)
for j in range(20):
    if b[j]%2==0:
        b[j]+=5
print(b)

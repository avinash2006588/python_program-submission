b,c=[],[]
print("enter 5 integers")
for i in range(5):
    n1=int(input("enter list1 element [i+1] ="))
    b.append(n1)
print("enter 5 strings")
for i in range(5):
    n2=input("enter list2 element [i+1] =")
    c.append(n2)
x=[]
for i in range(5):
        x.append(c[i]+"  "+str(b[i]))
print(x)

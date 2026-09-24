n=int(input("enter the number="))
x=[]
twin=[]
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
              if i%j==0:
                  c=c+1
    if c==2:
            x.append(i)
for i in range(len(x)-1):
    if x[i+1]-x[i]==2:
        twin.append((x[i],x[i+1]))
print("twin prime=",twin)

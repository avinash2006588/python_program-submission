print("enter 10 numbers")
l1=[]
for i in range(10):
    n=int(input(f"enter number {i+1}="))
    l1.append(n)
for i in range(len(l1)):
    for j in range(i,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)
print("second laregst=",l1[len(l1)-2])
print("second smallest=",l1[1])

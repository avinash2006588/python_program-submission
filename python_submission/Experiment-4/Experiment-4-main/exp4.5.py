def even_len(n):
    s=[]
    for i in n:
        if i%2==0:
            s.append(i)
    return s
x=input("enter the list elements separated by commas:")
n=[int (i) for i in x.split(",")]
e=even_len(n)
print("list of even values=",e)

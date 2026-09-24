x=input("enter the string=")
result=""
for char in x:
    if char not in result:
        result=result+char
print(result)

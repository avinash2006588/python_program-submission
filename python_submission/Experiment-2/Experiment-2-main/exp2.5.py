a=input("enter string=")
b=a[::-1]
c,v=0,0
print("reverse=",b)
for i in range(0,len(b)):
    if b[i].lower() in "aieou":
        v=v+1
    else:
        c=c+1
print("no. of vowels:",v)
print("no. of consonants:",c)

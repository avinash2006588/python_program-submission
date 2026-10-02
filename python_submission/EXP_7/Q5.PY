# 5. WAP to convert a given list of integer and a tuple of integer in a list of string using map().

def convert(c): 
    if c==1:
        return "one" 
    elif c==2:
        return "Two" 
    elif c==3:
        return "three" 
    elif c==4:
        return "four" 
    elif c==5:
        return "five" 
    elif c==6:
        return "six" 
    elif c==7:
        return "Seven" 
    elif c==8:
        return "eight" 
    elif c==9:
        return "nine" 
    else:
        return "zero"

l1=list(eval(input("Enter the number list:"))) 
l2=list(map(convert,l1))

print(l2)

t1=tuple(eval(input("enter the number tuple:"))) 
t2=list(map(convert,l2))

print(l2)
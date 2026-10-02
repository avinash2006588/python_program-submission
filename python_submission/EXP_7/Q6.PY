# 6. WAP to find the ratio of positive numbers, negative numbers and zeroes in an array of integers using map().

x=list(eval(input("Enter the integer array:"))) 

print("The original list:",x) 

pos=list(filter(lambda y:y>0,x)) 
zero=list(filter(lambda y:y==0,x)) 
neg=list(filter(lambda y:y<0,x))

n=len(x) 
z1=[]

P_ratio=round(len(pos)/n,2) 
N_ratio=round(len(neg)/n,2) 
Z_ratio=round(len(zero)/n,2) 

z1.append(P_ratio) 
z1.append(N_ratio) 
z1.append(Z_ratio)

def ratio(z1):
    return z1

l1=list(map(ratio,z1)) 

print("The ratio array:",l1)
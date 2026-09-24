# wap to print fibonacci  series up to  n terms  using lamda functions
n = int(input("Enter n: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
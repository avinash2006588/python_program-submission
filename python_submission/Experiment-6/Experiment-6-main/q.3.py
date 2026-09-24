# wap to print the transpose of a matrix of n*n order
n = int(input("Enter n: "))

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print("Transpose:")
for i in range(n):
    for j in range(n):
        print(a[j][i], end=" ")
    print()

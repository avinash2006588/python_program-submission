#wap to print a matrix along with summation of row elements and column elements after entering a 3* 3 matrix
a = []

for i in range(3):
    a.append(list(map(int, input().split())))

for i in range(3):
    print(a[i], "Row Sum =", sum(a[i]))

print("Column Sums:")
for j in range(3):
    s = 0
    for i in range(3):
        s += a[i][j]
    print(s)
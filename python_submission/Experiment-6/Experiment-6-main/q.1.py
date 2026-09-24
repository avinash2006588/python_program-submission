# wap to print a matrix containg group of similar elements by givung input randomly in another matrix using functions
def group(a):
    b = []
    for i in a:
        b += i
    b.sort()
    return [b[:3], b[3:6], b[6:9]]

a = []
for i in range(3):
    a.append(list(map(int, input().split())))

print(group(a))
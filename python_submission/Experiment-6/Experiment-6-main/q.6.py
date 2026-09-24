#wap to print the intersection of 2 arrays using lambda functions
a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

result = list(filter(lambda x: x in b, a))

print("Intersection:", result)
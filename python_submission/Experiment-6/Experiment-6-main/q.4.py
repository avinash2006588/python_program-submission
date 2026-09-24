#wap to check if a value  is present in the list or not ,using lamda functions
lst = list(map(int, input("Enter list: ").split()))
x = int(input("Enter value: "))

check = lambda: x in lst

print(check())
def maximum_unique(d):
    max_value = -1
    max_key = ""

    for key in d:
        if list(d.values()).count(d[key]) == 1 and d[key] > max_value:
            max_value = d[key]
            max_key = key

    return max_key


d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print("Key with maximum unique value:", maximum_unique(d))

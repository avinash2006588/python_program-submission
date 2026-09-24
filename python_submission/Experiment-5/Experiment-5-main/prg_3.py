def remove_duplicate(d):
    new = {}

    for key in d:
        if d[key] not in new.values():
            new[key] = d[key]

    return new


d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print("Dictionary after removing duplicates:", remove_duplicate(d))

def merge_dictionaries(dict1, dict2):
    dict1.update(dict2)
    return dict1


# Input first dictionary
d1 = {}
n1 = int(input("Enter number of elements in first dictionary: "))

for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

# Input second dictionary
d2 = {}
n2 = int(input("Enter number of elements in second dictionary: "))

for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

# Merge dictionaries
result = merge_dictionaries(d1, d2)

print("Merged Dictionary:", result)

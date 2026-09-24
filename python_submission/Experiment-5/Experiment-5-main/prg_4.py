def copy_set(s):
    new_set = set()

    for x in s:
        new_set.add(x)

    return new_set


s = set(input("Enter elements separated by space: ").split())

new_set = copy_set(s)

print("Original set:", s)
print("New set:", new_set)

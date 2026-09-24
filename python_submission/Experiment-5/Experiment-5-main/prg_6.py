def combine_sets(a, b):
    return a | b


a = set(input("Enter elements of Set A: ").split())
b = set(input("Enter elements of Set B: ").split())

new_set = combine_sets(a, b)

print("New set:", new_set)

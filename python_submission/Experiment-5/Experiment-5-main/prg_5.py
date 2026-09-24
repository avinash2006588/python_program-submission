def set_operations(a, b):
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference (A-B):", a - b)
    print("Difference (B-A):", b - a)
    print("Symmetric Difference:", a ^ b)


a = set(input("Enter elements of Set A: ").split())
b = set(input("Enter elements of Set B: ").split())

set_operations(a, b)

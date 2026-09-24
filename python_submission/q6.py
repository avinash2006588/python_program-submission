arr = [1, -2, 0, 3, -4, 0, 5, -6]
result = list(map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr))
positive = result.count(1)
negative = result.count(-1)
zero = result.count(0)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Ratio =", positive, ":", negative, ":", zero)

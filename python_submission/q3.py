bases = [2, 3, 4, 5, 6]
result = list(map(lambda x: x ** bases.index(x), bases))
print(result)

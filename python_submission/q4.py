sequence = ['a', 'B', 'c', 'A', 'b', 'C', 'd']
uppercase = list(map(str.upper, sequence))
lowercase = list(map(str.lower, sequence))
unique = list(set(uppercase))
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Without duplicates:", unique)

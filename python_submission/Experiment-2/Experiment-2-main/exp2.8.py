def armstrong(n):
    s = 0
    temp = n

    while n > 0:
        digit = n % 10
        s = s + digit ** 3
        n = n // 10

    return s == temp


n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

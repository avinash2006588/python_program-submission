def prime_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            prime = True

            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break

            if prime:
                print(i, end=" ")


n = int(input("Enter a 3 digit number: "))

print("Prime factors:", end=" ")
prime_factors(n)

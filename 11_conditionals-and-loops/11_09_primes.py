# Print out every prime number between 1 and 1000.

for n in range(1, 1001):
    if n in [1, 2]:
        print(n)
        continue

    is_prime = True

    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(n)




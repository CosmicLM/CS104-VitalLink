for prime in range(2, 101):
    is_prime = True
    for divisor in range(2,int(prime ** 0.5) + 1):
        if prime % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(prime)
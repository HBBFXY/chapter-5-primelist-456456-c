def PrimeList(N):
    primes = []
    for num in range(2, N):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return ' '.join(primes)

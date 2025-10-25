def PrimeList(N):
    # 小于2没有质数
    if N <= 2:
        return ""
    
    primes = []
    for i in range(2, N):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(str(i))
    
    return " ".join(primes)

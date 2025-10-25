def PrimeList(N):
    primes = []
    for i in range(2, N):  # 从2开始到N-1
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  # 判断是否为质数
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(i))
    print(" ".join(primes))  # 以空格分隔输出，无末尾空格

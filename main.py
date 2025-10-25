# main.py

def PrimeList(N):
    """
    返回一个字符串，包含所有小于 N 的质数，质数之间用单个空格分隔，末尾无空格。
    要求：返回类型必须是 str（测试脚本会检查）。
    """
    # 尽量容错：允许传入可以转换为 int 的值
    try:
        N = int(N)
    except Exception:
        return ""

    if N <= 2:
        return ""

    # Sieve of Eratosthenes
    sieve = [True] * N  # index i 表示 i 是否为质数（暂定）
    sieve[0] = False
    if N > 1:
        sieve[1] = False

    limit = int(N ** 0.5)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            # 若 start >= N 则切片会为空，安全
            step = p
            sieve[start:N:step] = [False] * (((N - 1 - start) // step) + 1 if start < N else 0)

    primes = [str(i) for i, is_prime in enumerate(sieve) if is_prime]
    return " ".join(primes)


if __name__ == "__main__":
    # 方便手工运行：从标准输入读取一个整数并打印结果
    try:
        import sys
        data = sys.stdin.read().strip().split()
        if not data:
            # 如果没有输入，什么都不做
            sys.exit(0)
        N = int(data[0])
        print(PrimeList(N))
    except Exception:
        # 输入解析错误时安静退出（不抛异常到外面）
        sys.exit(0)

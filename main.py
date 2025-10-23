def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""
    
    # 初始化一个布尔数组，长度为N，初始值设为True，表示当前所有数都可能是质数
    is_prime = [True] * N
    is_prime[0] = False  # 0不是质数
    is_prime[1] = False  # 1不是质数
    
    # 从2开始遍历到N的平方根（包含）
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            # 如果i是质数，则将其所有倍数标记为非质数
            # 从i*i开始标记，因为更小的倍数已被之前的质数标记过
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有标记为True的索引，即为小于N的质数
    primes = [str(num) for num, prime in enumerate(is_prime) if prime]
    return ' '.join(primes)

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理特殊情况，小于 2 的数没有质数
    if N <= 2:
        return ""
    # 初始化一个列表，用于标记每个数是否为质数
    is_prime = [True] * N
    # 0 和 1 不是质数
    is_prime[0] = is_prime[1] = False
    # 从 2 开始遍历到 N 的平方根
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            # 将 i 的倍数标记为非质数
            for j in range(i * i, N, i):
                is_prime[j] = False
    # 收集所有质数
    primes = [str(i) for i in range(N) if is_prime[i]]
    # 将质数列表转换为以空格分隔的字符串
    return " ".join(primes)

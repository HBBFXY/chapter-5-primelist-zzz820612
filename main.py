def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数: N - 整数
    返回: str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理边界情况：N <= 2 时没有小于 N 的质数
    if N <= 2:
        return ""
    
    # 初始化标记数组
    is_prime = [True] * N
    is_prime[0] = False  # 0 不是质数
    is_prime[1] = False  # 1 不是质数
    
    # 埃拉托斯特尼筛法
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            # 标记 i 的所有倍数
            for j in range(i * i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = []
    for num in range(2, N):  # 从 2 开始，确保不包含 1
        if is_prime[num]:
            primes.append(str(num))
    return " ".join(primes)

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理所有小于2的情况（包括负数、0、1），返回空字符串
    if N <= 2:
        return ""
    
    # 初始化质数标记列表（埃拉托斯特尼筛法）
    is_prime = [True] * N
    is_prime[0], is_prime[1] = False, False  # 0和1不是质数
    
    # 标记非质数
    for current in range(2, int(N ** 0.5) + 1):
        if is_prime[current]:
            # 从current的平方开始标记其倍数为非质数
            for multiple in range(current * current, N, current):
                is_prime[multiple] = False
    
    # 收集所有质数并转换为字符串列表
    primes = [str(num) for num in range(2, N) if is_prime[num]]
    
    # 用空格连接所有质数字符串
    return " ".join(primes)

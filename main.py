import math

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数: N - 整数
    返回: str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理边界情况：当 N 小于等于 1 时，没有质数，返回空字符串
    if N <= 1:
        return ""
    # 特别处理 N=2 的情况，此时只有一个质数 2
    if N == 2:
        return "2"
    
    # 初始化一个长度为 N 的布尔列表，表示对应索引的数是否可能是质数
    is_prime = [True] * N
    # 0 和 1 不是质数
    is_prime[0] = False
    is_prime[1] = False
    
    # 埃拉托斯特尼筛法核心：从 2 开始遍历到 N 的平方根
    for i in range(2, math.isqrt(N) + 1): # 使用 math.isqrt 获取整数平方根
        if is_prime[i]:
            # 如果 i 是质数，标记其所有倍数为非质数
            # 从 i*i 开始标记，因为更小的倍数已经被之前的质数标记过
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有标记为 True 的索引（即质数），并转换为字符串列表
    primes = []
    for num in range(2, N): # 从 2 开始遍历，确保不会包含 1
        if is_prime[num]:
            primes.append(str(num))
    
    # 用空格连接质数字符串列表
    return " ".join(primes)

+

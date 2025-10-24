import math

def PrimeList(N):
    """
    使用埃拉托斯特尼筛法生成小于N的所有质数，并以空格分隔的字符串形式返回。
    
    参数:
        N (int): 正整数
        
    返回:
        str: 包含所有小于N的质数的字符串，以空格分隔
    """
    # 处理边界情况
    if N <= 2:
        return ""
    
    # 初始化标记数组，长度为N
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    
    # 埃拉托斯特尼筛法核心算法[1](@ref)[2](@ref)
    # 只需检查到sqrt(N)即可[1](@ref)[4](@ref)
    for i in range(2, int(math.sqrt(N)) + 1):
        if is_prime[i]:
            # 标记i的所有倍数为非质数[1](@ref)[2](@ref)
            # 从i*i开始标记，因为更小的倍数已经被更小的质数标记过了
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = []
    for num in range(2, N):
        if is_prime[num]:
            primes.append(str(num))
    
    return " ".join(primes)

def main():
    """
    主函数：提供命令行交互界面，接收用户输入并显示结果
    """
    print("质数生成器")
    print("输入一个正整数，程序将输出所有小于该数的质数")
    print("输入 'exit' 或 'quit' 退出程序\n")
    
    while True:
        user_input = input("请输入一个整数 (或输入 'exit' 退出): ").strip()
        
        # 检查退出条件
        if user_input.lower() in ['exit', 'quit']:
            print("程序已退出，谢谢使用！")
            break
        
        # 验证输入是否为有效正整数
        if not user_input.isdigit():
            print("错误：请输入一个有效的正整数！\n")
            continue
        
        N = int(user_input)
        
        if N <= 0:
            print("错误：请输入一个大于0的正整数！\n")
            continue
        
        # 调用PrimeList函数并显示结果
        result = PrimeList(N)
        
        if result:
            print(f"小于 {N} 的所有质数为:")
            print(result)
        else:
            print(f"小于 {N} 的质数不存在")
        
        print()  # 空行分隔

# 如果直接运行此脚本，则执行主函数
if __name__ == "__main__":
    main()

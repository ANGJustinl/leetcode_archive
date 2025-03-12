# 难度超出预期，还得努力啊 25.3.12
from typing import List

a = 2147483647
b = [2,0,0]
MOD = 1337  # 题目要求的取模数

from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337  # 题目要求的取模值
        
        # 快速幂计算 (base^exponent) % MOD
        def quickPow(base, exponent):
            result = 1
            base %= MOD  # 先取模，防止数据过大
            while exponent:
                if exponent & 1:  # 如果当前指数是奇数
                    result = result * base % MOD
                base = base * base % MOD  # 基数平方
                exponent >>= 1  # 指数右移，相当于除以 2
            return result
        
        # 如果 a ≡ 1 (mod MOD)，则 a^b ≡ 1 (mod MOD)
        if a % MOD == 1:
            return 1
        
        total_power = 1  # 计算结果
        
        # 计算 a^b mod 1337，其中 b 是数组
        for digit in b:
            # 数学公式： (a^b[0...i-1])^10 * a^b[i]
            total_power = quickPow(total_power, 10) * quickPow(a, digit) % MOD
        
        return total_power


if __name__ == '__main__':
    s = Solution()
    result = s.superPow(a, b)
    print(result)
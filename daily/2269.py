# 美丽值 = 一个整数 num  中符合 长度 = k, 能整除 num 数目 25.3.10

num = 430043
k = 2

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        count = 0
        for i in range(len(str_num) - k + 1):
            substring = str_num[i:i+k]
            if int(substring) != 0 and num % int(substring) == 0:
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    result = s.divisorSubstrings(num, k)
    print(result)
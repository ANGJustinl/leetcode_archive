# 不太好，ai的 25.3.11
from typing import List

nums = [2,4,6,4]

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_min = [0] * n  # 后缀最小值数组
        suf = nums[-1]  # 后缀最小

        # 计算后缀最小值数组
        for i in range(n - 2, -1, -1):
            suffix_min[i] = suf
            if nums[i] < suf:
                suf = nums[i]

        pre = nums[0]  # 前缀最大
        res = 0

        # 一边计算前缀最大，一边计算美丽值
        for i in range(1, n - 1):
            if nums[i] > pre and nums[i] < suffix_min[i]:
                res += 2  # 满足条件1，美丽值加2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                res += 1  # 满足条件2，美丽值加1
            if pre < nums[i]:
                pre = nums[i]  # 更新最大

        return res

if __name__ == "__main__":
    s = Solution()
    res = s.sumOfBeauties(nums)
    print(res)
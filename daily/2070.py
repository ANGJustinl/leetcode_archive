# 先排序，找到第一个满足的price，然后取最大的那个beauty 25.3.9

import time
import bisect
from typing import List
from operator import itemgetter

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
output = [2,4,5,5,6,6]

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=itemgetter(0))

        prices = []
        beauties = []
        max_beauty = 0
        for price, beauty in items:
            if beauty > max_beauty:  # 只在最大美丽值变化时才存储
                max_beauty = beauty
                prices.append(price)
                beauties.append(max_beauty)

        ans = []
        for query in queries:
            idx = bisect.bisect_right(prices, query) - 1  # 找到满足 price <= query 的最大索引
            ans.append(beauties[idx] if idx >= 0 else 0)
        return ans


if __name__ == '__main__':
    solution = Solution()
    s_t = time.time()
    result = solution.maximumBeauty(items, queries)
    e_t = time.time() - s_t
    assert result == output
    print(f"pass (Execution time: {e_t:.6f} seconds)")
# 比较忙，参考题解。25.3.13

word = "iqeaouqi"
k = 2

from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        cnt_vowel1 = defaultdict(int)  # 记录窗口1中的元音频次
        cnt_vowel2 = defaultdict(int)  # 记录窗口2中的元音频次
        cnt_consonant1 = cnt_consonant2 = 0  # 记录窗口1和窗口2中的辅音个数
        ans = left1 = left2 = 0  # 结果计数 & 两个左指针

        for b in word:  # 遍历字符串，每次扩展右窗口
            if b in "aeiou":  # 如果是元音
                cnt_vowel1[b] += 1
                cnt_vowel2[b] += 1
            else:  # 如果是辅音
                cnt_consonant1 += 1
                cnt_consonant2 += 1

            # **窗口1（left1）：寻找 “>= k” 的窗口**
            while len(cnt_vowel1) == 5 and cnt_consonant1 >= k:
                out = word[left1]
                if out in "aeiou":
                    cnt_vowel1[out] -= 1
                    if cnt_vowel1[out] == 0:
                        del cnt_vowel1[out]  # 如果元音计数变为0，移除它
                else:
                    cnt_consonant1 -= 1
                left1 += 1  # 移动窗口左边界

            # **窗口2（left2）：寻找 “> k” 的窗口**
            while len(cnt_vowel2) == 5 and cnt_consonant2 > k:
                out = word[left2]
                if out in "aeiou":
                    cnt_vowel2[out] -= 1
                    if cnt_vowel2[out] == 0:
                        del cnt_vowel2[out]
                else:
                    cnt_consonant2 -= 1
                left2 += 1  # 移动窗口左边界

            # 关键：所有满足 "== k" 的子串数量 = `left1 - left2`
            ans += left1 - left2

        return ans
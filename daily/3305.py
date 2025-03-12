# 一开始用的辅音list长度是否等于k，然后发现这个题目不是固定长度遍历。。。 25.3.12

word = "iqeaouqi"
k = 2


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        count = 0
        n = len(word)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        # 遍历所有可能的子串
        for i in range(n):
            # 记录当前子串中的元音和辅音
            current_vowels = set()
            consonants_count = 0
            
            for j in range(i, n):
                if word[j] in vowels:
                    current_vowels.add(word[j])
                else:
                    consonants_count += 1
                
                # 检查是否满足所有条件
                if len(current_vowels) == 5 and consonants_count == k:
                    count += 1
                
                # 如果辅音数量超过k，就没必要继续扩展子串，结束就行
                if consonants_count > k:
                    break
                    
        return count

if __name__ == '__main__':
    s = Solution()
    result = s.countOfSubstrings(word, k)
    print(result)
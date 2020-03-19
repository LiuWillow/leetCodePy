# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"
# b a b a b
# 012345678  下标从1开始遍历，0-2*(n-1)
class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        if length == 0:
            return ""
        if length == 1:
            return s
        indexMax = 2 * (length - 1)
        begin = 1
        longest = 1
        resultL = 0
        resultR = 0
        for i in range(begin, indexMax):
            notTowPlus = i % 2 == 1
            l = int(i / 2) if notTowPlus else int(i / 2) - 1
            r = int(i / 2) + 1 if notTowPlus else int(i / 2) + 1
            while(l >= 0 and r < length):
                if s[l] == s[r]:
                    l = l - 1
                    r = r + 1
                    continue
                else:
                    break
            if longest < r - l - 1:
                resultL = l
                resultR = r
                longest = r - l - 1
            
        if longest == 1:
            return s[0]
        return s[resultL + 1: resultR]
        

result = Solution().longestPalindrome("abbabbaacbbcaa")
print(result)

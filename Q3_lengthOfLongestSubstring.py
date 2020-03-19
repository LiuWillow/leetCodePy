# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# a b c d
# 0123456
#  l   r
# 输入: "pwwpkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if length <= 1:
            return length
        dic = {}
        maxLen = 1
        l = r = 0
        while(l < length and r < length):
            cha = s[r]
            if cha in dic:
                l = max(dic[cha], l)
            maxLen = max(r - l + 1, maxLen)
            dic[cha] = r + 1
            r += 1
        return maxLen


str = "tmmzuxt"
print(Solution().lengthOfLongestSubstring(str))
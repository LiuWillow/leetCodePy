# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:

# 所有输入只包含小写字母 a-z 。
class Solution(object):
    def longestCommonPrefix(self, strs):
        length = len(strs)
        if length == 0:
            return ""
        common = strs[0]
        for i in range(1, length):
            # str.find(s)  返回的是s的第一个字符在str中的位置，并且后续的字符串也是完全一致，否则返回-1
            while strs[i].find(common) != 0:
                common = common[:-1]
        return common


    # 下面是分治的方式
    def longestCommonPrefixDepart(self, strs):
        return self.longestCommonPrefixChild(strs, 0, len(strs) - 1)
    
    def longestCommonPrefixChild(self, strs, begin, end):
        if end - begin == 1:
            return self.commonTwo(strs[begin], strs[end])
        if end == begin:
            return strs[begin]
        mid = begin + int((end - begin) / 2)
        leftCommon = self.longestCommonPrefixChild(strs, begin, mid)
        rightCommon = self.longestCommonPrefixChild(strs, mid + 1, end)
        return self.commonTwo(leftCommon, rightCommon)

    def commonTwo(self, strLeft, strRight):
        while strRight.find(strLeft) != 0:
            strLeft = strLeft[:-1]
        return strLeft
    
    # 分治结束

print(Solution().longestCommonPrefixDepart(["sdfdsf", "sdf", "sdf"]))
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true
# 示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:

# 输入: "(]"
# 输出: false
# 示例 4:

# 输入: "([)]"
# 输出: false
# 示例 5:

# 输入: "{[]}"
# 输出: true
# ()(({{{()}}}}))
class Solution(object):
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        leftDic = {"(" : 1, "[":2, "{":3}
        rightDic = {")" : 1, "]":2, "}":3}
        leftStack = []

        for c in s:
            if c in leftDic:
                leftStack.append(c)
            else:
                if len(leftStack) == 0:
                    return False
                lc = leftStack.pop()
                lIndex = leftDic[lc]
                rIndex = rightDic[c]
                if lIndex != rIndex:
                    return False
        return True if len(leftStack) == 0 else False

print(Solution().isValid("()(({{{()}}}))"))

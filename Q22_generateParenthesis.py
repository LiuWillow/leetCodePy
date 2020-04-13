# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# 回溯
# stack 已经放进去的左边的括号
# c 即将要放进去的括号
# resultList 返回的列表结果
# str 当前组装到一半的str
# f(stack, c, resultList, str, n)
# 返回条件：str.length == 2 * n || 不符合括号规则
# 要加入resultList的条件：str.len == 2 * n && stack.len == 0
class Solution(object):
    leftDic = {"(" : 1, "[":2, "{":3}
    rightDic = {")" : 1, "]":2, "}":3}

    def generateParenthesis(self, n):
        stack = []
        if n == 0:
            return stack
        resultList = []
        self.f(stack, "(", resultList, "", n)
        return resultList

    def f(self, stack, c, resultList, str, n):
        isRight = c in self.rightDic
        stackLen = len(stack)
        if isRight:
            if stackLen == 0:
                return
            else:
                lC = stack.pop()
                lIndex = self.leftDic[lC]
                rIndex = self.rightDic[c]
                if lIndex == rIndex:
                    str = str + c
                    if len(str) == 2 * n and len(stack) == 0:
                        resultList.append(str)
                        return
                    else:
                        self.f(stack, "(", resultList, str, n)
                        self.f(stack, ")", resultList, str, n)
                else:
                    # 放回去
                    stack.append(lC)
                    return
        else:
            # 如果是左括号，判断是不是最后一个了，是的话表示不符合规则
            if len(str) == 2 * n - 1:
                return
            else:
                stack.append(c)
                str = str + c
                self.f(stack, "(", resultList, str, n)
                self.f(stack, ")", resultList, str, n)

print(Solution().generateParenthesis(2))

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        tempResult = result
        carry = 0
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = 1 if sum > 9 else 0
            result.next = ListNode(sum % 10) 
            result = result.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry > 0:
            result.next = ListNode(1)
        return tempResult.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = Solution().addTwoNumbers(l1, l2)

while(result):
    print(result.val)
    result = result.next
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

#  

# 示例:

# 给定 1->2-
# >3->4, 你应该返回 2->1->4->3.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            next = head.next
            nextHead = next.next
            next.next = head
            head.next = self.swapPairs(nextHead)
            return next
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
temp = Solution().swapPairs(head)
while temp:
    print(temp.val)
    temp= temp.next

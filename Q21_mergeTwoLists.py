# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        tempHead = head
        while l1 or l2:
            if l1 is None:
                tempHead.next = l2
                break
            if l2 is None:
                tempHead.next = l1
                break
            if l1.val > l2.val:
                tempHead.next = ListNode(l2.val)
                l2 = l2.next
                tempHead = tempHead.next
                continue
            else:
                tempHead.next = ListNode(l1.val)
                l1 = l1.next
                tempHead = tempHead.next
        
        return head.next
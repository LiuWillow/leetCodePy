# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。
# 进阶：
# 你能尝试使用一趟扫描实现吗？

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        duilie = [None] * (n+1)
        #  大小为n
        currentIndex = 0
        

        tempHead = head
        limit = n
        while tempHead:
            duilie[currentIndex] = tempHead
            if currentIndex == limit:
                currentIndex = 0
            else:
                currentIndex += 1
            tempHead = tempHead.next

        currentIndex = currentIndex - 1 if currentIndex > 0 else n
        daoshuIndex = currentIndex - n + 1 if currentIndex - n + 1 >= 0 else currentIndex - n + 2 + limit
        daoshuN = duilie[daoshuIndex]
        qianmianIndex = daoshuIndex - 1 if daoshuIndex > 0 else limit
        qianmian = duilie[qianmianIndex]
    
        if qianmian:
            qianmian.next = daoshuN.next
            daoshuN.next = None
        else:
            return head.next
        return head
        
    def createNode(self, n):
        head = ListNode(0)
        tempHead = head
        for i in range(1, n+1):
            tempHead.next = ListNode(i)
            tempHead = tempHead.next
        return head.next

head = Solution().createNode(10)

result = Solution().removeNthFromEnd(head, 7)
while result:
    print(result.val)
    result = result.next
    
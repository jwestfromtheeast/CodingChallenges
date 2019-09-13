# Leetcode 206
class Solution:
    def helper(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.helper(next, head)
        
    def reverseListR(self, head: ListNode) -> ListNode:
        return self.helper(head, None)
            
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = None
        while head is not None:
            next = head.next
            head.next = newHead
            newHead = head
            head = next
        return newHead
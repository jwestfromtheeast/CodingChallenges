# Leetcode 141
class Solution:
    # Complexity O(n) time O(n) space
    def hasCyclee(self, head: ListNode) -> bool:
        if not head:
            return False
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    
    # Complexity O(n) time O(1) space
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
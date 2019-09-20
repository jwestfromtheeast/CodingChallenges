# Leetcode 142
class Solution:
    # Complexity O(n) time O(n) space
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = set()
        while head:
            if head in prev:
                return head
            prev.add(head)
            head = head.next
        return None

    # Complexity O(n) time O(1) space
    # Explanation for inner loop: Once you know a cycle exists,
    # Start at the head and increment that and slow (which is at the cycle) until
    # they are at the same spot. This must be where the cycle begins
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while (slow != slow2):
                    slow = slow.next
                    slow2 = slow2.next
                return slow2
        return None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Idea: Want to do this in O(1) space. Simply make separate lists of odd and even nodes
    # Then, combine them
    # Complexity: Time O(n) Space O(1)
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        oddHead = ListNode(-1)
        evenHead = ListNode(-2)
        oddCurr, evenCurr = oddHead, evenHead
        isOdd = True
        while head:
            if isOdd:
                oddCurr.next = head
                oddCurr = oddCurr.next
            else:
                evenCurr.next = head
                evenCurr = evenCurr.next
            head = head.next
            isOdd = not isOdd
        evenCurr.next = None
        oddCurr.next = evenHead.next
        return oddHead.next
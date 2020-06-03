# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Complexity: O(1) time, in-place so no space used
    # Logic: This question is fairly unintuitive, and I didn't understand it at first. When you do,
    # realize you can simply move the next node value to the current one, then splice out the next node.
    # This effectively removes the current node. The edge cases are already taken care of for you.
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

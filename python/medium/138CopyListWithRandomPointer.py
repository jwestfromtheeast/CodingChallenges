"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    # Rationale: Make a new node for every node in original, where the new node is value to a key of the original
    # On the second pass, move all of the pointers in each node to the proper spot in memory
    # Complexity: Time O(n), Space O(n)
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copy = {}
        temp1 = temp2 = head
        while temp1:
            copy[temp1] = Node(temp1.val, temp1.next, temp1.random)
            temp1 = temp1.next
        while temp2:
            copy[temp2].next = copy.get(temp2.next, None)
            copy[temp2].random = copy.get(temp2.random, None)
            temp2 = temp2.next
        return copy[head]
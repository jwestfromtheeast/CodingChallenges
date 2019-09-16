# Leetcode 200
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # O(n) time, O(n) space
    # Concise, elegant recursive solution
    def isSameTreeR(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTreeR(p.left, q.left) and self.isSameTreeR(p.right, q.right)
    
    # Iterative solution, a bit more messy, in case you are ever asked to solve iteratively
    # Requires a queue to keep track of each tree
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        p_queue = deque()
        q_queue = deque()
        p_queue.append(p)
        q_queue.append(q)
        while p_queue and q_queue:
            p = p_queue.popleft()
            q = q_queue.popleft()
            if p.val != q.val:
                return False
            if p.left and q.left:
                p_queue.append(p.left)
                q_queue.append(q.left)
            elif p.left or q.left:
                return False
            if p.right and q.right:
                p_queue.append(p.right)
                q_queue.append(q.right)
            elif p.right or q.right:
                return False
        return True
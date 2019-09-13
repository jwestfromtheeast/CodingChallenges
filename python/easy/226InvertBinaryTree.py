# Leetcode 226
from collections import deque
class Solution:
    # Recursive
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        left = root.left
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root
    
    # Iterative via BFS with queue
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        queue = deque([root])
        oroot = root
        while queue:
            root = queue.popleft()
            root.left, root.right = root.right, root.left
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
        return oroot
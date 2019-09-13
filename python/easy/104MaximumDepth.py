# Leetcode 104
from collections import deque
class Solution:
    # Iterative solution
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while len(queue) > 0:
            curr = len(queue)
            while curr > 0:
                root = queue.popleft()
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
                curr -= 1
            depth += 1
        return depth
    
    # Recursive solution
    def maxDepthR(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepthR(root.left), self.maxDepthR(root.right))
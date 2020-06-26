# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Complexity: O(n) time [each node added once], O(n) space
    # Iterative solution, use a stack and visit as far left as possible. Process after visiting
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        vals = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            vals.append(curr.val)
            curr = curr.right
        return vals

    # Trivial recursive solution, where you follow the inorder principle of operating on left, root, right in that order
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        vals = []

        def helper(curr):
            if curr:
                helper(curr.left)
                vals.append(curr.val)
                helper(curr.right)
        helper(root)
        return vals

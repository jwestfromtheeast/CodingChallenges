# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # Idea: Recursively prune the left and right children of the current node
    # Complexity: Time O(n), Space O(h) (height of tree)
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if not root.val and not root.left and not root.right:
            return None
        else:
            return root
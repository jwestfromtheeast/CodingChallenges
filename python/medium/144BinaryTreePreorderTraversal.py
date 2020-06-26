# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Complexity: O(n) time, O(n) space
    # Iterative solution, use a stack to naturally traverse through the tree. Process the current value while moving as far left as possible to
    # ensure the preorder definition of root, left, right
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        vals = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                vals.append(curr.val)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return vals

    # Trivial recursive solution, always follow the preorder order of visiting of root, left, right
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nums = []

        def helper(curr):
            if curr:
                nums.append(curr.val)
                helper(curr.left)
                helper(curr.right)
        helper(root)
        return nums

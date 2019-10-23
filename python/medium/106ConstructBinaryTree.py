# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # See 105 first if you have not.
    # Here, you must recurse the right side before the left due to it being postorder this time.
    # Complexity: O(n^2) time O(n) space. TODO improvement: Shorten the ind line, as it has to find the index each time. Use a map to store in advance + helper func.
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind + 1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
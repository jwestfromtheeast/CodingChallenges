# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # You know the first index of preorder will be the root, work from there
    # Complexity: O(n^2) time O(n) space. TODO improvement: Shorten the ind line, as it has to find the index each time. Use a map to store in advance + helper func.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # Technically this pop is an O(n) operation. Conversion to a deque would make this O(1), which we can assume
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
class Solution:
    # Complexity: O(logn) time, O(logn) space [recursion depth]
    # Logic: Use the concept of a binary search tree. If we have found the value, return it.
    # If the root is null, the value doesn't exist in the tree, so return that null root.
    # Otherwise, compare value to the current value and move accordingly. If root val < target,
    # go right to find a larger value, else go left.
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        return self.searchBST(root.right, val) if root.val < val else self.searchBST(root.left, val)

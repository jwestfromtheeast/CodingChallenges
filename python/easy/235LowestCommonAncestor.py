# Leetcode 235
class Solution:
    # Complexity: Time O(n) Space O(n) (unbalanced tree visit all nodes)
    # Recursive approach
    def lowestCommonAncestorR(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorR(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorR(root.right, p, q)
        return root
    
    # Complexity: Time O(n) Space O(1)
    # Iterative approach
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Complexity: O(n) time, O(h) space [height of the tree, worst case could be O(n) for completely unbalanced]
    # Logic: Perform a dfs using a stack, or a bfs using a queue, or a recursive solution. Except, instead of just appending the nodes, append a tuple
    # of the node and the accumulated value. If you have hit a leaf node [by definition, no child nodes], add the current value to the total.
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        total = 0
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                total += val
            if curr.left:
                stack.append((curr.left, val * 10 + curr.left.val))
            if curr.right:
                stack.append((curr.right, val * 10 + curr.right.val))
        return total

    # Queue bfs version (same idea as above)
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = collections.deque([(root, root.val)])
        total = 0
        while q:
            curr, val = q.popleft()
            if not curr.left and not curr.right:
                total += val
            if curr.left:
                q.append((curr.left, val * 10 + curr.left.val))
            if curr.right:
                q.append((curr.right, val * 10 + curr.right.val))
        return total

    # Recurisve solution
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        # Note that here we have to slightly modify the logic for accumulating the total, since we cannot guarantee curr.left and curr.right exist when making recursive calls
        # (and thus cannot access curr.left.val and curr.right.val as we did in the iterative solution)

        def dfs(curr, accum):
            if curr:
                if not curr.left and not curr.right:
                    self.total += accum * 10 + curr.val
                dfs(curr.left, accum * 10 + curr.val)
                dfs(curr.right, accum * 10 + curr.val)
        dfs(root, 0)
        return self.total

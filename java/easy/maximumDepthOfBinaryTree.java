// Leetcode 104
import java.util.*;

class Solution {
    // Simple recursive solution
    // O(n) time O(h) space height of tree
    public int maxDepthR(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(1 + maxDepthR(root.left), 1 + maxDepthR(root.right));
    }
    
    // Iterative solution using BFS via queue
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        // Simple implementation of Queue in Java is to use a LinkedList with Queue interface
        Queue<TreeNode> queue = new LinkedList<>();
        int maxd = 0;
        queue.offer(root);
        while (!queue.isEmpty()) {
            // The size of the queue here represents a "level" of the tree
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                root = queue.poll();
                if (root.left != null) {
                    queue.offer(root.left);
                }
                if (root.right != null) {
                    queue.offer(root.right);
                }
            }
            // After finishing a level, the depth increases by one as you move to the next level
            maxd++;
        }
        return maxd;
    }
}
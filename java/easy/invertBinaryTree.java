// Leetcode 226
import java.util.*;

class Solution {
    // Recursive, very simple
    public TreeNode invertTreeR(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode left = root.left;
        TreeNode right = root.right;
        root.left = invertTreeR(right);
        root.right = invertTreeR(left);
        return root;
    }
    
    // Iterative with queue, bfs of tree
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return root;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        TreeNode curr = root;
        while (!q.isEmpty()) {
            curr = q.poll();
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            if (curr.left != null) {
                q.offer(curr.left);
            }
            if (curr.right != null) {
                q.offer(curr.right);
            }
        }
        return root;
    }
}
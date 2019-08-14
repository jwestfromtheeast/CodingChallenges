//Leetcode 236. Lowest Common Ancestor of a Binary Tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class RecursiveSolution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL) return NULL; //empty tree
        if(root == p || root == q) return root; //found a target
        
        TreeNode* left = lowestCommonAncestor(root->left, p, q); //create recursion on the left child
        TreeNode* right = lowestCommonAncestor(root->right, p, q); //create recursion on the right child
        
        if(left != NULL && right != NULL) return root; //something here
        if(left == NULL && right == NULL) return NULL; //nothing here
        
        return left != NULL ? left : right; //else, return the non-null child
    }
};

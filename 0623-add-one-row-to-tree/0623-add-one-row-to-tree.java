/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            TreeNode newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        }
        return addHelper(root, val, depth, 1);
    }

    public TreeNode addHelper(TreeNode root, int val, int depth, int curr)
    {
        if (root == null)
            return null;
        
        if (curr == depth - 1) {
            TreeNode leftTemp = root.left;
            TreeNode rightTemp = root.right;

            root.left = new TreeNode(val);
            root.right = new TreeNode(val);
            root.left.left = leftTemp;
            root.right.right = rightTemp;

            return root;
        }

        root.left = addHelper(root.left, val, depth, curr + 1);
        root.right = addHelper(root.right, val, depth, curr + 1);

        return root;
    }
}
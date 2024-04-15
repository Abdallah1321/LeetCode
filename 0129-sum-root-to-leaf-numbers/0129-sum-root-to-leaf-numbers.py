# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        def depthFirst(node, total):
            if not node:
                return 0

            total = (total * 10) + node.val
            
            if not node.left and not node.right:
                return total
            return depthFirst(node.left, total) + depthFirst(node.right, total)
        
        return depthFirst(root, 0)

        
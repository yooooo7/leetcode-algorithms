# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root) -> list:
        l = []
        if root is None:
            return []
        
        l += self.inorderTraversal(root.left)
        l += [root.val]
        l += self.inorderTraversal(root.right)
        
        return l
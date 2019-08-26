# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root) -> list:
        l = []
        
        if root is None:
            return []
        
        l += [root.val]
        l += self.preorderTraversal(root.left)
        l += self.preorderTraversal(root.right)
        
        return l
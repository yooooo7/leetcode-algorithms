# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root) -> list:
        l = []
        
        if root is None:
            return []
        
        l += self.postorderTraversal(root.left)
        l += self.postorderTraversal(root.right)
        l += [root.val]
        
        return l
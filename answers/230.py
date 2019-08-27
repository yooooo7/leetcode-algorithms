# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l = self.midSort(root)
        return l[k-1]
    
    def midSort(self, root: TreeNode) -> list:
        l = []
        
        if root is None:
            return []
        
        l += self.midSort(root.left)
        l += [root.val]
        l += self.midSort(root.right)
        
        return l
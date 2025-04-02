# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], s=0) -> int:
        if not root:
            return 0
        s = s*10+root.val
        if not root.left and not root.right:
            return s
        return self.sumNumbers(root.left,s)+self.sumNumbers(root.right,s)

'''SOLVED BY ADIT MUGDHA DAS'''
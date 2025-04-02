# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.p=None
        self.m=float('inf')
        def dfs(n):
            if not n:
                return
            dfs(n.left)
            if self.p is not None:
                self.m=min(self.m, n.val-self.p)
            self.p=n.val
            dfs(n.right)
        dfs(root)
        return self.m

'''SOLVED BY ADIT MUGDHA DAS'''
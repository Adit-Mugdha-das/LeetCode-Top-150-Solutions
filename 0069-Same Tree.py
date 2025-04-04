# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(s, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val !=q.val:
            return False
        return s.isSameTree(p.left,q.left) and s.isSameTree(p.right,q.right)

'''SOLVED BY ADIT MUGDHA DAS'''
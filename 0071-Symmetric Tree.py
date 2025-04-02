# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(s, root: TreeNode) -> bool:
        def sym(l: TreeNode, r: TreeNode) -> bool:
            if not l and not r:
                return True
            if not l or not r or l.val !=r.val:
                return False
            return sym(l.left,r.right) and sym(l.right,r.left)
        return sym(root.left,root.right) if root else True

'''SOLVED BY ADIT MUGDHA DAS'''
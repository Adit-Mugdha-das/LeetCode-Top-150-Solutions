# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(s, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left,root.right=s.invertTree(root.right),s.invertTree(root.left)
        return root

'''SOLVED BY ADIT MUGDHA DAS'''
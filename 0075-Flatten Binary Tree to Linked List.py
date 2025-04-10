# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur=root
        while cur:
            if cur.left:
                pre=cur.left
                while pre.right:
                    pre=pre.right
                pre.right=cur.right
                cur.right=cur.left
                cur.left=None
            cur=cur.right
            
'''SOLVED BY ADIT MUGDHA DAS'''
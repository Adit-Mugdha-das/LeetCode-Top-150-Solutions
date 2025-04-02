# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(s, pre: List[int], ino: List[int]) -> Optional[TreeNode]:
        if not pre or not ino:
            return None
        r=TreeNode(pre[0])
        i=ino.index(pre[0])
        r.left=s.buildTree(pre[1:i+1],ino[:i])
        r.right=s.buildTree(pre[i+1:],ino[i+1:])
        return r
    
'''SOLVED BY ADIT MUGDHA DAS'''
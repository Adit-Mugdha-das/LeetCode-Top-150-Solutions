# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(s, ino: List[int], post: List[int]) -> Optional[TreeNode]:
        if not ino or not post:
            return None
        r=TreeNode(post.pop())
        i=ino.index(r.val)
        r.right=s.buildTree(ino[i+1:],post)
        r.left=s.buildTree(ino[:i],post)
        return r

'''SOLVED BY ADIT MUGDHA DAS'''
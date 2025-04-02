# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return
        res=[]
        q=deque([root])
        while q:
            n=len(q)
            tmp=0
            edges=0
            for i in range(n):
                node=q.popleft()
                tmp+=node.val
                edges+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp/edges)
        return res
    
'''SOLVED BY ADIT MUGDHA DAS'''
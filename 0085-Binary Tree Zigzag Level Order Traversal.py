# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque([root])
        count=0
        while q:
            n=len(q)
            tmp=[]
            for i in range(n):
                node=q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count%2==1:
                tmp.reverse()
            res.append(tmp)
            count+=1
        return res
        
'''SOLVED BY ADIT MUGDHA DAS'''
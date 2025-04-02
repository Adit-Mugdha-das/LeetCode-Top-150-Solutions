"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isuni(x1,y1,x2,y2):
            val=grid[x1][y1]
            for i in range(x1,x2):
                for j in range(y1,y2):
                    if grid[i][j] !=val:
                        return False,-1
            return True,val

        def build(x1,y1,x2,y2):
            uni,val=isuni(x1,y1,x2,y2)
            if uni:
                return Node(val=bool(val),isLeaf=True)
            midx=(x1+x2)//2
            midy=(y1+y2)//2
            return Node(
                val=True,
                isLeaf=False,
                topLeft=build(x1,y1,midx,midy),
                topRight=build(x1,midy,midx,y2),
                bottomLeft=build(midx,y1,x2,midy),
                bottomRight=build(midx,midy,x2,y2)
            )
        n=len(grid)
        return build(0,0,n,n)
    
    '''SOLVED BY ADIT MUGDHA DAS'''
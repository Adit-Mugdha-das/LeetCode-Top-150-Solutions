"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        vis={}
        vis[node]=Node(node.val)
        queue=deque([node])
        while queue:
            cur=queue.popleft()
            for nei in cur.neighbors:
                if nei not in vis:
                    vis[nei]=Node(nei.val)
                    queue.append(nei) 
                vis[cur].neighbors.append(vis[nei])
        return vis[node]
    
'''SOLVED BY ADIT MUGDHA DAS'''
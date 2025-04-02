"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(s, root: 'Node') -> 'Node':
        if not root:
            return None
        q=deque([root])
        while q:
            size=len(q)
            for i in range(size):
                cur=q.popleft()
                if i<size-1:
                    cur.next=q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
    
'''SOLVED BY ADIT MUGDHA DAS'''
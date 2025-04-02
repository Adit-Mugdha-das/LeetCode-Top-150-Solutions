"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val=int(x)
        self.next=next
        self.random=random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur=head
        while cur:
            nnode=Node(cur.val,cur.next)
            cur.next=nnode
            cur=nnode.next
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        cur=head
        chead=head.next
        ccur=chead
        while cur:
            cur.next=cur.next.next
            if ccur.next:
                ccur.next=ccur.next.next
            cur=cur.next
            ccur=ccur.next
        return chead

'''SOLVED BY ADIT MUGDHA DAS'''
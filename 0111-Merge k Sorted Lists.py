# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        for i,l in enumerate(lists):
            if l:
                heappush(h, (l.val,i,l))
        d=r=ListNode()
        while h:
            v,i,n=heappop(h)
            r.next=n
            r=r.next
            if n.next:
                heappush(h,(n.next.val,i,n.next))
        return d.next
    
'''SOLVED BY ADIT MUGDHA DAS'''
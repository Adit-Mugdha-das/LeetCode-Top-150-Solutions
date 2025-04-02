# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, h: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not h or not h.next or k==0:
            return h
        l=1
        c=h
        while c.next:
            c=c.next
            l +=1
        c.next=h
        k=k%l
        s=l-k
        t=h
        for _ in range(s-1):
            t=t.next
        nh=t.next
        t.next=None
        return nh

'''SOLVED BY ADIT MUGDHA DAS'''
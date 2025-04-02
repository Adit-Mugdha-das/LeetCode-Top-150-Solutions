# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, h: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1=l2=ListNode(0)
        r1=r2=ListNode(0)
        while h:
            if h.val<x:
                l2.next=h
                l2=l2.next
            else:
                r2.next=h
                r2=r2.next
            h=h.next
        r2.next=None
        l2.next=r1.next
        return l1.next

'''SOLVED BY ADIT MUGDHA DAS'''
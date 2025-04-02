# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        first=sec=dummy
        for i in range(n + 1):
            first=first.next
        while first:
            first,sec=first.next,sec.next
        sec.next=sec.next.next
        return dummy.next
    
'''SOLVED BY ADIT MUGDHA DAS'''
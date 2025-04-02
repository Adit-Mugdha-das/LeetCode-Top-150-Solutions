# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, current=None, head
            while k:
                future=current.next
                current.next=prev
                prev=current
                current=future
                k-=1
            return prev
        count=0
        ptr=head
        while ptr and count<k:
            count+= 1
            ptr=ptr.next
        if count < k:
            return head
        new_head = reverse(head, k)
        head.next=self.reverseKGroup(ptr, k)
        return new_head
'''SOLVED BY ADIT MUGDHA DAS'''
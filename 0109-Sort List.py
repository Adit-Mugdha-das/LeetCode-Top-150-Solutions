# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid=self.getMiddle(head)
        rhead=mid.next
        mid.next=None
        lsorted=self.sortList(head)
        rsorted=self.sortList(rhead)
        return self.mergeTwoLists(lsorted,rsorted)
    def getMiddle(self, head: ListNode) -> ListNode:
        slow,fast=head,head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 if l1 else l2
        return dummy.next
    
    '''SOLVED BY ADIT MUGDHA DAS'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        #Right pointer move to n Node so that when it reaches last node left will point to nth node from end
        while n>0 and right:
            right=right.next
            n-=1

        while right:
            left=left.next
            right=right.next
        left.next= not left.next

        return dummy.next
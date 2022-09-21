from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr:
            if curr.val=='chk':
                return curr
            curr.val="chk"
            curr=curr.next
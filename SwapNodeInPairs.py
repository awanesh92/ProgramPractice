# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode(-1)
        node.next=head
        prev,p=node,head
        while p!=None and p.next!= None:
            q,r=p.next,p.next.next
            prev.next=q
            q.next=p
            p.next=r
            prev=p
            p=r

        return node.next

s=Solution()


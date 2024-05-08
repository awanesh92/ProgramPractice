from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        stk=[]
        while curr:
            while stk and stk[-1].val<curr.val:
                stk.pop()
            stk.append(curr)
            curr=curr.next
        nxt=None
        while stk:
            curr=stk.pop()
            curr.next=nxt
            nxt=curr
        print(curr)
        return curr
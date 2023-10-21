from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            None

        fast,slow=head,head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next

        mid=slow

        prev,curr=None,mid

        while curr:
            curr.next,curr,prev=prev,curr.next,curr

        sec_rev=prev

        first,second=head,sec_rev

        while second.next:
            next_hop=first.next
            first.next=second
            first=next_hop

            next_hop=second.next
            second.next=first
            second=next_hop
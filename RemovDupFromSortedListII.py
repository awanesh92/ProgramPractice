# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        result=ListNode(None,None) #Set dummy value
        result.next=head
        prev=result
        curr=head
        while curr and curr.next:
            if curr.next.val==curr.val: #check it like this so that we can point the current value to None if its no longer duplicate
                # and the curr value will be the new non-dup value
                while curr.next and curr.next.val==curr.val:
                    curr=curr.next
                curr.next,curr=None,curr.next
                print(curr.val)
                prev.next=curr
            else:
                prev=curr
                curr=curr.next
        return result.next
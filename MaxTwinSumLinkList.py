from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stk=[]
        track=head
        n=0
        while track:
            track=track.next
            n+=1
        track=head
        i=0
        while track:
            if i>=n//2:
                stk.append(track.val)
            i+=1
            track=track.next
        #main calculation
        n_max=0
        track=head
        while stk:
            n_max=max(n_max,track.val+stk.pop())
            track=track.next

        return n_max
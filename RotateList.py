from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not temp:
            return
        #To keep the initial pointer
        dummy=ListNode(0,head)
        temp=right=head
        left=dummy
        cnt=0
        #To count the rotation if the k values is more than the no of elements in list
        while temp:
            temp=temp.next
            cnt+=1
        k%=cnt
        while k>0 and right:
            right=right.next
            k-=1
        #To get to the last element of the left along with left element where we want to rotate it
        while right:
            t=right  #to store the rightmost element as after exit the value will be None
            left=left.next
            right=right.next
        #Calculation of pointing the last elemnent to head and new head pointer
        t.next=head
        head=left.next
        left.next=None

        return head
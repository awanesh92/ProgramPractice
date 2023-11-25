from typing import Optional# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''    arr=[]
        if not head:
            return None
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in arr:
            temp=ListNode(i)
            curr.next=temp
            curr=temp
        return dummy.next '''
        # Approach 2
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right

        return dummy.next
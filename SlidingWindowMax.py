from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        md=deque()
        res=[]

        for i,num in enumerate(nums):
            while md and md[0]<i-k+1:
                md.popleft()

            while md and nums[md[-1]]<num:
                md.pop()

            md.append(i)

            if i-k+1>=0:
                res.append(nums[md[0]])

        return res

s=Solution()
assert [3,3,5,5,6,7]==s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
assert [1]==s.maxSlidingWindow([1],1)
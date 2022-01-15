from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=nums[:k]
        heapq.heapify(h)
        for i in range(k,len(nums)):
            if nums[i]>h[0]:
                heapq.heapreplace(h,nums[i])
        return h[0]

s=Solution()
assert 5==s.findKthLargest([3,2,1,5,6,4],2)
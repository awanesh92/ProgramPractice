from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0

        for i in nums:
            if currsum < 0:
                currsum = 0
            currsum += i
            maxsum = max(maxsum, currsum)

        return maxsum

s=Solution()
assert 6==s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
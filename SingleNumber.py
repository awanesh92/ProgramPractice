from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=nums[0]
        for i in range(1,len(nums)):
            c^=nums[i]
        return c

s=Solution()
assert 1==s.singleNumber([2,2,1])
assert 4==s.singleNumber([4,1,2,1,2])
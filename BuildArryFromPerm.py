from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[x]] for x in range(len(nums))]

s=Solution()
assert [0,1,2,4,5,3]==s.buildArray([0,2,1,5,3,4])
assert [4,5,0,1,2,3]==s.buildArray([5,0,1,2,3,4])
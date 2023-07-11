from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt=1
        l=1
        for r in range(1,len(nums)):
            if nums[r]==nums[r-1]:
                cnt+=1
            else:
                cnt=1
            if cnt<=2:
                nums[l]=nums[r]
                l+=1
        return l

s=Solution()
assert 7==s.removeDuplicates([0,0,1,1,1,1,2,3,3])
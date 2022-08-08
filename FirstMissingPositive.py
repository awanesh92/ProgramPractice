from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result=1
        for i in sorted(nums):
            if i>0 and result==i:
                result+=1
        return result

s=Solution()
assert 3==s.firstMissingPositive([1,2,0])
assert 1==s.firstMissingPositive([0,-1,-2,4,5,6])
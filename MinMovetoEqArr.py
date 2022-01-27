from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result=0
        #Appraoch 1
        # m=min(nums)
        # for i in nums:
        #     result+=i-m
        # return result
        #Approach2
        return sum(nums)-len(nums)*min(nums)

s=Solution()
assert 3==s.minMoves([1,2,3])
assert 0==s.minMoves([1,1,1])
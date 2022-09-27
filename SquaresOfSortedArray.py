from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])

s=Solution()
assert [0,1,9,16,100]==s.sortedSquares([-4,-1,0,3,10])
assert [4,9,9,49,121]==s.sortedSquares([-7,-3,2,3,11])
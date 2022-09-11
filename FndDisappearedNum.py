from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(range(1,len(nums)+1))
        n=set(nums)
        return list(s.difference(n))

s=Solution()
assert [5,6]==s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
assert [2]==s.findDisappearedNumbers([1,1])
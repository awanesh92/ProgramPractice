from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=sorted(list(set(nums)))
        return len(s),s

s=Solution()
assert (2,[1,2])==s.removeDuplicates([1,2,2,2,1])
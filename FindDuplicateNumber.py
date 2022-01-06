from typing import List
from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            if i in d:
                return i
            else:
                d[i]+=1

s=Solution()

assert 2==s.findDuplicate([1,3,4,2,2])
assert 3==s.findDuplicate([3,1,3,4,2])
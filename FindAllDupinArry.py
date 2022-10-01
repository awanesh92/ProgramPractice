from typing import List
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=set()
        res=[]
        for i in nums:
            if i in s:
                res.append(i)
            else:
                s.add(i)
        return res

s=Solution()
assert [2,3]==s.findDuplicates([4,3,2,7,8,2,3,1])
assert [1]==s.findDuplicates([1,1,2])
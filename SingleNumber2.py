from typing import List
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=defaultdict(int)
        for i in nums:
            s[i]+=1
        l=list(filter(lambda x:x[1]==1,s.items()))
        return l[0][0]

s=Solution()
assert 3==s.singleNumber([2,2,3,2])
assert 99==s.singleNumber([0,1,0,1,0,1,99])
from typing import List
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s=defaultdict(int)
        for i in nums:
            s[i]+=1
        l=list(filter(lambda x:x[1]==1,s.items()))
        result=[x[0] for x in l]
        return result

s=Solution()
assert [3,5]==s.singleNumber([1,2,1,3,2,5])
assert [-1,0]==s.singleNumber([-1,0])
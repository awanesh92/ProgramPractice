from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        return max(d.items(),key=lambda x:x[1])[0]

s=Solution()
assert 3==s.majorityElement([3,2,3])
assert 2==s.majorityElement([2,2,1,1,1,2,2])
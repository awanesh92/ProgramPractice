from typing import List
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        l=list(filter(lambda x:x[1]>len(nums)//3,d.items()))
        return [x[0] for x in l]

s=Solution()
assert [3]==s.majorityElement([3,2,3])
assert [1]==s.majorityElement([1])
assert [1,2]==s.majorityElement([1,2])
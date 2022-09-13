from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        d=sorted(d.items(),key=lambda x:x[1],reverse=True)
        return [i[0] for i in d][:k]

s=Solution()
assert [1,2]==s.topKFrequent([1,1,1,2,2,3],2)
assert [1]==s.topKFrequent([1,1],1)
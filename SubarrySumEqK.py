from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            return 0
        d=defaultdict(int)
        cnt,currsum=0,0
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum==k:
                cnt+=1
            if (currsum-k) in d:
                cnt+=d[currsum-k]
            d[currsum]+=1
        return cnt

s=Solution()
assert 2==s.subarraySum([1,1,1],2)
assert 55==s.subarraySum([0,0,0,0,0,0,0,0,0,0],0)
assert 2==s.subarraySum([1,2,3],3)
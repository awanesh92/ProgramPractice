from collections import deque
from typing import List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        q=deque([([],-1)])
        res=0
        while q:
            curr,indx=q.popleft()
            res+=1

            for i in range(indx+1,len(nums)):
                if nums[i]-k in curr or nums[i]+k in curr:
                    continue
                q.append((curr+[nums[i]],i))
        return res-1
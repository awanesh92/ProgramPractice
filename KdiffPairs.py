from collections import Counter
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result=0
        c=Counter(nums)
        if k==0:
            for ky,v in c.items():
                if v>1:
                    result+=1
        else:
            for ky,v in c.items():
                if ky+k in c:
                    result+=1
        return result
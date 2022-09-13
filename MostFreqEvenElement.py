from typing import List
from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c=Counter(list(filter(lambda x:x%2==0,nums)))
        if c:
            a=sorted(c.items())
            l=max(a,key=lambda x:x[1])
            return l[0]
        else:
            return -1

s=Solution()
assert 2==s.mostFrequentEven([0,1,2,2,4,4,1])
assert -1==s.mostFrequentEven([29,47,21,41,13,37,25,7])
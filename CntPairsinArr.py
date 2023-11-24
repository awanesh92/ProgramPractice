from typing import List
from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def rev_num(x):
            return int(str(x)[::-1])
        differences=[num-rev_num(num) for num in nums]
        occurences=defaultdict(int)
        for i in differences:
            occurences[i]+=1
        nice_pair=sum(count*(count-1)//2 for count in occurences.values())
        return nice_pair%(10**9+7)
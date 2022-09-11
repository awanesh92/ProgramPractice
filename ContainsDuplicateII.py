from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i,num in enumerate(nums):
            if d.get(num) is not None:
                if abs(d[num]-i)<=k:
                    return True
                d[num]=i
            else:
                d[num]=i
        return False
s=Solution()
assert True==s.containsNearbyDuplicate([1,2,3,1],3)
assert False==s.containsNearbyDuplicate([1,2,3,1,2,3],2)
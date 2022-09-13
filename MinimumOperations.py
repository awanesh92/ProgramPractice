from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(list(filter(lambda x:x>0,nums))))

s=Solution()
assert 3==s.minimumOperations([1,5,0,3,5])
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        elif k == 1:
            return True

        d = dict()
        d[0] = -1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            total %= k
            if d.get(total) is not None:
                if i - d[total] >= 2:
                    return True
            else:
                d[total] = i
        return False

s=Solution()
assert True==s.checkSubarraySum([23,2,5,6,0],6)
assert False==s.checkSubarraySum([23,2,6,4,7],13)
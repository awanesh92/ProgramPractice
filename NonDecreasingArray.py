from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l, cnt = len(nums), 0
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                if cnt >= 1 or (i > 0 and nums[i + 1] < nums[i - 1] and i < l - 2 and nums[i] > nums[i + 2]):
                    return False
                cnt += 1
        return True

s=Solution()
assert s.checkPossibility([4,2,1,8]) == False
from typing import List
class Solution:
    def maxsubarray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = nums[0]
        for i in range(1, len(nums)):
            currsum = max(nums[i], currsum + nums[i])
            maxsum = max(currsum, maxsum)
        return 0 if maxsum < 0 else maxsum

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.maxsubarray(arr) % (10 ** 9 + 7)
        arraysum = sum(arr)
        concatsum = self.maxsubarray(arr * 2) % (10 ** 9 + 7)
        if arraysum > 0:
            return (concatsum + arraysum * (k - 2)) % (10 ** 9 + 7)
        else:
            return concatsum

s=Solution()

assert 20==s.kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4],5)
assert 0==s.kConcatenationMaxSum([-1,-2],7)
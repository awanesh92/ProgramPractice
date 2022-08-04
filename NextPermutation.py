from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        j = n - 1
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            nums.reverse()
        else:
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1:] = reversed(nums[i + 1:])

nums=[1,3,5,4,2]
s=Solution()
s.nextPermutation(nums)
assert [1,4,2,3,5]==nums
nums=[1,2,3]
s.nextPermutation(nums)
assert [1,3,2]==nums
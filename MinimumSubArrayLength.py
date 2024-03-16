from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        n=len(nums)
        min_sum=float('inf')
        curr_sum=0
        for right in range(n):
            curr_sum+=nums[right]

            while curr_sum>=target:
                min_sum=min(min_sum,right-left+1)
                curr_sum-=nums[left]
                left+=1
        return min_sum if min_sum!=float('inf') else 0
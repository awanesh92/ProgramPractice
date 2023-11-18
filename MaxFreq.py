from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        i,total,result=0,0,1

        for j in range(len(nums)):
            total+=nums[j]
            while nums[j]*(j-i+1)>total+k:
                total-=nums[i]
                i+=1
            result=max(result,j-i+1)
        return result

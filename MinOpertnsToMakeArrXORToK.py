from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tempResult=nums[0]
        for i in range(1,len(nums)):
            tempResult^=nums[i]
        count=0
        while k or tempResult:
            if tempResult%2!=k%2:
                count+=1
            k//=2
            tempResult//=2
        return count
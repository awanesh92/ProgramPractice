from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        output=[1]
        #generated left array product
        for i in range(len(nums)-1):
            output.append(nums[i]*product)
            product*=nums[i]
        #generate right array product
        product=nums[-1]
        for i in range(len(nums)-1,0,-1):
            output[i-1]=product*output[i-1]
            product*=nums[i-1]
        return output

s=Solution()

assert [24,12,8,6]==s.productExceptSelf([1,2,3,4])
assert [0,0,9,0,0]==s.productExceptSelf([-1,1,0,-3,3])
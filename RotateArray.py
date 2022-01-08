from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:]=nums[-(s:=k%len(nums)):]+nums[:-s]
        #Appraoch 2
        temp=nums.copy()
        for i in range(len(nums)):
            temp[(i+k)%len(nums)]=nums[i]

        nums=temp

s=Solution()
n=[1,2,3,4,5,6,7]
s.rotate(n,3)
assert n==[5,6,7,1,2,3,4]
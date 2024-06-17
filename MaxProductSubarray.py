from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=float("-inf")
        prefixProd=1
        suffixProd=1
        n=len(nums)
        for i in range(n):
            if prefixProd==0:
                prefixProd=1
            if suffixProd==0:
                suffixProd=1
            prefixProd*=nums[i]
            suffixProd*=nums[n-i-1]
            result=max(result,max(prefixProd,suffixProd))
        return result
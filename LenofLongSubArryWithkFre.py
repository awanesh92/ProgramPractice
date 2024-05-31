from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        res=0
        l=0
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
            if freq[nums[i]]>k:
                while nums[l]!=nums[i]:
                    l+=1
                    freq[nums[l]]-=1
                freq[nums[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res
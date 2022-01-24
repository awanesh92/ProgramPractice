from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()

        for i in range(len(nums)-1):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return list(res)

s=Solution()
assert [(-1,0,1),(-1,-1,2)]==s.threeSum([-1,0,1,2,-1,-4])
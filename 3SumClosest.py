from typing import List
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minimum = 10000000
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                res=nums[i]+nums[j]+nums[k]-target
                if abs(res)<abs(minimum):
                    minimum=res
                if res==0:
                    return 0
                elif res<0:
                    j+=1
                else:
                    k-=1
        return minimum+target

s=Solution()
assert 2==s.threeSumClosest([-1,2,1,-4],1)
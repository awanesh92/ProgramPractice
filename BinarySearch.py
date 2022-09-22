from typing import List
class Solution:
    def binSearch(self,nums,l,r,t):
        if r>=l:
            mid=l+(r-l)//2
            if nums[mid]==t:
                return mid
            elif nums[mid]>t:
                return self.binSearch(nums,l,mid-1,t)
            else:
                return self.binSearch(nums,mid+1,r,t)
        else:
            return -1


    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums,0,len(nums)-1,target)

s=Solution()
assert 4==s.search([-1,0,3,5,9,12],9)
assert -1==s.search([-1,0,3,5,9,12],2)
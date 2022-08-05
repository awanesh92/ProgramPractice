from typing import List
class Solution:
    def first(self,nums, l, r, x, n):
        if l<=r:
            mid = l + (r - l) // 2
            if (mid==0 or nums[mid-1]<x) and nums[mid]==x:
                return mid
            elif nums[mid]<x:
                return self.first(nums, mid+1, r, x, n)
            else:
                return self.first(nums, l, mid-1 ,x , n)
        return -1

    def last(self, nums, l ,r , x, n):
        if l<=r:
            mid=l+(r-l)//2
            if (mid==n-1 or nums[mid+1]>x) and nums[mid]==x:
                return mid
            elif nums[mid]>x:
                return self.last(nums, l, mid-1, x, n)
            else:
                return self.last(nums, mid+1, r, x, n)

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        result.append(self.first(nums, 0, len(nums)-1,target, len(nums)))
        result.append(self.last(nums, 0, len(nums) - 1, target, len(nums)))
        return result

s=Solution()
assert [3,4]==s.searchRange([5,7,7,8,8,10],8)
assert [0,1]==s.searchRange([2,2],2)
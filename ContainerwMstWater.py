from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        l,r=0,len(height)-1
        while l<r:
            result=max(result,min(height[l],height[r])*abs(l-r))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return result

s=Solution()
assert 49==s.maxArea([1,8,6,2,5,4,8,3,7])
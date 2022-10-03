from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l,max_zero,n=-1,0,len(seats)
        for i in range(n):
            if seats[i]==1:
                if l==-1:
                    max_zero=i
                else:
                    max_zero=max(max_zero,(i-l)//2)
                l=i
        if seats[n-1]==0:
            max_zero=max(max_zero,n-l-1)
        return max_zero

s=Solution()
assert 2==s.maxDistToClosest([1,0,0,0,1,0,1])
assert 3==s.maxDistToClosest([1,0,0,0])
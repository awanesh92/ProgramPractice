from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        maxjmp=0
        nxtmjmp=0
        for i,num in enumerate(nums):
            if maxjmp<i:
                res+=1
                maxjmp=nxtmjmp
            nxtmjmp=max(nxtmjmp,i+num)

        return res

s=Solution()
assert 2==s.jump([2,3,1,1,4])
assert 2==s.jump([2,3,0,1,4])
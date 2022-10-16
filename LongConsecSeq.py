from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        s=set(nums)
        for i in s:
            if i-1 not in s:
                curr=i
                c=1
                while curr+1 in s:
                    curr+=1
                    c+=1
                res=max(c,res)
        return res

s=Solution()
assert 4==s.longestConsecutive([100,4,200,1,3,2])
assert 9==s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
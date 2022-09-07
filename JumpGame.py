from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums)==1:
            return True

        max_pos=nums[0]
        step,last_indx=0,len(nums)-1
        while step<=max_pos:
            if max_pos>=last_indx:
                return True
            max_pos=max(max_pos,step+nums[step])
            step+=1
        return False
s=Solution()
assert True==s.canJump([2,3,1,1,4])
assert False==s.canJump([3,2,1,0,4])
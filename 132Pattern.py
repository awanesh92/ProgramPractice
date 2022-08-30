from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk=[] #pair of current num and min number on left [curr,minleft]
        currmin=nums[0]

        for i in nums[1:]:
            while stk and i>=stk[-1][0]:
                stk.pop()

            if stk and i>stk[-1][1]:
                return True
            stk.append([i,currmin])

            currmin=min(currmin,i)
        return False

s=Solution()

assert False==s.find132pattern([1,2,3,4])
assert True==s.find132pattern([3,1,4,2])
assert True==s.find132pattern([-1,3,2,0])
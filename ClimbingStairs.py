from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:

        firstVal=1
        secondVal=2

        if n==1:
            return firstVal

        for x in range(3,n+1):
            thirdVal=firstVal+secondVal
            firstVal=secondVal
            secondVal=thirdVal
        return secondVal

s=Solution()
assert 2==s.climbStairs(2)
assert 3==s.climbStairs(3)

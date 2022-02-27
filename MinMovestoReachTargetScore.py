class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target==1:
            return 0
        elif maxDoubles==0:
            return target-1
        elif target%2!=0:
            return self.minMoves(target-1,maxDoubles)+1
        else:
            return self.minMoves(target//2,maxDoubles-1)+1

s=Solution()
assert 4==s.minMoves(5,0)
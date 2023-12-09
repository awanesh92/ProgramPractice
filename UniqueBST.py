class Solution:
    def numTrees(self, n: int) -> int:
        res=1.0
        for i in range(1,n+1):
            res=res*(n+i)/i
        res/=n+1
        return int(res)
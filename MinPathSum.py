from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        #Follow bottom up appraoch
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                left=grid[i][j-1] if j-1>=0 else float('inf')
                up=grid[i-1][j] if i-1>=0 else float('inf')
                grid[i][j]+=min(left,up)
        return grid[m-1][n-1]

s=Solution()
assert 7==s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
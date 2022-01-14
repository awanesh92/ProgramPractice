from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def valid(row: int,col: int) -> bool:
            if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==0:
                return True
            return False

        if grid[0][0]!=0 or grid[len(grid)-1][len(grid[0])-1]!=0:
            return -1

        q=deque([(0,0,1)])
        directions=[(i,j) for i in range(-1,2) for j in range(-1,2)]
        grid[0][0]=1
        while q:
            r,c,cnt=q.popleft()
            if r==len(grid)-1 and c==len(grid[0])-1:
                return cnt
            for i,j in directions:
                nR=r+i
                nC=c+j
                if valid(nR,nC):
                    grid[nR][nC]=1
                    q.append((nR,nC,cnt+1))
        return -1

s=Solution()
assert 3==s.shortestPathBinaryMatrix([[0,0,0],[0,0,0],[0,0,0]])
assert 4==s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
assert -1==s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result=-1
        row,col=len(grid),len(grid[0])
        q=list()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append([i,j])

        while q:
            tmp=q.copy()
            q.clear()

            for i,j in tmp:
                if i+1<row and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    q.append([i+1,j])
                if i-1>=row and grid[i+1][j]==1:
                    grid[i-1][j]=2
                    q.append([i-1,j])
                if j+1<col and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    q.append([i,j+1])
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    q.append([i,j-1])
            result+=1

        for r in grid:
            if 1 in r:
                return -1

        return result
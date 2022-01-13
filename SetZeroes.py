from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        r, c = set(), set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        # set row to zero
        for i in r:
            matrix[i] = [0] * col

        # set col to zero
        for i in c:
            for j in range(row):
                matrix[j][i] = 0

s=Solution()
m=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(m)
assert m==[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
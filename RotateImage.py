from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                temp=matrix[n-j-1][i]
                matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
                matrix[j][n-i-1]=matrix[i][j]
                matrix[i][j]=temp
        return matrix

s=Solution()
assert [[7,4,1],[8,5,2],[9,6,3]]==s.rotate([[1,2,3],[4,5,6],[7,8,9]])
assert [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]==s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
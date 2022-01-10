from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t,r,b,l=0,len(matrix[0]),len(matrix),0
        result=[]
        while l<r and t<b:
            #traverse each side/direction
            for i in range(l,r):
                result.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                result.append(matrix[i][r-1])
            r-=1
            if t<b:
                for i in range(r-1,l-1,-1):
                    result.append(matrix[b-1][i])
            b-=1
            if l<r:
                for i in range(b-1,t-1,-1):
                    result.append(matrix[i][l])
            l+=1
        return result
s=Solution()
assert [1,2,3,6,9,8,7,4,5]==s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
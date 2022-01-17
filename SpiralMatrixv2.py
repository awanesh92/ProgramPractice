from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        t,b,l,r=0,n,0,n
        result=[[0 for _ in range(n)] for _ in range(n)]
        cnt=1
        while l<r and t<b:
            #print top row
            for i in range(l,r):
                result[t][i]=cnt
                cnt+=1
            t+=1
            for i in range(t,b):#right
                result[i][r-1]=cnt
                cnt+=1
            r-=1
            if t<b:#bottom
                for i in range(r-1,l-1,-1):
                    result[b-1][i]=cnt
                    cnt+=1
            b-=1
            if l<r:
                for i in range(b-1,t-1,-1):
                    result[i][l]=cnt
                    cnt+=1
            l+=1
        return result
s=Solution()
assert [[1,2],[4,3]]==s.generateMatrix(2)
assert [[1]]==s.generateMatrix(1)
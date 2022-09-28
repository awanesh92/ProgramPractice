from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        x=0
        fin=[]
        for i in range(m):
            res=[]
            for j in range(n):
                res.append(original[x])
                x+=1
            fin.append(res)
        return fin
s=Solution()
assert [[1,2],[3,4]]==s.construct2DArray([1,2,3,4],2,2)
assert []==s.construct2DArray([1,2],1,1)
assert [[1,2,3]]==s.construct2DArray([1,2,3],1,3)
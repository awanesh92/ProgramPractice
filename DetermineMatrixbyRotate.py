from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rot(res):
            l,r=0,len(res)-1
            while l<r:
                for i in range(r-l):
                    t,b=l,r
                    temp=res[t][l+i]
                    res[t][l+i]=res[b-i][l]
                    res[b-i][l]=res[b][r-i]
                    res[b][r-i]=res[t+i][r]
                    res[t+i][r]=temp
                l+=1
                r-=1
            return res
        for i in range(4):
            mat=rot(mat)
            if mat==target:
                return True
        return False

s=Solution()
assert True==s.findRotation([[0,1],[1,0]],[[1,0],[0,1]])
assert False==s.findRotation([[0,1],[1,1]],[[1,0],[0,1]])
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cp={c:0 for c in range(numCourses)}#for count of courses
        pc={p:[] for p in range(numCourses)}#for edge of course
        for c,p in prerequisites:
            cp[c]+=1
            pc[p].append(c)
        coursett=[c for c,ps in cp.items() if not ps]
        res=[]
        while coursett:
            res.extend(coursett)
            nextcourse=[]
            for p in coursett:
                for c in pc[p]:
                    cp[c]-=1
                    if not cp[c]:
                        nextcourse.append(c)
            coursett=nextcourse
        return res if not any(cp.values()) else []

s=Solution()
print(s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
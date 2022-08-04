from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]

        fininterval=sorted(intervals+[newInterval])
        out=[fininterval[0]]
        for i in range(1,len(fininterval)):
            if fininterval[i][0]<=out[-1][1]:
                out[-1][1]=max(fininterval[i][1],out[-1][1])
            else:
                out.append(fininterval[i])
        return out

s=Solution()
assert [[1,5],[6,9]]==s.insert([[1,3],[6,9]],[2,5])
assert [[1,2],[3,10],[12,16]]==s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
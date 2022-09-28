from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        res=[]
        while i<=len(firstList)-1 and j<=len(secondList)-1:
            left=max(firstList[i][0],secondList[j][0])
            right=min(firstList[i][1],secondList[j][1])
            if left<=right:
                res.append([left,right])
            if firstList[i][1]>secondList[j][1]:
                j+=1
            else:
                i+=1
        return res
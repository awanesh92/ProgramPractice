from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans,rowIndex=1,rowIndex+1
        ansRow=[1]
        for col in range(1,rowIndex):
            ans*=(rowIndex-col)
            ans//=col
            ansRow.append(ans)
        return ansRow
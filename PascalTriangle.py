from typing import List
class Solution:
    def generateRow(self,rows: int) -> List[int]:
        ans=1
        ansRow=[1]

        for col in range(1,rows):
            ans*=(rows-col)
            ans//=col
            ansRow.append(ans)
        return ansRow

    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(1,numRows+1):
            result.append(self.generateRow(i))
        return result
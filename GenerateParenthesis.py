from typing import List
class Solution:
    def findAll(self,string: str,open: int,close: int,result: List[str],n: int):

        if len(string)==n*2:
            result.append(string)
            return
        if open<n:
            self.findAll(string+"(",open+1,close,result,n)
        if close<open:
            self.findAll(string+")",open,close+1,result,n)

    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        self.findAll("(",1,0,result,n)
        return result

s=Solution()
assert ["((()))","(()())","(())()","()(())","()()()"]==s.generateParenthesis(3)
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def subtrack(sub='',i=0):
            if len(sub)==len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    subtrack(sub+s[i].swapcase(),i+1)
                subtrack(sub+s[i],i+1)
        res=[]
        subtrack()
        return res

s=Solution()
assert sorted(["a1b2","a1B2","A1b2","A1B2"])==sorted(s.letterCasePermutation("a1b2"))
assert sorted(["3z4","3Z4"])==sorted(s.letterCasePermutation("3z4"))
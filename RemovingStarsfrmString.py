class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for i in s:
            if i=='*':
                if stk:
                    stk.pop()
            else:
                stk.append(i)
        return ''.join(stk)

s=Solution()
assert "lecoe"==s.removeStars("leet**cod*e")
assert ""==s.removeStars("erase*****")
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result=0
        stk=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    l=i-stk[-1]
                    result=max(l,result)
        return result

s=Solution()
assert 4==s.longestValidParentheses(")()())")
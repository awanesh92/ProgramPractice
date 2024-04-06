class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk=[]
        s=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stk.append(i)
            elif s[i]==')':
                if stk:
                    stk.pop()
                else:
                    s[i]=''
        while stk:
            s[stk.pop()]=''
        return ''.join(s)
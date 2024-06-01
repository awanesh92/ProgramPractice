class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        curr_num=0
        curr_str=''
        for c in s:
            if c == '[':
                stk.append(curr_num)
                stk.append(curr_str)
                curr_str=''
                curr_num=0
            elif c.isdigit():
                curr_num=curr_num*10+int(c)
            elif c == ']':
                tempstr=stk.pop()
                n=stk.pop()
                curr_str=tempstr+n*curr_str
            else:
                curr_str+=c
        return curr_str
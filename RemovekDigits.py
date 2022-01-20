from typing import List
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        cnt=k
        for i in num:
            while stk and cnt and stk[-1]>i:#till the element counter is 0 and stk does not contain greater value than current element
                stk.pop()
                cnt-=1
            stk.append(i)
        result=''.join(stk[0:len(num)-k]).lstrip("0")
        if len(result):
            return result
        else:
            return "0"

s=Solution()
assert "0"==s.removeKdigits("9",1)
assert "1219"==s.removeKdigits("1432219",3)
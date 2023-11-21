from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v=sorted(strs)
        ans=''
        print(v)
        frst=v[0]
        lst=v[-1]
        for i in range(min(len(frst),len(lst))):
            if(frst[i])!=lst[i]:
                return ans
            ans+=frst[i]
        return ans
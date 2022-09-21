from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Appraoch1
        # nxt=ord(target)+1
        # while True:
        #     if nxt>ord('z'):
        #         nxt=ord('a')
        #     if chr(nxt) in letters:
        #         return chr(nxt)
        #     nxt+=1
        #Approach2
        last,first=len(letters)-1,0
        temp=0
        while first<=last:
            mid=(first+last)//2

            l=ord(letters[mid])-ord(target)
            if l>0:
                temp=mid
                last=mid-1
            else:
                first=mid+1
        return letters[temp]


s=Solution()
assert "c"==s.nextGreatestLetter(["c","f","j"],'a')
assert "f"==s.nextGreatestLetter(["c","f","j"],"d")
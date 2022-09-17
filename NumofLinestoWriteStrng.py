from typing import List
import string
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        st=list(string.ascii_lowercase)
        letter,line=0,0
        words={}
        for i in range(26):
            if st[i] not in words:
                words[st[i]]=widths[i]

        i=0
        while i<len(s):
            if letter+words[s[i]]>100:
                letter=0
                line+=1
            letter+=words[s[i]]
            i+=1
        return [line+1,letter]

s=Solution()
assert [3,60]==s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                               "abcdefghijklmnopqrstuvwxyz")
assert [2,4]==s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                              "bbbcccdddaaa")

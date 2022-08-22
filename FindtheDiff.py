from typing import List
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c=0
        for i in s:
            c^=ord(i)
        for i in t:
            c^=ord(i)

        return chr(c)
s=Solution()
assert "e"==s.findTheDifference("abcd","abcde")
assert "y"==s.findTheDifference("","y")
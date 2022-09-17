from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i==i[::-1]:
                return i
        return ''

s=Solution()
assert "ada"==s.firstPalindrome(["abc","car","ada","racecar","cool"])
assert "racecar"==s.firstPalindrome(["notapalindrome","racecar"])
from typing import List
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                left_chk = s[:left] + s[left + 1:] == (s[:left] + s[left + 1:])[::-1]
                right_chk = s[:right] + s[right + 1:] == (s[:right] + s[right + 1:])[::-1]

                if left_chk or right_chk:
                    return True
                else:
                    return False
            left += 1
            right -= 1

s=Solution()
assert True==s.validPalindrome("aba")
assert False==s.validPalindrome("abs")
class Solution:
    def palindrome(self, s, i, j):
        p = 1
        while i - p >= 0 and j + p <= len(s) - 1:
            if s[i - p] == s[j + p]:
                p += 1
            else:
                break
        return s[i - p + 1:j + p]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        p = ''
        for i in range(len(s)):
            if s[i] == s[i - 1]:
                d = self.palindrome(s, i - 1, i)
                p = d if len(d) > len(p) else p
            d = self.palindrome(s, i, i)
            p = d if len(d) > len(p) else p
        return p

s=Solution()
assert "bab"==s.longestPalindrome("babad")
assert "abcba"==s.longestPalindrome("abcba")
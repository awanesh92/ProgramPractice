class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

s=Solution()
assert "blue is sky the"==s.reverseWords("the sky is blue")
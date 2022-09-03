class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

s=Solution()
assert 4==s.lengthOfLastWord("   fly me   to   the moon  ")
assert 6==s.lengthOfLastWord("luffy is still joyboy")
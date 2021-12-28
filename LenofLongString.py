class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        result=0
        if len(s)<=1 or len(s)==len(set(s)):
            return len(s)
        while r<len(s):
            if len(s[l:r+1])==len(set(s[l:r+1])):
                r+=1
            else:
                result=max(result,r-l)
                l+=1
        return max(result,r-l)

s=Solution()
assert 2==s.lengthOfLongestSubstring("aab")
assert 2==s.lengthOfLongestSubstring("au")
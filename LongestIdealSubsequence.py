class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*27
        n=len(s)

        for i in range(n-1,-1,-1):
            cc=s[i]
            idx=ord(cc)-ord('a')
            maxLen=0
            left=max(0,idx-k)
            right=min(26,idx+k)

            maxLen = max(dp[left:right+1])
            dp[idx]=maxLen+1

        return max(dp)
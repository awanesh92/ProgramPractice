class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''stk=list(s)
        for i in range(len(t)):
            if not stk:
                return True
            if stk[0]==t[i]:
                stk.pop(0)
        if stk:
            return False
        else:
            return True '''
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[len(s)][len(t)] == len(s)
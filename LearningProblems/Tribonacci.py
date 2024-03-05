class Solution:
    def tribonacci(self, n: int) -> int:

        def fib(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 1
            elif dp[n]!=-1:
                return dp[n]
            dp[n]=fib(n-1)+fib(n-2)+fib(n-3)
            return dp[n]

        dp=[-1]*(n+1)
        return fib(n)
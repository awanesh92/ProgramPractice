class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2)

s=Solution()
assert 1024.00000==s.myPow(2.00000,10)
assert 0.25000==s.myPow(2.00000,-2)
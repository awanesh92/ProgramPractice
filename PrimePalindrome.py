import math
class Solution:
    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def pal(self, n: int) -> bool:
        return n == int(str(n)[::-1])

    def primePalindrome(self, n: int) -> int:
        for i in range(n, 10 ** 7):
            if self.is_prime(i) and self.pal(i):
                return i
        return 100030001

s=Solution()

assert 100030001==s.primePalindrome(9989900)
assert 2==s.primePalindrome(1)
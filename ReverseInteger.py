class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(str(x)[1:])
            x = -1 * int(x[::-1])
        else:
            x = int(str(x)[::-1])

        return x if -2 ** 31 < x < 2 ** 31 - 1 else 0

s=Solution()
assert s.reverse(1534236469) == 0
assert s.reverse(-123) == -321
assert s.reverse(120) == 21
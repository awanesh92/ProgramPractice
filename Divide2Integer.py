class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0

        a = abs(dividend)
        b = abs(divisor)

        while a >= b:
            temp = b
            mul = 1

            while a >= temp:
                a -= temp
                result += mul
                mul += mul
                temp += temp

        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            return -result
        return min((2 ** 31) - 1, max(-2 ** 31, result))

s=Solution()

assert 3==s.divide(10,3)
assert -2==s.divide(7,-3)
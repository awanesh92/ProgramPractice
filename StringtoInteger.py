import string


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        strt = 0
        signmult = 1
        if s[0] == '+':
            strt = 1
        elif s[0] == '-':
            signmult = -1
            strt = 1

        result = 0
        indx = strt
        while indx < len(s):
            if not ('0' <= s[indx] <= '9'):
                return result * signmult

            result = result * 10 + ord(s[indx]) - ord('0')

            min32 = 2 ** 31
            if result * signmult <= -min32:
                return -min32
            elif result * signmult >= min32 - 1:
                return min32 - 1

            indx += 1

        return result * signmult

s=Solution()
assert -42==s.myAtoi("   -42")
assert 0==s.myAtoi("words and 987")
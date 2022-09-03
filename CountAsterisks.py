class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        flg = False
        for x in s:
            if x == '|':
                flg = not flg
            if x == '*' and not flg:
                res = res + 1

        return res

s=Solution()
assert 5==s.countAsterisks("yo|uar|e**|b|e***au|tifu|l")
assert 2==s.countAsterisks("l|*e*et|c**o|*de|")
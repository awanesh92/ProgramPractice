class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        cnt = 0
        i = 1
        temp = a
        while b not in a:
            if len(a) <= len(b) + len(temp):
                a = temp * i
                i += 1
                cnt += 1
            else:
                break
        if b in a:
            return cnt
        return -1

s=Solution()
assert 3==s.repeatedStringMatch("abcd","cdabcdab")
assert 2==s.repeatedStringMatch("a","aa")
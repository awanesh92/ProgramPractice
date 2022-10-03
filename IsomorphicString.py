class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        z=zip(s,t)
        return len(set(s))==len(set(t))==len(set(z))

s=Solution()
assert True==s.isIsomorphic("egg","add")
assert False==s.isIsomorphic("foo","bar")
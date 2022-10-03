class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s):
            return False
        d={}
        for i,j in zip(pattern,s):
            if (i in d and j!=d[i]):
                return False
            d[i]=j
            if (len(set(d.values()))!=len(set(d.keys()))):
                return False
        return True

s=Solution()
assert True==s.wordPattern("abba","dog cat cat dog")
assert False==s.wordPattern("abba","dog cat cat fish")
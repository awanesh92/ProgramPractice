from itertools import permutations
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s1,s2):
            if s1==s2 or s2 in s1:
                return s1
            if s1 in s2:
                return s2
            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i]+s2
            return s1+s2

        strings=[a,b,c]
        res=[]
        for p in permutations(strings):
            merged=merge(merge(p[0],p[1]),p[2])
            res.append(merged)
        return min(res,key=lambda x:(len(x),x))

from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(p, q):
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == q[j]:
                    i += 1
                elif q[j].isupper():
                    return False
            return i == len(p)

        return [True if match(pattern, st) else False for st in queries]

s=Solution()

assert [True,False,True,True,False] == s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB")
assert [False,False,False,False,False] == s.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBaTr")
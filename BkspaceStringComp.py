class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stks,stkt=[],[]
        for i in s:
            if i=='#':
                if stks:
                    stks.pop()
            else:
                stks.append(i)
        for i in t:
            if i=='#':
                if stkt:
                    stkt.pop()
            else:
                stkt.append(i)
        return stks==stkt

s=Solution()
assert True==s.backspaceCompare("ab#c","ad#c")
assert False==s.backspaceCompare("a#c","b")
from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)

        wrdset=[set(i) for i in words]

        product=[len(words[i])*len(words[j]) for i in range(n) for j in range(i,n) if wrdset[i].isdisjoint(wrdset[j])]
        if len(product)==0:
            return 0

        return max(product)

s=Solution()
assert 16==s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
assert 4==s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"])
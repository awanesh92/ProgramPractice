from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
              '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}

        def findletter(s):
            #returns the last digit base case for recursion
            if len(s)==1:
                return m[s]

            a=m[s[0]]
            b=findletter(s[1:])

            return [i+j for i in a for j in b]
        return findletter(digits) if digits else []

s=Solution()
assert ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg",
        "bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]==s.letterCombinations("234")

assert ["ad","ae","af","bd","be","bf","cd","ce","cf"]==s.letterCombinations("23")

from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for item in strs:
            srtstr=''.join(sorted(item))
            res[srtstr].append(item)
        return list(res.values())

s=Solution()
assert [["eat","tea","ate"],["tan","nat"],["bat"]]==s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
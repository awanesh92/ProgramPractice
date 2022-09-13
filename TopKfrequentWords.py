from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=defaultdict(int)
        for i in words:
            d[i]+=1
        d=sorted(d.items(),key=lambda x:(-x[1],x[0]))
        return [i[0] for i in d][:k]

s=Solution()
assert ["i","love"]==s.topKFrequent(["i","love","leetcode","i","love","coding"],2)
assert ["the","is","sunny","day"]==s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4)
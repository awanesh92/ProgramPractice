from typing import List
class Solution:
    def countGarbage(self,g: List[str]):
        return sum(sum(s.count(char) for s in g)for char in 'MPG')
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        result=self.countGarbage(garbage)

        for char in 'MPG':
            #create a list with 1s and 0s for flag value of garbage
            char_check=[1 if char in i else 0 for i in garbage[1:]]
            #will return index till which we need to pick the garbage/or travel
            check_len=len(char_check)-char_check[::-1].index(1) if 1 in char_check else 0
            result+=sum(travel[:check_len])
        return result
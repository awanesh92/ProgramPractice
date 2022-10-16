from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            for i in range(len(res)):
                currsub=res[i]
                if sorted(currsub+[num]) not in res:
                    res.append(sorted(currsub+[num]))
        return res

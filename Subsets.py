from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub=[[]]
        for num in nums:
            for i in range(len(sub)):
                currsub=sub[i]
                sub.append(currsub+[num])
        return sub

s=Solution()
assert sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])==sorted(s.subsets([1,2,3]))
assert sorted([[],[0]])==sorted(s.subsets([0]))
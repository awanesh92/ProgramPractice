from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(x,curr_xor):
            if x == len(nums):
                return curr_xor

            include = dfs(x+1, curr_xor^nums[x])
            exclude = dfs(x+1, curr_xor)

            return include+exclude
        return dfs(0,0)
from bisect import bisect_left
from typing import List
class Solution:
    def binsearch(self, matrix: List[int], target: int) -> int:
        i = bisect_left(matrix, target)
        if i != len(matrix) and matrix[i] == target:
            return i
        else:
            return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = False
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            if matrix[i][0] > target:
                continue
            if self.binsearch(matrix[i], target) != -1:
                result = True
        return result

s=Solution()
assert True==s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)
assert False==s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20)
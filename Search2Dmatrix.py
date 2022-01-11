from bisect import bisect_left
from typing import List
class Solution:
    def binsearch(self, n: List[int], k: int) -> int:
        i = bisect_left(n, k)
        if i != len(n) and n[i] == k:
            return i
        else:
            return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix[0]) - 1
        row = 0
        result = False
        while row < len(matrix):
            #Appraoch 2
            #     if target in matrix[row]:
            #         return True
            #     row+=1
            # return False
            # print(matrix[row][s],matrix[row][e])
            if (matrix[row][s] <= target and target <= matrix[row][e]):
                # print(matrix[row],target)
                if self.binsearch(matrix[row], target) != -1:
                    result = True
            row += 1
        return result

s=Solution()
assert False == s.searchMatrix([[1]],0)
assert True == s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],16)
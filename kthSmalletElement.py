# import numpy as np
import heapq
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Approach 1
        # m=np.array(matrix)
        # m=sorted(m.flatten())
        # return m[k-1]
        # Approach 2
        # result=matrix[0]
        # heapq.heapify(result)
        # for i in matrix[1:]:
        #     for e in i:
        #         heapq.heappush(result,e)
        # r=heapq.nsmallest(k,result)
        # return r[-1]
        # Approach3
        m, n = len(matrix), len(matrix[0])
        h = [(matrix[0][0], (0, 0))]
        cnt, visited = 0, {(0, 0)}
        small = None
        while cnt < k:
            smallest, (i, j) = heapq.heappop(h)
            cnt += 1

            if i + 1 < m and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(h, (matrix[i + 1][j], (i + 1, j)))
            if j + 1 < n and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(h, (matrix[i][j + 1], (i, j + 1)))
        return smallest

s=Solution()
assert 13==s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)
assert -5==s.kthSmallest([[-5]],1)
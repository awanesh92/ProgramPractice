class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path=[[0]*n for _ in range(m)]

        for i in range(m):
            path[i][0]=1

        for i in range(n):
            path[0][i]=1

        for i in range(1,m):
            for j in range(1,n):
                path[i][j]=path[i-1][j]+path[i][j-1]

        return path[-1][-1]

s=Solution()
assert 28==s.uniquePaths(3,7)
assert 3==s.uniquePaths(3,2)
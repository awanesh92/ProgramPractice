from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])

        def check(r,c,cnt):
            if len(word)==cnt:
                return True
            for ri,ci in [[1,0],[0,1],[-1,0],[0,-1]]:
                if -1<ri+r<row and -1<ci+c<col and board[ri+r][ci+c]==word[cnt]:
                    board[ri+r][ci+c]=None
                    if check(ri+r,ci+c,cnt+1):
                        return True
                    board[ri+r][ci+c]=word[cnt]
            return False

        for r in range(row):
            for c in range(col):
                if board[r][c]==word[0]:
                    board[r][c]=None
                    if check(r,c,1):
                        return True
                    board[r][c]=word[0]
        return False

s=Solution()
assert True==s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
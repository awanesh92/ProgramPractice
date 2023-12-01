from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for x in range(9)]
        col = [set() for x in range(9)]
        sqr = [[set() for x in range(3)] for y in range(3)]

        for x in range(9):
            for y in range(9):
                curr = board[x][y]
                if curr == '.':
                    continue
                else:
                    if curr in row[x] or curr in col[y] or curr in sqr[x // 3][y // 3]:
                        return False

                row[x].add(curr)
                col[y].add(curr)
                sqr[x // 3][y // 3].add(curr)
        return True
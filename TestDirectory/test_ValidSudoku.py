import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from ValidSudoku import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("c, expected", [
        ([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]],True),
        ([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"]
           ,[".",".",".",".","8",".",".","7","9"]],False)
    ])
    def test_findPairs(self, solution, c, expected):
        result=solution.isValidSudoku(c)
        assert result == expected
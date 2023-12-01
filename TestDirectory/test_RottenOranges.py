import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from RottenOranges import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("grid, expected",[([[2,1,1],[1,1,0],[0,1,1]],4),
                             ([[2,1,1],[0,1,1],[1,0,1]],-1),
                             ([[0,2]],0)])
    def test_findPairs(self, solution, grid, expected):
        result=solution.orangesRotting(grid)
        assert result == expected
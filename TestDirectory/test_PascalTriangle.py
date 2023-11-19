import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from PascalTriangle import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("numRows,expected", [
        (5,[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
        (1,[[1]])
    ])
    def test_PasCalTriangle(self, solution, numRows, expected):
        result = solution.generate(numRows)
        assert result == expected
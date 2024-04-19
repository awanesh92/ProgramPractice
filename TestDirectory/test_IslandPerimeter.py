import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from IslandPerimeter import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("grid, expected", [
        ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],16),
        ([[1]],4),
        ([[1,0]],4),
    ])
    def test_islandPerimeter(self, solution, grid, expected):
        result=solution.islandPerimeter(grid)
        assert result == expected
import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LearningProblems.DivisorGame import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (2, True),
        (3, False),
        (4, True)
    ])
    def test_minCostClimbingStairs(self, solution, n, expected):
        result=solution.divisorGame(n)
        assert result == expected
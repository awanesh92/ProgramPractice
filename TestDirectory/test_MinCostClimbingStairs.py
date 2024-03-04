import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LearningProblems.MinCostClimbingStairs import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("cost, expected", [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
    ])
    def test_minCostClimbingStairs(self, solution, cost, expected):
        result=solution.minCostClimbingStairs(cost)
        assert result == expected
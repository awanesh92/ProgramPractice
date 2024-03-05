import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LearningProblems.Tribonacci import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (2, 1),
        (3, 2),
        (25, 1389537)
    ])
    def test_tribonacci(self, solution, n, expected):
        result=solution.tribonacci(n)
        assert result == expected
import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SumOfSqrNumbers import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("c, expected", [
        (5,True),
        (3,False),
        (4,True)
    ])
    def test_findPairs(self, solution, c, expected):
        result=solution.judgeSquareSum(c)
        assert result == expected
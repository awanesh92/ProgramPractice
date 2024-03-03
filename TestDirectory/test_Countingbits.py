import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from Countingbits import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (2,[0,1,1]),
        (5,[0,1,1,2,1,2])
    ])
    def test_countBits(self, solution, n, expected):
        result=solution.countBits(n)
        assert result == expected
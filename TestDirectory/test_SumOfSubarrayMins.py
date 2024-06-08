import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SumOfSubarrayMins import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("arr, expected", [
        ([3,1,2,4],17),
        ([11,81,94,43,3],444)
    ])
    def test_sumOfSubarrayMins(self, solution, arr, expected):
        result=solution.sumSubarrayMins(arr)
        assert result == expected
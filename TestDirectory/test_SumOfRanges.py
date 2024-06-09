import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SumOfRanges import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("arr, expected", [
        ([1,2,3],4),
        ([1,3,3],4),
        ([4,-2,-3,4,1],59)
    ])
    def test_sumOfSubarrayMins(self, solution, arr, expected):
        result=solution.subArrayRanges(arr)
        assert result == expected
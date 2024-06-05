import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LargestNumber import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([10,2], "210"),
        ([3,30,34,5,9],"9534330")
    ])
    def test_maxProfit(self, solution, nums, expected):
        result=solution.largestNumber(nums)
        assert result == expected
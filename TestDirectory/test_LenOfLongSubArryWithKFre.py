import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LenofLongSubArryWithkFre import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, k, expected", [
        ([1,4,4,3], 1, 2),
        ([1,2,1,2,1,2,1,2], 1, 2)
    ])
    def test_maxProfit(self, solution, nums, k, expected):
        result=solution.maxSubarrayLength(nums,k)
        assert result == expected
import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from MaxProductSubarray import Solution
import pytest

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums,expected", [
        ([2,3,-2,4],6),
        ([-2,0,-1],0)
    ])
    def test_maxSubArrayProd(self, solution, nums, expected):
        result = solution.maxProduct(nums)
        assert result == expected

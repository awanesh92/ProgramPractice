import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from CntPairsinArr import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([42,11,1,97],2),
        ([13,10,35,24,76],4)
    ])
    def test_longestCommonPrefix(self, solution, nums, expected):
        result=solution.countNicePairs(nums)
        assert result == expected
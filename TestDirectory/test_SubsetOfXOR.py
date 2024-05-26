import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SubsetOfXOR import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        ([1,3], 6),
        ([5,1,6], 28),
        ([3,4,5,6,7,8], 480)
    ])
    def test_relativeRanks(self, solution, nums, expected):
        result = solution.subsetXORSum(nums)
        assert result == expected
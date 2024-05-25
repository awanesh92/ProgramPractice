import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from NoOfBeautifulSubsets import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, k, expected", [
        ([2,4,6], 2, 4),
        ([1],1, 1)
    ])
    def test_relativeRanks(self, solution, nums, k, expected):
        result = solution.beautifulSubsets(nums, k)
        assert result == expected
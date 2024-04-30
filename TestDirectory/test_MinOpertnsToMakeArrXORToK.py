import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from MinOpertnsToMakeArrXORToK import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, k, expected", [
        ([2,1,3,4], 1, 2),
        ([2,0,2,0], 0, 0),
    ])
    def test_countAndSay(self, solution, nums, k, expected):
        result=solution.minOperations(nums,k)
        assert result == expected
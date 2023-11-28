import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from KdiffPairs import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, k, expected", [
        ([3,1,4,1,5],2,2),
        ([1,2,3,4,5],1,4),
        ([1,3,1,5,4],0,1)
    ])
    def test_findPairs(self, solution, nums, k, expected):
        result=solution.findPairs(nums,k)
        assert result == expected
import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from MinimumSubArrayLength import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("target, nums, expected", [
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
        (7, [2,3,1,2,4,3], 2),
    ])
    def test_minSubArrayLen(self, solution, target, nums, expected):
        result=solution.minSubArrayLen(target, nums)
        assert result == expected
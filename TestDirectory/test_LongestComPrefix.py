import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LongestComPrefix import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums, expected", [
        (["flower","flow","flight"],"fl"),
        (["dog","racecar","car"],"")
    ])
    def test_longestCommonPrefix(self, solution, nums, expected):
        result=solution.longestCommonPrefix(nums)
        assert result == expected
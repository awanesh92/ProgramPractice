import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from MaxFreq import Solution
import pytest

class TestSolution:

    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("nums,k,expected", [
        ([3, 9, 6], 2, 1),
        ([1, 4, 8, 13], 5, 2),
        ([1, 2, 4], 5, 3),
        ([],5,0)
    ])
    def test_maxFrequency(self, solution, nums, k, expected):
        print("Running test_maxFrequency.")
        result = solution.maxFrequency(nums, k)
        assert result == expected

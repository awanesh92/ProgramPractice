import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from KthSmallestprimeFaction import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("arr, k, expected", [
        ([1,2,3,5], 3, [2,5]),
        ([1,7], 1, [1,7]),
    ])
    def test_relativeRanks(self, solution, arr, k, expected):
        result=solution.kthSmallestPrimeFraction(arr, k)
        assert result == expected
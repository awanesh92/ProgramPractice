import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from GarbageCollection import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("garbage, travel, expected", [
        (["G","P","GP","GG"],[2,4,3],21),
        (["MMM","PGM","GP"],[3,10],37)
    ])
    def test_longestCommonPrefix(self, solution, garbage, travel, expected):
        result=solution.garbageCollection(garbage, travel)
        assert result == expected
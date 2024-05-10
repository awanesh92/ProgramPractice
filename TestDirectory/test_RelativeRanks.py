import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from RelativeRanks import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("score,expected", [
        ([5, 4, 3, 2, 1],["Gold Medal","Silver Medal","Bronze Medal","4","5"]),
        ([10,3,8,9,4],["Gold Medal","5","Bronze Medal","Silver Medal","4"])
    ])
    def test_relativeRanks(self, solution, score, expected):
        result=solution.findRelativeRanks(score)
        assert result == expected
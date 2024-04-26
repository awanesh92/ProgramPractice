import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from LongestIdealSubsequence import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, k, expected", [
        ("acfgbd", 2, 4),
        ("abcd", 3, 4),
    ])
    def test_longIdealString(self, solution, s, k, expected):
        result=solution.longestIdealString(s,k)
        assert result == expected
import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from IsSubsequence import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, t, expected", [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False)
    ])
    def test_countBits(self, solution, s, t, expected):
        result=solution.isSubsequence(s,t)
        assert result == expected
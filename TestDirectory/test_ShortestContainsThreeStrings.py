import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from ShortestContainsthreeStrings import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("a, b, c, expected", [
        ("abc", "bca", "aaa", "aaabca"),
        ("ab","ba","aba","aba")
    ])
    def test_shortestStrings(self, solution, a, b, c, expected):
        result = solution.minimumString(a, b, c)
        assert result == expected
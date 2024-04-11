import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from RemovekDigits import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("num, k, expected", [
        ("9", 1, "0"),
        ("1432219", 3,"1219")
    ])
    def test_removeKDigits(self, solution, num, k, expected):
        result = solution.removeKdigits(num, k)
        assert result == expected
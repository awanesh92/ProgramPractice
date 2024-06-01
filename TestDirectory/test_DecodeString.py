import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from DecodeString import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, expected", [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc")
    ])
    def test_maxProfit(self, solution, s, expected):
        result=solution.decodeString(s)
        assert result == expected
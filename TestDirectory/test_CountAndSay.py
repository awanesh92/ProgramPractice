import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from CountAndSay import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("n, expected", [
        (1,'1'),
        (4,'1211'),
        (5,'111221')
    ])
    def test_countAndSay(self, solution, n, expected):
        result=solution.countAndSay(n)
        assert result == expected
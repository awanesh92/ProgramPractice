import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from ValidParenthesisString import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, expected", [
        ("(*)", True),
        ('(()))',False),
        ('((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()',True)
    ])
    def test_checkValidString(self, solution, s, expected):
        result = solution.checkValidString(s)
        assert result == expected
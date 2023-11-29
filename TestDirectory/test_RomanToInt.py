import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from RomanToInt import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("st, expected", [
        ('III',3),
        ('LVIII',58),
        ('MCMXCIV',1994)
    ])
    def test_findPairs(self, solution, st, expected):
        result=solution.romanToInt(st)
        assert result == expected
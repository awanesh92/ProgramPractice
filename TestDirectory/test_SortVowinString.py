import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SortVowinString import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("st, expected", [
        ("lEetcOde","lEOtcede"),
        ("lYmpH","lYmpH")
    ])
    def test_SortVowinString(self, solution, st, expected):
        result=solution.sortVowels(st)
        assert result == expected
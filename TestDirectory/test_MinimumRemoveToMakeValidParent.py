import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from MinimumRemoveToMakeValidParent import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("s, expected", [
        ("))((", ''),
        ('lee(t(c)o)de)','lee(t(c)o)de')
    ])
    def test_minimum_remove_to_make_valid_parent(self, solution, s, expected):
        result = solution.minRemoveToMakeValid(s)
        assert result == expected
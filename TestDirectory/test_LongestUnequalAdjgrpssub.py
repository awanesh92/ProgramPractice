import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from Greedy.LongestUnequaladjgrpssub import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("words, groups, expected", [
        (["e","a","b"], [0,0,1], ["e","b"]),
        (["a","b","c","d"], [1,0,1,1], ["a","b","c"])
    ])
    def test_relativeRanks(self, solution, words, groups, expected):
        result=solution.getLongestSubsequence(words, groups)
        assert result == expected
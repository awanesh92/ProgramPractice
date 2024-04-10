import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from RevealCardsInAscOrder import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("deck, expected", [
        ([17,13,11,2,3,5,7], [2,13,3,11,5,17,7]),
        ([1,1000], [1,1000])
    ])
    def test_deckRevealedIncreasing(self, solution, deck, expected):
        result = solution.deckRevealedIncreasing(deck)
        assert result == expected
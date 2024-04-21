import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from BestTimetoBySellStock import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("prices, expected", [
        ([7,1,5,3,6,4], 7),
        ([7,6,4,3,1], 0),
    ])
    def test_maxProfit(self, solution, prices, expected):
        result=solution.maxProfit(prices)
        assert result == expected